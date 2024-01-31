Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import*
>>> from tkinter import ttk
>>> import tkinter as tk
>>> window=tk.Tk()
>>> greeting=tk.Label(text="Registartion form")
>>> greeting.pack()
>>> Label1=tk.Label(text="Hello,Tkinter",fg="white",bg="black",width=10,height=10)
>>> Label1=tk.Label(text="Enter Name",fg="white",bg="black",width=10,height=10)
>>> entry1=tk.entry
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    entry1=tk.entry
AttributeError: module 'tkinter' has no attribute 'entry'. Did you mean: 'Entry'?
>>> entry1=tk.Entry
>>> Label2=tk.Label(text="Enter password",fg="white",bg="black",width=10,height=10)
>>> entry2=tk.Entry()
>>> button1=tk.Button(text="sign in")
>>> button2=tk.Button(text="sign up")
>>> Label1.pack()
>>> Entry1.pack()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Entry1.pack()
NameError: name 'Entry1' is not defined. Did you mean: 'entry1'?
>>> entry1.pack()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    entry1.pack()
TypeError: Pack.pack_configure() missing 1 required positional argument: 'self'
>>> entry.pack()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    entry.pack()
NameError: name 'entry' is not defined. Did you mean: 'Entry'?
>>> entry1=tk.Entry()
>>> entry1.pack()
>>> Label2.pack()
>>> entry2.pack()
>>> button1.pack()
>>> button2.pack()
name=Entry1.get()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name=Entry1.get()
NameError: name 'Entry1' is not defined. Did you mean: 'entry1'?
name=entry1.get()
print(name)
Shubham
name=entry2.get()
print(name)
Rahul760
name=entry1.delete(0)
print(name)
None
name=entry2.insert(0,"kane")
print(name)
None
name1=entry2.insert(0,"kane")
print(name1)
None
