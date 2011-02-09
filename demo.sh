#! /bin/bash
# Russ Ferriday
# 2011-02-06
echo 'operating on patterns'
grep "[0-9]*\-[0-9]*\-[0-9]*" census-spaced

echo ""
echo 'alternative syntax - note the additional [] as part of the predefined class symbols'
grep "[[:digit:]]*\-[[:digit:]]*\-[[:digit:]]*" census-spaced


echo ""
echo 'Bracket expressions ...'
grep b[aeiou]g basicregex


echo ""
echo 'Range expressions ...'
grep a[2-4]z basicregex

echo ""
echo 'Single character ...'
grep a.z basicregex

echo ""
echo 'Start and end of line ...'
grep '^water' basicregex
grep 'water$' basicregex

echo ""
echo 'repetition...'
echo 'zero "a"s...'
grep bd basicregex 

echo ""
echo 'zero or more "a"s...'
grep ba*d basicregex 

echo ""
echo 'at least one "a"...'
grep -E 'ba+d' basicregex

echo ""
echo 'zero or one "a"...'
grep -E 'ba?d' basicregex

echo ""
echo "Abe... "
grep A.*Lincoln basicregex

