def dig_pow(n, p):
    input = str(n)
    sum = 0

    for num in input:
        sum += int(num) ** p
        p+=1

    remainder = int(sum /n)
    total = remainder* n

    if total == sum:
        return remainder
    else:
        return -1

def main():
    print(dig_pow(46288, 3))

if __name__ == "__main__":
    main()
