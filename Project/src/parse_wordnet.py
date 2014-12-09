#Takes wordnet data and gives the synsets to 'synset.txt'
import sys

def main():
	#inp_file = open('inputs/wordnet_data_wx.txt')
	inp_file = open(sys.argv[1],'r')
	lines = inp_file.readlines()
	lenlines = len(lines)
	synset = {}

	for i in range(lenlines):
		lines[i] = lines[i][:-1]
		if lines[i] != '':
			temp = lines[i].split()[3]
			temp = temp.split(':')
			synset[temp[0]] = temp[1:]
	
	out = open('outputs/synset.txt','w')
	for i in synset:
		if i == '':
			out.write('om' + ':')
		else:
			out.write(i + ':')
		for j in synset[i]:
			out.write(j + ' ')
		out.write('\n')
	out.close()

if __name__ == '__main__':
	main()
