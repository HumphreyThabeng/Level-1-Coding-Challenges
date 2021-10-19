list1 = ["one", "three", "four", "my", "chickens"]


def find_longest_word(list1):
    longest_word = ''
    for x in list1:
        if len(x) > len(longest_word):
            longest_word = x
    print("Longest Word is " + longest_word)


find_longest_word(list1)
