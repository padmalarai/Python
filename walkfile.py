import os

inpatth=r'..\..\koenig\AppData\Local\Programs\Python\Python36-32'
os.chdir(inpatth)
absolute_path=os.getcwd()

for path, listdir, listfile  in os.walk(absolute_path):
    #cur_path=os.getcwd()
    for filename in listfile:
        if filename.endswith(".py"):
            print('{}\{}'.format(path,filename))
        
                            
                              
