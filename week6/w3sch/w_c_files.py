#changing the file
f= open("C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/demofile.txt", "a")
f.write("\nNow the file has more content!")
f.close()
f= open("C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/demofile.txt", "r")
print(f.read())
f.close()

#comment the code above and try the next:
#rewriting the file
f= open("C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f= open("C:/Users/Аружан/OneDrive/Рабочий стол/pp2/week6/demofile.txt", "r")
print(f.read())
f.close()

#creating file
f = open("myfile.txt", 'w')


