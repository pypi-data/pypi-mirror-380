import os
import sys
import time
import threading
import logging
import json
import atexit
from datetime import datetime
from collections import deque
from pathlib import Path

from . import config
from .template import HTML_TEMPLATE


def get_local_timestamp():
    x = datetime.now()
    return "%04d-%02d-%02d %02d:%02d:%02d.%03d" % (x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond / 1000)


class LogWriter:
    # Pre-compiled constants (class-level for all instances)
    HTML_ESCAPE_TABLE = str.maketrans({
        '<': '&lt;',
        '>': '&gt;',
        '&': '&amp;'
    })

    # Pre-compiled replacement pairs (order matters: \r\n before \n)
    REPLACEMENTS = (
        ('\r\n', '<br>'),
        ('\n', '<br>'),
        ('=>', '&rArr;')
    )

    def __init__(self):
        os.makedirs(config.log_dir, exist_ok=True)
        self.trace_file = None
        self.__last_color = None
        self.last_flush = 0
        self.trace_lock = threading.RLock()  # Use RLock for better reliability
        self.current_size = 0
        self.write_buffer = deque(maxlen=1000)  # Buffer for high-volume logging
        self.buffer_size = 0
        self.max_buffer_size = 64 * 1024  # 64KB buffer
        self.retry_count = 3
        self.logger = logging.getLogger(__name__)

        # Multi-process coordination
        self.process_id = os.getpid()
        self._process_registered = False

        self._remove_existing_footer()

        # Register process AFTER directory exists
        self._register_process()

        # Register cleanup on exit
        atexit.register(self._cleanup_on_exit)

    def _get_filename(self):
        return os.path.join(config.log_dir, config.main_filename)

    def _get_lock_filename(self):
        """Get the lock file path for multi-process coordination"""
        base_name = Path(config.main_filename).stem
        return os.path.join(config.log_dir, f".{base_name}.lock")

    def _register_process(self):
        """Register this process as active user of the log file"""
        if self._process_registered:
            return

        lock_file = self._get_lock_filename()

        try:
            # Read existing processes
            processes = {}
            if os.path.exists(lock_file):
                try:
                    with open(lock_file, 'r') as f:
                        processes = json.load(f)
                except (json.JSONDecodeError, IOError):
                    processes = {}

            # Add current process
            processes[str(self.process_id)] = {
                'pid': self.process_id,
                'started': time.time()
            }

            # Write back atomically
            temp_file = lock_file + '.tmp'
            with open(temp_file, 'w') as f:
                json.dump(processes, f)

            # Atomic rename (works on Windows and Unix)
            try:
                os.replace(temp_file, lock_file)
            except OSError:
                # Fallback for some file systems
                if os.path.exists(lock_file):
                    os.remove(lock_file)
                os.rename(temp_file, lock_file)

            self._process_registered = True

        except Exception as e:
            self.logger.warning(f"Could not register process in lock file: {e}")

    def _cleanup_on_exit(self):
        """Cleanup on process exit (called by atexit)"""
        try:
            self._unregister_process()
        except:
            pass

    def _unregister_process(self):
        """Unregister this process and check if we're the last one"""
        if not self._process_registered:
            return False

        lock_file = self._get_lock_filename()

        try:
            if not os.path.exists(lock_file):
                self._process_registered = False
                return True

            # Read existing processes
            processes = {}
            try:
                with open(lock_file, 'r') as f:
                    processes = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._process_registered = False
                return True

            # Remove current process
            processes.pop(str(self.process_id), None)

            # Clean up stale processes (more than 1 hour old or not running)
            current_time = time.time()
            stale_pids = []
            for pid_str, info in list(processes.items()):
                pid = info.get('pid')
                started = info.get('started', 0)

                # Check if process is stale (1 hour timeout or process not running)
                if current_time - started > 3600 or not self._is_process_running(pid):
                    stale_pids.append(pid_str)

            for pid_str in stale_pids:
                processes.pop(pid_str, None)

            # Write back
            if processes:
                # Other processes still active
                temp_file = lock_file + '.tmp'
                with open(temp_file, 'w') as f:
                    json.dump(processes, f)
                try:
                    os.replace(temp_file, lock_file)
                except OSError:
                    if os.path.exists(lock_file):
                        os.remove(lock_file)
                    os.rename(temp_file, lock_file)
            else:
                # Last process - remove lock file
                try:
                    os.remove(lock_file)
                except OSError:
                    pass

            self._process_registered = False
            return len(processes) == 0  # True if we're the last process

        except Exception as e:
            self.logger.warning(f"Could not unregister process from lock file: {e}")
            self._process_registered = False
            return False

    def _is_process_running(self, pid):
        """Check if a process is running (cross-platform)"""
        if pid is None:
            return False

        try:
            if sys.platform == 'win32':
                import ctypes
                kernel32 = ctypes.windll.kernel32
                PROCESS_QUERY_INFORMATION = 0x0400
                handle = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, 0, pid)
                if handle:
                    kernel32.CloseHandle(handle)
                    return True
                return False
            else:
                # Unix-like systems
                os.kill(pid, 0)
                return True
        except (OSError, AttributeError):
            return False

    def _is_last_process(self):
        """Check if this is the last active process using the log file"""
        lock_file = self._get_lock_filename()

        try:
            if not os.path.exists(lock_file):
                return True  # No lock file means we're alone

            with open(lock_file, 'r') as f:
                processes = json.load(f)

            # Count active processes (excluding stale ones)
            current_time = time.time()
            active_count = 0

            for pid_str, info in processes.items():
                pid = info.get('pid')
                started = info.get('started', 0)

                # Skip stale processes
                if current_time - started > 3600:
                    continue

                # Check if process is running
                if pid == self.process_id or self._is_process_running(pid):
                    active_count += 1

            return active_count <= 1  # Only us or nobody

        except (json.JSONDecodeError, IOError, FileNotFoundError):
            return True  # If we can't read, assume we're alone

    def _remove_existing_footer(self):
        filename = self._get_filename()
        if os.path.exists(filename):
            try:
                with open(filename, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    footer = "<!-- CONTAINER_END -->\n</div>\n</body>\n</html>"
                    if content.endswith(footer):
                        new_content = content[:-len(footer)]
                        f.seek(0)
                        f.write(new_content)
                        f.truncate()
            except Exception:
                pass

    def _load_template(self):
        """Load HTML template from Python module"""
        return HTML_TEMPLATE

    def _remove_extra_files(self, pattern, limit):
        import glob
        try:
            files = glob.glob(pattern)
            if len(files) > limit:
                files.sort()
                for f in files[:-limit]:
                    os.remove(f)
        except Exception:
            pass

    def _handle_new_log_file(self, file_name, file_pattern, fd):
        target = file_pattern % (fd)
        limit_count = config.log_files_limit_count

        target += ".tmp"
        limit_count -= 1

        try:
            os.rename(file_name, target)
        except OSError:
            pass

        self._remove_extra_files(file_pattern % "*", limit_count)

        # Cross-platform file operations
        import platform
        import subprocess
        import glob
        
        try:
            # Compress the target file if gzip is available
            if platform.system() != 'Windows':
                subprocess.run(['gzip', '-c', target], 
                             stdout=open(target[:-4], 'wb'), 
                             stderr=subprocess.DEVNULL,
                             check=False)
            
            # Remove temporary files cross-platform
            os.remove(target) if os.path.exists(target) else None
            
            # Clean up temporary files
            for temp_file in glob.glob("trace_*.dat.tmp") + glob.glob("ErrorLog_*.txt.gz.tmp"):
                try:
                    os.remove(temp_file)
                except OSError:
                    pass
                    
        except (subprocess.SubprocessError, OSError):
            # If compression fails, just remove the original file
            try:
                os.remove(target) if os.path.exists(target) else None
            except OSError:
                pass

    def _safe_file_operation(self, operation, *args, **kwargs):
        """Execute file operation with retry mechanism"""
        for attempt in range(self.retry_count):
            try:
                return operation(*args, **kwargs)
            except (BrokenPipeError, OSError) as e:
                if attempt == self.retry_count - 1:
                    self.logger.error(f"File operation failed after {self.retry_count} attempts: {e}")
                    raise
                time.sleep(0.1 * (attempt + 1))  # Exponential backoff
            except Exception as e:
                self.logger.error(f"Unexpected error in file operation: {e}")
                raise

    def _ensure_file_handle(self):
        """Ensure file handle is valid and open"""
        filename = self._get_filename()

        if not self.trace_file or self.trace_file.closed:
            try:
                if os.path.exists(filename):
                    self.trace_file = open(filename, 'a', encoding='utf-8', buffering=8192)
                else:
                    self.trace_file = open(filename, 'w', encoding='utf-8', buffering=8192)
                    self.trace_file.write(self._load_template())
            except (OSError, IOError) as e:
                self.logger.error(f"Failed to open log file {filename}: {e}")
                raise

    def _write_to_buffer(self, formated_msg):
        """Add message to buffer for batch writing"""
        self.write_buffer.append(formated_msg)
        self.buffer_size += len(formated_msg)

        # Flush buffer if it's getting too large
        if self.buffer_size >= self.max_buffer_size:
            self._flush_buffer()

    def _flush_buffer(self):
        """Flush buffered messages to file"""
        if not self.write_buffer:
            return

        try:
            self._ensure_file_handle()

            # Write all buffered messages at once
            buffer_content = ''.join(self.write_buffer)

            def write_operation():
                self.trace_file.write(buffer_content)
                self.trace_file.flush()

            self._safe_file_operation(write_operation)

            # Update size tracking
            self.current_size += self.buffer_size

            # Clear buffer
            self.write_buffer.clear()
            self.buffer_size = 0

            # Check if we need to rotate the file
            if self.current_size >= config.log_files_limit_size:
                self._rotate_file()

        except Exception as e:
            self.logger.error(f"Failed to flush buffer: {e}")
            # Clear buffer even on error to prevent memory issues
            self.write_buffer.clear()
            self.buffer_size = 0

    def write_direct(self, msg, color, tag):
        """Write log message with improved error handling and buffering"""
        try:
            # Sanitize input (done outside lock for better concurrency)
            if not isinstance(msg, str):
                msg = str(msg)
            if not isinstance(color, str):
                color = str(color) if color else 'white'
            if not isinstance(tag, str):
                tag = str(tag) if tag else 'log'

            # Escape HTML characters using pre-compiled table
            msg = msg.translate(self.HTML_ESCAPE_TABLE)

            # Apply replacements using pre-compiled tuples
            for old, new in self.REPLACEMENTS:
                msg = msg.replace(old, new)

            # Generate timestamp (optimized format)
            x = datetime.now()
            date_str = "%04d-%02d-%02d %02d:%02d:%02d.%03d" % (
                x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond // 1000
            )

            # Build formatted message
            formated_msg = f'<font color="{color}" tag="{tag}">{date_str} - {msg}</font>\n'

            # Check time BEFORE acquiring lock to reduce lock duration
            current_time = time.monotonic()
            should_flush = (current_time - self.last_flush) > 1.0

            # Minimal critical section with lock
            with self.trace_lock:
                self._write_to_buffer(formated_msg)

                if should_flush:
                    self._flush_buffer()
                    self.last_flush = current_time

        except Exception as e:
            # Log the error but don't raise to prevent breaking the application
            self.logger.error(f"Error in write_direct: {e}")
            try:
                # Emergency fallback - try to write to stderr
                sys.stderr.write(f"LogHTML Error: {e}\n")
                sys.stderr.flush()
            except:
                pass  # Last resort - silent fail

    def _rotate_file(self):
        """Rotate the log file if it exceeds the size limit"""
        try:
            # Flush any remaining buffer first
            self._flush_buffer()

            if self.trace_file and not self.trace_file.closed:
                def rotation_operation():
                    self.trace_file.write("<!-- CONTAINER_END -->\n</div>\n</body>\n</html>")
                    self.trace_file.flush()
                    self.trace_file.close()

                self._safe_file_operation(rotation_operation)
                self.trace_file = None

            # Create a backup of the current file
            import glob
            from datetime import datetime

            filename = self._get_filename()
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_name = os.path.join(config.log_dir, f"{timestamp}_{config.main_filename}")

            try:
                if os.path.exists(filename):
                    os.rename(filename, backup_name)
            except OSError as e:
                self.logger.warning(f"Failed to rotate log file: {e}")

            # Remove old files if exceeding the limit
            try:
                pattern = os.path.join(config.log_dir, f"*_{config.main_filename}")
                files = glob.glob(pattern)
                if len(files) > config.log_files_limit_count:
                    files.sort()
                    for f in files[:-config.log_files_limit_count]:
                        try:
                            os.remove(f)
                        except OSError as e:
                            self.logger.warning(f"Failed to remove old log file {f}: {e}")
            except Exception as e:
                self.logger.warning(f"Failed to clean up old log files: {e}")

            self.current_size = 0

        except Exception as e:
            self.logger.error(f"Error during file rotation: {e}")
            # Reset file handle on rotation error
            self.trace_file = None
            self.current_size = 0

    def close(self):
        """Close the log file with proper cleanup"""
        with self.trace_lock:
            try:
                # Flush any remaining buffered content
                self._flush_buffer()

                # Check if we're the last process before writing footer
                is_last = self._is_last_process()

                if self.trace_file and not self.trace_file.closed:
                    def close_operation():
                        # Only write footer if we're the last process
                        if is_last:
                            self.trace_file.write("<!-- CONTAINER_END -->\n</div>\n</body>\n</html>")
                        self.trace_file.flush()
                        self.trace_file.close()

                    self._safe_file_operation(close_operation)
                    self.trace_file = None

                # Unregister this process from lock file
                self._unregister_process()

            except Exception as e:
                self.logger.error(f"Error closing log file: {e}")
                # Force close file handle if it exists
                if self.trace_file:
                    try:
                        self.trace_file.close()
                    except:
                        pass
                    self.trace_file = None

                # Try to unregister even on error
                try:
                    self._unregister_process()
                except:
                    pass
