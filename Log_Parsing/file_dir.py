#!/usr/bin/env python3

import os
import glob

for file in glob.glob("*.py"):
    print (file)

print("\n")

allfiles = os.listdir()
print (allfiles)