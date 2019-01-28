function! matlab#InsertFunctionStub()
	let filename = expand("%:t:r")
	exe "normal!ggifunction " . filename
	normal!oend
	normal!gg
endfunction

function! matlab#GenerateTags()
	let tagspath = '.tags'
	let files = systemlist('find **/*\.m')

	let _ = system("rm -f " . tagspath)
	for file in files
		let newline = fnamemodify(file, ':t:r') . '\t' . file . '\t1'
		let _ = system('echo "' . newline . '" >> ' . tagspath)
	endfor

	let _ = SortTags()
endfunction

function! matlab#AppendToTags()
	let tagspath = '.tags'
	let doestagsexists = !empty(glob(tagspath))

	if doestagsexists
		let newline = expand('%:r') . '\t'. expand('%:t') . '\t1'
		let _  = system('echo "' . newline . '" >> ' . tagspath)
	endif

	let _ = SortTags()
endfunction

function! SortTags()
	let tagspath = '.tags'
	let _ = system('sort ' . tagspath . '> tmp && mv tmp ' . tagspath)
endfunction

function! matlab#GotoDefinition()
	let tagspath = '.tags'
	let func = expand("<cword>")
	let tag = system("grep " . func . " " . tagspath)

	if DoesFileContain('function .* ' . func, expand('%'))
		return "[\<C-d>"
	elseif DoesFileContain(func, tagspath)
		return ":tab split\<CR>:exec('tag " . func . "')\<CR>"
	endif

	echom "Function not found"
endfunction

function! DoesFileContain(func, file)
	" let errcode = system('grep "' . a:func . '" ' . a:file . ' 1>/dev/null; echo $?')
	let numinstances = system('grep -c "' . a:func . '" ' . a:file)
	return numinstances > 0
endfunction

let b:searchpath = ['.', '~/Documents/MATLAB/', "$work/programs/readers/"]
function! GetWordsIn(file)
	return system("grep -o '[[:alpha:]][[:alnum:]]*' " . a:file)
endfunction

function! GetFunctionsIn(path)
	let pattern = " -name '*.m' -not -path 'private' -exec basename {} \;"
	return system("find " . a:path . pattern . " | grep -o '^[[:alnum:]]*[^\.]'")
endfunction
