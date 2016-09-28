print "Write a program to read in the text of that file and count the number of\
 occurrences of each word in that file. You will print one line for each word \
 encountered, and output the number of times that word appearred in the file."

# program prints out the frequency of each word in a file. two ways to
# eliminate extra characters commented below:

my_file = open('programmers_blues.txt')
my_file_lines = my_file.readlines()

words_encountered = {}

for line in my_file_lines:
    for word in line.split():
        # OPTION 1: strip off extra characters in the loop every time
        word = word.replace('.', '').replace('(', '').replace(')', '')
        words_encountered[word] = words_encountered.get(word, 0) + 1

# for word, frequency in words_encountered.items():
#     print "%s appears %d times" % (word, frequency)


##########
print "\n\n\n"
##########


my_file = open('programmers_blues.txt')
my_file_text = my_file.read()
# OPTION 2: strip off extra characters in the entire text...
my_file_text = my_file_text.replace('.', '').replace('(', '').replace(')', '')
# ... and split the entire text into a list of words
my_file_list = my_file_text.split()

words_encountered = {}

for word in my_file_list:
    words_encountered[word] = words_encountered.get(word, 0) + 1

# for word, frequency in words_encountered.items():
#     print "%s appears %d times" % (word, frequency)


# both ways produce the same result!


### BONUS CHALLENGE: ###
print "Print the top 10 most frequently used words in the file"
entries = []

# we want to make a list of tuples (right now we have words_encountered, which
# is a dictionary of key-value pairs)
entries = words_encountered.items()

# print the sorted list with either sorted(), which doesn't affect the original
# print sorted(entries, key=lambda tup: tup[1], reverse=True)

# ... or with sort(), which does replace the original and returns "None"
entries.sort(key=lambda tup: tup[1], reverse=True)
# print entries

# print the top ten most commonly-appearing words
for i in range(10):
    print entries[i]
