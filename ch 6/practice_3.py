from typing import Text


comment = input("enter the comment :")
spam= False
if("make a lot of money" in comment):
    spam =True
elif("buy now " in comment):
    spam = True
elif("watch this  " in comment):
    spam = True
elif("subscribe this " in comment):
    spam = True
else:
    spam = False

if (spam):
    print("this text is spam")
else:
    print("this text is not spam")

