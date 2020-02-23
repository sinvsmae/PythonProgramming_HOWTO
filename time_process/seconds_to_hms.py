# Given seconds, return a string of HH:MM:SS. 不满两位自动补充0
# Updated version， -> 如果超过24h，#day, HH:MM:SS,
# Option 1

import math


def time_convert1(seconds_sum):
    """暴力解，"""
    M, H = 60, 60 ** 2
    hours = str(seconds_sum // H)
    minutes = str(seconds_sum % H // M)
    seconds = str(seconds_sum % H % M)
    if len(minutes) == 1:
        minutes += '0'
    if len(seconds) == 1:
        seconds += '0'
    return str(f'{hours} : {minutes} : {seconds}')


if "__name__" == "__main__":
    print


print(time_convert(s))