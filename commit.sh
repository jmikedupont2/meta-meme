#the commit loop

while [ 1 ]
do
      git commit -m 'step' -a
      git push origin
      sleep 10
done
