# Takes unigrams and gives the unigrams with reasonably high probability into 'testunigram.txt'
funi = open('outputs/unigram.txt','r')
out = open('outputs/testunigram.txt','w')
out2 = open('outputs/testunigram2.txt','w')
lines = funi.readlines()
for line in lines:
	freq = int(line.split()[1])
	if freq >= 43 and freq <= 100000:
		out.write(line)
	if freq >= 1000 and freq <= 100000:
		out2.write(line)
out.close()
out2.close()
