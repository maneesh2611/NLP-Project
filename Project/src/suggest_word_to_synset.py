fsug = open('outputs/wx_suggestions2.txt','r')
out = open('outputs/final/suggestions2.txt','w')
lines = fsug.readlines()

for line in lines:
	temp = line.split()
	if temp[1] == ':':
		out.write(temp[0] + ' Belongs to synset: ' + temp[2] + '\n')
	elif temp[1] == ';':
		out.write(temp[0] + ' Should belong to synset: ' + temp[2] + '\n')
out.close()
