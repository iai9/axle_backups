
fib = [1,1,2,3,5]

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

    time = [0,0,0]

    split_str = list(cstr)
    for color in range(len(split_str)):
        num = fib[color]
        if split_str[color] == "R":
            time[0] += num
        elif split_str[color] == "G":
            time[1] += (num*5)
        elif split_str[color] == "B":
            time[2] += (num*5)
        elif split_str[color] == "Y":
            time[0] += num
            time[1] += (num*5)
        elif split_str[color] == "M":
            time[0] += num
            time[2] += (num*5)
        elif split_str[color] == "C":
            time[1] += (num*5)
            time[2] += (num*5)
        elif split_str[color] == "W":
            continue


    time = handle_overflow(time)


    for idx in range(len(time)):
        time[idx] = str(time[idx])
        time[idx] = time[idx].zfill(2)

    return ":".join(time)

print(findTime("YYYYY"))