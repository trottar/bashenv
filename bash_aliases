#!/bin/bash
#####
# Define your aliases.
#####
alias ls='ls $LS_OPTIONS'
alias dir='dir --color=always'
alias vdir='vdir --color=always'
alias grep='grep --color=always'
alias la='ls -la'
alias cl='clear;ls'
alias root='root -l'
alias h='history'
alias d='dirs'
alias pd='pushd'
alias pd2='pushd +2'
alias po='popd'
alias m='more'
alias rm='rm -i'
alias ram='htop'
alias emacs='emacs -q --load "$HOME/users/trottar/.emacs.d/init.el"'
alias em='emacs'
alias rem='emacs $1 --funcall toggle-read-only'
alias sem='sudo emacs'

alias word='libreoffice'
alias snapshot='shutter'

alias help='source $HOME/users/trottar/.help.csh'
alias set-title="source $HOME/users/trottar/.nameTerm.csh"
alias howto="evince $HOME/users/trottar/commands.pdf"

alias trottar="cd $HOME/users/trottar;cl"

alias kaonlt='source $HOME/users/trottar/.kaonlt.csh;cl'
alias runlist="emacs kaonlt_runlist_8p2-6p2.csv"