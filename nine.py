# #Loops:--

# # while Loop 

# count=1
# while count <=5 :
#     print("hello")
#     count +=1


# i=1
# while i<=6:
#     print("Hello Ram")
#     i=i+1

# #print numbers 1 to 5
# j=1
# while j<=5:
#     print(j)
#     j +=1

# print("Loop Ended")

# #print number 5 to 1
# k=5
# while k>=1:
#     print(k)
#     k -=1

# print("Loop Ended")


# #print 1 to 100
# l=1
# while l<=100:
#     print(l)
#     l+=1

# #print 100 to 1
# m=100
# while m>=1:
#     print(m)
#     m-=1

# #print multiplicaton table of a number n
# n=1
# while n<=10:
#     print(3*n)
#     n+=1

# # #input number

# # a=int(input("enter number: "))
# # b=1
# # while b<=10:
# #     print(a*b)
# #     b+=1

# # Print the list[] 
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1

# heros=["heroman","superman","spiderman","ravan","rama"]
# indx=0
# while indx<len(heros):
#     print(heros[indx])
#     indx+=1


# Search for a number x in this tuple using loop 
# ns = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 49
# i = 0

# while i < len(ns):
#     if ns[i] == x:
#         print("Found at idx", i)
#         break
#     i += 1


# Break & Continue :---

# i=1
# while i<= 5:
#     print(i)
#     if(i==3):
#         break
#     i +=1
# print("end of the loop")


#  continue:---
# i=0
# while i <= 5:
#     if(i==3):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1


# i=0
# while i <= 10:
#     if(i%2==0):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1


# --------------------- For Loops:--
# vegitable=["potato","brinjal","ladyfinger","cucumber"]
# for val in vegitable:
#     print(val)


# tup = (1,2,3,45,6,8,5)
# for val2 in tup:
#     print(val2)

# for using else loop 

# str="Bhimashankar"
# for char in str:
#     if(char == 's'):
#         print("s found")
#         break
#     print(char)
# else:
#     print("End")


#print the element of the following list using a loop:
# ns=[1,4,9,16,25,36,49,64,81,100]
# for val in ns:
#     print(val)


#Search for a number x in this tuple using loop:
# ns=(1,4,9,16,25,36,49,64,9,100)
# x=9
# idx=0

# for el in ns:
#     if(el ==x):
#         print("number found at idx",idx)
#         break # if need only on time number need
#     idx += 1


# range(start,stop,step):--
# print(range(5))

# seq=range(10) #range(stop)
# for i in seq:
#     print(i)


# seq=range(2,10) #range(start,stop)
# for i in seq:
#     print(i)


# seq=range(0,10,3) #range(start,stop,step)
# for i in seq:
#     print(i)


# seq=range(0,100,2) #range(start.stop,step)
# for i in seq:
#     print(i)

# practise:==================
# print 1 to 100

# for i in range(1,101):
#     print(i)

# #numbers 100 to 1
# for i in range(100,0,-1):
#     print(i)


# # print the multiplication table of n number n.
# n=int(input("enter number: "))
# for i in range(1,11):
#     print(n*i)



#Pass Statement:------------------(null loop)
# for i in range(5):
#     pass
# print("Bhimashankar")


# Practise: ---=====
# wap to find the sum of natural numbers.(using while)

# n=10
# sum=0

# for i in range(1,n+1):
#     sum +=i
# print("Total sum =",sum)


# WAP to find the factorial of first n numbers,(using for)
# n=7
# sum=0
# i=1
# while i<=n:
#     sum +=i
#     i +=1
# print("Total sum=",sum)


#WAP to find the factorial of first n number (using for(1*2*3*4*n))
# n=7
# fact=1
# i=1
# while i<=n:
#     fact *=i
#     i +=1
# print("Factorial =",fact)

#for Loop:--
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("factorial=",fact)