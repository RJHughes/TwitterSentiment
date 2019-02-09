 
for day in 2017/11/*/; do
	for folder in $day/*/; do
		for filename in $folder*.bz2; do 
			bunzip2 $filename -d
			echo $filename
		done
	done
done


