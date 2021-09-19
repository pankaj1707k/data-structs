""" https://www.hackerrank.com/challenges/the-time-in-words/problem """


def timeInWords(h, m):
    minute_map = {
        0: "o' clock",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "half",
    }

    hour = minute_map[h]

    if m == 0:
        time_in_words = hour + " " + minute_map[0]
    elif m == 15 or m == 30:
        time_in_words = minute_map[m] + " past " + hour
    elif m == 45:
        time_in_words = minute_map[15] + " to " + minute_map[h+1]
    elif m <= 20:
        if m == 1:
            time_in_words = minute_map[m] + " minute past " + hour
        else:
            time_in_words = minute_map[m] + " minutes past " + hour
    elif m < 30:
        time_in_words = minute_map[(m//10)*10] + " " + minute_map[m%10] + " minutes past " + hour
    elif m < 40:
        time_in_words = minute_map[((60-m)//10)*10] + " " + minute_map[(60-m)%10] + " minutes to " + minute_map[h+1]
    else:
        time_in_words = minute_map[60-m] + " minutes to " + minute_map[h+1]
    
    return time_in_words


h = int(input())
m = int(input())
print(timeInWords(h, m))