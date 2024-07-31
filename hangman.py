# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 07:52:42 2020

@author: microsoft
"""

def hangman():
    global ss,ll,ssl,n,ffdata,temps,inpp,input1,first,wordlabel,ans,leftchances,introlabel,root
    first=inpp.get()
    input1.delete(0,END)
    if(n>0):
        if(first in ss):
            for i in range(ssl):
                if(ss[i]==first and ll[i]=='*'):
                    ll.pop(i)
                    ll.insert(i,ss[i])
                    xx=''.join(ll)
                    ss=list(ss)
                    ss.pop(i)
                    ss.insert(i,'*')
                    wordlabel.configure(text=xx)
                    if(xx==temps):
                        ans.configure(text='congratulation you won the game.....')
                        res=messagebox.askyesno("Notification",'congratulation you won the game..... \n want to play again?')
                        if(res==True):
                            chooseword()
                        else:
                            root.destroy()
                    else:
                        break
        else:
            n-=1
            leftchances.configure(text='Left={}'.format(n))
    if(n<=0):
        ans.configure(text='oops! you loss the game.....')
        res=messagebox.askyesno("Notification",'oops you loss the game..... \n want to play again?')
        if(res==True):
            chooseword()
        else:
            root.destroy()
        
def jj(event):
    hangman()
from tkinter import*
import random
wordlist=['black','white','red','blue','green','orange','grey','brown','pink','yellow','purple','golden','violet','chocolate','silver','cream','maroon','lime','peach','indigo','cherry','lemon','skyblue']

def main():
    global ss,ll,ssl,n,ffdata,temps,inpp,input1,wordlabel,ans,leftchances,introlabel,root,chooseword
    root = Tk()
    root.configure(bg='cyan')
    root.title('hangman game')
    root.minsize(width=800,height=500)
    
    introlabel=Label(root,text='welcome to hagman game',font=('arial',35,'underline bold'),bg='cyan')
    introlabel.place(x=100,y=10)
    
    wordlabel=Label(root,text='',font=('arial',55,'bold'),bg='cyan',fg='red')
    wordlabel.place(x=300,y=150)
    
    leftchances=Label(root,text='',font=('arial',25,'bold'),bg='cyan')
    leftchances.place(x=650,y=100)
    
    ans=Label(root,text='',font=('arial',25,'bold'),bg='cyan')
    ans.place(x=150,y=440)
    
    inpp=StringVar()
    input1=Entry(root,font=('arial',25,'bold'),relief=RIDGE,bd=5,bg='green',justify='center',fg='white',textvariable=inpp)
    input1.focus_set()
    input1.place(x=210,y=250)
    
    bt1=Button(root,text='submit',font=('arial',15,'bold'),width=15,bd=5,bg='red',activebackground='blue',activeforeground='white',command=hangman)
    bt1.place(x=300,y=350)
    root.bind("<Return>",jj)
    
    def chooseword():
        global ss,ll,ssl,n,ffdata,temps
        ss=random.choice(wordlist)
        ll=["*" for i in ss]
        ssl=len(ss)
        n=ssl
        temps=ss
        leftchances.configure(text='left={}'.format(n))
        
        ffdata=''
        for i in ll:
            ffdata+=i+' '
        wordlabel.configure(text=ffdata)
        ans.configure(text='')
        
    chooseword()
    root.mainloop()

if __name__=="__main__":
    main()
