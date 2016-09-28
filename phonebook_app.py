import pickle
from os.path import exists

if exists('phonebook.pickle'):
    # open the phonebook file in read mode
    phonebook = open('phonebook.pickle','r')
    # load the contents from the file and store it in the phonebook_dict variable
    phonebook_dict = pickle.load(phonebook)
else:
    phonebook_dict = {}

prompt = "> "
using = True

while using == True:
    print """
    Electronic Phone Book
    =====================
    1\. Look up an entry
    2\. Set an entry
    3\. Delete an entry
    4\. List all entries
    5\. Save changes
    6\. Quit

    What do you want to do (1-5)?
    """
    choice = int(raw_input(prompt))

    if choice == 1:
        print "Enter name to search for: "
        search = raw_input(prompt)
        if search in phonebook_dict.keys():
            print phonebook_dict[search]
        else:
            print 'Contact not found'
    elif choice == 2:
        print "Enter new contact's name: "
        new_name = raw_input(prompt)
        print "Enter new contact's phone"
        new_phone = raw_input(prompt)
        phonebook_dict[new_name] = new_phone
        print "New contact '%s' saved" % new_name
    elif choice == 3:
        print "Enter name of the contact to delete:"
        name_to_delete = raw_input(prompt)
        if name_to_delete in phonebook_dict.keys():
            del phonebook_dict[name_to_delete]
            print "Contact '%s' deleted" % name_to_delete
        else:
            print 'Contact not found'
    elif choice == 4:
        print sorted(phonebook_dict.keys())
    elif choice == 5:
        # open the file in write mode
        phonebook = open('phonebook.pickle', 'w')
        # dump the contents of the phonebook dictionary into the open file
        pickle.dump(phonebook_dict, phonebook)
        # close the file
        phonebook.close()
        print "Changes saved successfully"
    elif choice == 6:
        print "Goodbye!"
        using = False
    else:
        print "Invalid option"
