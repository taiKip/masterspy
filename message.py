
infile = open('message.txt','r')


for line in infile:
    word_list = line.split()
    print(word_list)

infile.close()