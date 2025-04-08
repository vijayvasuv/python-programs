def good_vs_evil(good, evil):
    split_good = good.split(" ")
    split_evil = evil.split(" ")

    good_result=[]
    evil_result=[]

    good_result_new = []
    evil_result_new = []

    for g in split_good:
        good_result.append(int(g))

    for e in split_evil:
        evil_result.append(int(e))

    good = [1,2,3,3,4,10]
    evil = [1,2,2,2,3,5,10]

    for i in range(len(good_result)):
        value = good_result[i] * good[i]
        good_result_new.append(value)

    for j in range(len(evil_result)):
        values = evil_result[j] * evil[j]
        evil_result_new.append(values)


    good_total = 0
    for num in good_result_new:
        good_total+= num
    evil_total = 0
    for nums in evil_result_new:
        evil_total+= nums


    if good_total < evil_total:
        return "Battle Result: Evil eradicates all trace of Good"
    elif good_total > evil_total:
        return "Battle Result: Good triumphs over Evil"
    else:
        return "Battle Result: No victor on this battle field"

def main():
    print(good_vs_evil('5085 1106 3904 6278 5694 9549', '7413 9388 2769 5467 6235 3297 7123'))

if __name__ == "__main__":
    main()
