#Lecture link:https://www.youtube.com/watch?v=KDcBhTAncU0&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=64
#Lecture link2:https://www.youtube.com/watch?v=e9c9E7MGwgg&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=65

#SUPER CLASS
class OTTsubs:
    def __init__(self,subs_id,plan,total_payment):
        self.subs_id=subs_id
        self.subs_plan=plan
        self.total_payment=total_payment
    def subscribtion(self):
        print(f"You subscribed for {self.subs_plan} plan and yor total payment is {self.total_payment}")
    def unsubscribtion(self):
        print(f"You unsubscribed for {self.subs_plan} plan and yor total payment is {self.total_payment}")

#hotstar=OTTsubs(121221,"Monthly",1000)
#hotstar.subscribtion()
#hotstar.unsubscribtion()

#SUB CLASS
class PREMsubs(OTTsubs):
    def __init__(self,subs_id,plan,total_payment,max_screens):
        super().__init__(subs_id,plan,total_payment)
        self.max_screens=max_screens

    def set_max_screeens(self,max_screens):
        self.max_screens = max_screens
        print(f"Max screens set to {self.max_screens} in the premium plan")

hotstar=PREMsubs(121221,"Monthly",1000,4)
hotstar.subscribtion()
hotstar.unsubscribtion()
hotstar.set_max_screeens(4)




