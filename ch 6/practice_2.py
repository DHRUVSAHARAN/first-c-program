a = int(input ("enter the science marks :"))
b = int(input ("enter the computer marks :"))
c = int(input ("enter the maths marks :"))

if (a<33 or b<33 or c<33):
     print ("you are failed ")

if ((a +b+c)/3) <40:
    print ("you are failed due to inssuiciant marks")

else:
    print("you are passed! ")

