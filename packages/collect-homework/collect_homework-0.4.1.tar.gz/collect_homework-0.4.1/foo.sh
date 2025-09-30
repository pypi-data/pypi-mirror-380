#!/bin/bash

student="$1"; shift

# echo -
# git -C $student ls-tree -r --name-only HEAD \
#   | sed -e 's|^|./|' -e 's|[^/]*$||' \
#   | sort -u \
#   | wc -l

# echo --


# git -C $student ls-tree -r --full-tree --name-only HEAD \
#   | awk -F/ 'NF>1 {for (i=1;i<NF;i++) {d=""; for (j=1;j<=i;j++) d=d $j "/"; print d}}' \
#   | sort -u \
#   | wc -l

echo --- $student
git -C $student ls-tree -r --name-only HEAD \
  | awk -F/ 'NF>1{ p=$1; print p; for(i=2;i<NF;i++){ p=p"/"$i; print p }}' \
  | sort -u \
  | (cat -; echo .) \
  | wc -l
