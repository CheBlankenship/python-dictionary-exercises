print "Given the following dictionary, representing a mapping from names to \
phone numbers:"

phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

print phonebook_dict['Elizabeth']
phonebook_dict['Kareem'] = "938-489-1234"
del phonebook_dict['Alice']
phonebook_dict['Bob'] = '968-345-2345'

# Prints the names in the phonebook using the keys() method
# for name in phonebook_dict.keys():
#     print name

# Prints the numbers in the phonebook using the values() method
for number in phonebook_dict.values():
    print number

# Prints the names and numbers in the phonebook using the items() method
# for name, number in phonebook_dict.items():
#     print name, number
