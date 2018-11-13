from data.DataGernerator import birthdays
from LunarGenerator import solar2lunar, lunar2solar
from auxi import tup2str
import time
t = time.localtime(time.time())[0:3]
#t = (2018, 11,22)
solar = (t[1], t[2])
lunar = solar2lunar(tup2str(t))
res = ''
for item in birthdays:
    #item.show()
    if (item.celebrate == 'solar' or item.celebrate == 'both') and item.get_solar_birthday() == solar:
        res += '今天是{}的生日！(公历)\n'.format(item.name)
    elif (item.celebrate == 'lunar' or item.celebrate == 'both') and item.get_lunar_birthday() == lunar:
        res += '今天是{}的生日！(农历)\n'.format(item.name)
if len(res):
    print(res)
else:
    print('今天没有人过生日。')