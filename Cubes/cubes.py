def find_nb(m):
    value = 0
    i = 0
    while True:
        value+= i * i * i
        if value == m:
            return i
        elif value > m:
            return -1
        i+=1

def main():
    print(find_nb(1071225))

if __name__ == "__main__":
    main()
