import os
import queue
import re
import threading
import time
from datetime import datetime, timedelta, timezone
from typing import Optional


class FileLogRepository:
    def __init__(
        self,
        log_dir: str = "files/logs",
        retention_days: int = 3,
        log_queue: Optional[queue.Queue] = None
    ):
        self.log_dir = log_dir
        self.retention_days = retention_days
        self.log_queue = log_queue
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        self._last_cleanup = datetime.now(timezone.utc)

        os.makedirs(self.log_dir, exist_ok=True)
        self.delete_old_logs()

    def _should_cleanup(self) -> bool:
        now = datetime.now(timezone.utc)
        return (now - self._last_cleanup) >= timedelta(hours=24)

    def _cleanup_if_needed(self):
        if self._should_cleanup():
            self.delete_old_logs()
            self._last_cleanup = datetime.now(timezone.utc)

    def _get_log_filename(self) -> str:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return os.path.join(self.log_dir, f"app_{today}.log")
    
    def _write_log(self, log_entry: dict):
        """نوشتن لاگ به صورت ساده: timestamp [LEVEL] message"""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        level = log_entry.get("level", "INFO").upper()
        message = log_entry.get("message", "")

        # فرمت: 2025-04-05 14:30:22 [INFO] پیام...
        log_line = f"{timestamp} [{level}] {message}\n"

        log_file = self._get_log_filename()
        try:
            with self._lock:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_line)
        except Exception as e:
            print(f"[FileLogRepository] خطا در نوشتن لاگ: {e}")

    def start_queue_processor(self):
        if not self.log_queue:
            print("[FileLogRepository] کیو تعریف نشده است.")
            return

        def process_queue():
            while not self._stop_event.is_set():
                try:
                    log = self.log_queue.get(timeout=3)
                    self._write_log({
                        "level": log["level"],
                        "message": log["message"],
                        # سایر فیلدها (function_name و ...) نادیده گرفته می‌شوند
                    })
                    self.log_queue.task_done()
                except queue.Empty:
                    pass
                except Exception as e:
                    print(f"[FileQueueProcessor] خطا: {e}")
                    time.sleep(1)

                self._cleanup_if_needed()

        thread = threading.Thread(target=process_queue, daemon=True)
        thread.start()

    def stop_queue_processor(self):
        self._stop_event.set()

    def get_logs(self, limit: int = 20, offset: int = 0) -> list:
        """
        خواندن لاگ‌ها و بازگرداندن به صورت لیستی از دیکشنری‌ها:
        [
            {"timestamp": "2025-04-05 14:30:22", "level": "INFO", "message": "..."},
            ...
        ]
        """
        logs = []
        log_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[([A-Z]+)\] (.*)$')

        try:
            log_files = []
            for i in range(self.retention_days):
                date_str = (datetime.now(timezone.utc).date() - timedelta(days=i)).strftime("%Y-%m-%d")
                file_path = os.path.join(self.log_dir, f"app_{date_str}.log")
                if os.path.exists(file_path):
                    log_files.append(file_path)

            # خواندن از جدیدترین فایل به قدیمی‌ترین
            for log_file in log_files:
                with open(log_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    # معکوس کردن خطوط هر فایل برای جدیدترین اول
                    for line in reversed(lines):
                        line = line.strip()
                        if not line:
                            continue
                        match = log_pattern.match(line)
                        if match:
                            timestamp, level, message = match.groups()
                            logs.append({
                                "timestamp": timestamp,
                                "level": level,
                                "message": message
                            })
                        # اگر خط فرمت استاندارد نداشت، نادیده گرفته می‌شود

            return logs[offset:offset + limit]

        except Exception as e:
            print(f"[FileLogRepository] خطا در خواندن لاگ‌ها: {e}")
            return []

    def delete_old_logs(self):
        try:
            cutoff = datetime.now(timezone.utc).date() - timedelta(days=self.retention_days)
            for filename in os.listdir(self.log_dir):
                if filename.startswith("app_") and filename.endswith(".log"):
                    try:
                        date_str = filename.replace("app_", "").replace(".log", "")
                        log_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                        if log_date < cutoff:
                            os.remove(os.path.join(self.log_dir, filename))
                    except Exception:
                        continue
            self._last_cleanup = datetime.now(timezone.utc)
        except Exception as e:
            print(f"[FileLogRepository] خطا در حذف فایل‌های قدیمی: {e}")

    def get_total_log_count(self) -> int:
        # اگر نیاز به شمارش دقیق دارید، می‌توانید خطوط را بشمارید
        # ولی برای سادگی همچنان 100 برمی‌گردانیم
        return 1000
        
    def close_connection(self):
        self.stop_queue_processor()
        self.delete_old_logs()