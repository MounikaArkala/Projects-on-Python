import os
def rename_files():
    #r---> refers to raw path
    file_list=os.listdir(r"C:\Users\manishreddy\Desktop\udacity\udacity projects\Secret Message\prank\prank")
    os.chdir(r"C:\Users\manishreddy\Desktop\udacity\udacity projects\Secret Message\prank\prank")
    print(file_list)
    for file_temp in file_list:
        os.rename(file_temp,file_temp.translate(None,"0123456789"))
rename_files()
    
