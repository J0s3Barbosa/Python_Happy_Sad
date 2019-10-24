import tkinter as tk  
from functools import partial  
import HappySad as HsControll
from tkinter import messagebox  

def fun(label_result, num):  
    num1 = (num.get())  
    if num1 > 0:
        response = HsControll.isHappySadNumber(num1)
        if(response):  
            happyResult = str(num1) + " is a happy number"
            label_result.config(text="Result = %s" %happyResult)  
        else:   
            sadResult = str(num1) + " is not a happy number"
            label_result.config(text="Result = %s " %(sadResult))                               
    else:
        messagebox.showinfo("information","Number should be bigger than 0")  

root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('HappySad Number')  
   
number1 = tk.IntVar()  

labelNum1 = tk.Label(root, text="Enter a number").grid(row=1, column=0)  
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
fun = partial(fun, labelResult, number1)  
  
buttonCal = tk.Button(root, text="Check", command=fun).grid(row=3, column=0)  
  
root.mainloop()  
