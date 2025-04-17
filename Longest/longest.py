def longest_consec(strarr, k):
    n = len(strarr)

    if n == 0 or k >n or k <=0:
        return ""

    longest_string = ""
    for i in range(n - k + 1):
        consecutive_string = "".join(strarr[i: i+k])
        if len(consecutive_string) > len(longest_string):
            longest_string = consecutive_string
    return longest_string


def main():
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))

if __name__ == "__main__":
    main()
