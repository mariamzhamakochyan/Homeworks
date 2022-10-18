def verbose(num):
    dict_ = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
            "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten",
            "11": "eleven", "12": "twoelfe", "13": "thirteen", "14": "fourteen",
            "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen",
            "19": "nineteen", "20": "twenty", "30": "thirty", "40": "forty",
            "50": "fifty", "60": "sixty", "70": "seventy", "80": "eighty", "90": "ninety",
            "100": "hundred", "1000": "thousand"
            }
    if num <= 20:
        return dict_['num']
    elif 20 < num < 100:
        res = dict_[num // 10]
        res1 = [num % 10]
        res = ''.join(res1)
        return res
    elif 100 <= num < 1000:
        res = dict_[num // 100]
        num -= res * 100
        res1 = dict_[num // 10]
        res2 = dict_[num % 10]
        ress = res + "hundred" + res1 + '-' + res2
        return ress
    elif num >= 1000:
        res = dict_[num // 1000]
        res11 = dict_[num // 100]
        num -= res * 100
        res1 = dict_[num // 10]
        res2 = dict_[num % 10]
        ress = res + "thousand" + res11 + 'hundred' + res1 + '-' + res2
        return ress


num = int(input("Enter a number: "))
print(verbose(num))
