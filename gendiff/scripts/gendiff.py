# -*- coding: utf-8 -*- #

"""Импортируем argparse."""
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('file', metavar='first_file')
    parser.add_argument('file', metavar='second_file')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
