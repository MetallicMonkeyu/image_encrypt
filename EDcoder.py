from tkinter import *
from tkFileDialog import *
from Cube import *

class EDFrame:
    def __init__(self):
        self.root = tk()
        self.cube = Cube()
    
    def DrawMainMenu(self):
        auto_button = Button(self.root, text = 'Auto Encode')
        def ClickAuto(event):
            print ("You are clicking the 'Auto Button'")
            self.AutoEncode()
        auto_button.bind('<ButtonRelease-1>',ClickAuto)
        auto_button.pack()
        
        
        enc_button = Button(self.root, text = 'Manual Encode')
        def ClickEnc(event):
            print ("You are clicking the 'Enc Button'")
            self.Encode()
        enc_button.bind('<ButtonRelease-1>',ClickEnc)
        enc_button.pack()

        dec_button = Button(self.root, text = 'Decode')
        def ClickDec(event):
            print ("You are clicking the 'Dec Button'")
            self.Decode()
        dec_button.bind('<ButtonRelease-1>',ClickDec)
        dec_button.pack()
    
    def DrawEncMenu(self):
        img_frame = Frame(self.root, height = 160, width = 120)
        img_frame.pack()
        
        img_button = Button(self.root, text = 'Choose Image')
        def ClickImage(event):
            print ("You are clicking the 'Img Button'")
        img_button.bind('<ButtonRelease-1>',ClickImage)
        img_button.pack()

        key_button = Button(self.root, text = 'Choose KeyFile' )
        def ClickKey(event):
            print ("You are clicking the 'Key Button'")
        key_button.bind('<ButtonRelease-1>',ClickKey)
        key_button.pack()
    
    def DrawDecMenu(self):
        img_frame = Frame(self.root, height = 160, width = 120)
        img_frame.pack()
        
        img_button = Button(self.root, text = 'Choose Image')
        def ClickImage(event):
            print "You are clicking the 'Img Button'"
        img_button.bind('<ButtonRelease-1>',ClickImage)
        img_button.pack()

        key_button = Button(self.root, text = 'Choose KeyFile' )
        def ClickKey(event):
            print ("You are clicking the 'Key Button'")
        key_button.bind('<ButtonRelease-1>',ClickKey)
        key_button.pack()

    def AutoEncode(self):
        img_path = askopenfilename(filetypes=[("Image files",".jpg")])
        self.cube.OpenImg(img_path)
        #------------------------#
        self.cube.Enc(auto = True)
        #------------------------#
        self.cube.CloseImg()
    
    def Encode(self):
        img_path = askopenfilename(filetypes=[("Image files",".jpg")])
        self.cube.OpenImg(img_path)
        #------------------------#
        key_path = askopenfilename(filetypes=[("Key files",".key")])
        self.cube.Enc(key_path = key_path)
        #------------------------#
        self.cube.CloseImg()


    def Decode(self):
        #Open Image File
        img_path = askopenfilename(filetypes=[("Image files",".jpg")])
        self.cube.OpenImg(img_path)
        #------------------------#
        key_path = askopenfilename(filetypes=[("Key files",".key")])
        self.cube.Dec(key_path) 
        #------------------------#
        self.cube.CloseImg()
        
    
    
    
    

mine = EDFrame()
mine.DrawMainMenu()
#mine.DrawDecMenu()
mine.root.mainloop()
