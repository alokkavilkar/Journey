
file="states"

for state in `cat $file`
do
	echo $state
done


file="state2"
IFS=:
while FS= read -r line
do
	echo $line
done < $file
