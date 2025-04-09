import math
def list_squared(m,n):
    result = []
    for num in range(m,n+1):
        value = 0
        for i in range(1, num+1):
            if num % i == 0:
               value += i **2

        sqrt = math.sqrt(value)
        if sqrt == int(sqrt):
            result.append([num,value])
    return result

def main():
    print(list_squared(1,256))

if __name__ == "__main__":
    main()
