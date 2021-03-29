.POSIX:
CC      = cc
CFLAGS  = -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) pyapi.cpp -o pyapi$(python3-config --extension-suffix)
LDFLAGS =
LDLIBS  =

all: tests/tests tests/dump

tests/tests: tests/tests.c aes128ni.h
	$(CC) $(LDFLAGS) $(CFLAGS) -o $@ tests/tests.c $(LDLIBS)

tests/dump: tests/dump.c aes128ni.h
	$(CC) $(LDFLAGS) $(CFLAGS) -o $@ tests/dump.c $(LDLIBS)

check: tests/tests
	tests/tests

clean:
	rm -f tests/dump tests/tests