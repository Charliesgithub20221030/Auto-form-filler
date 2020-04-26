set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
call vundle#end()            " required

call plug#begin('~/.vim/plugged')
Plug 'liuchengxu/space-vim-theme'
call plug#end()

filetype plugin indent on    " required


set number
set t_Co=256
syntax on
set cursorline
hi CursorLine cterm=none ctermbg=236 ctermfg=White
set cursorcolumn
hi CursorColumn cterm=none ctermbg=236 ctermfg=White
set ignorecase
set hlsearch
hi Search cterm=reverse ctermbg=none ctermfg=none
colorscheme space_vim_theme
hi Comment guifg=#5C6370 ctermfg=59
set incsearch
set cindent
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4
set mouse=a
set encoding=utf-8
