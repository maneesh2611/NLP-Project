## Usage ./runWrapper.sh <inputFolder>

if [ -e $1/wx]
then
echo "Output in $1/wx"
else
mkdir $1/wx
echo "Creating $1/wx"
fi

for file in $1/*.Hindi
do
#echo $file
name=`basename $file`
echo $name
perl -C convertor.pl -f=text -l=hin -s=utf -t=wx -i=$file > $1/wx/$name
#sed 's/. $/./g' $file > temp.txt
#sed 's/ \. /./g' temp.txt > $1/1/$name
#sed 's/\\[^ ]\+\( \|$\)/ /g' $file > $1/english_replace/$name
#python cut_pos.py $file $1/train_pos/$name
#java -mx1G -classpath stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -model models/english-bidirectional-distsim.tagger -textFile $file > $1/pos_tagged/$name
done
