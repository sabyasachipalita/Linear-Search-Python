def linear_serch(list,n,key):
            for i in range(0,n):
                    if(list[i]==key):
                            return i
            return -1

list=[1,2,3,4,5,6,7]
n=len(list)
key=3
s=linear_serch(list,n,key)
if(s==-1):
        print("elements is not position")
else:
        print("elements is present",s)








# to find the linear serch in python
# def linear_serch(list,key,n):
#         for i in range(0,n):
#                 if(list[i]==key):
#                         return i
#         return -1

# list=[1,2,3,4,5]
# n=len(list)
# key=4
# s=linear_serch(list,key,n)
# if(key==-1):
#         print("elements is not in position")
# else:
#         print("elements is present at the position",s)






# #code in binary serch in python
# def binary_serch(arr,target):
#         low=0
#         high=len(arr)-1
#         while low<=high:
#               mid=(high+low)//2
#               if(arr[mid]==target):
#                   return mid
#               elif(arr[mid]<target):
#                 low=mid+1
#               else:
#                 high=mid-1
#         return -1        



# arr=[1,2,3,4,5,6,7,8,9,10]
# d=binary_serch(arr,6)
# print("the position is that",d)



        
                        
