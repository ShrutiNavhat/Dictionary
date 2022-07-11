

question_list = [
"How many continents are there?",  # pehla question
"What is the capital of India?",# doosra question
"NG mei kaun se course padhaya jaata hai?"# teesra question
]
options_list = [
#pehle question ke liye options
["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#second question ke liye options
["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#third question ke liye options
["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
]
solution_list=[3,4,1]
options_list2=[["1.Nine","3.Seven"],["1.Chandigarh","4.Delhi"],["1.Software Engineering","2.Agriculture"]]
print("kaun banega crorepati[KBC]")
# solution_list2=[2,2,1]
i=0
sum=0
count=0
while i<len(question_list):
        print(question_list[i])
        print(options_list[i])
        lifeline=input("you want to take lifeline yes or no:")
        if lifeline=="yes":
                if count==0:
                        print(options_list2[i])
                        ans=int(input("choose the option"))
                        if ans==solution_list[i]:
                                sum=sum+1000
                                print("correct answer")
                                print("you win rs/",sum)
                                count+=1
                        elif ans!=solution_list[i]:
                                print("incorrect answer")
                                print("you lose the game")
                                break
                else:
                        print("you already used your lifeline")
                        ans=input("choose the option")
                        if ans==solution_list[i]:
                                sum=sum+200
                                print("enterred correct answer")
                                print("you win RS/",sum)
        else:
                ans=int(input("Choose the option"))
                if ans==solution_list[i]:
                                sum+=3000
                                print("correct answer")
                                print("you win RS/",sum)
                elif ans!=solution_list[i]:
                        print("incorrect answer")
                        print("you lose the game")
                        print("do you want to play game")
                        break
        if i==2:
           if ans==solution_list[i]:
                print("congratulations you win the game")
        i+=1
	
