fsug = open('outputs/wx_suggestions.txt','r')
out = open('outputs/final/suggestions.txt','w')
lines = fsug.readlines()

for line in lines:
	temp = line.split()
	if temp[1] == ':':
		out.write(temp[0] + ' Already present in wordnet with synset: ' + temp[2] + '\n')
	elif temp[1] == ';':
		out.write(temp[0] + ' Suggested synset: ' + temp[2] + '\n')
out.close()
