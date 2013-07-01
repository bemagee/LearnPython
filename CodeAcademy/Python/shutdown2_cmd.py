
def shut_down(s):
    if s in ["YES","Yes", "yes"]:
        return "Shutting down..."
    elif s in ["NO", "No", "no"]:
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand you."
