
for f in flat/*.txt
do

echo  `sed -n '/^File/p' $f | awk '{print $3}'` `sed -n '/^Total/p' $f | awk '{print $4}'` >> amount_list

done