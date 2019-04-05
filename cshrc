# Define ls colors
setenv CLICOLOR "true"
setenv LS_COLORS "di=1;36:fi=01:ex=92:ln=7;106:or=31:*.png=33:*.jpg=33:*.pdf=97"

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
alias       pip     'sudo python -m pip'
alias       paint   'sudo inkscape'

alias word libreoffice 
alias snapshot shutter

alias redmine 'google-chrome http://127.0.0.1/redmine'
# alias redmine-start 'cd /opt/redmine-4.0.2-3/; sudo ./ctlscript.sh start'
# alias redmine-restart 'sudo ./opt/redmine-4.0.2-3/ctlscript.sh restart'
# alias redmine-stop 'sudo ./opt/redmine-4.0.2-3/ctlscript.sh stop'
alias reset 'source ~/.cshrc;cl'
alias jlab 'set-title Jlab; ssh -X -Y trottar@login.jlab.org'
alias backup 'gksu deja-dup-prefences'
alias vncstart 'vncserver -geometry 1200x1000 :7'
alias vnckill 'vncserver -kill :7'
alias help 'source $HOME/bin/help.csh'
alias ipconfig "source $HOME/bin/findHost.csh"
alias set-title "source $HOME/bin/nameTerm.csh"
alias howto "evince $ORG/commands.pdf"
alias server "source $HOME/bin/run_server.csh"
alias send "sh $HOME/bin/copyFiles.sh"
alias go_analysis "cd $hcana;source setup.csh;cd $replay_kaonlt;source setup.csh"

alias runplan-8.2 "evince $HOME/Documents/runplan_8p2gev.pdf"
alias runplan-6.2 "evince $HOME/Documents/runplan_6p2gev.pdf"
alias runplan-3.8 "evince $HOME/Documents/runplan_3p8gev.pdf"
alias runplan-4.9 "evince $HOME/Documents/runplan_4p9gev.pdf"
alias runplan-10.6 "evince $HOME/Documents/runplan_10p6gev.pdf"

# Number of commands to save in history list
set history=50

# Number of commands to save in ~/.history upon logout.
set savehist=50

# Find branch name
alias __git_current_branch 'git rev-parse --abbrev-ref HEAD >& /dev/null && echo "[`git rev-parse --abbrev-ref HEAD`]"'

# Set shell prompt
alias precmd 'set prompt="\n%{\033[35m%}Branch-`__git_current_branch`\n%{\033[34m%}%B%m%b %B%{\033[1;36m%}%~%b%{\033[00m%}> "'

# Assure working jlab software
setenv JLAB_ROOT /opt/jlab_software
source $JLAB_ROOT/2.2/ce/jlab.csh

echo
echo
echo "~~~~~~~~~~~~~~~~~~~~"
eval "date"
echo "New terminal is open"
echo "~~~~~~~~~~~~~~~~~~~~"
echo
echo
