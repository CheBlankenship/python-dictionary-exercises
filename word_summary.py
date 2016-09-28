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

for word, frequency in words_encountered.items():
    print "%s appears %d times" % (word, frequency)


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

for word, frequency in words_encountered.items():
    print "%s appears %d times" % (word, frequency)


# both ways produce the same result!
