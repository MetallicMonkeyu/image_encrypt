from PIL import Image
from Key import *
class Cube:
    #im_path can be pefected by asking user to choose a folder
    def __init__(self, img_path = [], block_size = 8):
        self.image = []   #Open a new file
        self.blc_size = block_size
        self.img_path = img_path
    
    def Row(self, row_index, shift_times):
        """
        All operations in this function are index operation (start from 0)
        """
        #Get operation vector
        """
        block_nums: how many blocks in each row
        blcok_nums = image.width [0] / block.size
        """
        blc_nums = self.image.size[0] / self.blc_size
        opt_vector = shiftBits(shift_times, blc_nums)
        #Copy original image for reference
        ori_image = self.image.copy()
        ori_image.load()
        #Execute row rolling operation
        """
        each Element in vector is the Relative Coordinate of the Block in Original Image
        each Index of Element is the Relative Coordinate of the Block in New Image
        """
        for index, elm in enumerate(opt_vector):
            #Crop a block from original image
            crop_area = (self.blc_size * elm, self.blc_size * row_index, \
                self.blc_size * (elm + 1), self.blc_size * (row_index + 1))
            crop_blc = ori_image.crop(crop_area)
            crop_blc.load()
            #Paste the block to new image
            paste_area = (self.blc_size * index, self.blc_size * row_index,\
                self.blc_size * (index + 1), self.blc_size * (row_index + 1))
            self.image.paste(crop_blc, paste_area)
            
    
    def Col(self, col_index, shift_times):
        """
        All operations in this function are index operation (start from 0)
        """
        #Get operation vector
        """
        block_nums: how many blocks in each colum
        blcok_nums = image.height [1] / block.size
        """
        blc_nums = self.image.size[1] / self.blc_size
        opt_vector = shiftBits(shift_times, blc_nums)
        #Copy original image for reference
        ori_image = self.image.copy()
        ori_image.load()
        #Execute row rolling operation
        """
        each Element in vector is the Relative Coordinate of the Block in Original Image
        each Index of Element is the Relative Coordinate of the Block in New Image
        """
        for index, elm in enumerate(opt_vector):
            #Crop a block from original image
            crop_area = (self.blc_size * col_index, self.blc_size * elm, \
                self.blc_size * (col_index + 1), self.blc_size * (elm + 1))
            crop_blc = ori_image.crop(crop_area)
            crop_blc.load()
            #Paste the block to new image
            paste_area = (self.blc_size * col_index, self.blc_size * index,\
                self.blc_size * (col_index + 1), self.blc_size * (index + 1))
            self.image.paste(crop_blc, paste_area)
    
    def Enc(self, auto = False, key_path = [],wd_num = 20):
        #Plase Choose a file:
        #
        #If auto = True, generate a Key_map Automatically
        key_mgr = Key()
        if auto == True:
            key_mgr.SetKeyPath(self.img_path + '.key')
            key_mgr.GenKey(word_num = wd_num)
        else:
            key_mgr.SetKeyPath(key_path)
        key_mgr.OpenFile()
        #Operation Begin
        opt_info = key_mgr.GetKeyInfo()
        for rl_round in range(0,opt_info['rl_round']):
            for row_index in range(0,self.image.size[0]/self.blc_size):
                shift_times = key_mgr.GetEncKey()
                self.Row(row_index, shift_times)
            for col_index in range(0,self.image.size[1]/self.blc_size):
                shift_times = key_mgr.GetEncKey()
                self.Col(col_index, shift_times)
        #Operation End
        key_mgr.CloseFile()
        self.image.save(fp = self.img_path)

    def Dec(self, key_path):
        #Please choose a key?
        key_mgr = Key()
        key_mgr.SetKeyPath(key_path) 
        key_mgr.OpenFile()#Here should choose the file path
        opt_info = key_mgr.GetKeyInfo()
        #Calculate stop_index:
        used_knum = (self.image.size[0]/self.blc_size + self.image.size[1]/self.blc_size) * opt_info['rl_round']
        stop_index = used_knum % opt_info['wd_num'] 
        #Set Key Cursor:
        key_mgr.SetKeyCursor(key_index = stop_index) 
        for rl_round in range(0,opt_info['rl_round']):
            for col_index in list(reversed(range(0, self.image.size[1]/self.blc_size))):
                shift_times =  - key_mgr.GetDecKey()
                self.Col(col_index, shift_times)
            for row_index in list(reversed(range(0, self.image.size[0]/self.blc_size))):
                shift_times =  - key_mgr.GetDecKey()
                self.Row(row_index, shift_times)
        key_mgr.CloseFile()
        self.image.save(fp = self.img_path)

    def OpenImg(self, path):
        self.image = Image.open(path)
        self.img_path = path
    
    def SetBlockSize(self, size):
        self.blc_size = size
    
    def CloseImg(self):
        self.image.close()
    

def shiftBits(times, block_num):
    #Generate Origin coordinate vector:
    vector = [x for x in range(0,block_num)]
    #Shift Operation:
    times = times % block_num
    for i in range(0,times):
        vector.insert(0,vector[-1])
        del vector[-1]
    print (vector)
    return vector

