def multiply(i):
    return i*i
x=map(multiply,(3,5,7,11,13))
print(list(x))

# example = ["welcome","to","sem3"]
# x=list(map(len,example))
# print(x)

# def example(s):
#     return s.upper()
# tuple_exm = ('this','is',' map')
# upd_tup=map(example,tuple_exm)
# print(tuple(upd_tup))

# def example(i):
#     return i%3
# set_exm ={33,102,62,96,44,28,227}
# upd_itms = map(example,set_exm)
# print(set(upd_itms))


# # mapfunction,iter(list,tuple,set,dictionary)
# import numbers
# from tkinter.tix import Tree
# from unittest import result


# def multiply(num):
    # return num*num
# result=map(multiply,(2,4,6,8))
# print(tuple(result))

# using lambda function
# result=map(lambda num:num*num,(2,4,6,8))#lambda var:return
# print(tuple(result))

# to convert into upper case
# def toUpper(str):
#     return str.upper()
# result=map(toUpper,("software","sem","3"))
# print(tuple(result))

# to append in list
# newlist=list(result)
# newlist.append("hey")
# print(newlist)
# newlist1=list(result)
# newlist1.append("hey tuple")
# print(newlist1)


# dict_item={"a":"car","b":"bike","c":"train"}
# a=map(lambda i:(i[0]+"_",i[1]+"s"),dict_item.items())
# print(dict(a))




# 1 oct


# to check number is even or odd using filter


# numbers=[1,2,3,4,5,6,7,8,9,10]

# def check_even(number):
#     if number%2==0:
#         return True
#     return False

# even_number_iterator=filter(check_even,numbers)
# even_numbers=list(even_number_iterator)
# print(even_numbers)

# to check vowels using filter 

# letters=['a','b','d','e','i','j','o']

# def filter_vowels(letter):
#     vowels = ['a','e','i','o','u']
#     return True if letter in vowels else False

# filtered_vowels = filter(filter_vowels,letters)
# vowels= list(filtered_vowels)
# print(vowels)

# number to check even or odd using lambda
# number=[1,2,3,4,5,6,7]
# even_number_iterator=filter(lambda x:(x%2==0),number)
# even_number=list(even_number_iterator)
# print(even_number)


# tkinter

# from tkinter import *
# root = Tk()
# root.mainloop() 




# from tkinter import *
# from tkinter import messagebox
# top = Tk()
# top.geometry("200x100")
# def fun():
#     messagebox.showinfo("hello",'red button clicked')
# b1=Button(top,text="red",command=fun,activebackground="red", activeforeground="pink",pady=10)
# b2=Button(top,text="green",activeforeground="green",activebackground="pink",pady=10)
# b3=Button(top,text="blue",activeforeground="green",activebackground="pink",pady=10)
# b4=Button(top,text="violet",activeforeground="green",activebackground="pink",pady=10)

# b1.pack(side=LEFT)
# b2.pack(side=RIGHT)
# b3.pack(side=TOP)
# b4.pack(side=BOTTOM)
# top.mainloop()


# from tkinter import *
# pane=Tk()
# b1=Button(pane,text="click me!")
# b1.pack(fill=Y,expand=True)

# b2=Button(pane,text="click me too")
# b2.pack(fill=X,expand=True)

# pane.mainloop()

# from tkinter import *

# m=Tk()
# # m.geometry("500x500")
# b1=Button(m,text="submit")
# b1.place(anchor=CENTER)
# m.mainloop()



# try:
#     print("try block")
#     num1=int(input("enter first number"))
#     num2=int(input("enter second number"))
#     res=num1/num2
# except:
#     print("else block ")
#     print("number 1 is not divisible by zero")
# else:
#     print("else block")
#     print("output ",res)
# finally:print("exceptional handling program")


# try:
#     print("try block")
#     age=int(input("enter your age"))
#     if age>18:
#         print("enter again")
#         raise ValueError(age)
# except ValueError:
#     print(age,"above 18")
# else:
#     print(age,"good")