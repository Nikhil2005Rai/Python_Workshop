#_____TypeCasting
a = 12
b = str(a)
print(b) #int a become string

#print(b-1) will raise an error because b is str(12)

c = 12.34 #Float value
d = c + a #will return float value
print(d) 

e = "Hello"
#print(float(e)) will raise an error, because we can't turn string into float

lst = [1,2,3]
tpl_of_lst = tuple(lst)
print(lst,tpl_of_lst)

tpl = (4,5,6)
lst_of_tpl = list(tpl)
print(tpl,lst_of_tpl)
'''
string, float --> integer
dtring, float --> float
integer, float, list,tuple, dictionaru --> String

'''