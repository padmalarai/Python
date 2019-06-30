try:
    fo=open("sysinfo.csv")  #open("abc.txt")
    data=fo.read()
    print(data)
except IOError:
    print("File not found")
except AttributeError:
    print("Check function")
else:
    fo.close()
    print("File has been closed")





    
