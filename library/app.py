
import c_module
from datetime import datetime


def fib_python(n):
    if n < 3:
        return 1
    return fib_python(n - 1) + fib_python(n - 2)


# start = datetime.now()
# res = fib_python(38)
# stop =  datetime.now() - start


# print("Result - {0}, Time - {1}".format(res, stop))
# Result - 39088169, Time - 0:00:11.219167
# Result - 39088169, Time - 0:00:11.390807


start = datetime.now()
res2 = c_module.c_fib(50)
stop =  datetime.now() - start

print("Result2 - {0}, Time2 - {1}".format(res2, stop))
# Result2 - 39088169, Time2 - 0:00:00.083142
# Result2 - 39088169, Time2 - 0:00:00.088332