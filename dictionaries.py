# Denoted in curly Brackets {}
# keys are immutable
dict1={'Thriller': 1982, 'Back in Black': 1980, 'The Dark Side of the Moon': 1973, 'The Bodyguard': 1992}
print(dict1['Thriller'])

Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6} 
print(Dict["D"])

print('D' in Dict)

print(Dict.values())
print(Dict.keys())

Dict['Newkey']='newvalue'
print(Dict)

#delete value from dict
del(Dict['A'])
print(Dict)
