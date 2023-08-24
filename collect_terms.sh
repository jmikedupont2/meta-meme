  528  cd meta-meme/
  526  git log --all > patch.txt
  528  cd meta-meme.wiki/
  529  git log --all > patch.txt
  533  cp ../meta-meme.wiki/patch.txt wiki-patch.txt
  538  cat wiki-patch.txt patch.txt >total.txt
  545  grep -P  -o -e '([a-zA-Z0-9]+)' total.txt  |sort |uniq -c | sort -n >tokens.txt
