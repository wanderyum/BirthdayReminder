# 1950年2月17日为正月初一
D = {}                 #1   2   3   4   5   6   7   8   9  10  11  12
D[1950] = ['19500217', 29, 30, 30, 29, 30, 30, 29, 29, 30, 29, 30, 29]
D[1951] = ['19510206', 30, 29, 30, 30, 29, 30, 29, 30, 29, 30, 29, 30]
D[1963] = ['19630125', 30, 29, 30, [29, 29], 30, 29, 30, 29, 30, 30, 30, 29]
D[1989] = ['19890206', 30, 29, 29, 30, 29, 30, 29, 30, 29, 30, 30, 30]
D[1991] = ['19910215', 29, 30, 29, 29, 30, 29, 29, 30, 29, 30, 30, 30]
D[2017] = ['20170128', 29, 30, 29, 30, 29, [29, 30], 29, 30, 29, 30, 30, 30]
D[2018] = ['20180216', 29, 30, 29, 30, 29, 29, 30, 29, 30, 29, 30, 30]
D[2019] = ['20190205', 30, 29, 30, 29, 30, 29, 29, 30, 29, 29, 30, 30]


def is_leap_year(year):
    if year % 4:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True

def get_days(year, month):
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        l[1] = 29
    return l[month-1]
    
def next_day_solar(year, month, day):
    if day == get_days(year, month):
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        day = 1
    else:
        day += 1
    return year, month, day
    
def next_day_lunar(year, month, day, rerun):
    day_num = D[year][month]
    if type(day_num) is type([1,2]):
        if rerun:
            if day == day_num[1]:
                day = 1
                month += 1
                return month, day, True
            else:
                day += 1
                return month, day, True
        else:
            if day == day_num[0]:
                day = 1
                return month, day, True
            else:
                day += 1
                return month, day, False
    else:
        if day == D[year][month]:
            month += 1
            day = 1
        else:
            day += 1
        return month, day, False

def compare_solar(date1, date2):
    sign = 1
    if date1 > date2:
        date1, date2 = date2, date1
        sign = -1
    count = 0
    year = int(date1[:4])
    month = int(date1[4:6])
    day = int(date1[6:])
    year2 = int(date2[:4])
    month2 = int(date2[4:6])
    day2 = int(date2[6:])
    while year != year2 or month != month2 or day != day2:
        year, month, day = next_day_solar(year, month, day)
        count += 1
    
    return count * sign
    
def solar2lunar(date):
    sy = int(date[0:4])
    if date < D[sy][0]:
        year = sy - 1
    else:
        year = sy
    count = compare_solar(D[year][0], date)
    lm, ld = 1, 1
    while count > 0:
        # 有闰月
        if type(D[year][lm]) is type([1,2]):
            tmp = sum(D[year][lm])
            if count >= tmp:
                count -= tmp
                lm += 1
            else:
                if count >= D[year][lm][0]:
                    count -= D[year][lm][0]
                    ld += count
                    count = 0
                else:
                    ld += count
                    count = 0
        else:
            if count >= D[year][lm]:
                count -= D[year][lm]
                lm += 1
                
            else:
                ld += count
                count = 0
    return lm, ld
    
def lunar2solar(date, leap_month=False):
    ly = int(date[0:4])
    lm = int(date[4:6])
    ld = int(date[6:8])
    sdate = D[ly][0]
    sy = int(sdate[0:4])
    sm = int(sdate[4:6])
    sd = int(sdate[6:8])
    m, d = 1, 1
    rerun = False
    while m!=lm or d!=ld:
        m, d, rerun = next_day_lunar(ly, m, d, rerun)
        sy, sm, sd = next_day_solar(sy, sm, sd)
    for item in D[ly]:
        if type(item) is type([1,2]) and leap_month:
            m, d, rerun = next_day_lunar(ly, m, d, rerun)
            sy, sm, sd = next_day_solar(sy, sm, sd)
            while m!=lm or d!=ld:
                m, d, rerun = next_day_lunar(ly, m, d, rerun)
                sy, sm, sd = next_day_solar(sy, sm, sd)
    return sy, sm, sd
    
    
if __name__ == '__main__':
    print(compare_solar('19891012', '19891013'))
    test_cases1 = ['20180102', '20181013', '19891013', '20170304', '20170802', '20171231']
    for item in test_cases1:
        m, d = solar2lunar(item)
        print(item + ': 阴历' + str(m) + '月' + str(d) + '日')
    test_cases2 = ['19910623', '20170630']
    for item in test_cases2:
        y, m, d = lunar2solar(item, False)
        print('阴历'+item+'为阳历'+str(y)+'年'+str(m)+'月'+str(d)+'日')