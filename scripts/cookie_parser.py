#!/usr/bin/env python3

import argparse
import re


def crumble_cookie(cookie):
    regex = r"_?([^;]+)+"
    print(re.finditer(regex, cookie))
    print(re.match(regex, cookie))
    yield re.findall(regex, cookie)


def main(args):

    if args.cookie:
        crumbs = crumble_cookie(args.cookie)
        print(crumbs)
        for c in crumbs:
            print(c)

        # for crumb in crumble_cookie(args.cookie):
        #    print(crumb)

    if args.file:
        with open(args.file, "r") as f:
            for cookie in f:
                cookie = cookie.strip('\n')



'''__gads=4165079571:1:846:131; _gat=10.0.19045.64; _ga=1.591597.1635208534.1040; _u=4445534B544F502D34565A46525350:75736572313031:39414231333532444136393736323546; __io=21_3625792553_1955020779_2750360736; _gid=0078B91C290D'''

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cookie", help="An IP address to enrich.")
    parser.add_argument("-f", "--file", dest="file", help="A path to a file listing IP addresses.")
    args = parser.parse_args()
    main(args)
