groups = ['Red Hot Chili Peppers', 'Green Day', 'The White Stripes', 'Black Sabbath', 'Pink Floyd', 'Deep Purple']
with open('rock.txt', "w") as myfile:
        for c in groups:
                myfile.write("%s\n" % c)

content = open('rock.txt')
print(content.read())