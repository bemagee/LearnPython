def shut_down(s):
    print s
    if s.lower() == 'yes':
        return "Shutting down..."
    elif s.lower() == 'no':
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand you"

Answer = shut_down('YES');
print Answer
