# Define ls colors
setenv CLICOLOR "true"
setenv LS_COLORS "di=1;36:fi=01:ex=92:ln=7;106:or=31:*.png=33:*.jpg=33:*.pdf=97"

# Run bash profile
source ~/.bash_profile

# Defined file locations
setenv ORG $HOME/ResearchNP/org_file

setenv hcana $HOME/Analysis/hcana

setenv hallc_replay $HOME/Analysis/hallc_replay

setenv replay_kaonlt $HOME/Analysis/hallc_replay_lt

setenv ROOTFILES $HOME/ResearchNP/ROOTfiles

setenv PROGRAMS $HOME/Programs/my_programs

#######################################################################################################
# EJPM package for g4e and ejana ######################################################################
#######################################################################################################
# env command also regenerated files:
# /home/trottar/.local/share/ejpm/env.csh


#######################################################################################################

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
alias       nem     'emacs -nw'
alias       ls      'ls -F'
alias       la      'ls -la'
alias       ls      ls --color=always
alias       root    'root -l'
alias       pip     'sudo python -m pip'
alias       pip3    'sudo python3 -m pip'
alias       paint   'sudo inkscape'
alias       install 'sudo apt-get install'
alias       calc    'genius'
alias       remote  'teamviewer'
alias       docker  'sudo docker'
alias       chrome  'google-chrome \!:1'
alias       git-all  'find ~/ -name ".git"'

alias word libreoffice 
alias snapshot shutter

# alias redmine 'google-chrome http://127.0.0.1/redmine'
# alias redmine-start 'cd /opt/redmine-4.0.2-3/; sudo ./ctlscript.sh start'
# alias redmine-restart 'sudo ./opt/redmine-4.0.2-3/ctlscript.sh restart'
# alias redmine-stop 'sudo ./opt/redmine-4.0.2-3/ctlscript.sh stop'
alias battery 'upower -i /org/freedesktop/UPower/devices/battery_BAT0'
alias reset 'source ~/.cshrc;cl'
alias jlab 'set-title Jlab; ssh -X -Y trottar@login.jlab.org'
alias backup 'gksu deja-dup-prefences'
alias vncstart 'vncserver -geometry 1200x1000 :7'
alias vnckill 'vncserver -kill :7'
alias help 'source $HOME/bin/help.csh'
alias ipconfig "source $HOME/bin/findHost.csh"
alias set-title "source $HOME/bin/nameTerm.csh"
alias search "$HOME/bin/physics_dict/run_physics_dict.sh \!:1"
alias howto "evince $ORG/commands.pdf"
alias server "source $HOME/bin/run_server.csh"
alias send "sh $HOME/bin/copyFiles.sh"
alias go_analysis "cd $hcana;source setup.csh;cd $replay_kaonlt;source setup.csh"
alias cpu-info "inxi -Fxzd"
# alias root2py "cd $HOME/bin/;sh root2py.sh \!:1;"
alias ROOT2PY "$HOME/bin/root2py.sh"
# alias load "gnome-terminal --tab --tab-with-profile="trottar" --working-directory=$HOME;gnome-terminal --geometry=81x260-0+0 --tab-with-profile="trottar" --working-directory=$HOME/ResearchNP/JLEIC/Trotta-EIC;wmctrl -r eic_SF -t 3;gnome-terminal --geometry=81x260-0+0 --tab-with-profile="trottar" --working-directory=$HOME/Analysis/hallc_replay_kaonlt/UTIL_KAONLT;wmctrl -r hallc_kaonlt  -t 2"
alias load "gnome-terminal --geometry=81x260-0+0 --working-directory=$HOME;gnome-terminal --geometry=81x260-0+0  --working-directory=$HOME/ResearchNP/JLEIC/USERS/trottar;wmctrl -r eic_SF -t 3;gnome-terminal --geometry=81x260-0+0  --working-directory=$HOME/Analysis/hallc_replay_lt/UTIL_KAONLT;wmctrl -r hallc_kaonlt  -t 2;google-chrome &"
alias memleak "valgrind --tool=memcheck --leak-check=yes \!:1"
# alias rootleak "valgrind --leak-check=full --show-leak-kinds=all --tool=memcheck --track-origins=yes --suppressions=$ROOTSYS/etc/valgrind-root.supp root.exe -l -b -q \!:1"
alias pdf-shrink '~/Programs/pdfsizeopt/pdfsizeopt \!:1 \!:2'
alias updatepip 'sh ~/bin/upgradePython.sh'
alias anki '~/Programs/anki-2.1.15-linux-amd64/bin/anki'
alias jlab_docker 'google-chrome http://127.0.0.1:8888/;docker run -it -p8888:8888 electronioncollider/epic'
alias share_jlab_docker 'sh ~/bin/shareDocker.sh \!:1'
alias ssh_docker 'google-chrome http://127.0.0.1:8888/;docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --rm -it -p8888:8888 --user 1000 electronioncollider/epic bash'
alias pull_docker 'docker pull electronioncollider/epic'
alias plot "$HOME/bin/quick_plot/plotRoot.sh"
alias update_calendar "sh $ORG/google_calendar/update_calendar.sh"
alias email "sh $PROGRAMS/google_email/send_gmail.sh"
alias clion "sh ~/Programs/clion-*/bin/clion.sh"
alias ejpm_env "source $HOME/.local/share/ejpm/env.csh"

alias runplan-8.2 "evince $HOME/Documents/runplans/runplan_8p2gev.pdf"
alias runplan-6.2 "evince $HOME/Documents/runplans/runplan_6p2gev.pdf"
alias runplan-3.8 "evince $HOME/Documents/runplans/runplan_3p8gev.pdf"
alias runplan-4.9 "evince $HOME/Documents/runplans/runplan_4p9gev.pdf"
alias runplan-10.6 "evince $HOME/Documents/runplans/runplan_10p6gev.pdf"

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

setenv ROOTSYS $HOME/ResearchNP/gemc/eic/root/root-v6-20-00/
source $ROOTSYS/bin/thisroot.csh

echo
echo
echo "~~~~~~~~~~~~~~~~~~~~"
eval "date"
echo "New terminal is open"
echo "~~~~~~~~~~~~~~~~~~~~"
echo
echo
