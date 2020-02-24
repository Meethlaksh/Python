#Write a python function to find the max of three numbers.

def m1(l):
    d = max(l)
    return d

l = [1,2,3,4,5]
print(m1(l))


#Write a python function to sum up all the items in a list
e = sum([1, 2, 3, 4, 5])
print(e)


#multiply all the items in a list

import math
x = [1,2,3,4]
f = math.prod(x)
print(f)

#function that checks whether a passed string is palindrome
str1 = 'racecar'
str2 = ''.join(reversed(str1))
print(str2)
if str1 == str2:
    print ('yes')
else:
    print('no')    

#string is a pangram
str3 = "The quick brown fox jumps over the lazy dog"
alphabet = ["a","b","c","d"]
value = True
for x in alphabet:
    if x not in str3:
        value = False

print(value)




