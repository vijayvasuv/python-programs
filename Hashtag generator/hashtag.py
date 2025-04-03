def generate_hashtag(s):
    new_value = []
    final_value = []
    result = ""
    value = s.split(" ")

    for item in value:
        new_value.append(item.lower())

    for items in new_value:
        final_value.append(items.title())

    for new_item in final_value:
        result += new_item

    if len(result) >= 140 or len(result) == 0:
        return False
    else:
        return f"#{result}"

def main():
    print(generate_hashtag("Codewars has great kata"))

if __name__ == "__main__":
    main()
