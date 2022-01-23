def check_consecutive(s):
    ch = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == ch:
            count += 1
            if count == 4:
                return False
        else:
            ch = s[i]
            count = 1
    return True

def check():
    a=input()
    card= a.split("-")
    card_num = "".join(card)
    if len(card_num) != 16:
        return "Invalid"
    if card_num[0] < '4' or card_num[0] > '6':
        return "Invalid"
    if not card_num.isdigit():
        return "Invalid"
    if len(card) > 1:
        if not all(len(i) == 4 for i in card):
            return "Invalid"
    if not check_consecutive(card_num):
        return "Invalid"
    return "Valid"

for i in range(int(input())):
    print(check())
