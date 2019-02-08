

for folder in 2017/11/01/*/; do
	for filename in $folder*.bz2; do 
		bunzip2 $filename -d
		echo $filename
	done
done
