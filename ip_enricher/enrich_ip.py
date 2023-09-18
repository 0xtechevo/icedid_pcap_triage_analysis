#!/usr/bin/env python3

import ipinfo
import argparse


def lookup_ipinfo(token, ip):
    handler = ipinfo.getHandler(access_token=token)
    details = handler.getDetails(ip)

    return details


def main(args):

    if args.ip:
        lookup_ipinfo(args.token, args.ip)

    if args.file:
        with open(args.file, "r") as f:
            for ip in f:
                ip = ip.strip('\n')
                details = lookup_ipinfo(args.token, ip)
                print(details.org)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="An IP address to enrich.")
    parser.add_argument("-f", "--file", help="A path to a file listing IP \
            addresses.")
    parser.add_argument("--token", help="Your Ipinfo API Token")
    args = parser.parse_args()

    main(args)
