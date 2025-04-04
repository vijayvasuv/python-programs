def find_uniq(arr):
    counts = {}

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():
        if count == 1:
            return num


def main():
    print(find_uniq([ 0, 0, 0.55, 0, 0 ]))

if __name__ == "__main__":
    main()
