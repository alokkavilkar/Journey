

f = open('sample.txt')
data = f.read() # print all line and pointer will move to end. 
# print(data)
f.close()


f1 = open('sample.txt')
# readline by line data
data = f1.readline()
# print(data)


# writing into the file
f = open('sample.txt', 'w')
f.write("Hello from someone")
# data = f.read()
print(data)


# advanced and must use python file I/O

with open('sample.txt', 'r') as f:
    print(f.read())
