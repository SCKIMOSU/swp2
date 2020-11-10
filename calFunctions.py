# This is the calFunctions python file for the mycalc10.py under the directory of 07-2 in swp2 class.

from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

#def decToRoman(numStr):
#    return 'dec -> Roman'

def decToRoman(numStr):

    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    result = ''

    while n >= 1000:
        result += "M"
        n -= 1000
    while n >= 900:
        result += "CM"
        n -= 900
    while n >= 500:
        result += "D"
        n -= 500

    while n >= 400:
        result += "CD"
        n -= 400
    while n >= 100:
        result += "C"
        n -= 100
    while n >= 90:
        result += "XC"
        n -= 90
    while n >= 50:
        result += "L"
        n -= 50
    while n >= 40:
        result += "XL"
        n -= 40
    while n >= 10:
        result += "X"
        n -= 10
    while n >= 9:
        result += "IX"
        n -= 9
    while n >= 5:
        result += "V"
        n -= 5
    while n >= 4:
        result += "IV"
        n -= 4
    while n >= 1:
        result += "I"
        n -= 1

    return result


'''''''''
# 리스트와 사전을 이용해 보자!
def decToRoman(numStr):

    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n>= 4000:
        return 'Error!'

    numberBreaks = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letters = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
              100: 'C',    90: 'XC',   50: 'L',    40: 'XL',
               10: 'X',      9: 'IX',       5: 'V',      4: 'IV',
                  1: 'I'
    }

    result = ''
    for value in numberBreaks:
            while n >= value:
                    result += letters[value]
                    n -= value
    return result
'''''''''

'''''''''
def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result
    
'''''''''
def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    romans = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    result = ''
    for value in romans.keys():
        while n >= value:
            result += romans[value]
            n -= value

    return result

