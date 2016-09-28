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
    1\. Look up a contact
    2\. Create a contact
    3\. Delete a contact
    4\. List all contacts
    5\. Save changes
    6\. Quit

    What do you want to do (1-5)?
    """
    choice = int(raw_input(prompt))

    if choice == 1:
        print "Enter name to search for:"
        search = raw_input(prompt)
        if search in phonebook_dict.keys():
            print phonebook_dict[search]
        else:
            print 'Contact not found'
    elif choice == 2:
        print "Enter new contact's name:"
        new_name = raw_input(prompt).capitalize()
        phonebook_dict[new_name] = {}
        choosing = True
        while choosing:
            print "Do you want to enter a home, work, or mobile number?"
            decision = raw_input(prompt).lower()
            if decision == "home":
                print "Enter contact's home phone number:"
                new_phone = raw_input(prompt)
                phonebook_dict[new_name]['home'] = new_phone
                choosing = False
            elif decision == "work":
                print "Enter contact's work phone number:"
                new_phone = raw_input(prompt)
                phonebook_dict[new_name]['work'] = new_phone
                choosing = False
            elif decision == "mobile":
                print "Enter contact's mobile phone number:"
                new_phone = raw_input(prompt)
                phonebook_dict[new_name]['mobile'] = new_phone
                choosing = False
            else:
                print "Invalid option"
            # print "Enter Y/N":
            # decision = raw_input(prompt).upper()
            # if decision == "Y"
            #     print ""
            #     decision =
            #         number_type = raw_input(prompt).lower()
            #         print "Enter new contact's phone:"
            #         new_phone = raw_input(prompt)
            #         phonebook_dict[new_name] = new_phone
        print "New contact '%s' saved" % new_name
    elif choice == 3:
        print "Enter name of the contact to delete:"
        name_to_delete = raw_input(prompt)
        if name_to_delete in phonebook_dict:
            del phonebook_dict[name_to_delete]
            print "Contact '%s' deleted" % name_to_delete
        else:
            print 'Contact not found'
    elif choice == 4:
        print phonebook_dict.items()
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
