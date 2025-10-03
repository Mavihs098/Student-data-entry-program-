from tkinter import *
import tkinter.messagebox as MessageBox
import pandas as pd
import os


directory = "C:\STUDENT INFO\information"
os.makedirs(directory)
path = "C:\STUDENT INFO\information\info.csv"

with open(path,'w') as g:
    g.write('ADMNISSION NO , STUDENT NAME , FATHER NAME , MOTHER NAME , PHONE NO , ADDRESS\n')
    g.close





def submit():
    entryname = name.get()
    entryfname = fname.get()
    entryadmno = admno.get()
    entrymname = mname.get()
    entryphone = phone.get()
    entryadress = adress.get()


    if(entryadmno=="" or entryname=="" or entryfname=="" or entrymname=='' or entryphone=='' or entryadress=='' ):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        

        l = (f'{entryadmno} , {entryname} , {entryfname} , {entrymname} , {entryphone} , {entryadress}')

        with open(path,'a') as k:
            k.write(f'{l}\n')
            k.close()

            


        entry_admno.delete(0, 'end')
        entry_name.delete(0, 'end')
        entry_fname.delete(0, 'end')
        entry_mname.delete(0, 'end')
        entry_phone.delete(0,'end')
        entry_adress.delete(0,'end')

      
  
        MessageBox.showinfo("insert status", "Inserted Successfully")



def Search():
    searchadmno = search_admno.get()
    

    if( searchadmno ==""):
        MessageBox.showinfo("insert Status","ID Fields is required")
    else:
        dtf = pd.read_csv(path)
        
        mia = dtf.loc[dtf['ADMNISSION NO '] == int(searchadmno)]

      

        k = pd.DataFrame(mia)
        l = k.values
        
        

        output_name2.delete(0,'end')

        output_moteher2.delete(0,'end')

        output_father2.delete(0,'end') 

        output_phone2.delete(0,'end')

        output_address.delete(0,'end')

                
        for row in l:
            stu = row[1]
            fat = row[2]                                       
            mot = row[3]
            pho = row[4]
            add = row[5]

            
           
        output_name2.insert(0,stu)

        output_moteher2.insert(0,mot)

        output_father2.insert(0,fat) 

        output_phone2.insert(0,pho)

        output_address.insert(0,add)

def drp():
    
    deleteadmno = delete_admno.get()
    

    if( deleteadmno ==""):
       MessageBox.showinfo("insert Status","ID Fields is required")
    else:

        dtf = pd.read_csv(path)
        
        kahlifa = dtf[dtf['ADMNISSION NO '] == int(deleteadmno)].index
        
        

        dtf.drop(kahlifa, inplace = True)
        os.remove(path)
        
        dtf.to_csv(path,index = False)
        
        
        
        MessageBox.showinfo("congrats","Done, row has been deleted")


def opn():
    
    os.startfile(path, 'open')    

       



root = Tk()
root.title('==============ALL STUDENTS INFO===============')



root.geometry('900x900')
root .configure(bg = 'light blue')

f = Frame(root, height = 500 , width = 680, bg = 'grey' , borderwidth = 10)
f.place(x = 0 , y = 0)

entry = Label(f, text = 'STUDENTS INFO :- fill'  , pady = 20 , padx = 150 , fg = 'blue', bg = 'grey' , font = 'Helvetica 25 underline bold ').place(x = 20 , y = 5)




admno1 = Label(f ,text = 'ADMISSION NO :-' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 20 , y = 100)
name2 = Label(f , text = 'NAME :-' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 20 , y = 150)
Fname3 = Label(f , text = 'FATHER NAME :-' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 20 , y = 200)
Mname4 = Label(f , text = 'MOTHER NAME :-' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 20 , y = 250)
phone5 = Label(f , text = 'PHONE NO :-' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 20 , y = 300)
adress6 = Label(f ,text = 'ADDRESS :-' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 20 , y = 350)


admno = StringVar()    #####
name = StringVar()  #######
fname = StringVar() ##### 
mname = StringVar() #####  
phone = StringVar()    ####  
adress = StringVar()######
###################

entry_admno = Entry(f ,textvariable = admno , fg = 'blue' ,borderwidth = 2 , bg = 'light blue' , font = 'ariel 15 ' )
entry_admno.place(x = 280 , y = 100)

entry_name = Entry(f ,textvariable = name , fg = 'blue' ,borderwidth = 2 , bg = 'light blue' , font = 'ariel 15 ' )
entry_name.place(x = 280 , y = 150)

entry_fname = Entry(f ,textvariable = fname , fg = 'blue',borderwidth = 2  , bg = 'light blue' , font = 'ariel 15 ' )
entry_fname.place(x = 280 , y = 200)

entry_mname = Entry(f ,textvariable = mname , fg = 'blue' ,borderwidth = 2 , bg = 'light blue' , font = 'ariel 15 ' )
entry_mname.place(x = 280 , y = 250)

entry_phone = Entry(f ,textvariable = phone , fg = 'blue' ,borderwidth = 2 , bg = 'light blue' , font = 'ariel 15 ' )
entry_phone.place(x = 280 , y = 300)

entry_adress = Entry(f ,textvariable = adress , fg = 'blue' ,borderwidth = 2 , bg = 'light blue' , font = 'ariel 15 ' )
entry_adress.place(x = 280 , y = 350)


submit_button = Button(f , text = 'sumbit' , font = ' ariel 20 bold underline' , bg = 'light blue' , padx = 5 , pady = 5 , command = submit ).place(x= 100 , y = 400)


#___________________________________________________________-----------------------------------_________________________________________________________

f2 = Frame(root , bg = 'grey' , height = 500 , width = 680)
f2.place(x = 700 , y = 0)

search = Label(f2 , text = 'STUDENTS INFO :- get' , pady = 20 , padx = 150, fg  = 'blue' , bg = 'grey' , font = 'Helvetica 25 underline bold ').place(x = 5 , y = 5)



admno2 = Label(f2 ,text = 'ADMISSION NO ' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 40 , y = 100 )

search_admno = Entry(f2  , fg = 'blue' , bg = 'light blue' ,borderwidth = 2 , font = 'ariel 15 ' )
search_admno.place(x = 280 , y = 100)

search_button = Button(f2, text = 'search' , font = ' ariel 20 bold underline' , bg = 'light blue' , padx =5 , pady = 5 , command = Search ).place(x= 145 , y = 400)



name2 = Label(f2 ,text = 'NAME ' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 10 , y = 150  )
mother2 = Label(f2 ,text = 'MOTHER NAME ' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 10 , y = 200  )
father2 = Label(f2 ,text = 'FATHER NAME ' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 10 , y = 250 )
phone_no2 = Label(f2 ,text = 'PHONE NO ' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 10 , y = 300  )
address2 = Label(f2 ,text = 'ADDRESS ' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 10 , y = 350  )

output_name2 =  Entry(f2 , fg = 'blue' , bg = 'grey' ,borderwidth = 0 , font = 'ariel 15 ' )
output_name2.place(x = 250 , y = 150)

output_moteher2 = Entry(f2 , fg = 'blue' , bg = 'grey' ,borderwidth = 0 , font = 'ariel 15 ' )
output_moteher2.place(x = 250 , y = 200)

output_father2 = Entry(f2 , fg = 'blue' , bg = 'grey' ,borderwidth = 0 , font = 'ariel 15 ' )
output_father2.place(x = 250 , y = 250)

output_phone2 = Entry(f2 , fg = 'blue' , bg = 'grey' ,borderwidth = 0 , font = 'ariel 15 ' )
output_phone2.place(x = 250 , y =300)

output_address = Entry(f2 , fg = 'blue' , bg = 'grey' ,borderwidth = 0 , font = 'ariel 15 ' )
output_address.place(x = 250 , y =350)

#----------------------------------------------------________________________________________---------------------------------------------------------

f3 = Frame(root , bg = 'grey' , height = 183 , width = 600 )
f3.place(x = 80 , y = 520)

delete = Label(f3 , text = 'STUDENTS INFO :- delete' , pady = 20 , padx = 100, fg  = 'blue' , bg = 'grey' , font = 'Helvetica 25 underline bold ').place(x = 5 , y = 5)
del_admno = Label(f3 ,text = 'ADMISSION NO ' , bg = 'grey', font = 'RocknRoll 20 bold ').place(x = 80 , y = 100 )

delete_admno = Entry(f3  , fg = 'blue' , bg = 'light blue' ,borderwidth = 2 , font = 'ariel 15 ' )
delete_admno.place(x = 80 , y = 140)

delete_button = Button(f3, text = 'delete' , font = ' ariel 20 bold underline' , bg = 'light blue' , padx =5 , pady = 5 , command = drp )
delete_button.place(x= 380 , y = 110)

#-----------------------------------------------------______________________________________________---------------------------------------------------



f4 = Frame(root , bg = 'grey' , height = 183 , width = 600 )
f4.place(x = 700 , y = 520)
op = Label(f4 , text = 'want to open file where these values ' , pady = 15 , padx = 10, fg  = 'blue' , bg = 'grey' , font = 'Helvetica 25 underline bold ').place(x = 5 , y = 5)

ope = Label(f4 , text = 'are stored then ' , pady = 10 , padx = 10, fg  = 'blue' , bg = 'grey' , font = 'Helvetica 25 underline bold ').place(x = 5 , y =65)

opu = Button(f4, text = 'Click' , font = ' ariel 20 bold underline' , bg = 'light blue' , padx =5 , pady = 5 , command =opn )
opu.place(x= 280 , y = 70)



root.mainloop()
#code goes here
