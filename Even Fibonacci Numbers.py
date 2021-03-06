from functools import reduce

'''
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

#every third term in the Fibonacci sequence is even
#the code below only calculates these terms
#hence, there is no need to check whether a particular fibonacci number is even or not
def generateFibonacci():
    a = 1
    b = 1
    c = a + b
    while a < 40000000:
        yield c
        a = c + b
        b = a + c
        c = a + b


def main():
    summation = reduce(lambda x, y: x + y, generateFibonacci())
    print(summation)


if __name__ == '__main__':
    main()


