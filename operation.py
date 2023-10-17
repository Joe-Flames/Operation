import random
list= ["+","-","/","×"]
while True:
	a=random.randint(1,100)
	b=random.randint(1,50)
	computer=random.choice(list)
	print(str(a) + computer + str(b))
	user=input("What's your answer: ")
	if computer=="+":
		if int(user)==a+b:
			print("Your are correct ")
		else:
			print("You are wrong,the answer is ",a+b)
	if computer=="×":
		if int(user)==a*b:
			print("Your are correct ")
		else:
			print("You are wrong,the answer is ",a*b)
	if computer=="-":
		if int(user)==a-b:
			print("Your are correct ")
		else:
			print("You are wrong,the answer is ",a-b)
	if computer=="/":
		if int(user)==a/b or float(user)==a/b:
			print("Your are correct ")
		else:
			print("You are wrong,the answer is ",a/b)
	replay=input("Would you like to play again(y/n): ")
	if replay!="y":
		print("Thanks for playing")
		break
	else:
		print("Lets continue")
		continue