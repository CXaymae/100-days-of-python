import subprocess

for i in range(5):
    subprocess.check_call(["python3", "example.py"])

    # check_call it runs an executable in the terminal and waits until the process it has finished before continuing the scripting 