f=str(input("Enter a file name with extention: "))
ext=f.split(".")
print ("The extention of the file name is : "+ repr(ext[-1]))
 #-1 to acess the last element of the list
#repr() is a function that returns a string containing a printable represntation of an object
