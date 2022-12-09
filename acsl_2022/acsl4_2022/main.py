"""
ok this one seems like it sucks but lets go

first thing to do is to create the recursive mandelbrot function

"""

# we have the input with the real and imaginary components of a complex number, a + bi
# lets store them in a list as [a,b] and forget the i, its unnessecary in the scope of the problem
# 0 can be represented as [0,0]
# we can mult via [a,b][c,d] = [(a*c - b*d), (a*d + b*c)]
# adding [a,b] + [c,d] = [(a+c), (b+d)]
# abs val of [a,b] = (a**2 + b**2)**(1/2)


def mult_cmplx(first_number, second_number): # where args are of form [a,b]
    a = first_number[0]
    b = first_number[1]
    c = second_number[0]
    d = second_number[1]
    
    multiplied = [round((a*c - b*d),3), round((a*d + b*c),3)]
    return multiplied

def add_cmplx(first_number, second_number): # where args are of form [a,b]
    a = first_number[0]
    b = first_number[1]
    c = second_number[0]
    d = second_number[1]
    
    added = [round((a+c),3), round((b+d),3)]
    return added

def abs_val(complex_num):
    a = complex_num[0]
    b = complex_num[1]

    abs = round((a**2 + b**2)**(1/2),3)

    return abs

def recursive_brot(init_val, const, ans_list):
    

    squared = mult_cmplx(init_val, init_val)
    ans = add_cmplx(squared, const)

    ans_list.append(ans)

    for i in range(len(ans_list)-1):
        if ans == ans_list[i]:
            return len(ans_list) - i - 1

    if abs_val(ans) >= 4:
        return 0
    
    else:
        return recursive_brot(ans, const, ans_list)


# ok the above seems to be just fine
# now we need to find all of the incrememtns

def list_increments(s1, s2, e1, e2, increment):
    list_of_all = []

    vert_steps = round((e2-s2)/increment)

    horiz_steps = round((e1-s1)/increment)


    for i in range(vert_steps+1):

        for j in range(horiz_steps+1):   
            list_of_all.append([round(s1+(j*increment),4), s2])

        s2 = round(s2+increment,4)
    
    return list_of_all


def numFibonacciCycles(realPartLL, imagPartLL, realPartUR, imagPartUR, incr):

    list_of_all = list_increments(realPartLL, imagPartLL, realPartUR, imagPartUR, incr)

    fib_list = []

    for i in range(len(list_of_all)):
        ans_list = []

        sln = recursive_brot([0,0,], list_of_all[i], ans_list)
        if sln in (1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377):
            fib_list.append(sln)

    return len(fib_list)

print(numFibonacciCycles(0.1, 0.2, 0.4, 0.35, 0.075))
