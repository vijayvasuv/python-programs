def digitize(n):
    digits = []
    for i in str(n):
        digits.append(int(i))
    digits.reverse()
    return digits

def main():
    print(digitize(2334534))

if __name__ == "__main__":
    main()
