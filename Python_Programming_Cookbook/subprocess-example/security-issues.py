import subprocess
import shlex


def unsafe(directory):
    command = "du -sh {}".format(directory)
    subprocess.call(command, shell=True)


def safe(directory):
    sanitized_directory = shlex.quote(directory)
    command = "du -sh {}".format(sanitized_directory)
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    directory = "/dev/null; ls -l /tmp"
    unsafe(directory)
    safe(directory)
