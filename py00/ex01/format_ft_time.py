import time
import calendar
struct_time = time.gmtime()
precise_epoch = time.time_ns() / (10 ** 9)
formated = time.asctime(struct_time)
s_epoch = calendar.timegm(struct_time)
string = "Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation"
print(string.format(precise_epoch, s_epoch))
splited = formated.split()
print(f"{splited[1]} {splited[2]} {splited[4]}")