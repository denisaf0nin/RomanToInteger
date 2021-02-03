def romanToInt(s: str) -> int:

    dict = {'m': 1000,
            'd': 500,
            'c': 100,
            'l': 50,
            'x': 10,
            'v': 5,
            'i': 1}

    dict2 = {'iv': 4,
             'ix': 9,
             'xl': 40,
             'xc': 90,
             'cd': 400,
             'cm': 900}

    lst = list(s.lower())
    int_answer = 0

    while len(lst) > 0:
        if len(lst) == 1:
            letter = lst.pop(0)
            int_answer += dict[letter]
        else:
            if "".join(lst[:2]) in dict2.keys():
                int_answer += dict2["".join(lst[:2])]
                lst.pop(0)
                lst.pop(0)
            else:
                letter = lst.pop(0)
                n = 1
                for i in range(len(lst)):
                    if lst[0] == letter:
                        lst.pop(0)
                        n += 1
                    else:
                        break
                int_answer += dict[letter] * n

    return int_answer

romanToInt('MCMLXXXIX')