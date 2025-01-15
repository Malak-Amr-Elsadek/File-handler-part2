file = open('Codingal.txt','r')
count=0

content=file.read()
list=content.split("\n")
for line in list:
    if line:
        count=count+1
print("Toltal line count:",count)