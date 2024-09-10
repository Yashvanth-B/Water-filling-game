#Water filler
import random
class project:
    def __init__(self):
        self.num=random.randint(11,26)
        self.name=input("Enter palyer name: ")

    def game_on(self,):
        
        self.point=self.num
    
        while 0<=self.point:
            self.com=random.randint(1,6)
            userp=int(input("\nFill the bottel:"))
            if userp <=0 or userp>6:
                print("invalid value.....")
                continue
            print(self.name,userp)
            print("Computer :",self.com)
            self.point-=userp
            if self.point <= 0:
                print("\n\n___Water over flow___\n",self.name,"loose the match.....\nComputer Won!!!!!")
                break
            self.point-=self.com
            if self.point<=0:
                print("\n\n___Water over flow___\nComputer loose the match.....",self.name,"Won the match!!!!!")
                    
    def game_onc(self,):
        try:
            self.point=self.num

            while 0<=self.point:
                self.com=random.randint(1,6)
                userp=int(input("Fill the bottel:"))
                if userp <=0 or userp>6:
                    raise ValueError
                    continue
                print("Computer :",self.com)
                print(self.name,userp)

                self.point-=self.com
                if self.point<=0:
                    print("\n\n___Water over flow___\nComputer loose the match.....",self.name,"Won the match!!!!!")
                    break
                self.point-=userp
                if self.point <= 0:
                   print("\n\n___Water over flow___\n",self.name,"loose the match.....\nComputer Won the match!!!!!")
        except ValueError:
            print("invalide data......, ")
    
    def game_round(self):
        try:
            print("\nCondition you can take only 1 to 6 numbers.\nif you over flow the water you will loose the game..... ")
            self.com=random.randint(1,6)
            odd=int(input("\nToss time!!!! \nEnter 1.odd or 2.even : "))
            if odd<=0 or odd>=3:
                raise ValueError
            usernum=int(input("Enter the number"))
            toss=int(usernum)+int(self.com)
            print("Toss value :",toss)
            if toss%2==0 and odd==2 or toss%2!=0 and odd==1 :
                print("\n",self.name,"won the toss!!!.\nYou can make 1st move.")
                pro.game_on()

            else:
                print("\nComputer win the toss!!!.\nComputer can make 1st move.")
                pro.game_onc()
        except ValueError:
            print("invalide data......, ")
                
    
pro=project()
pro.game_round()

    
