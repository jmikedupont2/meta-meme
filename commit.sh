#the commit loop

while [ 1 ]
do
      git commit -m 'step' -a
#      git push origin
      git push --set-upstream origin docs
      sleep 10
done
