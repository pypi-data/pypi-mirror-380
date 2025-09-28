import argparse
from rich.console import Console
from rich.text import Text
from tiny_taskbot.scheduler import run_scheduler, validate_tasks, dry_run
from importlib import resources
import json
import os

console = Console()

def load_tasks_from_package():
    """Load the default tasks.json included in the package."""
    with resources.open_text("tiny_taskbot", "tasks.json") as f:
        return json.load(f)

def load_tasks_from_file(path):
    """Load tasks.json from a user-specified file."""
    if not os.path.exists(path):
        console.print(Text(f"[red]File not found: {path}[/red]"))
        return []
    with open(path, "r") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Tiny TaskBot")
    parser.add_argument("--dry-run", action="store_true", help="Print tasks without running them")
    parser.add_argument("--log", type=str, help="Write scheduler output to a log file")
    parser.add_argument("--tasks", type=str, help="Path to custom tasks.json")
    args = parser.parse_args()

    from tiny_taskbot.scheduler import set_log_file
    if args.log:
        set_log_file(args.log)

    # Load tasks
    tasks = load_tasks_from_file(args.tasks) if args.tasks else load_tasks_from_package()
    if not tasks:
        console.print("[yellow]No tasks to run. Please provide a tasks.json[/yellow]")
        return

    # Validate tasks
    tasks = validate_tasks(tasks)
    if not tasks:
        console.print("[yellow]No valid tasks to run after validation.[/yellow]")
        return

    # Dry-run or actual run
    if args.dry_run:
        dry_run(tasks)
    else:
        run_scheduler(tasks)


if __name__ == "__main__":
    main()
