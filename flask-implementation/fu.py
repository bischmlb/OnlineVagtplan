import random

userList = []
def listUsers(self):
    for x in User.userList:
        print(x.name,x.accountID)

def listGroups(self):
    for x in Group.groupList:
        print("group ", x.groupID)

class User:
    Type = "Volenteer"
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.nrShift = 0
        self.accountID = self.createID()
        self.userList.append(self)


    def __repr__(self):
        return "<User info: name:%s - email:%s - groupID:%s, number:%s, total nr of shifts:%s, his personal id is: %s>" % (self.name, self.email,self.groupID,self.phone,self.nrShift,self.accountID)

    def createID(self):
        id = "0"+self.name+str(random.randint(2,2000))
        if self.checkUnique(id) != 0:
            return id
        else:
            self.createID()


    def checkUnique(self,id):
        for x in User.userList:
            if x.accountID == id:
                return 0




class Group:

    def __init__(self,groupID):
        self.groupID = groupID
        self.members = []
        self.supers = []
        self.activesuper = "None"
        self.groupList.append(self)
    groupList = []

    def __repr__(self):
        return "<Group info: members:%s - supers:%s - schedule:%s, activesuper is:%s>" % (
        self.members,self.super,self.schedule,self.activesuper)

    def add_user(self, User):
        self.members.append(User.accountID)



    def listMembers(self):
        for x in self.members:
            print(x, "is a member of",self.groupID)


class Schedule:

    def __init__(self,groupNr,Month):
        self.groupnr = groupNr
        self.month = Month
