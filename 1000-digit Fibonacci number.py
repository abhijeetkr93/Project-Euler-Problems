from math import log10, ceil


def fib(n):
    if n == 0:
        return (0, 1)

    a, b = fib(n // 2)

    c = a * (2 * b - a)
    d = a * a + b * b

    if n % 2 == 0:
        return (c, d)
    else:
        return (d, c + d)


def main():
    n = 1024
    while True:
        num = fib(n)[0]
        if ceil(log10(num)) == 1000:
            print(num % 100000007)
            break
        n += 1


if __name__ == '__main__':
    main()
