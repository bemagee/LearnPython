pay = raw_input("What is pay? ")
print pay
location = raw_input("What is location? ")

if location == "U.S.S. Enterprise":
    print "So long, suckers! I'll take it!"
elif location == "Massachusetts":
    if pay < 100000:
        print "No way"
    else:
        print "I'll take it!"
elif location == "California":
    if pay < 40000:
        print "I'll take it!"
    else:
        print "No thank you!"
elif pay > 60000:
    print "I'll take it!"
else:
    print "No thank you!"
