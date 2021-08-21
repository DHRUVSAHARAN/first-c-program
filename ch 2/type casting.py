# a = "3535"
# print (a +5)
#dont work as a int a 3535 is in "  " as the python language 
# thought it as a string

a = "3535"
a = int(a)
#we can use this  syntex to make a string into int only usable when 
# the string is also in numbers like "1234" not like "hello world"
print(type(a))
print (a +5 )