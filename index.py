#Single line comment
'''
Multi Line comment
'''
#Print sum of two numbers
a = 10
b = 90
print(a+b) # Sum of a and b

#_____KEYWORDS
import keyword as k
print(k.kwlist) #print all keywords

#print if something is keyword or not
print(k.iskeyword("def")) #True
print(k.iskeyword("jack")) #False


#print all soft keywords
print(k.softkwlist)

#check if something is softkeyword
print(k.issoftkeyword("case")) #False
print(k.issoftkeyword("ntht")) #False

#_____VARIABLE
P = 12 # Assignment
k , s = 9 , 66; x = y = z = 1; #Multiple assignment
a , b = b , a; #Swapping of variables
print(a,b)
num = 1
del num #Deleting variable, can also delete multiple variable
#print(num) --> Will cause error
#another way to assign variable
number = 5_000_000
print(number)

#PYTHON DATATYPE
#Text type
str = "Nikhil" #String 
print(type(str))
#Numeric Type
n1 = 1 #Integer
n2 = 23.02 #Float
n3 = 3 + 8j #complex 
print(type(n1), type(n2), type(n3))

#Sequence Type
List = [1,2,3,4,5]
Tuple = (1,2,3,4,5)
Range = range(5)
print(type(List),type(Tuple),type(Range)) #Key:Value pair

#Mapping type
Dictionary = {1:23,'a':934,9:'ab'}
print(type(Dictionary))

#Set Type
Set = {1,2,3} #Only hold unique elements
FrozenSet = frozenset({3,4,5}) #Set which can't be modified
print(type(Set), type(FrozenSet))

#Boolean Type (True/False)
bool_T = True
bool_F = False
print(type(bool_T),type(bool_F))

#Binary Type
#To be done while 

