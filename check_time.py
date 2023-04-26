import datetime


def time_left(expiration_date):
    # Define the format of the string
    date_format = "%Y-%m-%d %H:%M:%S"

    # Convert the string to a datetime object
    time_now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_now = datetime.datetime.strptime(time_now_str, date_format)
    days_left = expiration_date - time_now
    days_left = days_left.days
    return days_left
