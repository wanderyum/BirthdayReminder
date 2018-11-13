from LunarGenerator import solar2lunar, lunar2solar
class birthday():
    def __init__(self, name, bday, lunar_calendar=False, celebrate=None):
        self.name = name
        if len(bday) == 4:
            self.year = None
            self.month = bday[0:2]
            self.day = bday[2:4]
        elif len(bday) == 8:
            self.year = bday[0:4]
            self.month = bday[4:6]
            self.day = bday[6:8]
        else:
            raise Exception('The fomat of birthday must be either \"YYYYMMDD\" or \"MMDD\"!')
        self.lunar_calendar = lunar_calendar
        if celebrate is None:
            self.celebrate = 'lunar' if lunar_calendar else 'solar'
        else:
            self.celebrate = celebrate
    
    def show(self, lang='Chinese'):
        if lang == 'Chinese':
            print('姓名:', self.name)
            print('农历生日:' if self.lunar_calendar else '阳历生日:')
            if self.year:
                print('{}年{}月{}日'.format(self.year, self.month, self.day))
            else:
                print('{}月{}日'.format(self.month, self.day))
            if self.celebrate == 'solar':
                print('过阳历生日\n')
            elif self.celebrate == 'lunar':
                print('过农历生日\n')
            elif self.celebrate == 'both':
                print('过阳历、农历生日\n')
    
    def get_lunar_birthday(self):
        if self.lunar_calendar:
            return int(self.month), int(self.day)
        else:
            return solar2lunar(self.year+self.month+self.day)
    def get_solar_birthday(self, leap_month=False):
        if self.lunar_calendar:
            return lunar2solar(self.year+self.month+self.day)[1:]
        else:
            return int(self.month), int(self.day)
            
def tup2str(tup):
    res = str(tup[0])
    for i in [1, 2]:
        tmp = str(tup[i])
        if len(tmp) < 2:
            tmp = '0'+tmp
        res += tmp
    return res
    
if __name__ == '__main__':
    b1 = birthday('王之煜', '19891013')
    b2 = birthday('黎娇龙', '19910623', True, 'both')
    b1.show()
    b2.show()
    print(b2.get_lunar_birthday())
    print(b1.get_lunar_birthday())
    print(b1.get_solar_birthday())
    print(b2.get_solar_birthday())
    