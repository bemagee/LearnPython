#!/usr/bin/env python3

import os
import fnmatch

for root, dir, files in os.walk("."):
    #print ("")
    for items in fnmatch.filter(dir, "Text"):
        print (root)
        os.chdir(root)
        print ("found one", items)
        os.system("dir")

