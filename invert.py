def invert(lst):
    num = []
    for i in lst:
        if i > 0:
            num.append(-i)
        else:
            num.append(-i)
    return num

def main():
    lst = [1, 2, -3, -56, -78, 9]
    print(invert(lst))

if __name__ == "__main__":
    main()
