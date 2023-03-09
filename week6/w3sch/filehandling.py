# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists  
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
f = open("demofile.txt")
#the same as
f = open("demofile.txt","rt")
#because "r"- read and "t"- text are the default options