import os
file_pathname=(r'D:\pycharm\work\enhancepic')
filelist=os.listdir(file_pathname)
total_num=len(filelist)
i=0
for item in filelist:
    src=os.path.join(os.path.abspath(file_pathname),item)
    dst=os.path.join(os.path.abspath(file_pathname),str(i)+'.jpg')
    try:
        os.rename(src,dst)
        i+=1
    except:
        continue
print('total%d to rename&converted %d jpgs'%(total_num,i))