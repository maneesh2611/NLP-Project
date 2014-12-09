#Suggest synsets for words which do not have synsets in wordnet to 'suggestions.txt'
import gensim

def main():
	funi = open('outputs/testunigram.txt','r')
	fsyn = open('outputs/synset.txt','r')
	out = open('outputs/suggestions.txt','w')
	model = gensim.models.Word2Vec.load('vecmodel')
	unigram = {}
	synset = {}
	suggest = {}
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
			#out.write(i + ' Present in wordnet already with synset: [' + ','.join(synset[i]) + ']\n')
			out.write(i + ' : [' + ','.join(synset[i]) + ']\n')
		else:
			temp = model.most_similar(positive = [i], topn = 20)
			suggest[i] = []
			for j in temp:
				suggest[i].append(j[0])
			#out.write(i + ' Suggested synset: [' + ','.join(suggest[i]) + ']\n')
			out.write(i + ' ; [' + ','.join(suggest[i]) + ']\n')
	out.close()

if __name__ == '__main__':
	main()
