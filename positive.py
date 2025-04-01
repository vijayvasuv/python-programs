def positive_sum(arr):
    num = len(arr)
    i = 0
    sum = 0
    while i<num:
        if arr[i] >= 1:
            sum+= arr[i]
            i+=1
        else:
            i+=1
    return sum

def main():
    numbers = [1, 2, 3, -4, 56, 78, -90]
    print(positive_sum(numbers))

if __name__ == "__main__":
    main()
