
"Part 1 - Implement Fibonnaci Sequence Recursion"
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

"Part 2 Implement GCD algorithm Recursion"
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

"Part 3 Implement String Comparison Recusion"
def compareTo(s1, s2):
    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])


if __name__ == '__main__':
    print("Test of the fibonacci sequence the 12th number is {}.".format(fibonacci(12)))
    print("Test of the greatest common divisor of 132and 278 is {}.".format(gcd(132, 464)))
    print("Test of the comparison of the following two strings waterbottle1 and waterbottle2 is {}.".format(compareTo("waterbottle1", "waterbottle2")))