#TRAIN TIME TABLE MANAGEMENT

class Train:
    train_list=list()
    def __init__(self,train_name,train_number,train_arrival_time,train_depature_time,platform_no,source,destination):
        
        self.train_name=train_name
        self.train_number=train_number
        self.train_arrival_time=train_arrival_time
        self.train_depature_time=train_depature_time
        self.platform_no=platform_no
        self.source=source
        self.destination=destination
        
    def add_train(self):
        Train.train_list.append(self)
        
    @staticmethod   
    def gettrainlist():
        return Train.train_list
    
    #TO PROVIDE STRING REPRESENTATION OF AN OBJECT.
    
    def __str__(self):
        return f"{self.train_name} {self.train_number} {self.train_arrival_time} {self.train_depature_time} {self.platform_no} {self.source} {self.destination}"
    def gettrain_number(self):
        return self.train_number
    
    def settrain_number(self,train_number):
        self.train_number=train_number
        
    @staticmethod
    def updateTrain(train_name,train_number,train_arrival_time,train_depature_time,platform_no,source,destination):
        for train in Train.train_list:
            if train.gettrain_number() == train_number:
                train.train_name= train_name
                train.train_number= train_number
                train.train_arrival_time= train_arrival_time
                train.train_depature_time= train_depature_time
                train.platform_no= platform_no
                train.source= source
                train.destination= destination
                return True
        return False
    @staticmethod
    def delete_train(train_number):
        for train in Train.train_list:
            if train.gettrain_number() == train_number:
                Train.train_list.remove(train)
                return True
            return False
        
    @staticmethod
    def search_train(train_number):
        for train in Train.train_list:
            if train.gettrain_number() == train_number:
                return train
        return None
choice=1
while choice >=1 and choice <=5:
    print("!!WELCOM TO INDIAN RAILWAY TIME-TABLE!!")
    print("!!PLEASE CHOOSE OPTION!!")
    print("1.ADD TRAIN DETAILS\n 2.SHOW TRAIN DETAILS\n 3.UPDATE TRAIN DETAILS\n 4.DELETE\n 5.SEARCH TRAIN\n")
    choice=int(input("ENTER YOUR OPTION:"))
    if(choice==1):
         train_name=input("ENTER TRAIN NAME:")
         train_number=int(input("ENTER TRAIN NUMBER:"))
         train_arrival_time=input("ENTER ARRIVAL TIME:") 
         train_depature_time=input("ENTER DEPATURE TIME:")
         platform_no=int(input("ENTER PLATFORM NO:"))
         source=input("ENTER SOURCE:")
         destination= input("ENTER DESTINATION:")

         t=Train(train_name,train_number,train_arrival_time,train_depature_time,platform_no,source,destination)
         t.add_train()
         print("!!INFORMATION SUCCESSFULLY ADDED!!")
         
    elif(choice==2):
        for train in Train.gettrainlist():
            print(train)
    elif(choice==3):
         train_name=input("ENTER NEW TRAIN NAME:")
         train_number=int(input("ENTER NEW TRAIN NUMBER:"))
         train_arrival_time=input("ENTER NEW ARRIVAL TIME:") 
         train_depature_time=input("ENTER NEW DEPATURE TIME:")
         platform_no=int(input("ENTER NEW PLATFORM NO:"))
         source=input("ENTER NEW SOURCE:")
         destination= input("ENTER NEW DESTINATION:")

         if Train.updateTrain(train_name,train_number,train_arrival_time,train_depature_time,platform_no,source,destination):
             print("!!SUCCEFULLY UPDATE!!")
         else:
             print("TRAIN NOT FOUND:",train_number)
             
    elif(choice==4):
        print("!WELCOM TO TRAIN DELETATION DEPARTMENT!")
        train_number=int(input("ENTER TRAIN NUMBER:"))
        if Train.delete_train(train_number):
            print("!!SUCCESSFULLY DELETED TRAIN")
        else:
            print("TRAIN NOT FOUND",train_number)
    elif(choice==5):
        train_number=int(input("ENTER TRAIN NUMBER TO SEARCH:"))
        train=Train.search_train(train_number)
        if train:
           print("!!TRAIN FOUND!!")
           print(train)
        else:
           print("TRAIN NOT FOUND",train_number)
    else:
      break
            
