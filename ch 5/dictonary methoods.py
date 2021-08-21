mydict = {
"fast": "in a quick manner ",
"toxic": "something poisness",
"marks": [1,3,5,8,5]

}

print(mydict.keys())
print(mydict.values())
print(list(mydict.items()))
print (mydict)
updatedict = {
    "udhav": "brother" 
}
mydict.update(updatedict)
print (mydict)
print(mydict.get("toxic"))