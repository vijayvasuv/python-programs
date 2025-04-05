def find_dup(arr):
    seen = []
    dup = []
    for num in arr:
        if num in seen:
            if num not in dup:
                dup.append(num)
        else:
            seen.append(num)
    return dup

def main():
    print(find_dup([ 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6 ]))

if __name__ == "__main__":
    main()
