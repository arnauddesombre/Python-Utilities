# https://code.activestate.com/recipes/266464-date-to-day-of-the-week/
def weekday(day, month, year):
    d, m, y = day, month, year
    if m < 3:
        z = y - 1
    else:
        z = y
    dayofweek = (23 * m // 9 + d + 4 + y + z // 4 - z // 100 + z // 400)
    if m >= 3:
        dayofweek -= 2
    dayofweek = dayofweek % 7
    # 0: Sunday ... 6: Saturday
    return dayofweek

def isleap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# verify that periodicity is 2800 years
N = 2800
if __name__ == "__main__":
    for year in range(N):
        if isleap(year):
            if not isleap(year + N):
                print("ERROR")
            days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            if isleap(year + N):
                print("ERROR")
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month in range(1, 13):
            for day in range(1, days[month - 1] + 1):
                w1 = weekday(day, month, year)
                w2 = weekday(day, month, year + N)
                if w1 != w2:
                    print("ERROR")
    
