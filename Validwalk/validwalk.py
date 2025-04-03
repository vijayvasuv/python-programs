def validwalk(walk):

    if len(walk)!= 10:
        return False
    else:
        north = walk.count("n")
        south = walk.count("s")
        east = walk.count("e")
        west = walk.count("w")

        if north == south and east == west:
            return True
        else:
            return False


def main():
    direction = ["n", "s", "e", "w", "n", "s", "e", "w", "n", "s"]
    print(validwalk(direction))

if __name__ == "__main__":
    main()
