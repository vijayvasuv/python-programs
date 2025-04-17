class list:
    def __init__(self, list):
        self.list = list
        self.result = []

    def even(self):
        """
        for i in self.list:
            if isinstance(i, int):
                if i % 2 == 0:
                    self.result.append(i)
        return self.result
        """

        return [x for x in self.list if x % 2 == 0]

    def odd(self):
        for i in self.list:
            if isinstance(i, int):
                if i % 2 != 0:
                    self.result.append(i)
        return self.result

    def under(self, num):
        self.num = num
        for i in self.list:
            if isinstance(i, int):
                if i < num:
                    self.result.append(i)
        return self.result


    def over(self, num):
        self.num = num
        for i in self.list:
            if isinstance(i, int):
                if i > num:
                    self.result.append(i)
        return self.result

    def in_range(self, start, end):
        self.start = start
        self.end = end
        for i in self.list:
            if isinstance(i, int):
                if start <= i <= end:
                    self.result.append(i)
        return self.result


def main():
    new_list = list([1,2,3,4,5,6])
    print((new_list.even()))

if __name__ == "__main__":
    main()

