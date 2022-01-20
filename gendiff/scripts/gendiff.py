# -*- coding: utf-8 -*- #

"""Импортируем argparse."""
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('file', metavar='first_file')
    parser.add_argument('file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
