
# absolute speed options
CFLAGS += \
    -O3 \
    -march=native \
    -mtune=native \
    -fomit-frame-pointer \
    -finline-functions \
    -finline-limit=1000 \
    -finline-small-functions \
    -funroll-loops \
    -funroll-all-loops \
    -fprefetch-loop-arrays \
    -ftracer \
    -fpeel-loops \

maps: maps.o
	$(CC) $(CFLAGS) -o maps maps.o

maps.o: maps.c
	$(CC) $(CFLAGS) -c maps.c
