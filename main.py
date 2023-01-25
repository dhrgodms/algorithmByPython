test_char = input().lower()
char_sample = {}
for i in range(len(test_char)):
    if test_char[i] not in char_sample:
        char_sample[test_char[i]] = test_char.count(test_char[i])

