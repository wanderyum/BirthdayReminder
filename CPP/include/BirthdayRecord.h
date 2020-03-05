/*********************************
* BirthdayRecord.h
* 用于记录生日。
* Created by Manfredo
* 2020/3/5
*********************************/

#ifndef BIRTHDAY_RECORD_H
#define BIRTHDAY_RECORD_H
#define NAME_MAX 30
#define REMARK_MAX 100
#include <string>
#include <iostream>

class BrithdayRecord{
public:
    BrithdayRecord();
    ~BrithdayRecord();
    
    short setName(std::string name);
    short setSolar(short year, short month, short day);
    short setLunar(short year, short month, short day);
    short setRemark(std::string remark);
    friend std::ostream &operator<<(std::ostream &os, BrithdayRecord &br);
    
	char name[NAME_MAX]={0};        // 姓名
	short solar[3];                 // 公历生日
	short lunar[3];                 // 农历生日
	char remark[REMARK_MAX]={0};    // 备注
};
#endif