import random
import unittest

userList = []


def listUsers():
    for x in userList:
        print(x.accountID)

groupList = []
def listGroups(self):
    for x in Group.groupList:
        print("group ", x.groupID)


def storeAccount(account, password, file): #function to store user in database
    f = open(file, "a+")                   #open database, and append given input
    f.write(account.name + "," + account.email + "," + password + "," + str(account.phone) + "," + str(account.nrShift) + str(account.accountID) + "\n")
    f.close()                              #close

def stringerror(string, attribute):
    if not string:
        raise ValueError("Invalid input " + attribute + " must not be an empty string")
    if not type(string) is str:
        raise ValueError("Invalid input " + attribute + " must be a string")

def phoneerror(string):
    if not string:
        raise ValueError("Invalid input phone must not be an empty string")
    if len(string) != 8:
        raise ValueError("valid phone number must be 8 digits long")
    if string.isdigit() == False:
        raise ValueError("input given for phone must be an Integer")

class User:
    Type = "Volenteer"
    def __init__(self,name,email,phone):
        stringerror(name,"name")
        stringerror(email, "email")
        if isinstance(phone, int) == True:
            phone = str(phone)
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
        else:
            pass


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

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user1 = User("John","john@shit.com","22334455")
        self.user2 = User("Carl", "carl@shit.com", "55443322")
    def test_email(self):
        self.assertEqual(self.user1.email,"john@shit.com")
        self.assertEqual(self.user2.email, "carl@shit.com")
    def test_name(self):
        self.assertEqual(self.user1.name, "John")
        self.assertEqual(self.user2.name,"Carl")
    def test_phone(self):
        self.assertEqual(self.user1.phone,"22334455")
        self.assertEqual(self.user2.phone, "55443322")
    def test_UserID(self):
        self.assertEqual(self.user1.checkUnique(self.user1.accountID),0)
        self.assertEqual(self.user1.checkUnique(self.user2.accountID), 0)
    def test_stringTest(self):
        self.assertRaises(ValueError, stringerror, "", "user")
        self.assertRaises(ValueError, stringerror, 2, "user")
        self.assertRaises(ValueError, stringerror, ["dum"], "user")

    def test_phoneTest(self):
        self.assertRaises(ValueError,phoneerror,"")
        self.assertRaises(ValueError, phoneerror, "2233445b")
        self.assertRaises(ValueError, phoneerror, "2233445")
        self.assertRaises(ValueError, phoneerror, "223344555")
        self.assertRaises(ValueError, phoneerror, 223344555)

if __name__ == '__main__':
    John = User("john","john",22222222)
    unittest.main()

