#Sets are unordered --> no element positions a[0] does not exist
# type casting: converting list to set
a={'set', 'bb', 'anda'}
a.add('baba')
print(a)
a.remove('bb')
print(a)

print('set' in a)