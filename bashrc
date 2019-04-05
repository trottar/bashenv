#!/bin/bash

# Define ls colors
export CLICOLOR=1
export LS_COLORS="di=36:fi=32:ex=34:ln=07;106:or=31:*.png=33:*.jpg=33:*.pdf=33:"
export LS_OPTIONS='--color=auto'

export TERM="xterm-256color"

export SCREENRC=$HOME/users/trottar/.screenrc
export SCREENDIR=$HOME/users/trottar/.screen/$host

if [ -f $HOME/users/trottar/.bash_aliases ]; then
    . $HOME/users/trottar/.bash_aliases
fi

if [ ! -e /environment ] ; then
  running_singularity=
else
  running_singularity="\#singularity"
fi

git_branch(){
    git describe --contains --all HEAD 2>/dev/null
}

# If this is an xterm set the title to user@host:dir
case $TERM in
    xterm*|rxvt*)
    PS1='${debian_chroot:+($debian_chroot)}\n\[\033[35m\]Branch-[$(git_branch)\[\033[35m\]]\n\[\033[34m\]\h:trottar\[\033[36m\]:\[\033[36m\]\w\[\033[00m\]> '
    ;;
    *)
    ;;
esac

# Number of commands to save in history list
set history=50

# Number of commands to save in ~/.history upon logout.
set savehist=50

echo
echo
echo "~~~~~~~~~~~~~~~~~~~~"
eval "date"
echo "New terminal is open"
echo "~~~~~~~~~~~~~~~~~~~~"
echo
echo
