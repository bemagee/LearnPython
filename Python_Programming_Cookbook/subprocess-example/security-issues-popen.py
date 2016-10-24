from subprocess import Popen
import shlex


def unsafe(directory):
    command = "du -sh {}".format(directory)
    proc = Popen(command, shell=True)
    proc.wait()


def safe(directory):
    sanitized_directory = shlex.quote(directory)
    command = "du -sh {}".format(sanitized_directory)
    proc = Popen(command, shell=True)
    proc.wait()

if __name__ == "__main__":
    directory = "/dev/null; ls -l /tmp"
    unsafe(directory)
    safe(directory)
