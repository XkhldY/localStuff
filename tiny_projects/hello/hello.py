#! /usr/bin/env python
# purpose: not mych

import argparse


def main():
    parser = argparse.ArgumentParser(description='type a name')
    parser.add_argument('--name', '-n', metavar='name', help='type name', default='people')
    args = parser.parse_args()
    print('help please ' + args.name)


if __name__ == '__main__':
    main()
