def WhichFib(fibo):
    
    i = 1
    f = 0
    counter = 1
    while i != fibo:
        counter += 1
        i = i+f
        f = i-f

    return counter

def PascalsTriangle(rows):

    pascal_tri = []

    for n in range(rows):
        row_2_append = None

        if n <= 4:
            row_2_append = [int(char) for char in (str(11**n))]
        else:
            prev_line = pascal_tri[n-1]
            row_2_append = [(prev_line[idx-1]+prev_line[idx]) for idx in range(1, len(prev_line))]
            row_2_append.insert(0,1)
            row_2_append.append(1)

        pascal_tri.append(row_2_append)

    return pascal_tri

def Diagonals(fib_idx):
    tri = PascalsTriangle(fib_idx)

    if fib_idx == 1:
        return [[1]]

    diag_list = []

    for i in range(fib_idx-1, 0, -1):
        j = 0
        diag_2_append = []

        while len(tri[i-1]) >= j and i>0:
            diag_2_append.append(tri[i][j])
            i = i-1
            j = j+1

        diag_list.append(diag_2_append)

    return diag_list

def total_diagonals(diag_list):
    total_diags = []
    
    for i in range(len(diag_list)):
        total_diags.extend(diag_list[i])

    return total_diags

def occurs_once(total_diag_list):
    l = [x for x in total_diag_list if total_diag_list.count(x) ==1]
    return len(l)

def countUniqueValues(fibNumber):
    
    fib_idx = WhichFib(fibNumber)
    diag_list_frag = Diagonals(fib_idx)
    whole_diag_list = total_diagonals(diag_list_frag)
    howmany = occurs_once(whole_diag_list)

    return int(howmany)