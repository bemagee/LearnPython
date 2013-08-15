import fnmatch
import os
import re

for file in os.listdir('/users/brmagee/bin'):
    if fnmatch.fnmatch(file, '*.pl'):
        print file
