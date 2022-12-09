# def duplicate_letters(word):
#     l = []
#     d = []
#     for letter in word:
#         if letter not in l:
#             l.append(letter)
#         elif letter in l:
#             d.append(letter)
#     return d

# def develop_colors(target, guess): # target is a list of 5 letters and so is guess

#     color_list = ['-', '-', '-', '-', '-'] # color list that assumes all letters are wrong
#     dupes = duplicate_letters(guess)
#     d_list = []
    
#     for idx in range(len(guess)): # we go through the guess to see for greens
#         if guess[idx] == target[idx]: # if the letters are exact same pos and val
#             color_list[idx] = "g" # we make the position green
#             if guess[idx] in dupes:
#                 d_list.append(guess[idx])
    
#     used = [] # list for used letters
#     for idx in range(len(guess)): # i shouldve put this above green but whatever it works and im timed
#         # if (guess[idx] in target) and (guess[idx] != target[idx]) and (guess[idx] not in used) and (guess[idx] not in d_list): # if the letter is is the target but not in the exact position and not already used left to right
#         if (guess[idx] in target) and (color_list[idx] != "g") and (guess[idx] not in used) and (guess[idx] not in d_list):
#             color_list[idx] = "y" # then we add yellow to the color list
#         used.append(guess[idx]) # we add the letter to the used list

#     return color_list # well return the color list

# def develop_info(word_list): # color list is 2d list with [color, word]
#     info = [0,0,0,0,0] # list that will store frequency of greens and yellows with greens in idx 0 and yellow in idx 
#     # gyflv will also store whether or not the first/last letter is green and also how many green vowels it has
#     # order is gcount, ycount, first, last, vowel count

#     for color in word_list[0]:
#         if color == "g":
#             info[0] += 1
#         elif color == "y":
#             info[1] += 1
    
#     if word_list[0][0] == "g":
#         info[2] = 1
    
#     if word_list[0][-1] == "y":
#         info[3] = 1

#     for idx in range(5):
#         if (word_list[0][idx] == "g") and (word_list[1][idx] in ['a', 'e', 'i', 'o', 'u']):
#             info[-1] += 1
    
#     return info

# def sorting_(big_list): # big list is a list of word lists, that is it is of the form [[c, w, i], [c, w, i]...] where c and w are also lists

#     s = sorted(big_list, key=lambda x: (x[-1][0], x[-1][1], x[-1][2], x[-1][3], x[-1][4]), reverse=True)
#     for idx in range(len(s)):
#         for idx2 in range(idx+1, len(s)):
#             if s[idx][-1] == s[idx2][-1]:
#                 s[idx][1], s[idx2][1] = min(s[idx][1], s[idx2][1]), max(s[idx][1], s[idx2][1])
#     return s

# def findMatch(word, guesses):
#     guesses = guesses.strip()
#     word = word.strip()
#     guesses = guesses.split(' ')

#     for idx in range(len(guesses)):
#         if len(guesses[idx]) != 5:
#             del guesses[idx]

#     guesses = sorted(guesses)
#     big_holder = []
#     for guess in guesses:
#         h = []
#         cinfo = develop_colors(word, list(guess))
#         h.append(cinfo)
#         h.append(list(guess))
#         big_holder.append(h)

#     for word in big_holder:
#         a = develop_info(word)
#         word.append(a)
    
#     sorted_l = sorting_(big_holder)

#     for i in range(0,6):
#         if sorted_l[i][-1][0] == 0 and sorted_l[i][-1][1] == 0:
            
#             used_ls = []
#             for row in sorted_l:
#                 for letter in row[1]:
#                     if letter not in used_ls:
#                         used_ls.append(letter)
#             unused_ls = []
#             for char in list("abcdefghijklmnopqrstuvwxyz"):
#                 if char not in used_ls:
#                     unused_ls.append(char)
            
#             return ''.join(unused_ls)
    
#     h = []
#     for i in range(0,6):
#         temp = ''.join(sorted_l[i][1])
#         h.append(temp)
    
#     sln = ' '.join(h)
#     sln.strip()
#     return sln