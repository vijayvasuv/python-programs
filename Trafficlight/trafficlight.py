class SmartTrafficLight:
    def __init__(self, st1, st2):
        self.st1 = st1
        self.st2 = st2
        self.flag = ""

    def turngreen(self):
        cars1 = int(self.st1[0])
        cars2 = int(self.st2[0])

        if cars1 == cars2:
            return None
        if self.flag == "":
            if cars1 > cars2:
                self.flag = "c1"
                return self.st1[1]
            else:
                self.flag = "c2"
                return self.st2[1]

        elif self.flag == "c1":
            self.flag = "y"
            return self.st2[1]

        elif self.flag == "c2":
            self.flag = "y"
            return self.st1[1]

        elif self.flag == "y":
            return None

def main():
    t=SmartTrafficLight([42, "27th ave"], [72, "3rd st"])
    print(t.turngreen())
    print(t.turngreen())
    print(t.turngreen())

if __name__ == "__main__":
    main()
