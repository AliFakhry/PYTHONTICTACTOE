from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
import shutil
import glob

root=Tk()
root.title("AI TICTACTOE VS PLAYER!")

#VARIABLES

bu1=ttk.Button(root,text=' ')
bu1.grid(row=1,column=0,sticky='snew',ipadx=90,ipady=90)
bu1.config(command=lambda: RUNNING(1))

bu2=ttk.Button(root,text=' ')
bu2.grid(row=1,column=1,sticky='snew',ipadx=90,ipady=90)
bu2.config(command=lambda: RUNNING(2))

bu3=ttk.Button(root,text=' ')
bu3.grid(row=1,column=2,sticky='snew',ipadx=90,ipady=90)
bu3.config(command=lambda: RUNNING(3))

bu4=ttk.Button(root,text=' ')
bu4.grid(row=2,column=0,sticky='snew',ipadx=90,ipady=90)
bu4.config(command=lambda: RUNNING(4))

bu5=ttk.Button(root,text=' ')
bu5.grid(row=2,column=1,sticky='snew',ipadx=90,ipady=90)
bu5.config(command=lambda: RUNNING(5))

bu6=ttk.Button(root,text=' ')
bu6.grid(row=2,column=2,sticky='snew',ipadx=90,ipady=90)
bu6.config(command=lambda: RUNNING(6))

bu7=ttk.Button(root,text=' ')
bu7.grid(row=3,column=0,sticky='snew',ipadx=90,ipady=90)
bu7.config(command=lambda: RUNNING(7))

bu8=ttk.Button(root,text=' ')
bu8.grid(row=3,column=1,sticky='snew',ipadx=90,ipady=90)
bu8.config(command=lambda: RUNNING(8))

bu9=ttk.Button(root,text=' ')
bu9.grid(row=3,column=2,sticky='snew',ipadx=90,ipady=90)
bu9.config(command=lambda: RUNNING(9))

a="XTURN"
DRAWCOUNT=0


def RUNNING(id):
    global a,DRAWCOUNT

    print(DRAWCOUNT)
    
    #PLAYER CLICKING BUTTONS!
    
    if id==1 and bu1['text']==' ' and a=="XTURN":
        bu1['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
    elif id==2 and bu2['text']==' ' and a=="XTURN":
        bu2['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
    elif id==3 and bu3['text']==' ' and a=="XTURN":
        bu3['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
    elif id==4 and bu4['text']==' ' and a=="XTURN":
        bu4['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
    elif id==5 and bu5['text']==' ' and a=="XTURN":
        bu5['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
    elif id==6 and bu6['text']==' ' and a=="XTURN":
        bu6['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
    elif id==7 and bu7['text']==' ' and a=="XTURN":
        bu7['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
    elif id==8 and bu8['text']==' ' and a=="XTURN":
        bu8['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
    elif id==9 and bu9['text']==' ' and a=="XTURN":
        bu9['text']="X"
        a="OTURN"
        DRAWCOUNT+=1
        
    #AI MOVES:

    #TRYING TO WIN

    #HORIZONTAL WIN (LAST SPOT EMPTY)
    if  bu1['text']=="O" and bu2['text']=="O" and a=="OTURN" and bu3['text']==' ':
        bu3['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu4['text']=="O" and bu5['text']=="O" and a=="OTURN" and bu6['text']==' ':
        bu6['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu7['text']=="O" and bu8['text']=="O" and a=="OTURN" and bu9['text']==' ':
        bu9['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
   #HORIZONTAL BLOCKS (CENTER SPOT EMPTY)
    elif  bu1['text']=="O" and bu3['text']=="O" and a=="OTURN" and bu2['text']==' ':
        bu2['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu4['text']=="O" and bu6['text']=="O" and a=="OTURN" and bu5['text']==' ':
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu7['text']=="O" and bu9['text']=="O" and a=="OTURN" and bu8['text']==' ':
        bu8['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    #HORIZONTAL BLOCKS (FIRST SPOT EMPTY)

    elif  bu2['text']=="O" and bu3['text']=="O" and a=="OTURN" and bu1['text']==' ':
        bu1['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu5['text']=="O" and bu6['text']=="O" and a=="OTURN" and but4['text']==' ':
        bu4['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu8['text']=="O" and bu9['text']=="O" and a=="OTURN" and bu7['text']==' ':
        bu7['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    #VERTICAL BLOCKS (LAST SPOT EMPTY)
    
    elif  bu1['text']=="O" and bu4['text']=="O" and a=="OTURN" and bu7['text']==' ':
        bu7['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu2['text']=="O" and bu5['text']=="O" and a=="OTURN" and bu8['text']==' ':
        bu8['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu3['text']=="O" and bu6['text']=="O" and a=="OTURN" and bu9['text']==' ':
        bu9['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    #VERTICAL BLOCKS (CENTER SPOT EMPTY)
    
    elif  bu1['text']=="O" and bu7['text']=="O" and a=="OTURN" and bu4['text']==' ':
        bu4['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu2['text']=="O" and bu8['text']=="O" and a=="OTURN" and bu5['text']==' ':
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu3['text']=="O" and bu9['text']=="O" and a=="OTURN" and bu6['text']==' ':
        bu6['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
   #VERTICAL BLOCKS (FIRST SPOT EMPTY)
    
    elif  bu4['text']=="O" and bu7['text']=="O" and a=="OTURN" and bu1['text']==' ':
        bu1['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu5['text']=="O" and bu8['text']=="O" and a=="OTURN" and bu2['text']==' ':
        bu2['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu6['text']=="O" and bu9['text']=="O" and a=="OTURN" and bu3['text']==' ':
        bu3['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    #DIAGONAL (PART ONE)

    elif  bu1['text']=="O" and bu5['text']=="O" and a=="OTURN" and bu9['text']==' ':
        bu9['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu5['text']=="O" and bu9['text']=="O" and a=="OTURN" and bu1['text']==' ':
        bu1['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu1['text']=="O" and bu9['text']=="O" and a=="OTURN" and bu5['text']==' ':
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    #DIAGONAL (PART TWO)

    elif  bu3['text']=="O" and bu7['text']=="O" and a=="OTURN" and bu5['text']==' ':
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu3['text']=="O" and bu5['text']=="O" and a=="OTURN" and bu7['text']==' ':
        bu7['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu5['text']=="O" and bu7['text']=="O" and a=="OTURN" and bu9['text']==' ':
        bu9['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    #TRY TO BLOCK
        
    #HORIZONTAL BLOCKS (LAST SPOT EMPTY)
    elif  bu1['text']=="X" and bu2['text']=="X" and a=="OTURN" and bu3['text']==' ':
        bu3['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu4['text']=="X" and bu5['text']=="X" and a=="OTURN" and bu6['text']==' ':
        bu6['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu7['text']=="X" and bu8['text']=="X" and a=="OTURN" and bu9['text']==' ':
        bu9['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
   #HORIZONTAL BLOCKS (CENTER SPOT EMPTY)
    elif  bu1['text']=="X" and bu3['text']=="X" and a=="OTURN" and bu2['text']==' ':
        bu2['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu4['text']=="X" and bu6['text']=="X" and a=="OTURN" and bu5['text']==' ':
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu7['text']=="X" and bu9['text']=="X" and a=="OTURN" and bu8['text']==' ':
        bu8['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    #HORIZONTAL BLOCKS (FIRST SPOT EMPTY)

    elif  bu2['text']=="X" and bu3['text']=="X" and a=="OTURN" and bu1['text']==' ':
        bu1['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu5['text']=="X" and bu6['text']=="X" and a=="OTURN" and bu4['text']==' ':
        bu4['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu8['text']=="X" and bu9['text']=="X" and a=="OTURN" and bu7['text']==' ':
        bu7['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    #VERTICAL BLOCKS (LAST SPOT EMPTY)
    
    elif  bu1['text']=="X" and bu4['text']=="X" and a=="OTURN" and bu7['text']==' ':
        bu7['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu2['text']=="X" and bu5['text']=="X" and a=="OTURN" and bu8['text']==' ':
        bu8['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu3['text']=="X" and bu6['text']=="X" and a=="OTURN" and bu9['text']==' ':
        bu9['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    #VERTICAL BLOCKS (CENTER SPOT EMPTY)
    
    elif  bu1['text']=="X" and bu7['text']=="X" and a=="OTURN" and bu4['text']== ' ':
        bu4['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu2['text']=="X" and bu8['text']=="X" and a=="OTURN" and bu5['text']== ' ':
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu3['text']=="X" and bu9['text']=="X" and a=="OTURN" and bu6['text']== ' ':
        bu6['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
   #VERTICAL BLOCKS (FIRST SPOT EMPTY)
    
    elif  bu4['text']=="X" and bu7['text']=="X" and a=="OTURN" and bu1['text']==' ':
        bu1['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu5['text']=="X" and bu8['text']=="X" and a=="OTURN" and bu2['text']==' ':
        bu2['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu6['text']=="X" and bu9['text']=="X" and a=="OTURN" and bu3['text']== ' ':
        bu3['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    #DIAGONAL (PART ONE)

    elif  bu1['text']=="X" and bu5['text']=="X" and a=="OTURN" and bu9['text']==' ':
        bu9['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu5['text']=="X" and bu9['text']=="X" and a=="OTURN" and bu1['text']==' ':
        bu1['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu1['text']=="X" and bu9['text']=="X" and a=="OTURN" and bu5['text']==' ':
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    #DIAGONAL (PART TWO)

    elif  bu3['text']=="X" and bu7['text']=="X" and a=="OTURN" and bu5['text']==' ':
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu3['text']=="X" and bu5['text']=="X" and a=="OTURN" and bu7['text']==' ':
        bu7['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu5['text']=="X" and bu7['text']=="X" and a=="OTURN" and bu3['text']==' ':
        bu3['text']="O"
        a="XTURN"
        DRAWCOUNT+=1


    #CAN'T WIN OR BLOCK

    elif  bu1['text']==' ' and a=="OTURN":
        bu1['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    elif  bu2['text']==' ' and a=="OTURN":
        bu2['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu3['text']==' ' and a=="OTURN":
        bu3['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    elif  bu4['text']==' ' and a=="OTURN":
        bu4['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    elif  bu5['text']==' ' and a=="OTURN":
        bu5['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
        
    elif  bu6['text']==' ' and a=="OTURN":
        bu6['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    elif  bu7['text']==' ' and a=="OTURN":
        bu7['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    elif  bu8['text']==' ' and a=="OTURN":
        bu8['text']="O"
        a="XTURN"
        DRAWCOUNT+=1

    elif  bu9['text']==' ' and a=="OTURN":
        bu9['text']="O"
        a="XTURN"
        DRAWCOUNT+=1
    
    #CHECKS TO SEE IF THERE IS A WINNER
    if( bu1['text']=='X' and bu2['text']=='X' and bu3['text']=='X' or
        bu4['text']=='X' and bu5['text']=='X' and bu6['text']=='X' or
        bu7['text']=='X' and bu8['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu4['text']=='X' and bu7['text']=='X' or
        bu2['text']=='X' and bu5['text']=='X' and bu8['text']=='X' or
        bu3['text']=='X' and bu6['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu5['text']=='X' and bu9['text']=='X' or
        bu3['text']=='X' and bu5['text']=='X' and bu7['text']=='X'):

            tkinter.messagebox.showinfo("THE WINNER IS THE PLAYER! GOOD JOB!")
            bu1['text']=' '
            bu2['text']=' '
            bu3['text']=' '
            bu4['text']=' '
            bu5['text']=' '
            bu6['text']=' '
            bu7['text']=' '
            bu8['text']=' '
            bu9['text']=' '
            
            a="XTURN"

            DRAWCOUNT=0
    
            RUNNING()

    elif( bu1['text']=='O' and bu2['text']=='O' and bu3['text']=='O' or
        bu4['text']=='O' and bu5['text']=='O' and bu6['text']=='O' or
        bu7['text']=='O' and bu8['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu4['text']=='O' and bu7['text']=='O' or
        bu2['text']=='O' and bu5['text']=='O' and bu8['text']=='O' or
        bu3['text']=='O' and bu6['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu5['text']=='O' and bu9['text']=='O' or
        bu3['text']=='O' and bu5['text']=='O' and bu7['text']=='O'):

            
            tkinter.messagebox.showinfo("THE AI WON!")
            bu1['text']=' '
            bu2['text']=' '
            bu3['text']=' '
            bu4['text']=' '
            bu5['text']=' '
            bu6['text']=' '
            bu7['text']=' '
            bu8['text']=' '
            bu9['text']=' '

            a="XTURN"

            DRAWCOUNT=0

            RUNNING()

            
    elif DRAWCOUNT==9:
            
            tkinter.messagebox.showinfo("A DRAW. TOUGH.")
            bu1['text']=' '
            bu2['text']=' '
            bu3['text']=' '
            bu4['text']=' '
            bu5['text']=' '
            bu6['text']=' '
            bu7['text']=' '
            bu8['text']=' '
            bu9['text']=' '

            a="XTURN"

            DRAWCOUNT=0

            RUNNING()


root.mainloop()
