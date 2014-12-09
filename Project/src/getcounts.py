# Takes data corpus and gives vocabulary and counts in 'unigram.txt'
import sys,os,operator

def insert(d,word):
	try:
		d[word] += 1
	except:
		d[word] = 1

def main():
	#inp_file = open('inputs/bigCorpus_root.pos.wx','r')
	inp_file = open(sys.argv[1],'r')
	lines = inp_file.readlines()
	lenlines = len(lines)
	unigram = {}
	
	for i in range(lenlines):
		lines[i] = lines[i][:-1]
		if lines[i] != '':
			temp = lines[i].split()
			for word in temp:
				insert(unigram,word)

	unigramans = sorted(unigram.iteritems(), key=operator.itemgetter(1), reverse=True)
	out = open('outputs/unigram.txt','w')
	for i in unigramans:
		out.write(i[0] + ' ' + str(i[1]) + '\n')
	out.close()

if __name__ == '__main__':
	main()
