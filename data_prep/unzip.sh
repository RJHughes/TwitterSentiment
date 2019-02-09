

for d in */ ; do
for i in {10..17}; do
	tar xvf twitter-stream-2017-11-$i.tar
	rm  twitter-stream-2017-11-$i.tar
done
done
