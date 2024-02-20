import re

def is_valid_email(email):
    if "@" not in email:
        return False

    username, domain = email.split("@", 1)

    username_pattern = r"^(?!\.)(?!.*\.$)(?!.*\.\.)[a-zA-Z0-9+]+(?:\.[a-zA-Z0-9+]+)*$"
    domain_name_pattern = r"^(?!\.)(?!.*\.$)(?!.*\.\.)[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    tld_pattern = r"[a-zA-Z0-9-]+$"

    if not (re.match(username_pattern, username) and re.match(domain_name_pattern, domain)):
        return False
    
    domain_parts = domain.split(".")
    if len(domain_parts) < 2:
        return False
    
    tld = domain_parts[-1]
    if not re.match(tld_pattern, tld):
        return False

    for i in range(len(domain) - 1):
        if domain[i] == "." and domain[i + 1] == "-":
            return False
        if domain[i] == "-" and domain[i + 1] == ".":
            return False

    return True

email_input = input().strip()

if is_valid_email(email_input):
    print("Valid")
else:
    print("Invalid")
