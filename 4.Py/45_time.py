import time

# convert a time expressed in seconds since epoch to readable string
print(time.ctime(0))

# seconds since epoch
print(time.time())

# current date and time
print(time.ctime(time.time()))

time_obj = time.localtime()
print(time_obj)

local_time=time.strftime('%B %d %Y %H:%M:%S',time_obj)
print(local_time)

time_string = "31 July 2024"
time_object = time.strptime(time_string,"%d %B %Y")
print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
asctime = time.asctime(time_tuple)
print(asctime)

# time tuple to seconds since epoch
mktime = time.mktime(time_tuple)
print(mktime)