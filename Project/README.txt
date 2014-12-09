NLP Project: An experiment on WordNet Enhancement
Name:TSV Maneesh(201201183) & B.Chaitanya(201101163)


1- Requirements:
----------------
 Operating System               :       LINUX (tested on >= Fedora-19 , >= Ubuntu 10.04)

 Compiler/Interpreter/Librarie(s):      g++ / Perl / Java / Python

2- Directory Structure:
-----------------------
201201183
├── code
│   ├── bin
│   │   ├── compile.sh
│   │   ├── english.sh
│   │   ├── English_Test_Parse.txt
│   │   ├── hindi.sh
│   │   ├── Hindi_Test_Parse.txt
│   │   └── installib.sh
│   ├── lib
│   └── src
│       ├── assignment6.py
│       ├── engtrain.txt
│       ├── hintrain.txt
│       └── test.txt
├── README.txt
├── Report
│   └── report.pdf
└── Results
    ├── hindi.out
    └── telugu.out



6 directories, 14 files
                      
(FOLLOW THIS DIRECTORY STRUCTURE ONLY, recreate your own tree at last)


3 - About the files
--------------------
	> getcounts.py - gets the vocabulary and unigram counts from the training corpus - gives output to unigram.txt in outputs folder.
	> parse_wordnet.py - gets the synsets from the wordnet database file - gives output to synset.txt in outputs folder.
	> get_vemodel.py - prepares a Word2Vec model for the training corpus - gives output to vecmodel in outputs folder.
	> neededuni.py - gets required unigrams with frequency in some range (ex : 100,000 - 43) for which we suggest synsets and suggest additions for synsets.
		Outputs - i)testunigrams.txt in outputs folder for first task
			  ii)testunigrams2.txt in outputs folder for second task
	> word_synset.py and give_synset_to_word.py - Gives the necessary suggestions to suggestions.txt in outputs/final folder.
	> suggest_synset.py and suggest_word_to_synset.py - Gives the necessary suggestions to suggestions2.txt in outputs/final folder.
	> init.sh - Runs getcounts.py,parse_wordnet.py,get_vecmodel.py,neededuni.py. For necessary initializations.
	> synsettoword.sh - Runs word_synset.py and give_synset_to_word.py and suggests synsets for words present in testunigram.txt which do not already have a synset in the wordnet database.
	> wordtosynset.sh - Runs suggest_synset.py and suggest_word_to_synset.py to suggest the best suitable synset to a word present in testunigram2.txt which are not present in any synset.

4 - How to run
---------------
	---> To run this project, gensim library must be installed on the machine
	> ./init.sh training_corpus_name wordnet_database_name
	> ./synsettoword.sh
		---> For first task
	> ./wordtosynset.sh
		----> For second task
