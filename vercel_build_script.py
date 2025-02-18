# vercel_build_script.py
import os
import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error executing {command}:")
        print(error.decode())
        exit(1)
    print(output.decode())

# Install requirements
run_command("pip install -r requirements.txt")

# Run collectstatic
run_command("python manage.py collectstatic --noinput")

print("Build script completed successfully!")