from re import findall


class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainDomainError(Exception):
    pass


VALID_DOMAINS = (".com", ".bg", ".net", ".org")
domain_pattern = r'\.\w+'

email = input()

while email != "End":

    username = email.split("@")[0]

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters!")

    if "." not in email:
        raise MustContainDomainError("Email must contain domain!")

    domain = findall(domain_pattern, email)[-1]

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
