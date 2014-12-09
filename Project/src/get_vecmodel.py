# Computes the vector model from data corpus to 'vecmodel'
import gensim,sys,os

class MySentences(object):
	def __init__(self, fname):
		self.fname = fname
	def __iter__(self):
		for line in open(self.fname):
			yield line.split()

#sentences = MySentences('inputs/bigCorpus_root.pos.wx')
sentences = MySentences(sys.argv[1])
model = gensim.models.Word2Vec(sentences,min_count=25,workers=2)
model.save('vecmodel')
model.init_sims(replace=True)
