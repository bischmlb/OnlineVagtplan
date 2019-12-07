import random

userList = []


def listUsers():
    for x in userList:
        print(x.accountID)

groupList = []
def listGroups(self):
    for x in Group.groupList:
        print("group ", x.groupID)


def storeAccount(account, password, file):
    f = open(file, "a+")
    f.write(account.name + "," + account.email + "," + password + "," + str(account.phone) + "," + str(account.nrShift) + str(account.accountID) + "\n")
    f.close()

def stringerror(string, attribute):
    print("test")
    if not string:
        raise ValueError("Invalid input " + attribute + " must not be an empty string")
    if not type(string) is str:
        raise ValueError("Invalid input " + attribute + " must be a string")

def phoneerror(string):
    if not string:
        raise ValueError("Invalid input phone must not be an empty string")
    if string.isdigit() == False:
        raise ValueError("input given for phone must be an Integer")
    if len(string) > 8:
        raise ValueError("valid phone number must be 8 digits long")

class User:
    Type = "Volenteer"
    def __init__(self,name,email,phone):

        stringerror(name,"name")
        stringerror(email, "email")
        phoneerror(phone)
        self.name = name
        self.email = email
        self.phone = phone
        self.nrShift = 0
        self.accountID = self.createID()
        userList.append(self)


    def __repr__(self):
        return "<User info: name:%s - email:%s, number:%s, total nr of shifts:%s, his personal id is: %s>" % (self.name, self.email,self.phone,self.nrShift,self.accountID)

    def createID(self):
        id = "0-"+str(random.randint(2,2000))+"-"+str(self.name)
        if self.checkUnique(id) != 0:
            return id
        else:
            self.createID()


    def checkUnique(self,id):
        for x in userList:
            if x.accountID == id:
                return 0


def grouperror(string):
    if int(string)!=True:
        raise ValueError("input must be an Integer")



class Group:

    def __init__(self,groupID):
        grouperror(groupID)
        self.groupID = groupID
        self.checkID()
        groupList.append(self)
        self.members = []
        self.supers = []
        self.activesuper = "None"


    def checkID(self):
        for x in groupList:
            if self.groupID==x.groupID:
                raise Exception("this ID is already chosen, please choose another ID for the group")

    def __repr__(self):
        return "<Group info: members:%s - supers:%s - schedule:%s, activesuper is:%s>" % (
        self.members,self.super,self.schedule,self.activesuper)

    def add_user(self, User):
        for x in self.members:
            if User.accountID == x:
                raise Exception("user already  added to this group")
            pass
        self.members.append(User.accountID)




    def listMembers(self):
        for x in self.members:
            print(x, "is a member of",self.groupID)


class Schedule:

    def __init__(self,groupNr,Month):
        self.groupnr = groupNr
        self.month = Month

John = User("john","john@shit.com","22334455")
John2 = User("john2","john@shit.com","22334455")
Group1 = Group(1)

Group1.add_user(John)
Group1.add_user(John2)
Group1.add_user(John)
print(Group1.members)
if Group1.members[0] == John.accountID:
    print("ye")

