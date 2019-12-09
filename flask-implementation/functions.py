'''
This program is responsible for the rest of the functionality of the OnlineVagtplan
that is CMD-based. This includes functions for:
 - Listing all Users
 - Listing all groups
 - listing all members of a specified group
 - Adding a group to the system
 - Adding a user to an existing group
'''

def listUsers():
    # Function for listing all users in the system
    file = open('users.txt', 'r+')
    print('\n****** Users in the system ******')
    for line in file:
        if ('group' not in line):
            print(line.split(',')[0] + ' - ' + line.split(',')[1])
    file.close()

def addGroup(name):
    # Function for adding a group to the system
    found = False
    file = open('users.txt', "r+")
    for line in file:
        if name in line:        # if group already exists, break the loop
            print('\ngroup: \''  + name +'\' already exist')
            found = True
            break
    if (not found):             # If group does not exists, make it
        print('\n*** Adding group: '  + name + ' ***')
        file.write('group: ' + name + ',\n')
    file.close()

def addUserToGroup(name, group):
    data = ''
    found = False
    names = []
    file = open('users.txt', "r+")
    read = file.readlines()
    file.seek(0)
    for line in file:
        if ('group' not in line):       # adding all names to a list
            names.append(line.split(',')[0])
    file.seek(0)
    for line in read:
        if (group in line):             # if group found, save the line for later
            data = line[0:-1]
            found = True
        elif (group not in line):
            file.write(line)    # if the group is not on the given line, write to file
    file.truncate()
    if found:                   # if both the group and the user exists, add user to group
        if name not in data and name in names:
            print('\n*** Adding member \'' + name + '\' to group \'' + group + '\' ***')
            file.write(data + name + ',\n')
            file.close()
        else:                   # otherwise only write already existing members of group
            print('\nUser \'' + name + '\' already in group \'' + group +  '\' or does not exist. \'')
            file.write(data + '\n')
            file.close()
    else:
        print('\nGroup \'' + group + '\' not found')
    file.close()

def listGroupMembers(group):
    # function for listing all members of a specified group
    file = open('users.txt', "r+")
    for line in file:
        if group in line:
            print('\n*** members of group \'' + group + '\' ***')
            print(line.split(',')[1:-1])
            break
    file.close()

def listGroups():
    # function for listing all existing groups in the system
    print('\n*** Groups in the system ***')
    file = open('users.txt', "r+")
    for line in file:
        if 'group' in line:
            print(line.split(',')[0].split(':')[1])
    file.close()
#
def UI():
    print("\n")
    print("1: Print all users")
    print("2: Print groups")
    print("3: List members of group")
    print("4: Create new group")
    print("5: Add user to group")
    print("---------------------------")
    print("6: Show menu")
    print("0: Quit")
    print("\n")



if __name__ == "__main__":
    choice = ''
    UI()
    while choice != '0':
        choice = input("What would you like to do? ")
        if choice == '1':
            listUsers()
        elif choice == '2':
            listGroups()
        elif choice == '3':
            groupName = input("Which group?: ")
            listGroupMembers(groupName)
        elif choice == '4':
            groupName = input("New group name: ")
            addGroup(groupName)
        elif choice == '5':
            userName = input("Which user?: ")
            groupName = input("Which group?: ")
            addUserToGroup(userName, groupName)
        elif choice == '6':
            UI()
        else:
            print("Input not recognized, please try again.")
            UI()


#
# listUsers()
# # addGroup('Kohberg')
# addUserToGroup('troels', 'Kohberg')
# listGroupMembers('Kohberg')
#listGroups()
#addGroup('Boller')
#listGroups()
#addUserToGroup('Børge', 'Boller')
#listGroupMembers('Boller')

# data = ''
# file = open('testfile.txt', "r+")
# read = file.readlines()
# file.seek(0)
# for line in read:
#     if ('Kohberg' in line):
#         data = line[0:-1]
#     elif ('Kohberg' not in line):
#         file.write(line)
# file.truncate()
# file.write(data + 'jens,\n')
# file.close()
# print(data)
