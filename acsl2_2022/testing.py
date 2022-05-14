
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# l = list(alphabet)
# # l = l[::-1]
# # print(l)

# # s_idx = l.index("h")
# # rotate_int = 788    
# # ttl_to_go = s_idx + rotate_int
# # print(l[ttl_to_go % len(l)])

# def wrap(letter1, rotate_coef, chr_idx, abet=l):

#     if chr_idx % 2 == 1:
#         abet = abet[::-1]

#     s_idx = abet.index(letter1)
#     total_r_coef = s_idx + rotate_coef
#     wrapped_coef = total_r_coef % len(abet)

#     return abet[wrapped_coef]

# h = wrap("h", 788, 5)
# print(h)
# h = wrap("h", 71, 4)
# print(h)

# def fibonacci(n1, n2, length):
#     flist = list()
#     flist.append(n1)
#     flist.append(n2)

#     for i in range(length-2):
#         n_to_append = flist[-1] + flist[-2]
#         flist.append(n_to_append)

#     return flist

# print(fibonacci(3,7,12))

# '''
# acsl contest 2 2022

# fibonacci cipher coding/decoding

# '''



alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)

def wrap(letter1, rotate_coef, chr_idx, abet=alphabet):

    if chr_idx % 2 == 1: # subtracts or adds depending on which character in string it is
        abet = abet[::-1]

    s_idx = abet.index(letter1)
    total_r_coef = s_idx + rotate_coef
    wrapped_coef = total_r_coef % len(abet)

    return abet[wrapped_coef]

def fibonacci(n1, n2, length):
    flist = list()
    flist.append(n1)
    flist.append(n2)

    for i in range(length-2):
        n_to_append = flist[-1] + flist[-2]
        flist.append(n_to_append)

    return flist


def fibCypher(option, num1, num2, key, msg):

    n1 = num1
    n2 = num2


    if option == "E":

        msg_len = len(msg)

        fib = fibonacci(n1, n2, msg_len)
        offset_list = []
        for i in range(len(fib)):
            offset_letter = wrap(key, fib[i], i)
            offset_number= ord(offset_letter)
            offset_list.append(offset_number)

        char_ord_list = []
        for char in msg:
            c_ord = ord(char)
            char_ord_list.append(c_ord)

        final_number_list = []
        for i in range(msg_len):
            final_sum = char_ord_list[i] + (3*offset_list[i])
            final_number_list.append(final_sum)

        final_number_list = [str(element) for element in final_number_list]
        final_coded = " ".join(final_number_list)
        return final_coded

    elif option == "D":

        num_list = msg.split(" ")
        msg_len = len(num_list)

        fib = fibonacci(n1, n2, msg_len)
        offset_list = []
        for i in range(len(fib)):
            offset_letter = wrap(key, fib[i], i)
            offset_number = ord(offset_letter)
            offset_list.append(offset_number)
        
        chr_list = []
        for i in range(msg_len):
            subtract_this = 3*offset_list[i]
            decoded_ord = int(num_list[i]) - subtract_this
            decoded_chr = chr(decoded_ord)
            chr_list.append(decoded_chr)
        
        return chr_list



# print(fibCypher("E", 3, 7, "h", "ACSL Sr-5 c2"))
print(fibCypher("D", 3, 7, "h", "386 358 425 415 347 419 405 402 377 377 390 416"))

