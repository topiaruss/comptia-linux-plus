#! /bin/bash
echo 'operating on patterns'
grep "[0-9]*\-[0-9]*\-[0-9]*" census-spaced
echo 
echo 'alternative syntax'
grep "[[:digit:]]*\-[[:digit:]]*\-[[:digit:]]*" census-spaced
