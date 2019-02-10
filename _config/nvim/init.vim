set nocompatible

" Vundle setup
filetype off

set rtp+=~/.config/nvim/bundle/Vundle.vim
call vundle#begin('~/.config/nvim/bundle')
Plugin 'VundleVim/Vundle.vim'
" Add plugins here
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-commentary'
Plugin 'airblade/vim-gitgutter'
Plugin 'dracula/vim'

Plugin 'ervandew/supertab'
Plugin 'vim-airline/vim-airline'
Plugin 'junegunn/vader.vim'
call vundle#end()

filetype plugin indent on

" General Vim
set updatetime=100
set nobackup
set noswapfile
set shell=zsh\ -i

" Colors and fonts
colorscheme dracula
let g:airline_theme='dracula'
set background=dark
syntax enable
syntax spell toplevel
set termguicolors

" ui config
set	mouse=a
set number relativenumber
set lazyredraw

" Tab complete
set wildmode=longest,list,full
set wildmenu
set wildignore=*.o,*~,*.pyc,*/.git/*,*/.hg/*,*/.svn/*,*.DS_Store,.gitignore

" Show invisibles
set list
set listchars=tab:▸\ ,eol:¬

" Searching and autocomplete
set ignorecase
set smartcase
set showmatch
set incsearch
set hlsearch
set complete=.,t

" Tabs and spaces
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set cc=80
set backspace=indent,eol,start
set scrolloff=7

" Comment wrapping
set textwidth=75
set formatoptions=cqr

" Leader shortcuts
nnoremap <space> <Nop>
let mapleader =" "

	"Save and quit
nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>wq :wq<CR>
nnoremap <leader>Q :qa<CR>
"
	"Don't enter ex mode
noremap Q <nop>

	" Tabs
nnoremap <leader>t :tab drop<space>
nnoremap <leader>h :tab help<space>
nnoremap <leader>. :tab drop ~/.config/nvim/
nnoremap <leader>k gt
nnoremap <leader>j gT
nnoremap <leader>1 1gt
nnoremap <leader>2 2gt
nnoremap <leader>3 3gt
nnoremap <leader>4 4gt
nnoremap <leader>5 5gt
nnoremap <leader>6 6gt
nnoremap <leader>7 7gt
nnoremap <leader>8 8gt
nnoremap <leader>9 9gt

	"Splits
nnoremap <leader>s :vsplit<space>
nnoremap <leader>n <C-w><C-w>
nnoremap <leader>p <C-w><C-p>
nnoremap <leader>H <C-w>h
nnoremap <leader>J <C-w>j
nnoremap <leader>K <C-w>k
nnoremap <leader>L <C-w>l
set splitright

	"Jumps
nnoremap <leader>o <C-o>

	"Comments
map <leader>cl gcc
map <leader>cp gcap

	"Git
nnoremap <leader>gs :!gs<CR>g
nnoremap <leader>gl :!git logall<CR>g
nnoremap <leader>ga :silent !ga %<CR>
nnoremap <leader>gA :silent !ga .<CR>
nnoremap <leader>gr :!git reset HEAD %<CR>
nnoremap <leader>gR :!git reset HEAD .<CR>
nnoremap <leader>gp :tab drop term://ga\ -p\ %<CR>
nnoremap <leader>gc :!gc -m ""<left>
nnoremap <leader>gC :tab drop term://gc<CR>
nnoremap <leader>gb :!git checkout<Space>
nnoremap <leader>gB :!git checkout -b<Space>
nnoremap <expr> <silent> <leader>gn git#CheckoutCommit('next', v:count1)
nnoremap <expr> <silent> <leader>gN git#CheckoutCommit('previous', v:count1)
nnoremap <leader>gpu :silent !git stash push<CR>
nnoremap <leader>gpo :silent !git stash pop<CR>

	" Search and replace all in line or visual selection.
vnoremap <leader>r :s//g<left><left>
nnoremap <leader>r :s/\<<C-r><C-w>\>//g<left><left>
noremap <leader>R :%s/\<<C-r><C-w>\>//g<left><left>
noremap <leader>f ;

	" Change surrounding parenthesis/brackets.
nnoremap <leader>( mt%r)`tr(
nnoremap <leader>{ mt%r}`tr{
nnoremap <leader>[ mt%r]`tr[

nnoremap <leader>) mt%r(`tr)
nnoremap <leader>} mt%r{`tr}
nnoremap <leader>] mt%r[`tr]

	" Increment and deincrement
nnoremap <leader>+ <C-a>
nnoremap <leader>- <C-x>

	" Find definition
nnoremap <leader>d [<C-d>

	" From current line to line containing word
onoremap s //+0<left><left><left>

	" Toggles
nnoremap <leader>c :set spell!<CR>
nnoremap <leader>/ :nohl<CR>

" Remap
nnoremap ; :
nnoremap Y y$
nnoremap j gj
nnoremap k gk
nnoremap gf :tab drop <cfile><CR>

" Auto close
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap (<CR> (<CR>)<ESC>O
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O

" Plugin Options
	" Airline
let g:airline#extensions#tabline#enabled=1
let g:airline#extensions#tabline#formatter='unique_tail'
let g:airline#extensions#tabline#tab_nr_type=1
let airline#extensions#tabline#show_splits=0
let g:airline_powerline_fonts = 1

" SuperTab
let g:SuperTabDefaultCompletionType="context"
let g:SuperTabCompletionContexts=['s:ContextText', 's:ContextDiscover']
let g:SuperTabContextTextOmniPrecedence=['&completefunc', '&omnifunc']
let g:SuperTabContextDiscoverDiscovery=
		\ ["&completefunc:<c-p>", "&omnifunc:<c-x><c-o>"]
