# dict jupiter repitition
# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)

# Access to the value by the key

print(Dict["key1"])

# Access to the value by the key

print(Dict[(0, 1)])

# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)

# Get value by keys
print(release_year_dict['Thriller'])

# Get value by key
print(release_year_dict['The Bodyguard'])

# Get all the keys in dictionary
print(release_year_dict.keys())

# Get all the values in dictionary

print(release_year_dict.values())

# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
print(release_year_dict)

## Delete entries by key
print('')
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print(release_year_dict)

# Verify the key is in the dictionary
print('The Bodyguard' in release_year_dict)

# Question sample dictionary
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic)

# find the keys in dic
print(soundtrack_dic.keys())

# b) In the dictionary soundtrack_dict what are the values ?
print(soundtrack_dic.values())

# albums sales 
dict_album_sales={"Back":50, "Bodyguard":50, "Thriller":65}

# b) Use the dictionary to find the total sales of Thriller:
print(dict_album_sales["Thriller"])

# c) Find the names of the albums from the dictionary using the method keys
print(dict_album_sales.keys())

# d) Find the names of the recording sales from the dictionary using the method values:

print(dict_album_sales.values())
