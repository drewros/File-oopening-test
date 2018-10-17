file = open("myfile.txt", "a")
file. write("Hello World!")
file.close()

try:
    file = open("myfile.txt", "r")
    contents = file.read()
    file.close()
    print (contents)
except:
    print ("This file does not exist. Creating now...")
    file = open("myfile.text", "w")
    file.close()
