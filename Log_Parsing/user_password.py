#!/usr/bin/env python3

import getpass

usr = getpass.getuser()

pwd = getpass.getpass("Enter a password for user %s: "% usr)

print (usr, pwd)