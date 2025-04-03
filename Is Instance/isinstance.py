def filter_list(l):
    new_list = []
    for item in l:
        if isinstance(item,int):
            new_list.append(item)
    return new_list

def main():
    input = ["n", "s", 1, 2, 3, "e"]
    print(filter_list(input))

if __name__ == "__main__":
    main()
