from check_expiration import get_domain_expiration_date
from sns_publish import publish_sns
from check_time import time_left


def main():
    domain_dict = {}
    days_left = 0
    with open("domain_list.txt", "r") as file:
        for line in file:
            domain_name = ""
            domain_name = line
            domain_name = domain_name.strip()
            expiration_date = get_domain_expiration_date(domain_name)
            if expiration_date is None:
                continue

            days_left = time_left(expiration_date)

            if days_left >= 30:
                domain_dict[domain_name] = days_left
    if len(domain_dict) >= 1:
        publish_sns(domain_dict, days_left)
    else:
        return "No expiring domain found"


print(main())
