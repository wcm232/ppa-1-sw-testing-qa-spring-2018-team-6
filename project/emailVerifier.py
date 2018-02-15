import re

def verifyEmail(strEmailAddress):
    return re.match("^([a-z])*\@([a-z]|\.)*$", strEmailAddress) is not None