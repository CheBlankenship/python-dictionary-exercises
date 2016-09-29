import pickle
from os.path import exists

if exists('phonebook.pickle'):
    # open the phonebook file in read mode
    phonebook = open('phonebook.pickle','r')
    # load the contents from the file and store it in the phonebook_dict variable
    phonebook_dict = pickle.load(phonebook)
else:
    phonebook_dict = {}

tab = " " * 4
prompt = "> "
using_app = True
def more_changes_offer():
    global modifying
    print "Make more changes? Y/N"
    decision = raw_input(prompt).lower()
    if decision == "n":
        modifying = False
    else:
        modifying == True


while using_app:
    print """
    Electronic Phone Book
    =====================
    1\. List all contacts
    2\. Look up a contact
    3\. Create a contact
    4\. Modify a contact
    5\. Delete a contact
    6\. Save changes
    7\. Quit

    What do you want to do (1-7)?
    """
    menu_choice = raw_input(prompt)

    if menu_choice == "1":
        for contact in sorted(phonebook_dict):
            print tab + contact
            print "\tHome: %s" % phonebook_dict[contact].get('home', "")
            print "\tWork: %s" % phonebook_dict[contact].get('work', "")
            print "\tMobile: %s" % phonebook_dict[contact].get('mobile', "")
    elif menu_choice == "2":
        print tab + "Enter name to search for:"
        search = raw_input(prompt).capitalize()
        if search in phonebook_dict:
            print (" " * 4) + search
            print "\tHome: %s" % phonebook_dict[search].get('home', "")
            print "\tWork: %s" % phonebook_dict[search].get('work', "")
            print "\tMobile: %s" % phonebook_dict[search].get('mobile', "")
        else:
            print tab + "Contact not found"
    elif menu_choice == "3":
        print tab + "Enter new contact's name:"
        new_name = raw_input(prompt).capitalize()
        phonebook_dict[new_name] = {}
        print tab + "Enter either 'home', 'work', or 'mobile':"
        decision = raw_input(prompt).lower()
        if decision == "home":
            print tab + "Enter contact's home phone number:"
            new_phone = raw_input(prompt)
            phonebook_dict[new_name]['home'] = new_phone
        elif decision == "work":
            print tab + "Enter contact's work phone number:"
            new_phone = raw_input(prompt)
            phonebook_dict[new_name]['work'] = new_phone
        elif decision == "mobile":
            print tab + "Enter contact's mobile phone number:"
            new_phone = raw_input(prompt)
            phonebook_dict[new_name]['mobile'] = new_phone
        else:
            print tab + "Invalid option"
        print tab + "New contact '%s' saved" % new_name
    elif menu_choice == "4":
        print tab + "Enter name of the contact to modify:"
        name = raw_input(prompt).capitalize()
        if name in phonebook_dict:
            modifying = True
            while modifying == True:
                print tab + "Enter 'name', 'home', 'work', or 'mobile':"
                decision = raw_input(prompt)
                print tab + "Enter new %s:" % decision
                change = raw_input(prompt)
                if decision == "name":
                    phonebook_dict[name] = change
                    more_changes_offer()
                elif decision == "home":
                    phonebook_dict[name]['home'] = change
                    more_changes_offer()
                elif decision == "work":
                    phonebook_dict[name]['work'] = change
                    more_changes_offer()
                elif decision == "mobile":
                    phonebook_dict[name]['mobile'] = change
                    more_changes_offer()
                else:
                    "Invalid option"
                    modifying = False
        else:
            print tab + "Contact not found"
    elif menu_choice == "5":
        print tab + "Enter name of the contact to delete:"
        name_to_delete = raw_input(prompt).capitalize()
        if name_to_delete in phonebook_dict:
            del phonebook_dict[name_to_delete]
            print tab + "Contact '%s' deleted" % name_to_delete
        else:
            print tab + "Contact not found"
    elif menu_choice == "6":
        # open the file in write mode
        phonebook = open('phonebook.pickle', 'w')
        # dump the contents of the phonebook dictionary into the open file
        pickle.dump(phonebook_dict, phonebook)
        # close the file
        phonebook.close()
        print tab + "Changes saved successfully"
    elif menu_choice == "7":
        print tab + "Goodbye!"
        using_app = False
    else:
        print tab + "Invalid option"
