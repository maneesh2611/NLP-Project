#Suggest best suitable synset for words which are not already present in any synset to 'suggestions2.txt'
import gensim

def main():
	funi = open('outputs/testunigram2.txt','r')
	fsyn = open('outputs/synset.txt','r')
	out = open('outputs/suggestions2.txt','w')
	model = gensim.models.Word2Vec.load('vecmodel')
	unigram = {}
	synset = {}
	suggest = {}
	cos = {}
	unilines = funi.readlines()
	synlines = fsyn.readlines()
	lensynlines = len(synlines)

	for line in unilines:
		temp = line.split()
		unigram[temp[0]] = int(temp[1])
	for i in range(lensynlines):
		synlines[i] = synlines[i][:-1]
		temp = synlines[i].split(':')
		temp[1] = temp[1].split()
		synset[temp[0]] = temp[1]

	for i in unigram:
		if i in synset:
			#out.write(i + ' Belongs to synset: [' + i + ',' + ','.join(synset[i]) + ']\n') 
			out.write(i + ' : [' + i + ',' + ','.join(synset[i]) + ']\n') 
		else:
			cos[i] = {}
			max_sim = -1.0
			for j in synset:
				ans = 0
				cnt = 0
				fl = 0
				try:
					ans = model.similarity(i,j)
					cnt += 1
				except:
					pass
				for k in synset[j]:
					if i==k:
						fl = 1
						cos[i] = j
					else:
						try:
							ans = model.similarity(i,k)
							cnt += 1
						except:
							pass
				if cnt == 0:
					ans = 0
					cnt = 1
				if fl == 0 and max_sim < float(float(ans)/float(cnt)):
					max_sim = ans
					cos[i] = j
			#out.write(i + ' Should belong to synset: [' + cos[i] + ',' + ','.join(synset[cos[i]]) + ']\n')
			out.write(i + ' ; [' + cos[i] + ',' + ','.join(synset[cos[i]]) + ']\n')
	out.close()

if __name__ == '__main__':
	main()
