import random
import datetime
import sys

class Janken:

 
    def __init__(self, u_choice):
        self.u_choice = u_choice
        
        #CPU
    def judge(self):
        dic = {"a": "グー", "b": "チョキ","c": "パー"}
        choice_list = ["a", "b", "c"]
        npc = dic[random.choice(choice_list)]
        
        #PC
        draw = '俺の勝ち！あいこがある、そう思ってないですか？　だとしたら、明日も僕が勝ちます。'
        win = 'やるやん！明日は俺にリベンジさせて。'
        lose = '俺の勝ち！なんで負けたか、明日までに考えておいてください。'
        
        if self.u_choice == npc:
            keisuke = draw
        else:
            if self.u_choice == "グー":
                if npc == "チョキ":
                    keisuke = win
                else:
                    keisuke = lose
                    
            elif self.u_choice == "チョキ":
                if npc == "パー":
                    keisuke = win
                else:
                    keisuke = lose
                    
            else:
                if npc == "グー":
                    keisuke = win
                else:
                    keisuke = lose
        print("You　%s" % self.u_choice)
        print("Keisuke Honda %s" % npc)
        print("Keisuke Honda %s" % keisuke)
#時間取得
dt_now = datetime.datetime.now()

#動作
data = []
intdata = []
f = open('login.txt', 'r', encoding='UTF-8')
data = f.readlines()
for x in range(len(data)):
    intdata.append(int(data[x].rstrip('\n')))
f.close()

if(dt_now.year == intdata[0]and dt_now.month == intdata[1]and dt_now.day == intdata[2]):
        print("1日一回勝負！ほな、また明日ノシ")
        sys.exit()  
print("じゃん けん ぽん！")
print("a=グー　b=チョキ　ｃ=パー　a , b , c で入力")
user = input('...　')
dic = {"a": "グー", "b": "チョキ","c": "パー"}
user = user.lower()
try:
    user_choice = dic[user]
    j = Janken(user_choice)
    j.judge()
    with open('login.txt', 'w') as f:
        print(str(dt_now.year)+"\n"+str(dt_now.month)+"\n"+str(dt_now.day),file=f)
except:
    print("えっとー、、、a b c 以外うつのやめてもらっていいですか？")

                
