
fib = [1,1,2,3,5]

def red(time, num):
    time[0] += num

def green(time, num):
    time[1] += (num*5)

def blue(time, num):
    time[2] += (num*5)

color_key = {"R":["red"], "G":["green"], "B":["blue"], "Y":["red", "green"], "M":["red", "blue"], "C":["blue", "green"]}

def handle_overflow(time):
        
    if time[2] >= 60:
        time[2] = time[2]%60
        time[1] += 1
    if time[1] >= 60:
        time[1] = time[1]%60
        time[0] += 1
    if time[0] >= 12:
        time[0] = time[0]%12

    return time

def findTime(cstr):
    time =[0,0,0]
    cli = list(cstr)
    for idx in range(len(cli)):
        if cli[idx] in color_key:
            for i in range(len(color_key[cli[idx]])):
                globals()[color_key[cli[idx]][i]](time, fib[idx])
        else:
            continue
    
    time = handle_overflow(time)
    for idx in range(len(time)):
        time[idx] = str(time[idx])
        time[idx] = time[idx].zfill(2)

    return ":".join(time)





