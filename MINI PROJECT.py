from tkinter import *
from PIL import Image,ImageTk
from tkinter import Tk, Label, Button
from tkinter import messagebox
from playsound import playsound
import random
root1=Tk()
root1.title("battleships")
root1.geometry("800x800")
image1 = Image.open("pictureproj.jpg")
background = ImageTk.PhotoImage(image1)
root1.configure(bg='black')
label1 =Label(image=background).place(x=350,y=370)
def instructions():
    root2=Tk()
    instructions1="""
    HOW TO PLAY?
    1)You have 3 SHIPS which are 5 units, 4 units and 3 units long respectively 
    2)Out of 100 boxes these 3 ships will be placed randomly
    3)Hit each ship by clicking on the square , each time you hit a ship the square turns red if you miss ,it turns blue 
    4)Upon destroying the whole ship the messagebox box also indicts the same 
    5)You win the game if you guess where all 3 ships are under 35 CHANCES"""
    instructionslabel=Label(root2,text=instructions1,font=("Rockwell",15),bg='turquoise').pack()
def quit(): 
    res=messagebox.askyesno("QUIT", "Are you sure you want to quit?")
    if res==True:
        root1.quit()
    else:
        pass

shipsize=0
def startgame():
    #CREATING THE MAIN SCREEN
    root=Tk()
    root.geometry("500x550")
    root.wm_title("BATTLESHIPS")
    root.configure(background='gray19')
    matches=[]
    Font_tuple1 = ("Comic Sans MS", 20, "bold")
    result=LabelFrame(root,bg="lightblue",text="RESULT",width=200,height=200,font=Font_tuple1)
    def restart():
        #"""Restart the game!"""    
        ##python = sys.executable
        #os.execl(python, python, * sys.argv)
        root.destroy()
        startgame()

    restartbutton=Button(root,text="RESTART GAME",command=restart,bg="yellow",font='Bahnschrift',width=15,height=5)
    restartbutton.pack()
    restartbutton.place(x=800,y=100)

    result.pack(fill='both')
    result.place(x=800,y=300)
    global tries
    #global resultLabel
    tries=35
    Font_tuple2=("Comic Sans MS",15, "bold")
    tryLabel = Label(result, bg="lightblue",text="NUMBER OF TRIES: "+str(tries),height=2,width=50,font=Font_tuple2)
    #tryLabel.place(x=10,y=50)
    tryLabel.pack()
    
    #resultLabel=Label(result,height=5,width=50)
    #resultLabel.place(relx=0,rely=0)
    #resultLabel.pack()
    hitLabel=Label(result,text=" ",bg="lightblue",height=2,width=50,font=Font_tuple2,fg="red")
    hitandsunkLabel=Label(result,text=" ",bg="lightblue",height=2,width=50,font=Font_tuple2,fg="green")
    winLabel=Label(result,text=" ",bg="lightblue",height=2,width=50,font=Font_tuple2,fg="blue")
    hitLabel.pack()
    hitandsunkLabel.pack()
    winLabel.pack()

    for i in range(10):
        for j in range(10):
            matches.append(str(i)+str(j))

    '''
    myframe=Frame(root)
    myframe.grid(row=0,column=0,columnspan=10)
    '''

    #ARRAY OF SHIPS
    ships = [i for i in range(1, 100)]
    allships = {}
    badcoord = False
    global ship_len
    for i in range(1, 4):
        is_vertical = random.randint(0, 1)
        if is_vertical:#if it vertical
            ship_len = i + 2
            while True:
                #ship_coord = random.randint(0, 99)
                # fix the x not found error bcoz the sys cud gen same randint
                ship_coord = random.choice(ships)
                badcoord = False
                if ship_coord // 10 <= (10 - ship_len):#check if there is enough rows to go down from start position
                    for j in range(ship_len):
                        if(ship_coord + 10 * j) not in ships:#if the condition is true then the previous ship has already been placed so ignore
                            badcoord = True#if this variable is true then it refers to the already placed coords   
                            break
                    if badcoord: continue
                    # if it reaches here, it means that this is a viable coordinate
                    for j in range(ship_len):
                        ships.remove(ship_coord + 10 * j)#This makes sure that the next iteration doesnt pick up the previous coordinates
                    #allships[i] = [str(ship_coord + 10 * j) for j in range(ship_len)]
                    # fix the bug for 08 not recognized
                    allships[i]=[str(ship_coord+10*j) if (ship_coord+10*j > 9) else "0" + str(ship_coord+10*j) for j in range(ship_len)]

                    break
        else:#if it is horizontal
            ship_len = i + 2
            while True:
                #ship_coord = random.randint(0, 99)
                # fix the x not found error bcoz the sys cud gen same randint
                ship_coord = random.choice(ships)
                badcoord = False
                # fix overlap of rows -for horz change // to %
                if ship_coord % 10 <= (10 - ship_len):#check if there is enough rows to go down from start position
                    for j in range(ship_len):
                        if (ship_coord + j) not in ships:#if the condition is true then the previous ship has already been placed so ignore
                            badcoord = True
                            break
                    if badcoord: continue
                    # if it reaches here, it means that this is a viable coordinate
                    for j in range(ship_len):
                        ships.remove(ship_coord + j)#This makes sure that the next iteration doesnt pick up the previous coordinates
                    #allships[i] = [str(ship_coord + j) for j in range(ship_len)]
                    # fix the bug for 08 not recog
                    allships[i]=[str(ship_coord+j) if (ship_coord+j > 9) else "0" + str(ship_coord+j) for j in range(ship_len)]
                    
                    break

    print(allships)

    buttonarray=[]
    # allships={
    #    1:["10","11","12"],
    #    2:["45","46","47","48"],
    #    3:["23","33","43","53","63"]
    # }  
    """
    hitships1=[1,2,3]
    i,j = 1,100
    res= dict()
    for ele in hitships1:
    res[ele] = randint(i,j)
    print(res)

    """
    hitships={
    1:[False,False,False],
    2:[False,False,False,False],
    3:[False,False,False,False,False]
    }

    def checkifhit(x):
        global tries
        #global resultLabel
        tries-=1
        #resultLabel.config(text="")
        hitLabel.config(text="")
        tryLabel.config(text="NUMBER OF TRIES: "+str(tries))
        if tries <= 0:
            #resultLabel.config(text="YOU LOST THE GAME!!!!!")      
            winLabel.config(text="YOU LOST THE GAME :( ")
            playsound("losing audio.mp3")
            for i in buttonarray:
                i.config(state='disabled')
                for i in allships:
                    temp = allships[i]
                    for j in range(len(temp)):
                        for k in range(len(buttonarray)):
                            if buttonarray[k]["text"]==allships[i][j] and buttonarray[k]["bg"] != "red":
                                buttonarray[k].config(bg="green")

        for i in allships:
            temp=allships[i]
            for j in range(len(temp)):
                if x==allships[i][j]:
                    hitships[i][j]=True
                    for k in range(len(buttonarray)):
                        if buttonarray[k]["text"]==x:
                            #resultLabel.config(text="HIT!")
                            playsound("clicked.mp3")
                            hitLabel.config(text="HIT!")
                            buttonarray[k].config(bg="red")
                            break
    # color the missed ones      
        for k in range(len(buttonarray)):
            if buttonarray[k]["text"]==x and buttonarray[k]["bg"] != "red":
                buttonarray[k].config(bg="blue")
                break
        hitandsunk(x)

    def checkwin():
        #global resultLabel
        #resultLabel.config(text="")
        win=True
        for i in hitships:
            for j in range(len(hitships[i])):
                if hitships[i][j] == False:
                    win=False
                    break
        if win==True:
            #resultLabel.config(text="YOU WON THE GAME!!!!!")
            winLabel.config(text="YOU WON THE GAME!!!!!")
            playsound("winning audio.mp3")
    


    def hitandsunk(x):
    #global resultLabel
    #resultLabel.config(text="")
        hitandsunkLabel.config(text="")
        for i in allships:
            numships = len(allships[i])
            numhits = 0
            for j in range(numships):
                if hitships[i][j] == True:
                    numhits+=1
                if numhits == numships:
                    #resultLabel.config(text="HIT AND SUNK #" + str(i) + "\n")
                    hitandsunkLabel.config(text="HIT AND SUNK #" + str(i) + "\n")
        checkwin()
    
    dummyLabel = Label(root, text="                ", bg='gray19')
    dummyLabel.grid(row=0, column=0,rowspan=10)
    Font_tuple = ("Comic Sans MS",20, "bold")
    for rowcol in matches:
        b1=Button(root,text=rowcol,fg="white", bd=3,command=lambda name=rowcol: checkifhit(name),font=Font_tuple)
        b1.grid(row=int(rowcol[0])+1,column=int(rowcol[1])+1)
        buttonarray.append(b1)
    root.mainloop()



homepage1=Button(root1,text="START GAME!",padx=30,font='Bahnschrift',height=3,width=20,bg="lightgreen", command=startgame)
homepage2=Button(root1,text="INSTRUCTIONS",padx=30,font='Bahnschrift',height=3,width=20,command=instructions,bg="lightblue")
homepage3=Button(root1,text="QUIT GAME!!",padx=30,font='Bahnschrift',height=3,width=20,command=quit,bg="red")
#homepage4=Button(root1,text="RESTART GAME",padx=30,font='Bahnschrift',height=3,width=20,command=restartgame,bg="yellow")


homepage1.pack()
homepage2.pack()
homepage3.pack()
#homepage4.pack()
root1.mainloop()
    

