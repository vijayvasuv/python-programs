def persistence(n):
    value = str(n)
    result = 1
    inc = 0

    if len(value) == 1:
        return 0

    else:
        while True:
            for digits in value:
                result*= int(digits)
            inc+= 1
            value = str(result)
            result = 1

            if len(value) == 1:
                return inc

def main():
    print(persistence(999))

if __name__ == "__main__":
    main()
