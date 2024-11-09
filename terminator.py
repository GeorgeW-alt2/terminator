import subprocess

def kill_unsigned_processes():
    result = subprocess.run(['wmic', 'process', 'get', 'ProcessId,ExecutablePath'], capture_output=True, text=True)
    for line in result.stdout.splitlines()[1:]:  # Skip header line
        # Handle empty lines and lines with potentially missing data
        parts = line.split(maxsplit=1)
        if not parts:  # Check for empty line
            continue

        pid = parts[0] if len(parts) >= 1 else None  # Handle missing PID
        exe_path = parts[1] if len(parts) == 2 else None  # Handle missing executable path

        if not exe_path or not exe_path.endswith('.exe'):
            subprocess.run(['taskkill', '/F', '/PID', pid])

if __name__ == '__main__':
    kill_unsigned_processes()