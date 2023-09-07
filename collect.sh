find -name \*.md | xargs grep .  > total.txt
git commit -m 'update total' total.txt
git push
