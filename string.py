#!/usr/bin/python
#---utf-8---
temp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#访问单个元素
print(temp[0]) #A
print(temp[-1]) #Z

#普通切片操作
print(temp[0:10])   #ABCDEFGHIJ
#隔着取
print(temp[0:10:2])    #ACEGI

#输出从第一个到倒数第N个数
print(temp[0:-2])     #ABCDEFGHIJKLMNOPQRSTUVWX
print(temp[:-2])    #ABCDEFGHIJKLMNOPQRSTUVWX
print(temp[-2:])     #YZ

#逆序输出
print(temp[::-1])    #ZYXWVUTSRQPONMLKJIHGFEDCBA

#循环迭代输出
for s in temp:
    print(s,end=' ' )    #A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
