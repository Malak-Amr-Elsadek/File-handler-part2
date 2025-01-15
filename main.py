file = open('Codingal.txt')
print(file.read())
file.close()


file_w = open('Codingal.txt','w')
file_w.write("I love Miss Jemima!!!")
file.close()

file_a=open('Codingal.txt','a')
file_w.write("Codingal Penguin")
file.close()