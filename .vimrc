set number "turn on line number"
set numberwidth=2   "set the line numbers to 2 spaces"
set tabstop=2	"set 2 spaces for tab"

set shiftwidth=2 "set 2 space for insert indentation"

set lcs=eol:¬,tab:\ \  "set character ¬ in the end of line"
set list "turn on the character"
execute pathogen#infect()

let name = "Benegripe" "set name in to the name variable"


function! NoNum() "turn off the set number"
	set nonumber
	set nolist
endfunc

function! Num() "turn on the set number"
	set number
	set list
endfunc

function Why() "motivation phrases "
	echo "Why do you code Benegripe \?" 
endfunc

map <c-1> : call Why()<cr>
map <c-n> : call NoNum()<cr>
map <c-m> : call Num()<cr>
