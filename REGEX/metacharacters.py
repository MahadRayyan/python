import re
a = "charlie and the chocolate factory"
b="mahadrayaan@gmail.com"
c="hello"
d="xxyz xyyz xyyxz zyx xxyyzzy xyz xxx"

#\ is used when we are search special character in a string like .(which its self a meta character)
match=re.search(r"\.",b)


# [] is used to find a character in string
match=re.findall(r"[a]",b)  
match=re.search(r"[a]",b)  


# ^ is used to check if a string is started with particular character or word
match=re.search(r"^char",a)
match=re.search(r"^c",a)



# $ is used to check whether a string end with particular word or character
match=re.search(r"com$",b)
match=re.search(r"m$",b)


# . is used to match any character between two character except for new line 
match=re.findall(r"c.l",a)



# | is works as logic or that string either contain one of them or both
match=re.findall(r"xx|z",d)



# ? is used to find zero or only one occurence of character in this example it is checking charchter h
# it is checking whether h is coming one or zero time between ca if it is coming more than 1 time 
# then the output list is empty else it will return the string
match=re.findall(r"ch?a",a)



# * character can  occur zero time or infinite time in this example it check string either it
# contain x first and then n number times of y that can be 0
match=re.findall(r"xy*",d)
# output ['x', 'xyy', 'xyy', 'xyy', 'x', 'x', 'x', 'xyy', 'x']



# + character occur atleast 1 time or infinite time
match=re.findall(r"xy+",d)
# output ['xyy', 'xyy', 'xyy', 'xyy']



# {} if we want to check a particular character comes certain time in the string
# in this example it check where x xomes twice three or four time
match=re.findall(r"x{2,4}",d)
# output ['xx', 'xx', 'xxx']



# () enclose group of regex
match=re.findall(r"(xy)+z",d)
#output ['xy', 'xy']

# [] matches any one character or [^] match any character except char after ^ 
match=re.findall(r"[a-z]",d)
# output ['x', 'x', 'y', 'z', 'x', 'y', 'y', 'z', 'x', 'y', 'y', 'x', 'z', 'z', 
# 'y', 'x', 'x', 'x', 'y', 'y', 'z', 'z', 'y', 'x', 'y', 'z', 'x', 'x', 'x']