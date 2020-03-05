#include "../include/BirthdayRecord.h"

BrithdayRecord::BrithdayRecord(){
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
    std::string res = "";
    bool flag = 0;
    if (i<0){
        flag = 1;
        i = -i;
    }
    res = (char)('0'+i%10) + res;
    while(i/10){
        i /= 10;
        res = (char)('0'+i%10) + res;
    }
    return flag>0?"-"+res:res;
}
