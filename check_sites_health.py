import argparse
import requests
import os.path
import whois
from datetime import datetime, timedelta
from requests import ConnectionError, ConnectTimeout

DAYS_IN_MONTH = 30


def load_url4check(path):
    with open(path) as file:
        for line in file:
            yield line.strip()


def is_server_respond_with_200(url):
    try:
        server_response = requests.get(url, timeout=(1, 10))
    except (ConnectionError, ConnectTimeout):
        return False
    server_status_code = server_response.status_code
    return True if server_status_code == 200 else False


def check_domain_expiration_date(domain_name):
    whois_data = whois.whois(domain_name)
    # Expiration date is provided as list of datetime-objects for some sites.
    if isinstance(whois_data.expiration_date, list):
        expiration_date = whois_data.expiration_date[0]
    elif isinstance(whois_data.expiration_date, datetime):
        expiration_date = whois_data.expiration_date
    else:
        return None
    if datetime.now() + timedelta(DAYS_IN_MONTH) <= expiration_date:
        return expiration_date
    else:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="path to file with urls to check")
    args = parser.parse_args()
    if not os.path.isfile(args.filepath):
        print("File name does not exist! Exiting...")
        exit()
    print("{:^30}{:^20}{:>25}".format("URL", "200 OK", "Expiration date"))
    for url in load_url4check(args.filepath):
        is200_str = "Yes" if is_server_respond_with_200(url) else "No"
        if check_domain_expiration_date(url) is None:
            exp_date_str = "Less than a month left or can't get it."
        else:
            exp_date_str = check_domain_expiration_date(url).strftime("%d.%m.%Y")
        print("{:^30}{:>12}{:^50}".format(url, is200_str, exp_date_str))
