def up_low(s):
    count_uppercase = 0
    count_lowercase = 0

    for character in s:
        if character.isupper():
            count_uppercase += 1
        elif character.islower():
            count_lowercase += 1
        else:
            pass
    print("Original String: {}".format(s))
    print("Upper case character count: {}".format(count_uppercase))
    print("Lower case character count: {}".format(count_lowercase))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)