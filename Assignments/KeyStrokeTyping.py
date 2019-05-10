password = raw_input()
timings = raw_input()

password = password.split(",")
password = password[:len(password) / 2 +1]
password = "".join(password)

print password
timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings)/2 +1]
keyinterval = timings[len(timings)/2 +1:]

print "key press times = {}".format(keypress)
print "key intervals = {}".format(keyinterval)
