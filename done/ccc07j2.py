d = {"CU":'see you', ":-)":"I'm happy", ":-(":"I'm unhappy", ";-)":"wink",
	 ":-P":"stick out my tongue", "(~.~)":"sleepy", "TA":"totally awesome",
	 "CCC":"Canadian Computing Competition", "CUZ":"because", "TY":"thank-you",
	 "YW":"you're welcome", "TTYL":"talk to you later"}
	 
a = input()
while(True):
	print(d.get(a, a))
	if a == "TTYL": break
	a = input()
