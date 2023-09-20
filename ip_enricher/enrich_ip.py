#!/usr/bin/env python3

import ipinfo
import argparse
import sys

from rich.console import Console
from rich.table import Table


def lookup_ipinfo(token, ip):
    try:
        handler = ipinfo.getHandler(access_token=token)
        details = handler.getDetails(ip)
    except Exception as e:
        print(e)
        sys.exit(1)

    return details


def main(args):
    table = Table(title="IP Enrichment")

    table.add_column("IP Address", justify="right", style="cyan", no_wrap=True)
    table.add_column("Organization", style="magenta")
    table.add_column("City", justify="right", style="green")
    table.add_column("Country Name", justify="right", style="green")

    if args.ip:
        details = lookup_ipinfo(args.token, args.ip)

        table.add_row(details.ip, details.org, details.city, details.country_name)

    if args.file:
        with open(args.file, "r") as f:
            for ip in f:
                ip = ip.strip('\n')
                details = lookup_ipinfo(args.token, ip)
                if details:
                    table.add_row(details.ip, details.org, details.city, details.country_name)

    console = Console()
    console.print(table)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="An IP address to enrich.")
    parser.add_argument("-f", "--file", dest="file", help="A path to a file listing IP addresses.")
    parser.add_argument("--token", help="Your Ipinfo API Token")
    args = parser.parse_args()
    main(args)
