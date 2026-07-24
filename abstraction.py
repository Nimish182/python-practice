class Car():

    #creating constructor
    def __init__(self):
        self.acc= False
        self.brk= False
        self.clutch= False

    #creating a start fuction of car
    def start(self):
        self.clutch=True
        self.acc=True
        print("The car has started.............")

car1=Car()
car1.start()


#so here in the output the information of clutch and acc being engaged is not shown. Only the important information that
#car has started is shown. This is abstraction