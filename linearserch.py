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



















        
                        
