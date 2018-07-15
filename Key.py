from random import *
class Key:
    def __init__(self, cube_size = (3,5)):
        #self.value = []
        self.cube_size = cube_size
        self.index = []
        self.info_len = 8 + 16 + 16
        #Files:
        self.key_map = []                                #Can point out a specific location
        self.key_path = []
    def GenKey(self, word_num, word_lenth = 16, roll_round = 5):
        """
        Key Head:
        8_bit word_lenth | word_number | 16_bit roll_round | Key |
        Key Format:
        16_bit Row/Col index | 16_bit Shift times
        """
        key_file = open(self.key_path,'wb')                                    #Can point out a specific location
        #Write format info.
        key_file.write(str(bin(word_lenth)[2:].zfill(8)))
        key_file.write(str(bin(word_num)[2:].zfill(16)))
        key_file.write(str(bin(roll_round)[2:].zfill(16)))
        #Write key map
        for i in range(0, word_num):
            next_key = bin(randint(0,2**16-1))[2:].zfill(16)
            key_file.write(str(next_key))
        key_file.close()
    
    def SetKeyPath(self, path):
        self.key_path = path

    def OpenFile(self):
        self.key_map = open(self.key_path, 'rb')                                               #Can point out a specific location

    def CloseFile(self):
        self.key_map.close()

    def GetKeyInfo(self):
        self.key_map.seek(0)
        word_lenth = self.key_map.read(8)
        word_num = self.key_map.read(16)
        roll_round = self.key_map.read(16)
        return {'wd_lenth': int(word_lenth,2),'wd_num': int(word_num,2), 'rl_round': int(roll_round,2)}
    
    def SetKeyCursor(self,key_index, word_lenth = 16, postive_dir = True):
        #If the direction is normal, it's the index * word_lenth
        #If the direction is reverse, it's the (index + 1) * word_lenth
        if  postive_dir:
            self.key_map.seek(self.info_len + key_index * word_lenth, 0)
        else:
            self.key_map.seek(self.info_len + (key_index+1) * word_lenth, 0)

    def GetEncKey(self, word_lenth = 16):
        """
        Direction: normal
        Operation: key_index * word_lenth
        """
        #key_file.seek(self.info_len + key_index * word_lenth)
        key_value = self.key_map.read(word_lenth)
        if key_value == '':
            self.key_map.seek(self.info_len,0)
            key_value = self.key_map.read(word_lenth)
        print ("ENC KEY", int(key_value,2))
        return int(key_value,2)

    def GetDecKey(self, word_lenth = 16):
        """
        Direction: reverse
        Operation: Start from a specific index, read word before the cursor
        """
        #key_file.seek(self.info_len + (key_index-1) * word_lenth)                           #Need to rethink
        if self.key_map.tell() == self.info_len:
            self.key_map.seek(0,2)
        self.key_map.seek(-word_lenth, 1)
        key_value = self.key_map.read(word_lenth)
        self.key_map.seek(-word_lenth, 1)
        print ("DEC KEY", int(key_value,2))
        return int(key_value,2)
    

