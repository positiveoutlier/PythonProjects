"""     Created by Chantal Worp, 24/01/2017
        Solution to Problem Set 1
        Introduction to Computer Science and 
        Programming using Python (EDX)

Problem Set 1:
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
       Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
       Longest substring in alphabetical order is: abc
"""

s = input('Type a string: ')
s = s.lower()

#Variable 'overall_answer' will contain substring of strings in which the letters are in alphabetical order
overall_answer = []                               

#Maximum number of outermost loops is determined by number of letters in s
for letters in range(len(s)):
    search_string = s[letters:]     #search_string slices s to ensure that every substring of s is investigated
    i = 0                                 # i is used as counter, set to zero in every outermost loop
    subanswer = ""                        #re-initialising subanswer
    subanswer += s[letters]               #the first letter of every new subset is added to subanswer
    while i < (len(search_string)-1):      #Innerloop, will loop as long as i is smaller than the number of letters in search_string minus 1 (to avoid index getting out of range)
        first_letter = search_string[i]     # Determines first letter to be compared
        second_letter = search_string[i+1]   # Determines second letter to be compared
        if first_letter <= second_letter:    # If first letter is smaller than or equal to second letter, it means they are in alphabetical order
            subanswer += second_letter       # second letter will be added to subanswer (first letter was already added)
            i += 1                           # counter increases with 1
        else: 
            overall_answer.append(subanswer) # If first letter is greater than second letter, then they are not in alphabetical order. Second letter does not get added to subanswer
            break                            # subanswer gets added to list overall_answer and inner loop breaks, a new outerloop starts
    if i == (len(search_string)-1):          # If counter i equals the length of search_string, then subanswer gets appended to overall_answer and a new outerloop starts
        overall_answer.append(subanswer)

# after running the code above, overall_answer will be a list with substrings in alphabetical order
# the answer is then the longest substring in list overall_answer
ans = max(overall_answer, key=len)
print("Longest substring in alphabetical order is: " + ans)