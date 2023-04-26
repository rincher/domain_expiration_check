import whois
import datetime


def get_domain_expiration_date(domain_name):
    w = whois.whois(domain_name)
    expiration_date = w.expiration_date

    # If the expiration_date is a list, get the first item
    if type(expiration_date) is list:
        expiration_date = expiration_date[0]

    # If the expiration_date is a datetime object, return it
    if type(expiration_date) is datetime.datetime:
        return expiration_date

    # If the expiration_date is not a datetime object, parse it using dateutil
    from dateutil.parser import parse

    try:
        expiration_date = parse(expiration_date)
    except Exception as e:
        print(domain_name + " " + e)

    return expiration_date
