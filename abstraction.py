class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.cluth=False

    def start(self):
        self.cluth=True#see here the self.cluth and acc or not main or is unnessasary detalis are removed
        self.acc=True
        print("car started")


car1=car()
car1.start()         