key =['test']

def test(mylist, mydict):
    mylist.append('hallo')
    mydict[key]= 10

mylist=[1]
mydict={}
print(mylist)
print(mydict)

test(mylist, mydict)

print(mylist)
print(mydict)

key.append('item')

mydict['key'] = 15

print(mydict)