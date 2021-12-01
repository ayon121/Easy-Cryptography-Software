#In this project I am making a chipper code encryption and decrypption
#importing tkinterfor GUI
from tkinter import *
import tkinter
#importing string for code
import string
#importing filedialog
from tkinter import filedialog

#making the display
root_final = Tk()



#create a manu
my_menu = Menu(root_final )
root_final.config(menu= my_menu )
root_final.title("Easy Cryptography GUI Made By Ayon Saha")
root_final.geometry("600x600")
root_final.config (bg= "BLACK")
root_final.resizable(False,False)


'''
=======================================***EASY CRYPTOGRAPHY TEXT START***========================================
'''
#defining text label 1
my_label1 = Label (root_final,text= "  E  " ,font=("Times", "20", "bold italic"),borderwidth=2,relief=GROOVE )
my_label1.place (x= 170 , y= 30 )

#defining text label 2
my_label2 = Label (root_final,text= "  A  " ,font=("Times", "20", "bold italic"),borderwidth=2,relief=GROOVE )
my_label2.place (x= 230 , y= 30 )

#defining text label 3
my_label3 = Label (root_final,text= "  S  " ,font=("Times", "20", "bold italic"),borderwidth=2,relief=GROOVE )
my_label3.place (x= 290 , y= 30 )

#defining text label 4
my_label4 = Label (root_final,text= "  Y  " ,font=("Times", "20", "bold italic"),borderwidth=2,relief=GROOVE )
my_label4.place (x= 350 , y= 30 )

#defining text label 5
my_label5 = Label (root_final,text= "  C  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label5.place (x= 20 , y= 80 )


#defining text label 6
my_label6 = Label (root_final,text= "  R  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 60 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= "  Y  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 100 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= "  P  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 140 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= "  T  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 180 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= "  O  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 220 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= "  G  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 300 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= "  R  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 340 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= "  A  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 380 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= "  P  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 420 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text= " H  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 460 , y= 80)


#defining text label 6
my_label6 = Label (root_final,text=  "  Y  " ,font=("Times", "15", "bold italic"),borderwidth=2,relief=GROOVE )
my_label6.place (x= 500 , y= 80)
'''
=======================================***EASY CRYPTOGRAPHY TEXT END***=========================================
'''

'''
==========================================****From Page Design Start****========================================
'''
def text_animation():
    global canvas1
    canvas1 = tkinter.Canvas(root_final)
    canvas1.place(x= 100 , y= 200)
    canvas_text1 = canvas1.create_text(2,2,text ='',font=("Comic Sans MS", 12, "bold"), anchor = tkinter.NW)
    our_text = '''  Hello!!    Welcome to Easy Crytography.
***********************************************
 In this Software you can do basic Encryption 
                And Decrytion.
***********************************************
     
    Check The Manu Bar For More Options
***********************************************
    This Software is made by Ayon Saha

    '''

    delta = 100
    delay = 0
    for x in range (len(our_text)+1):
        s = our_text[:x]
        new_text = lambda s=s : canvas1.itemconfigure(canvas_text1, text=s )
        canvas1.after(delay,new_text)
        delay += delta

  
text_animation()



    


#in tkiner we use "ëntry" to take input
e = Entry (root_final, width=85,borderwidth = 10 ,bg = "black" , fg= "white")
e.place(x= 20 , y= 130)
current= e.get()
e.delete(0, END)
text1= " +-+-+-+-+-+-+-+-+-+-+-+-+WE WORK FOR YOUR SECURITY+-+-+-+-+-+-+-+-+-+-++-+-+"
e.insert(0,text1)
'''
==========================================****From Page Design End****========================================
'''
    


'''
===============================****Start cipher code****=========================================================
'''

def cipher_code():
    root = Tk()
    root.title("Chipper Code Encryption And Decryption GUI Made By Ayon Saha(EasyCryptography)")
    root.geometry("600x600")
    #background change
    root.config (bg= "BLACK")
    root.resizable(False,False)



    #defining button click for encryption key
    def button_click1():
        global shift
        num= key_button1.get()
        #shifting key selection
        shift = 26 - int(num)
        shift %= 26

    #defining function for encrypt
    def encrypt():
        global shift
        #taking the text
        plain_text = encryption.get(1.0,END)

        #making encryption
        alphabet = string.ascii_lowercase
        shifted = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet , shifted)

        encrypted= plain_text.translate(table)

        #opening filedialouge for saving encrypted file
        open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
        if open_file is None:
            return
        text= str(encrypted)
        open_file.write(text)
        open_file.close()


    #defining text label 1
    my_label1 = Label (root , text= "Paste your text for encryption" ,font= ("Helvetica" , 8) )
    my_label1.place (x= 50 , y= 10)

    #taking text for encryption
    encryption =Text(root , width= "60" , height= "5" , wrap= WORD , borderwidth= 6)
    encryption.place(x= 50 , y= 30)



    #defining text label 2
    my_label2 = Label (root,text= "Select your encryption key:" ,font=("Helveica" , 8) )
    my_label2.place (x= 60 , y= 130)

    #creating button for  encryption Key
    key_button1 = Spinbox(root ,from_= 1,to= 26, font= ("courier" , 10) ,  command= button_click1)
    key_button1.place (x=200 , y= 130)



    #making a button for encryption
    en_button = Button (root ,width= "15" , height= "5" ,text= "Encryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command= encrypt)
    en_button.place (x=400 , y= 130)


    '''
    ====================================================================================================================
    '''
    #defining button click for decryption key
    def button_click2():
        global shift
        num1 = key_button2.get()
        #shifting key selection
        shift = 26 + int(num1)
        shift %= 26


    #defining function for decrypt
    def decrypt():
        global shift
        #taking the text
        plain_text = decryption.get(1.0,END)

        #making decryption
        alphabet = string.ascii_lowercase
        shifted = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet , shifted)

        decrypted= plain_text.translate(table)

        #opening filedialouge for saving decrypted file
        open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
        if open_file is None:
            return
        text= str(decrypted)
        open_file.write(text)
        open_file.close()


    #defining text label 3
    my_label3 = Label (root , text= "Paste your text for decryption" ,font= ("Helvetica" , 8) )
    my_label3.place (x= 50 , y= 280)

    #taking text for decryption
    decryption =Text(root , width= "60" , height= "5" , wrap= WORD , borderwidth= 6)
    decryption.place(x= 50 , y= 300)




    #defining text label 4
    my_label4 = Label (root,text= "Select your decryption key:" ,font=("Helveica" , 8) )
    my_label4.place (x= 60 , y= 400)

    #creating button for  decryption Key
    key_button2 = Spinbox(root ,from_=1,to=26 , font= ("courier" , 10) ,  command=button_click2)
    key_button2.place (x=200 , y= 400)


    #making a button for decryption
    en_button = Button (root ,width= "15" , height= "5" , text= "Decryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command= decrypt)
    en_button.place (x=400 , y= 400)



    #defining text label 5
    my_label5 =Label (root,text= "  Chipper Code Encryption And Decryption  " ,font=("Helveica" , 11),borderwidth=4,relief=GROOVE )
    my_label5.place (x= 150 , y= 520 )
    
    
    
    #it is the mainloop of the proggram
    root.mainloop()
    

    
'''
==============================****End cipher code****=============================================================
'''




'''
=========================================***Start of Hash Encrption***=============================================
'''
def hash():
    
    root1 = Tk()
    root1.title("Hashing GUI made by Ayon Saha(EasyCryptography)")
    root1.geometry("600x600")
    root1.resizable(False,False)





    #background change
    root1.config (bg= "BLACK")



    #This code is for password hashing and recheck if the password is matched or not matched
    #For this I am using "bcrypt" 
    #To install "bcrypt" type "pip install bcrypt" in the terminal
    import bcrypt



    #in tkinter we use "ëntry" to take input
    #e = Entry (root, width=80,borderwidth = 5 ,bg = "black" , fg= "white")
    #e.place(x= 40 , y= 90)


    #taking text for encryption
    encryption =Text(root1 , width= "60" , height= "13" , wrap= WORD , borderwidth= 6)
    encryption.place(x= 50 , y= 80)



    password = encryption.get(1.0,END)
    password = password.encode('ascii')

    
    
    def hashing():
        #Here it will be hashed using bcrypt
        hashed = bcrypt.hashpw(password , bcrypt.gensalt())
        #Here it will print hashed password 
        encrypted= hashed

        #opening filedialouge for saving encrypted file
        open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
        if open_file is None:
            return
        text= str(encrypted)
        open_file.write(text)
        open_file.close()
    
    #defining open file function
    def open_file():
        file= filedialog.askopenfile(mode= "r" , filetypes= [("text files", ".txt")])
        if file is not None:
            content= file.read()
        encryption.insert(INSERT, content)
    
    #defining open file button
    my_button2 = Button (root1, width= "20", height= "2" , bg= "black" , fg= "white" , text= "open file" ,borderwidth=3,relief=RAISED, command= open_file )
    my_button2.place(x=50 , y= 310)

    #making a button for Hashing
    en_button = Button (root1 ,width= "15" , height= "5" ,text= "Hashing" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command= hashing)
    en_button.place (x=400 , y= 310)

    #defining text label 1
    my_label4 = Label (root1,text= "Type Here The Text You Want To Hash " ,font=("Helveica" , 10),borderwidth=2,relief=GROOVE )
    my_label4.place (x= 50 , y= 50 )

    #defining text label 2
    my_label4 = Label (root1,text= "   HASHING   " ,font=("Helveica" , 35),borderwidth=2,relief=GROOVE )
    my_label4.place (x= 160 , y= 450 )

    
    root1.mainloop()
    


'''
=========================================***End of Hash Encrption***=============================================
'''




'''
=========================================***Start of Binary Code Encryption and Decryption***=====================
'''

def binary_code():
    #making the display
    root2 = Tk()
    root2.title("Binary Encryption And Decryption GUI Made by Ayon Saha(EasyCryptography)")
    root2.geometry("600x600")
    root2.resizable(False,False)


    #background change
    root2.config (bg= "BLACK")

    #taking text for encryption
    encryption =Text(root2 , width= "60" , height= "5" , wrap= WORD , borderwidth= 6)
    encryption.place(x= 50 , y= 30)


    def binary_encryption():
        text=  encryption.get(1.0,END)
        total_encrypted_binary = ''
        
        for i in range(len(text)):
            binary = ''
            string_ord = ord(text[i:i+1])
            
            while string_ord > 0:
                x = string_ord % 2
                string_ord = string_ord // 2
                binary = str(x) + str(binary)
            total_encrypted_binary += binary + ''
        e.delete(0, END)
        e.insert(0, total_encrypted_binary)


    def  file_save():
        #opening filedialouge for saving decrypted file
        open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
        if open_file is None:
            return
        text= e.get()
        open_file.write(text)
        open_file.close()


    #defining text label 1
    my_label1 = Label (root2 , text= "Paste Your Text For Encryption" ,font= ("Helvetica" , 8) )
    my_label1.place (x= 50 , y= 10)


    #defining text label 2
    my_label1 = Label (root2 , text= "Here Is Your Encrypted Key" ,font= ("Helvetica" , 8) )
    my_label1.place (x= 50 , y= 170)

    #in tkiner we use "ëntry" to take input
    e = Entry (root2, width=80,borderwidth = 5 ,bg = "black" , fg= "white")
    e.place(x= 50 , y= 190)

    #making a button for encryption
    encryption_button = Button (root2 ,width= "18" , height= "3" ,text= "Encryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command=binary_encryption)
    encryption_button.place (x=400 , y= 130)

    #making a button for saving encrpted file
    save_button = Button (root2,width= "24" , height= "3" ,text= "Save The Encrypted File" , font= ("courier" , 8) ,borderwidth=2,relief=RIDGE,command= file_save)
    save_button.place (x=360 , y= 220)
    '''
    =============================================================================================================================================================================
    '''


    #taking text for encryption
    decryption =Text(root2, width= "60" , height= "5" , wrap= WORD , borderwidth= 6)
    decryption.place(x= 50 , y= 290)

    #in tkiner we use "ëntry" to take input
    e2 = Entry (root2, width=80,borderwidth = 5 ,bg = "black" , fg= "white")
    e2.place(x= 50 , y= 450)

    def binary_decryption():
        def binary_to_text(binary):
            string  = int(binary, 2)
        
            return string
        bin_data= decryption.get(1.0,END)
        str_data = ''

        for i in range(0,len(bin_data),7):
            temp_data = bin_data[i:i+7]
    
            decimal_data = binary_to_text(temp_data)
        
            str_data= str_data + chr(decimal_data)
        
        e2.delete(0, END)
        e2.insert(0, str_data)



    def  file_save2():
        #opening filedialouge for saving decrypted file
        open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
        if open_file is None:
            return
        text= e2.get()
        open_file.write(text)
        open_file.close()

    #defining text label 3
    my_label2 = Label (root2 , text= "Paste Your Code For Decryption" ,font= ("Helvetica" , 8) )
    my_label2.place (x= 50 , y= 270)

    #defining text label 4
    my_label1 = Label (root2 , text= "Here Is Your Decrypted Key" ,font= ("Helvetica" , 8) )
    my_label1.place (x= 50 , y= 430)

    #making a button for decryption
    decryption_button = Button (root2 ,width= "18" , height= "3" ,text= "Decryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command=binary_decryption)
    decryption_button.place (x=400 , y= 390)


    #making a button for saving decrypted file
    save_button = Button (root2,width= "24" , height= "3" ,text= "Save The Decrypted File" , font= ("courier" , 8) ,borderwidth=2,relief=RIDGE,command= file_save2)
    save_button.place (x=360 , y= 480)

    #defining text label 4
    my_label1 = Label (root2 , text= "   Binary  Code   " ,font= ("Helvetica" , 25),borderwidth=2,relief=GROOVE )
    my_label1.place (x= 190 , y= 540)
    
    #it is the mainloop of the proggram
    root2.mainloop()
'''
===========================***End of Binary Code Encryption and Decryption***==========================================
'''
def image_encrytion_decryption():
    #making the display
    root3 = Tk()
    root3.title("Image Encryption And Decryption GUI made by Ayon Saha(EasyCryptography)")
    root3.geometry("600x600")

    #background change
    root3.config (bg= "BLACK")
    root3.resizable(False,False)


    def open_file_for_encryption():
        e.delete(0, END)
        file1 = filedialog.askopenfile(mode= 'r' , filetypes= [('jpg file' , '*.jpg'),('png file' , '*.png')])
        #if file variable is empty or not
        if file1 is not None:
            #print(file1)
            global file_name
            file_name = file1.name
            #showing the file name on the screen 
            e.insert(0,"This file : (( " + file_name + " )) is selected for encryption" )
            

            

    def encrypt_decrypt(num):
            if num == 1:     
                key = encryption.get(1.0,END)
                #print(file_name ,key)
                fi = open(file_name , 'rb')
                image = fi.read()
                fi.close()
                image = bytearray(image)
                for index,values in enumerate(image):
                    image[index] = values^int(key)
                fi1 = open(file_name, 'wb')
                fi1.write(image)
                fi1.close()
            
            
            
                e.delete(0, END)
                e.insert(0,"This File : (( " + file_name + " )) Is Encrypted" )
                encryption.delete(1.0,END)
                
            else:
                key = decryption.get(1.0,END)
                #print(file_name ,key)
                fi = open(file_name , 'rb')
                image = fi.read()
                fi.close()
                image = bytearray(image)
                for index,values in enumerate(image):
                    image[index] = values^int(key)
                fi1 = open(file_name, 'wb')
                fi1.write(image)
                fi1.close()
                e1.delete(0, END)
                e1.insert(0,"This File : (( " + file_name + " )) Is Decrypted" )
                decryption.delete(1.0,END)
            
            

    #making a button for open image file
    open_button = Button (root3 ,width= "24" , height= "3" ,text= "Open Image File" , font= ("courier" , 8) ,borderwidth=2,relief=RIDGE,command= open_file_for_encryption )
    open_button.place (x=50 , y= 30)         


    #in tkiner we use "ëntry" to take input
    e = Entry (root3, width=80,borderwidth = 5 ,bg = "black" , fg= "white")
    e.place(x= 50 , y= 90)

    #defining text label 1
    my_label1 = Label (root3, text= "Type Here Your Key For Encrption(Must Be Integer)" ,font= ("Helvetica" , 8) )
    my_label1.place (x= 50 , y= 130)

    #taking number key for encryption
    encryption =Text(root3 , width= "60" , height= "2" , wrap= WORD , borderwidth= 6)
    encryption.place(x= 50 , y= 150)


    #making a button for Decryption
    en_button = Button (root3 ,width= "15" , height= "3" ,text= "Encryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command= lambda: encrypt_decrypt(1))
    en_button.place (x=430 , y= 200)

    #defining text label 2
    my_label2 = Label (root3 , text= "  Image Encrytion Decryption    " ,font= ("Helvetica" , 25),borderwidth=2,relief=GROOVE )
    my_label2.place (x= 80 , y= 540)
    '''
    ======================================================================================================================================================
    '''


    def open_file_for_decryption():
        e1.delete(0, END)
        file1 = filedialog.askopenfile(mode= 'r' , filetypes= [('jpg file' , '*.jpg'),('png file' , '*.png')])
        #if file variable is empty or not
        if file1 is not None:
            #print(file1)
            global file_name
            file_name = file1.name
            #showing the file name on the screen 
            e1.insert(0,"This file : (( " + file_name + " )) is selected for decryption" )


    #making a button for open image file
    open_button = Button (root3 ,width= "24" , height= "3" ,text= "Open Image File" , font= ("courier" , 8) ,borderwidth=2,relief=RIDGE,command= open_file_for_decryption)
    open_button.place (x=50 , y= 300)  

    #in tkiner we use "ëntry" to take input
    e1 = Entry (root3, width=80,borderwidth = 5 ,bg = "black" , fg= "white")
    e1.place(x= 50 , y= 360)

    #defining text label 2
    my_label2 = Label (root3 , text= "Type Here Your Key For Decrption(Must Be Integer)" ,font= ("Helvetica" , 8) )
    my_label2.place (x= 50 , y= 400)

    #taking text for Decryption
    decryption =Text(root3 , width= "60" , height= "1" , wrap= WORD , borderwidth= 6)
    decryption.place(x= 50 , y= 420)



    #making a button for Decryption
    de_button = Button (root3 ,width= "15" , height= "3" ,text= "Decryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command= lambda: encrypt_decrypt(2))
    de_button.place (x=430 , y= 450)





    #this is the main loop
    root3.mainloop()



'''
============================*** Image Encryption And Decrytion Start***==================================================
'''

'''
=========================================***ASCII ENCRYPTION START***====================================================
'''
def ascii_encryption():
     #making the display
    root4 = Tk()
    root4.title("ASCII code encryption GUI made by Ayon Saha(EasyCryptography)")
    root4.geometry("600x600")

    #background change
    root4.config (bg= "BLACK")
    root4.resizable(False,False)


    #defining encrypt function
    def encrypt():
        plain_text = encryption.get(1.0,END)
        for c in plain_text:
            encrypted=(ord(c))
            current= e.get()
            e.delete(0, END)
            e.insert(0, str(current) + str(encrypted) + ",")


    def  file_save():
        #opening filedialouge for saving decrypted file
        open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
        if open_file is None:
            return
        text= e.get()
        open_file.write(text)
        open_file.close()

    #creating clear button
    def delete():
        e.delete(0,END)

    #defining text label 1
    my_label1 = Label (root4 , text= "Here Is Your Encrypted ASCII Code" ,font= ("Helvetica" , 8) )
    my_label1.place (x= 50 , y= 280)       

    #in tkiner we use "ëntry" to take input
    e = Entry (root4, width=80,borderwidth = 7 ,bg = "black" , fg= "white")
    e.place(x= 50 , y= 300)


    #defining text label 1
    my_label2 = Label (root4 , text= "Paste Your Text For Encryption" ,font= ("Helvetica" , 8) )
    my_label2.place (x= 50 , y= 10)


    #taking text for encryption
    encryption =Text(root4 , width= "60" , height= "5" , wrap= WORD , borderwidth= 6)
    encryption.place(x= 50 , y= 30)


    #making a button for encryption
    en_button = Button (root4 ,width= "15" , height= "5" ,text= "Encryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command= encrypt)
    en_button.place (x=400 , y= 130)

    #making a button for saving encrpted file
    save_button = Button (root4 ,width= "24" , height= "3" ,text= "Save The Encrypted File" , font= ("courier" , 8) ,borderwidth=2,relief=RIDGE,command= file_save)
    save_button.place (x=360 , y= 340)

    #making a button for clearing encrpted file
    clear_button = Button (root4 ,width= "15" , height= "3" ,text= "  Clear " , font= ("courier" , 8) ,borderwidth=2,relief=RIDGE,command= delete)
    clear_button.place (x=50 , y= 340)

    #defining text label 5
    my_label5 =Label (root4,text= "  ASCII Code Encryption  " ,font=("Helveica" , 16),borderwidth=4,relief=GROOVE )
    my_label5.place (x= 152 , y= 520 )

    root4.mainloop()



'''
=========================================***ASCII ENCRYPTION END***====================================================
'''  








'''
=========================================***MANU OPTIONS***======================================================
'''
#creaing manu options
options_menu = Menu (my_menu , tearoff= False , bg="lightcyan")
my_menu.add_cascade(label="MENU" , menu= options_menu )
options_menu.add_cascade(label = "# Cipher Code" , command =cipher_code )
options_menu.add_cascade(label = "# Hash Generetor" , command =hash)
options_menu.add_cascade(label = "# Binary Code" , command = binary_code)
options_menu.add_cascade(label = "# ASCII Encryption" , command = ascii_encryption)
options_menu.add_cascade(label = "# Image Encryption And Decryption" , command = image_encrytion_decryption)


'''
==========================================****************======================================================
'''


#it is the mainloop of the proggram
root_final.mainloop()


