# Metacharacters
# Metacharacters are what make regular expressions more powerful than normal string methods.
# They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel".

# The existence of metacharacters poses a problem if you want to create a regular expression (or regex) that matches a literal metacharacter, such as "$". You can do this by escaping the metacharacters by putting a backslash in front of them.
# However, this can cause problems, since backslashes also have an escaping function in normal Python strings. This can mean putting three or four backslashes in a row to do all the escaping.


import re

print("Ex1")

# "^" means starts with 
# "$" means ends with 
pattern = r"^gr.y$" 

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")
   
# Simple Metacharacters
# Write a program that takes a word as input, and outputs "Match" if the word has 4 letters, starts with "m" and ends with "e".
# The program should output "No match" if these mentioned requirements aren't satisfied.

# Sample Input
# mine

# Sample Output
# Match

print("Ex2")

# word = input()
word = "milk"

# define a regular expression pattern
pattern = r'^m[a-z]*e$'

# use the re.match() function to check if the word matches the pattern
if re.match(pattern, word) and len(word) == 4:
    print("Match")
else:
    print("No match")

# Some more metacharacters are *, +, ?, { and }.
# These specify numbers of repetitions.
# The metacharacter * means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible. 
# The "previous thing" can be a single character, a class, or a group of characters in parentheses.

print("Ex3")

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")
  
print("Ex2:") 

# input
text = input()

# re pattern to match hashtags
pattern = r"#\w+"

# use re.findall() to find all hashtags in the text
hashtags = re.findall(pattern, text)

# print
for hashtag in hashtags:
    print(hashtag)
