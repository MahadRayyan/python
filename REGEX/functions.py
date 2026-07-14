import re

a="""sannan ismail cgpga is 40
muneeb ahmed cgpa is 35
sami cgpa equal to 37"""

# findall find all the occurence
match = re.findall(r"\d+",a)



# compile it is used to compile a pattern which can be reused 
pattern=re.compile("\d+")
match=pattern.findall(a)


# spilt it is used to split the string 
print(re.split("\d+",a))


# sub use to subsitute the value 
print(re.sub("\d+","3.6",a))

# subn same as sub but it return string in tuple
print(re.subn("\d+","3.6",a))


# search it return the first occurence of the pattern from the string 
match = re.search(r"\d+",a)
print(match)

