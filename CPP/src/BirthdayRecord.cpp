#include "../include/BirthdayRecord.h"
#include <ctime>

BrithdayRecord::BrithdayRecord(){
    which = 's';
}
BrithdayRecord::BrithdayRecord(std::string name){
    BrithdayRecord();
    setName(name);
}
BrithdayRecord::~BrithdayRecord(){
}

short BrithdayRecord::setName(std::string name){
    if (name.size() > NAME_MAX){
        return 1;
    }
    for (int i=0; i<name.size(); i++){
        this->name[i] = name[i];
    }
    return 0;
}

short BrithdayRecord::setSolar(short year, short month, short day){
    this->solar[0] = year;
    this->solar[1] = month;
    this->solar[2] = day;
    return 0;
}

short BrithdayRecord::setLunar(short year, short month, short day){
    this->lunar[0] = year;
    this->lunar[1] = month;
    this->lunar[2] = day;
    return 0;
}

short BrithdayRecord::setRemark(std::string remark){
    if (remark.size() > REMARK_MAX){
        return 1;
    }
    for (int i=0; i<remark.size(); i++){
        this->remark[i] = remark[i];
    }
    return 0;
}

bool BrithdayRecord::isSolarBirthday(short month, short day){
    if (solar[1] == month && solar[2] == day) return true;
    else return false;
}

bool BrithdayRecord::isLunarBirthday(short month, short day){
    if (lunar[1] == month && lunar[2] == day) return true;
    else return false;
}

char BrithdayRecord::isBirthday(short year, short month, short day){
    if (which == 's' || which == 'b'){
        if (isSolarBirthday(month, day)) return 's';
    }
    return 'n';
}

std::string BrithdayRecord::checkToday(){
    time_t now = time(0);
    tm *ltm = localtime(&now);
    short solar_year = 1900+ltm->tm_year;
    short solar_month = 1+ltm->tm_mon;
    short solar_day = ltm->tm_mday;
    if (isBirthday(solar_year, solar_month, solar_day) == 's'){
        std::string res = "今天是"+(std::string)name+"的生日: 公历"+i2s(solar[1])+"月"+i2s(solar[2])+"日";
        return res;
    }
    else {
        std::string res;
        //res = "今天是"+i2s(solar_year)+"年"+i2s(solar_month)+"月"+i2s(solar_day)+"日";
        return res;
    }
}

std::string BrithdayRecord::info(){
    std::string res = "Info of " + (std::string)name;
    res += ("\nSolar Birthday: "+i2s(solar[0])+"/"+i2s(solar[1])+"/"+i2s(solar[2]));
    res += ("\nLunar Birthday: "+i2s(lunar[0])+"/"+i2s(lunar[1])+"/"+i2s(lunar[2])+"\n");
    if (remark[0]){
        res += ("Remarks: "+(std::string)remark+"\n");
    }
    return res;
}

std::string BrithdayRecord::i2s(int i){
    char charArr[12] = {0};
    bool flag = 0;
    if (i<0){
        flag = 1;
        i = -i;
    }
    short si;
    for (si=10; si>0; si--){
        charArr[si] = '0' + i%10;
        if (i/10){
            i /= 10;
        }
        else{
            si--;
            break;
        }
    }
    if (flag>0) charArr[si] = '-';
    else si++;
    std::string res = charArr+si;
    return res;
}
