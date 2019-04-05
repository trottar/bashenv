#ident  "@(#).cshrc     ver 1.0     Aug 20, 1996"
# Default user .cshrc file.
#
# This file is executed each time a shell is started.
# This includes the execution of shell scripts.


#####
# Source the site-wide syscshrc file.
# The syscshrc file defines some needed aliases (setup amd unsetup)
# and environment variables (PATH and MANPATH).  This line
# should not be deleted.  You do, however, have a choice of
# syscshrc files.  Uncomment the one that you prefer.
#####
source /site/env/syscshrc       # Searches /usr/local/bin first.
#source /site/env/syscshrc.alt   # Searches /usr/local/bin last.

#####
# Set up the shell environment.  You may comment/uncomment
# the following entries to meet your needs.
#####
# Number of commands to save in history list.
set history=50
 
# Number of commands to save in ~/.history upon logout.
set savehist=50

# Notify user of completed jobs right away, instead of waiting
# for the next prompt.
#set notify

# Don't redirect output to an existing file.
# CAD NOTE!  This must be commented out for proper ME10 functionality!!
set noclobber

# Set the file creation mode mask (default permissions for newly created files).
umask 022

# Define ls colors
setenv CLICOLOR "true"
# setenv LS_COLORS "di=1;36:fi=01:ex=92:ln=7;106:or=31:*.png=33:*.jpg=33:*.pdf=97"
setenv LS_COLORS "di=36:fi=32:ex=34:ln=07;106:or=31:*.png=33:*.jpg=33:*.pdf=33:"

# Defined file locations
setenv ORG $HOME/ResearchNP/org_file

setenv hcana $HOME/Analysis/hcana

setenv hallc_replay $HOME/Analysis/hallc_replay

setenv replay_kaonlt $HOME/Analysis/hallc_replay_kaonlt

setenv kaonlt_analysis $HOME/ResearchNP/ROOTAnalysis/kaonlt_analysis

#####
# Define your aliases.
#####
alias       h       history
alias       d       dirs
alias       pd      pushd
alias       pd2     pushd +2
alias       po      popd
alias       m       more
alias       rm      'rm -i'
alias       ram     htop
alias       cl      'clear;ls'
alias       em      emacs
alias       sem     'sudo emacs'
alias       rem     'emacs \!:1 --funcall toggle-read-only'
alias       ls      'ls -F'
alias       la      'ls -la'
alias       ls      ls --color=always
alias       root    'root -l'
# alias       pip     'sudo python -m pip'
# alias       paint   'sudo inkscape'

alias word libreoffice 
alias snapshot shutter

alias reset 'source ~/.cshrc;cl'
# alias jlab 'set-title Jlab; ssh -X -Y trottar@ifarm'
alias backup 'gksu deja-dup-prefences'
alias help 'source $HOME/bin/bin/help.csh'
alias ipconfig "source $HOME/bin/bin/findHost.csh"
alias set-title "source $HOME/bin/bin/nameTerm.csh"
alias howto "evince $ORG/commands.pdf"
# alias server "source $HOME/bin/bin/run_server.csh"
alias send "sh $HOME/bin/bin/copyFiles.sh"
alias go_analysis "cd $hcana;source setup.csh;cd $replay_kaonlt;source setup.csh"

# alias runplan-8.2 "evince $HOME/Documents/runplan_8p2gev.pdf"
# alias runplan-6.2 "evince $HOME/Documents/runplan_6p2gev.pdf"
# alias runplan-3.8 "evince $HOME/Documents/runplan_3p8gev.pdf"
# alias runplan-4.9 "evince $HOME/Documents/runplan_4p9gev.pdf"
# alias runplan-10.6 "evince $HOME/Documents/runplan_10p6gev.pdf"

alias python python2.7

# Find branch name
alias __git_current_branch 'git rev-parse --abbrev-ref HEAD >& /dev/null && echo "[`git rev-parse --abbrev-ref HEAD`]"'

# Set shell prompt
alias precmd 'set prompt="\n%{\033[35m%}Branch-`__git_current_branch`\n%{\033[34m%}%m%{\033[34m%}:%n %{\033[36m%}%~%{\033[00m%}> "'

# Assure working jlab software
source /site/12gev_phys/softenv.csh 2.0

echo
echo
echo "~~~~~~~~~~~~~~~~~~~~"
eval "date"
echo "New terminal is open"
echo "~~~~~~~~~~~~~~~~~~~~"
echo
echo
