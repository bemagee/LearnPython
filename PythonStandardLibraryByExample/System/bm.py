import subprocess
print tempfile.__file__
output = subprocess.check_output(['ls', '-1'])
print 'Have %d bytes in output' % len(output)
print output
