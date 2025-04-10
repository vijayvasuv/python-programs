def pig_it(text):
    input = text.split(" ")
    additional_letter = "ay"
    result = []

    for word in input:
        if word.isalpha():
            first_letter = word[0]
            rest_letter = word[1:]
            new_letter = rest_letter+first_letter+additional_letter
            result.append(new_letter)
        else:
            result.append(word)

    return " ".join(result)


def main():
    print(pig_it("Quis custodiet ipsos custodes ?"))

if __name__ == "__main__":
    main()
