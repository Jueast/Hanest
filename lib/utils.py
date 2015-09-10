import re


def validName(name):
    USERNAME_RE = re.compile("^[a-zA-Z\xa0-\xff_][0-9a-zA-Z\xa0-\xff_]{3,20}$")
    return USERNAME_RE.match(name)
