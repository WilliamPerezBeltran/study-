#!/usr/bin/python -tt
# coding=utf-8


def sort_laTuple():
    a = [
        (1, "a"),
        (2, "c"),
        (4, "d"),
        (7, "s"),
        (4, "r"),
        (34, "y"),
        (8, "b"),
        (35, "q"),
        (0, "l"),
    ]
    # return sorted(a,)
    return sorted(a,key=last)


def last(item):
    return item[-1]


def main():
    print(sort_laTuple())


if __name__ == "__main__":
    main()
