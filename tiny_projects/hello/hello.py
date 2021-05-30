#! /usr/bin/env python
# purpose: say fuck you

import argparse


def main():
    parser = argparse.ArgumentParser(description='say fuck you asshole')
    parser.add_argument('--name', '-n', metavar='name', help='name to fuck', default='all motherfuckers')
    args = parser.parse_args()
    print('fuck you ' + args.name)


if __name__ == '__main__':
    main()
