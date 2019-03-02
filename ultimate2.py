#!/usr/bin/python

import Tkinter as tk
import random
import os
import sys
import time
import pprint
from PIL import Image,ImageTk

class TicTacToe(tk.Tk):
    def __init__(self):
        colors=['black','white','red','blue','yellow','brown','orange','pink','purple']
        self.turn=1
        tk.Tk.__init__(self)
        self.geometry("800x800+0+0")
        self.winfo_toplevel().title("Ultimate Tic-Tac-Toe")
        self.col='blue'
        self.mark='O'
        self.abg='light blue'
        #self.abg='pink'
        self.finboxes=[]
        self.frames=[]
        self.boxes={
        'A':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[0,0],'index':1,'buttons':[],'fin':False},
        'B':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[0,1],'index':2,'buttons':[],'fin':False},
        'C':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[0,2],'index':3,'buttons':[],'fin':False},
        'D':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[1,0],'index':4,'buttons':[],'fin':False},
        'E':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[1,1],'index':5,'buttons':[],'fin':False},
        'F':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[1,2],'index':6,'buttons':[],'fin':False},
        'G':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[2,0],'index':7,'buttons':[],'fin':False},
        'H':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[2,1],'index':8,'buttons':[],'fin':False},
        'I':{'subboard':[[1,2,3],[4,5,6],[7,8,9]],'project':[2,2],'index':9,'buttons':[],'fin':False}
        }
        self.ABC=['A','B','C','D','E','F','G','H','I']
        self.masterboard=[[1,2,3],[4,5,6],[7,8,9]]
        self.buttons=[]
        swd=os.getcwd()
        gameboard_img=swd+'/gameboard.jpeg'
        gameboard=ImageTk.PhotoImage(Image.open(gameboard_img))
        self.base=tk.Frame(self)
        self.base.place(x=0,y=0,relheight=1,relwidth=1)
        bckgrd= tk.Label(self.base,image=gameboard)
        self.plyFrm=tk.Frame(self.base,bg='black')
        self.turnFrm=tk.Frame(self.base,padx=3,pady=5,bg='black')
        self.turnFrm.place(relheight=.04,relwidth=.15,relx=0.075,rely=0.01)
        self.turnInd=tk.Label(self.turnFrm,bg='blue',fg='white')
        self.turnInd2=tk.Label(self.turnFrm,text='Turn:'+str(self.turn)+' ',fg='white',bg='black',anchor='c',padx=4,justify='center')
        self.turnInd.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.turnInd2.place(relheight=1,relwidth=.8,relx=.5,rely=.5,anchor='c')

        #plyh,self.plyw=Image.open(hash_img).size
        #print plyh,plyw

        #hash=tk.Label(self.plyFrm,image=hashed)

        self.plyFrm.place(height=700,width=700,relx=0.5,rely=0.5,anchor='center')
        bckgrd.place(x=0,y=0,relwidth=1,relheight=1)


        #print len(self.boxes['A']['subboard'])
        cnt=0
        for k in self.ABC:
            v=self.boxes[k]
            #Creating frame for each subboard
            fi=cnt/3
            fj=cnt%3
            self.frames.append(tk.Frame(self.plyFrm))
            #self.frames[cnt].grid(row=fi,column=fj)
            #print float(fj+1)/3,float(fi+1)/3
            self.frames[cnt].place(relx=float(fj*2+1)/6,rely=float(fi*2+1)/6,relheight=.32,relwidth=.32 ,anchor='c')
            #print self.frames[cnt]['anchor']
            #k['frames']=self.frames[cnt]
            for i in range(len(v['subboard'])*3):
                j=i/3
                l=i%3
                txt=v['project'],j,l,i
                #print v['buttons']
                v['buttons'].append(tk.Button(self.frames[cnt],anchor='center',activebackground='light blue',bg='black',command= lambda sb=k, x=j,y=l :self.placeMark(sb,x,y)))
                #self.buttons[i].grid(row=j,column=l,sticky='E'+'S'+'W')
                v['buttons'][i].place(relx=float(j)/3,rely=float(l)/3,relwidth=float(1)/3,relheight=float(1)/3)
                #print self.buttons[i]['anchor']
                #time.sleep(1)
            cnt+=1
        #for k,v in self.boxes.items():
        #    print k,v
        self.mainloop()
        exit()

    def placeMark(self,sb,x,y):
        print '#######################################################################'
        #print self.buttons
        print 'Turn:',self.turn
        print 'Color/Mark Placed:',self.col,self.mark
        arr=self.boxes[sb]['subboard']
        #print sb,x,y
        tempname="b%d%d" % (x+1,y+1)
        #self.buttons[x*3+y]["bg"]='white'
        if self.mark == 'X':
            self.abg='light blue'
            #self.buttons[x*3+y]["image"]=self.Xmark
        else:
            print' pink'
            self.abg='pink'

        buttarr=self.boxes[sb]['buttons']
        buttinquestion=buttarr[x*3+y]
        buttinquestion['bg']=self.col
        self.boxes[sb]['subboard'][y][x]=self.mark
        #self.abg='pink'


        buttinquestion['state']='disabled'

        self.subwinCheck(sb,x,y)
        self.turn+=1

        if self.mark == 'X':
            self.mark='O'
            self.col='blue'
        else:
            self.mark='X'
            self.col='red'
        self.turnInd['bg']=self.col
        self.turnInd2['text']='Turn:'+str(self.turn)+' '


        print '#######################################################################'
            #print float(j)/3,float(i)/3
    def subwinCheck(self,sb,x,y):
        print 'Subboard Win Check:',self.boxes[sb]['subboard']
        arr=self.boxes[sb]['subboard']
        mx=self.boxes[sb]['project'][0]
        my=self.boxes[sb]['project'][1]
        #print mx,my
        subwin=False
        for i in range(3):
            #print arr[i][:]
            if  len(set([arr[0][i],arr[1][i],arr[2][i]])) == 1:
                subwin=True
                #pprint.pprint(self.masterboard)
            if len(set(arr[i][:])) == 1:
                subwin=True
                #pprint.pprint(self.masterboard)
        if  len(set([arr[0][0],arr[1][1],arr[2][2]])) == 1 or \
            len(set([arr[0][2],arr[1][1],arr[2][0]])) ==1:
            subwin=True

        if subwin == True:
            #pprint.pprint(arr)
            if self.boxes[sb]['fin'] == False:
                for i in self.boxes[sb]['buttons']:
                #    i['state']='disabled'
                    i['text']=self.col
                    self.masterboard[mx][my]=self.mark
            self.boxes[sb]['fin']=True
            self.finboxes.append(sb)
            self.mainwinCheck()
            #pprint.pprint(self.masterboard)
        self.turnTrans(sb,x,y)

    def turnTrans(self,sb,x,y):
        #print 'tt'
        for k,v in self.boxes.items():
            #if y,x == project. setting next sub by looking at current x,y
            if v['project']==[y,x]:
                nsb=k
            if self.turn != 1:
                if v['project']==[self.py,self.px]:
                    psb=k
        print 'Selected Subboard:',sb
        print 'x,y Coordinates',x,y
        print 'Next Subboard',nsb
        print 'Active Background',self.abg


        #if self.turn != 1:
            #print 'psb',psb
            #print 'py,px',self.py,self.px
        # For My rules:v
        #if [y,x] == self.boxes[sb]['project'] or self.ABC[y*3+x] in self.finboxes:
        # For official rules
        test=[]
        for i in self.boxes[nsb]['subboard']:
            for j in i:
                if str(j).isdigit():
                    test.append(j)
        #for c,i in enumerate(self.boxes[sb]['subboard']):
        #    print i
        #    test[c]=[j for j in i if str(j).isdigit()]
        if test == []:
        #if [y,x] ==  self.ABC[y*3+x] in self.finboxes:
            print 'A filled subboard was selected, opening board'
            #cycle through keys to open up spaces
            for k,v in self.boxes.items():
                for i in v['buttons']:
                    #if v['fin'] == False:
                        if i['bg'] == 'black' or i['bg'] == 'gray':
                            i['bg']='black'
                            i['state']='normal'
                            #print self.abg
                            i['activebackground']=self.abg
            #print 'nsb=',nsb
            #print 'open','all'
        else:
            for k in self.boxes.keys():
                if  k != nsb:
                    #print nsb
                    for i in self.boxes[k]['buttons']:
                        i['state']='disabled'
                        if i['bg'] == 'black':
                            i['bg'] = 'gray'
                else:
                    for i in self.boxes[k]['buttons']:
                        if i['bg'] == 'gray' or i['bg'] == 'black':
                            i['state']='normal'
                            i['bg'] = 'black'
                            #print self.abg
                            i['activebackground']=self.abg

            #print sb
            if self.turn != 1:
                if psb != nsb:
                    for i in self.boxes[psb]['buttons']:
                        if i['bg'] == 'black' and i['state']=='normal':
                            #print psb,self.px,self.py,i['bg'],i['state']
                            i['bg'] = 'gray'
                            print self.abg
                            #if self.boxes[psb]['fin']==False:
                            #    i['state']='disabled'
                            #print psb,self.px,self.py,i['bg'],i['state']
                            #print
                    #print 'nsb=',nsb
                    #print 'psb=',psb
                    #print 'open',nsb
        self.px=x
        self.py=y


    def mainwinCheck(self):
        arr=self.masterboard

        #print mx,my
        for i in range(3):
            print 'Main Subboard Win Check:',arr[i][:]
            if  len(set([arr[0][i],arr[1][i],arr[2][i]])) == 1:
                pprint.pprint(self.masterboard)
                self.gameOver()
                #
            if len(set(arr[i][:])) == 1:
                pprint.pprint(self.masterboard)
                self.gameOver()
                #pprint.pprint(self.masterboard)
        if  len(set([arr[0][0],arr[1][1],arr[2][2]])) == 1 or \
            len(set([arr[0][2],arr[1][1],arr[2][0]])) ==1:
            pprint.pprint(self.masterboard)
            self.gameOver()


    def gameOver(self):
        for v in self.boxes.values():
            for i in v['buttons']:
                i['command']=""
        print 'Game Over'
        if self.turn % 2 == 1:
            win=tk.Label(self.base,fg='blue',text='Blue Wins!')
            print 'Blue Wins!'
        else:
            win=tk.Label(self.base,fg='red',text='Red Wins!')
            print 'Red Wins!'
        win.place(relx=.5,rely=0.15,relheight=0.15,width=750,anchor='center')
        self.keepGoing()

    def keepGoing(self):
        playAgain=tk.Frame(self.base)
        more=tk.Button(playAgain,fg='white',activebackground='gray',bg='black',text='Exit',command=lambda:self.leave())
        less=tk.Button(playAgain,fg='white',activebackground='gray',bg='black',text='Play Again',command=lambda:self.playAgain())
        playAgain.place(relx=.5,rely=0.85,relheight=0.15,width=750,anchor='center')
        more.place(relx=.25,rely=0.5,relheight=1,relwidth=.5,anchor='center')
        less.place(relx=.75,rely=0.5,relheight=1,relwidth=.5,anchor='center')

    def leave(self):
        exit()
    def playAgain(self):
        self.destroy()
        self.__init__()


board=TicTacToe()
#!/usr/bin/python
