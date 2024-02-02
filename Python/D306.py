import re


def mail(mail_):
    if '@' not in mail_ or "@@" in mail_:
        return False
    user, domain = mail_.split("@")
    pattern = r'[^a-zA-Z0-9.+]'
    if re.search(pattern, user):
        return False
    if user[0] == '.' or user[-1] == '.' or ".." in user:
        return False
    pattern = r'[^a-zA-Z0-9\-.]{3,}'
    if re.search(pattern, domain) or '+' in domain:
        return False
    if '.' not in domain or domain[0] == '.' or domain[-1] == '.' or ".." in domain:
        return False
    if "-." in domain or ".-" in domain:
        return False
    return True


if mail(input()):
    print("Valid")
else:
    print("Invalid")
