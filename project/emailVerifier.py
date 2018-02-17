import re

def verifyEmail(strEmailAddress):
    if strEmailAddress is None:
        return False

    if type(strEmailAddress) is not str:
        return False

    if ".." in strEmailAddress:
        return False

    if strEmailAddress.startswith("."):
        return False

    # Make sure the string left of the @ doesn't end with a period
    # The regex further on will make sure there's only 1 @
    if ".@" in strEmailAddress:        
        return False

    return re.match("""^[a-zA-Z\!\$\%\*\+\-\=\?\^\_\{\|\}\~]([a-zA-Z0-9\!\$\%\*\+\-\=\?\^\_\{\|\}\~]|\.)*\@([a-zA-Z0-9]|\.)+$""", strEmailAddress) is not None