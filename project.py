li=int(input("Enter your list of odd numbers : "))
list1=[li]
list2=[11,13,15,17,19,21,23,25]
result=map(lambda x,y:x**y,list1,list2)
print("First list is : ",list1)
print("Second list is : ",list2)
print("Final squaring on both lists is : ",list(result))