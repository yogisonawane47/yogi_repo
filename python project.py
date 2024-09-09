#HOSPITAL MANAGEMENT

class Patient:
    patient_list=list()
    def __init__ (self,SrNo,Name,Age,Gender,Disease,Mobile_No):
        self.SrNo=SrNo
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.Disease=Disease
        self.Mobile_No=Mobile_No

#their patient detail added||
    def add_patient(self):
        Patient.patient_list.append(self)
        
#their show patient detail||
    @staticmethod
    def get_patient_list():
        return Patient.patient_list
    
#their show propper detail||
    def __str__(self):
        return f"{self.SrNo} {self.Name} {self.Age} {self.Gender} {self.Disease} {self.Mobile_No}"
    def getpatient_SrNo (self):
        return self.SrNo
    
    def setpatient_SrNo(self,SrNo):
        self.SrNo=SrNo

#their patient detail change

    @staticmethod
    def updatepatient(SrNo,Name,Age,Gender,Disease,Mobile_No):
        for patient in Patient.patient_list:
            if patient.getpatient_SrNo() == SrNo:
                patient.SrNo=SrNo
                patient.Name=Name
                patient.Age=Age
                patient.Gender=Gender
                patient.Disease=Disease
                patient.Mobile_No=Mobile_No
                return True
        return False


    @staticmethod
    def search_patient(SrNo):
        for patient in Patient.patient_list:
            if patient.getpatient_SrNo() == SrNo:
                return patient
        return None

    @staticmethod
    def delete_patient(SrNo):
        for patient in Patient.patient_list:
            if patient.getpatient_SrNo() == SrNo:
                Patient.patient_list.remove(patient)
                return True
        return False
        
    

choice=1
while choice >=1 and choice <=5:
    print("!!WELCOME TO HOSPITAL MANAGEMENT SYSTEM!!")
    print("!!PLEASE CHOOSE OPTION!!")
    print("1.ADD PATIENT DETAILS\n 2.SHOW PATIENT DETAILS\n 3.CHANGE PATIENT DETAIL\n 4.SEARCH PATIENT DETAIL\n 5.DELETE PATIENT DETAIL")
    choice=int(input("ENTER OPTION:"))

    
    if(choice==1):
        SrNo=int(input("ENTER NO OF PATIENT:"))
        Name=input("ENTER PATIENT NAME:")
        Age=int(input("ENTER PATIENT AGE:"))
        Gender=input("ENTER PATIENT GENDER:")
        Disease=input("ENTER PATIENT DISEASE:")
        Mobile_No=int(input("ENTER MOBILE NO:"))

        p=Patient(SrNo,Name,Age,Gender,Disease,Mobile_No)
        p.add_patient()
        print("!!PATIENT DETAIL SUCCESSFULLY ADDED!!")

    elif(choice==2):
        for patient in Patient.get_patient_list():
            print(patient)

    elif(choice==3):
        SrNo=int(input("ENTER SrNo:"))
        Name=input("ENTER NAME:")
        Age=int(input("ENTER NEW AGE:"))
        Gender=input("ENTER GENDER:")
        Disease=input("ENTER NEW DISEASE:")
        Mobile_No=int(input("ENTER NEW MOBILE_NO:"))

        if Patient.updatepatient(SrNo,Name,Age,Gender,Disease,Mobile_No):
            print("!!SUCCEEFULLY UPDATE!!")
        else:
            print("PATIENT DETAIL NOT FOUND:",SrNo)


    elif(choice==4):
        SrNo=int(input("ENTER PATIENT SRNO TO SEARCH:"))
        patient=Patient.search_patient(SrNo)
        if patient:
           print("!!PATIENT DETAIL FOUND!!")
           print(patient)
        else:
            print("PATIENT DETAIL NOT FOUND:",SrNo)
            
    elif(choice==5):
        SrNo=int(input("ENTER PATIENT SRNO:"))
        if Patient.delete_patient(SrNo):
            print("!!SUCCESSFULLY DELETED PATIENT DETAILS!!")
        else:
            print("PATIENT DETAIL NOT FOUND",SrNo)
    else:
      break
        

    
