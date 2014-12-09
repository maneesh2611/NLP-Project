NLP Project: An experiment on WordNet Enhancement
Name:TSV Maneesh(201201183) & B.Chaitanya(201101163)


1- Requirements:
----------------
 Operating System               :       LINUX (tested on >= Fedora-19 , >= Ubuntu 10.04)

 Compiler/Interpreter/Librarie(s):      g++ / Perl / Java / Python

2- Directory Structure:
-----------------------
Project
├── lib
│   └── convertor-indic-1.4.9
│       ├── ChangeLog
│       ├── convertor.pl
│       ├── data_txt
│       ├── doc
│       ├── Kannada_WX
│       │   └── Kannada_WX.txt
│       ├── lib
│       │   └── IndicCC.pl
│       ├── README
│       ├── runWrapper.sh
│       ├── ssfapi
│       │   ├── feature_filter.pl
│       │   └── shakti_tree_api.pl
│       ├── tests
│       │   ├── afsar-utf-hin.txt
│       │   ├── case-caret_at-wx2utf-tel.out
│       │   ├── case-caret_at-wx.in
│       │   ├── error-case-wx2utf-tel-utf.txt
│       │   ├── error-case-wx.txt
│       │   ├── extra-inputs
│       │   │   ├── issue.txt
│       │   │   ├── utf.txt
│       │   │   ├── varna-mala-hin.txt
│       │   │   └── wx.txt
│       │   ├── hin
│       │   │   ├── issues-hin-utf.txt
│       │   │   ├── ssf
│       │   │   │   ├── all_input_merged.in
│       │   │   │   ├── all_input_merged_out_1
│       │   │   │   ├── all_input_merged_out.in
│       │   │   │   ├── Error_analysis_chunker
│       │   │   │   ├── sample_hin_utf.in
│       │   │   │   ├── sample_hin_utf.out
│       │   │   │   ├── sample_hin_wx.in
│       │   │   │   ├── sample_hin_wx.out
│       │   │   │   ├── test_case_1_utf.in
│       │   │   │   ├── test_case_1_utf.out
│       │   │   │   ├── test_case_1_wx.in
│       │   │   │   ├── test_case_1_wx.out
│       │   │   │   ├── test_case_2_utf.in
│       │   │   │   ├── test_case_2_utf.out
│       │   │   │   ├── test_case_2_wx.in
│       │   │   │   ├── test_case_2_wx.out
│       │   │   │   ├── test_case_3_utf.in
│       │   │   │   ├── test_case_3_utf.out
│       │   │   │   ├── test_case_3_wx.in
│       │   │   │   ├── test_case_3_wx.out
│       │   │   │   ├── test_case_4_utf.in
│       │   │   │   ├── test_case_4_utf.out
│       │   │   │   ├── test_case_4_wx.in
│       │   │   │   ├── test_case_4_wx.out
│       │   │   │   ├── test_case_single_file_wx.in
│       │   │   │   ├── test_case_single_file_wx.out
│       │   │   │   ├── test-ssf-wx.in
│       │   │   │   └── test-ssf-wx.out
│       │   │   ├── test_cases_utf.in
│       │   │   ├── test_cases_wx.in
│       │   │   └── text
│       │   │       ├── all_input_merged_out_1
│       │   │       ├── Error_analysis_chunker
│       │   │       ├── sample_story_utf.in
│       │   │       ├── sample_story_utf.out
│       │   │       ├── sample_story_wx.in
│       │   │       ├── sample_story_wx.out
│       │   │       ├── sentences_hin_100_utf.in
│       │   │       ├── sentences_hin_100_utf.out
│       │   │       ├── sentences_hin_100_wx.in
│       │   │       ├── sentences_hin_100_wx.out
│       │   │       ├── uniq-words-hin-820-utf.in
│       │   │       ├── uniq-words-hin-820-utf.out
│       │   │       ├── uniq-words-hin-820-wx.in
│       │   │       └── uniq-words-hin-820-wx.out
│       │   ├── issue-convertor-iiit-wx2utf-tel.txt
│       │   ├── pan
│       │   │   ├── sentences-pan-200-utf2wx-expert.txt
│       │   │   ├── sentences-pan-200-utf2wx-expert.txt~
│       │   │   ├── sentences-pan-200-utf2wx-iiit.txt
│       │   │   ├── sentences-pan-200-utf2wx-iiit.txt~
│       │   │   ├── sentences-pan-200-utf.txt
│       │   │   ├── test-1-utf.txt
│       │   │   ├── uniq-words-pan-1000-utf-iiit.txt
│       │   │   ├── uniq-words-pan-1000-wx-expert.txt
│       │   │   └── uniq-words-pan-1000-wx-iiit.txt
│       │   ├── sampale-cases-tel-utf.txt
│       │   ├── sampale-cases-tel-wx.txt
│       │   ├── tam
│       │   │   ├── old
│       │   │   │   ├── error-wx2utf-tam.txt
│       │   │   │   ├── sentences-tamil-words-uniq-wx.in
│       │   │   │   ├── uniq-words-tam-aukbc-utf.txt
│       │   │   │   ├── uniq-words-tam-aukbc-wx.txt
│       │   │   │   ├── uniq-words-tam-expert-utf.out
│       │   │   │   └── uniq-words-tam-expert-wx.out
│       │   │   ├── ssf
│       │   │   ├── test_case_1-wx.in
│       │   │   ├── test_cases-utf.in
│       │   │   ├── test_cases-wx.in
│       │   │   └── text
│       │   ├── tel
│       │   │   ├── ssf
│       │   │   │   ├── test_case_1_utf.in
│       │   │   │   ├── test_case_1_utf.out
│       │   │   │   ├── test_case_1_wx.in
│       │   │   │   ├── test_case_1_wx.out
│       │   │   │   ├── test_case_2_utf.in
│       │   │   │   ├── test_case_2_utf.out
│       │   │   │   ├── test_case_2_wx.in
│       │   │   │   ├── test_case_2_wx.out
│       │   │   │   ├── test_case_3_utf.in
│       │   │   │   ├── test_case_3_utf.out
│       │   │   │   ├── test_case_3_wx.in
│       │   │   │   ├── test_case_3_wx.out
│       │   │   │   ├── test_case_4_utf.in
│       │   │   │   ├── test_case_4_utf.out
│       │   │   │   ├── test_case_4_wx.in
│       │   │   │   ├── test_case_4_wx.out
│       │   │   │   ├── test_case_5_wx.in
│       │   │   │   └── test_case_5_wx.out
│       │   │   ├── test_cases_utf.in
│       │   │   ├── test_cases_wx.in
│       │   │   └── text
│       │   │       ├── telugu_utf.txt
│       │   │       ├── words-uniq-1600-tel-utf.in
│       │   │       └── words-uniq-1600-tel-utf.out
│       │   ├── transfergrammar.tmp
│       │   └── utf2wx.tmp.in2
│       ├── tmp1
│       ├── utf2wx_run.sh
│       └── wx2utf_run.sh
├── README.txt
├── report
│   ├── NLP PROJECT.docx
│   └── NLP PROJECT.pdf
└── src
    ├── getcounts.py
    ├── get_vecmodel.py
    ├── give_synset_to_word.py
    ├── init.sh
    ├── inputs
    │   ├── bigCorpus_root.pos.wx
    │   └── wordnet_data_wx.txt
    ├── neededuni.py
    ├── outputs
    │   ├── final
    │   │   ├── suggestions2.txt
    │   │   └── suggestions.txt
    │   ├── suggestions2.txt
    │   ├── suggestions.txt
    │   ├── synset.txt
    │   ├── testunigram2.txt
    │   ├── testunigram.txt
    │   ├── unigram.txt
    │   ├── wx_suggestions2.txt
    │   └── wx_suggestions.txt
    ├── parse_wordnet.py
    ├── suggest_word_to_synset.py
    ├── synset_suggest.py
    ├── synsettoword.sh
    ├── vecmodel
    ├── word_synset.py
    └── wordtosynset.sh

24 directories, 139 files


3 - About the files
--------------------
	> getcounts.py - gets the vocabulary and unigram counts from the training corpus - gives output to unigram.txt in outputs folder.
	> parse_wordnet.py - gets the synsets from the wordnet database file - gives output to synset.txt in outputs folder.
	> get_vecmodel.py - prepares a Word2Vec model for the training corpus - gives output to vecmodel in outputs folder.
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
