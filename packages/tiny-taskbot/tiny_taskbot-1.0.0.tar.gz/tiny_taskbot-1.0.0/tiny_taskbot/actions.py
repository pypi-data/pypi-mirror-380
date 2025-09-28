import subprocess
from plyer import notification

def notify(action):
    message = action.get("message", "No message provided")
    notification.notify(
        title="Tiny TaskBot",
        message=message,
        timeout=5
    )

def run_command(action):
    """
    Runs a shell command.
    """
    command = action.get("command")
    if not command:
        print("No command provided for run_command action.")
        return
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"[Tiny TaskBot] Command output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"[Tiny TaskBot] Command failed with error:\n{e.stderr}")
