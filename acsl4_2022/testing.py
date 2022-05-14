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

ans_list = []

print(recursive_brot([0,0], [0.1, 0.2], ans_list))
print(ans_list)