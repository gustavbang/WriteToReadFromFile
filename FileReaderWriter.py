file = open("demofile.txt", "a")
file.write("Now the file has one more line\n")


fileReader = open("demofile.txt", "r")
print(fileReader.read())