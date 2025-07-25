import sys
import pdb


def listas(l=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print("---")
    print("---")

    print("lista original")
    print(l)

    print("list.append (x)")
    l.append(100)
    print(l)

    print("list.extend (iterable)")
    l.extend([212, 232, 432, 454])
    print(l)

    print("list.insert(0, x) ")
    l.insert(0, 999)
    print(l)

    print("list.remove (x)")
    l.remove(999)
    print(l)

    print("list.pop ([, i])")
    l.pop()
    print(l)

    print("list.clear ()")
    l.clear()
    print(l)

    l=[1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("list.index (x[, start[, end]])")
    print(l.index(9))

    print("list.count (x)")
    print(l.count(9))

    print("list.sort (key=None, reverse=False)")
    # l.sort()
    # print(l)

    print("list.reverse()")
    l.reverse()
    print(l)

    a =list.copy ()


def main():
    listas()


if __name__ == "__main__":
    main()
