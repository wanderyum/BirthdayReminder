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
}

short BrithdayRecord::setLunar(short year, short month, short day){
    this->lunar[0] = year;
    this->lunar[1] = month;
    this->lunar[2] = day;
}

short BrithdayRecord::setRemark(std::string remark){
    if (remark.size() > REMARK_MAX){
        return 1;
    }
    for (int i=0; i<remark.size(); i++){
        this->remark[i] = remark[i];
    }
}

std::ostream &operator<<(std::ostream &os, BrithdayRecord &br){
    os << "Info of " << br.name;
    os << "\nSolar Birthday: " << br.solar[0] << "/" << br.solar[1] << "/" << br.solar[2];
    os << "\nLunar Birthday: " << br.lunar[0] << "/" << br.lunar[1] << "/" << br.lunar[2] << '\n';
    if (br.remark[0]){
        os << br.remark << '\n';
    }
    return os;
}