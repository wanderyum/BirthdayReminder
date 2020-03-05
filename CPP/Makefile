VPATH = src:include:lib
objs = BirthdayRecord.o

test.exe: $(objs)
	g++ -o bin/test.exe src/test_BirthdayRecord.cpp $(objs)

BirthdayRecord.o: BirthdayRecord.h

.PHONY: clean
clean:
	-rm bin/test.exe $(objs)