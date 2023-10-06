#!/usr/bin/env python3

import whois
import argparse
import sys
import json

from rich.console import Console
from rich.table import Table

# {'domain_name': ['GOOGLE.COM', 'google.com'], 'registrar': 'MarkMonitor, Inc.', 'whois_server': 'whois.markmonitor.com', 'referral_url': None, 'updated_date': '2019-09-09 15:39:04', 'creation_date': ['1997-09-15 04:00:00', '1997-09-15 07:00:00'], 'expiration_date': ['2028-09-14 04:00:00', '2028-09-13 07:00:00'], 'name_servers': ['NS1.GOOGLE.COM', 'NS2.GOOGLE.COM', 'NS3.GOOGLE.COM', 'NS4.GOOGLE.COM', 'ns1.google.com', 'ns2.google.com', 'ns4.google.com', 'ns3.google.com'], 'status': ['clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited', 'clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited', 'serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited', 'serverTransferProhibited https://icann.org/epp#serverTransferProhibited', 'serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited', 'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)', 'clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)', 'clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)', 'serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)', 'serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)', 'serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)'], 'emails': ['abusecomplaints@markmonitor.com', 'whoisrequest@markmonitor.com'], 'dnssec': 'unsigned', 'name': None, 'org': 'Google LLC', 'address': None, 'city': None, 'state': 'CA', 'registrant_postal_code': None, 'country': 'US'}


def lookup_domaininfo(domain):
    try:
        details = whois.whois(domain)
        #print(details)
    except Exception as e:
        print(e)
        sys.exit(1)

    return details


def print_details(details):

    if type(details.domain_name) is list:
        details.domain_name = details.domain_name[0]
    if type(details.creation_date) is list:
        details.creation_date = details.creation_date[0]
    if type(details.expiration_date) is list:
        details.expiration_date = details.expiration_date[0]
    if type(details.emails) is list:
        details.emails = ', '.join(details.emails)

    if details.address is not None:
        details['address'] = ', '.join([str(details.address), str(details.city), str(details.state), str(details.registrant_postal_code), str(details.country)])

    #print(details)
    print("")
    print(details.domain_name.lower().replace(".", "[.]"))
    print(f"\tCreation: {details.creation_date}")
    print(f"\tExpiration: {details.expiration_date}")
    print(f"\tName: {details.name}")
    print(f"\tEmail: {details.emails}")
    print(f"\tAddress: {details.address}")


def main(args):

    if args.domain:
        details = lookup_domaininfo(args.domain)
        print_details(details)

    if args.file:
        with open(args.file, "r") as f:
            for domain in f:
                domain = domain.strip('\n')
                details = lookup_domaininfo(domain)

                print_details(details)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="A FQDN to enrich.")
    parser.add_argument("-f", "--file", dest="file", help="A path to a file listing domain names.")
    args = parser.parse_args()
    main(args)
