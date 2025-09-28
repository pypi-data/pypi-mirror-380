import schedule
import time
from actions import notify, run_command
from rich.console import Console
from rich.text import Text
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
from datetime import datetime

console = Console()
log_file_path = None  # default: no file logging

# ===== Logging functions =====
def set_log_file(path):
    global log_file_path
    log_file_path = path

def log(msg):
    console.print(msg)
    if log_file_path:
        with open(log_file_path, "a") as f:
            f.write(f"{msg.plain}\n")

# ===== Helper for timestamp =====
def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ===== Action executor =====
def execute_action(action):
    if action["type"] == "notify":
        notify(action)
    elif action["type"] == "run_command":
        run_command(action)

# ===== File change handler =====
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, task):
        self.task = task

    def on_any_event(self, event):
        task_name = self.task.get("name", "Unnamed Task")
        msg = Text(f"[{timestamp()}] [FILE] {task_name}: Change detected", style="green")
        log(msg)
        execute_action(self.task["action"])

# ===== File-change task scheduler =====
def schedule_file_change_task(task):
    path = task["trigger"]["path"]
    event_handler = FileChangeHandler(task)
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)

    observer_thread = threading.Thread(target=observer.start)
    observer_thread.daemon = True
    observer_thread.start()

    msg = Text(f"[{timestamp()}] [FILE] Watching folder: {path} for changes", style="blue")
    log(msg)

# ===== Timer task scheduler =====
def schedule_timer_task(task):
    trigger = task["trigger"]
    action = task["action"]
    task_name = task.get("name", "Unnamed Task")

    def job():
        msg = Text(f"[{timestamp()}] [TIMER] Running task: {task_name}", style="green")
        log(msg)
        execute_action(action)

    schedule.every().day.at(trigger["time"]).do(job)
    msg = Text(f"[{timestamp()}] [TIMER] Scheduled daily task: {task_name} at {trigger['time']}", style="blue")
    log(msg)

# ===== Main scheduler runner =====
def run_scheduler(tasks):
    for task in tasks:
        trigger_type = task["trigger"]["type"]
        if trigger_type == "timer":
            schedule_timer_task(task)
        elif trigger_type == "file_change":
            schedule_file_change_task(task)

    log(Text(f"[{timestamp()}] Scheduler started. Press Ctrl+C to stop.", style="bold yellow"))
    while True:
        schedule.run_pending()
        time.sleep(1)
