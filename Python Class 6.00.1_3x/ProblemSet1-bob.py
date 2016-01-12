#!/usr/bin/env python

s = 'bobbbobbybobbbo'
bobcnt = 0
cnt = len(s)
for i in range(0,cnt):
    if i+2 >= cnt:
        break
    elif (s[i] == 'b') and (s[i+1] == 'o') and (s[i+2] == 'b'):
        bobcnt += 1
print bobcnt
