#include <iostream>
#include "../include/BirthdayRecord.h"

int main(){
	BrithdayRecord br1 = BrithdayRecord();
	br1.setName("王之煜");
	br1.setSolar(1989, 10, 13);
	br1.setRemark("全宇宙最纯洁的人。");
	std::cout << br1.info();
	return 0;
}