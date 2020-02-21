# Define ls colors
setenv CLICOLOR "true"
setenv LS_COLORS "di=1;36:fi=01:ex=92:ln=7;106:or=31:*.png=33:*.jpg=33:*.pdf=97"

# Defined file locations
setenv ORG $HOME/ResearchNP/org_file

setenv hcana $HOME/Analysis/hcana

setenv hallc_replay $HOME/Analysis/hallc_replay

setenv replay_kaonlt $HOME/Analysis/hallc_replay_lt

setenv ROOTFILES $HOME/ResearchNP/ROOTfiles/

#######################################################################################################
# EJPM package for g4e and ejana ######################################################################
#######################################################################################################

# =============================
# vgm
# =============================
setenv VGM_DIR "/home/trottar/ResearchNP/gemc/eic/vgm/vgm-v4-5"

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/vgm/vgm-v4-5/lib"
else
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:"/home/trottar/ResearchNP/gemc/eic/vgm/vgm-v4-5/lib"
endif

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/vgm/vgm-v4-5/lib64"
else
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:"/home/trottar/ResearchNP/gemc/eic/vgm/vgm-v4-5/lib64"
endif

# =============================
# g4e
# =============================

# Make sure PATH is set
if ( ! $?PATH ) then
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/g4e/g4e-dev"
else
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/g4e/g4e-dev":${PATH}
endif

# Make sure PYTHONPATH is set
if ( ! $?PYTHONPATH ) then
    setenv PYTHONPATH "/home/trottar/ResearchNP/gemc/eic/g4e/g4e-dev/python"
else
    setenv PYTHONPATH "/home/trottar/ResearchNP/gemc/eic/g4e/g4e-dev/python":${PYTHONPATH}
endif
setenv G4E_HOME "/home/trottar/ResearchNP/gemc/eic/g4e/g4e-dev"
setenv G4E_MACRO_PATH "/home/trottar/ResearchNP/gemc/eic/g4e/g4e-dev"

# =============================
# geant
# =============================

# Make sure PATH is set
if ( ! $?PATH ) then
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/geant/geant-v10.6.0/bin"
else
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/geant/geant-v10.6.0/bin":${PATH}
endif
source /home/trottar/ResearchNP/gemc/eic/geant/geant-v10.6.0/bin/geant4.csh /home/trottar/ResearchNP/gemc/eic/geant/geant-v10.6.0/bin

# =============================
# eic-smear
# =============================
setenv EIC_SMEAR_HOME "/home/trottar/ResearchNP/gemc/eic/eic-smear/eic-smear-master"

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/eic-smear/eic-smear-master/lib"
else
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:"/home/trottar/ResearchNP/gemc/eic/eic-smear/eic-smear-master/lib"
endif

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/eic-smear/eic-smear-master/lib64"
else
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:"/home/trottar/ResearchNP/gemc/eic/eic-smear/eic-smear-master/lib64"
endif

# =============================
# ejana
# =============================

# Make sure JANA_PLUGIN_PATH is set
if ( ! $?JANA_PLUGIN_PATH ) then
    setenv JANA_PLUGIN_PATH "/home/trottar/ResearchNP/gemc/eic/ejana/dev/compiled/plugins"
else
    setenv JANA_PLUGIN_PATH "/home/trottar/ResearchNP/gemc/eic/ejana/dev/compiled/plugins":${JANA_PLUGIN_PATH}
endif

# Make sure PATH is set
if ( ! $?PATH ) then
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/ejana/dev/compiled/bin"
else
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/ejana/dev/compiled/bin":${PATH}
endif

# =============================
# jana
# =============================
setenv JANA_HOME "/home/trottar/ResearchNP/gemc/eic/jana/jana-master"

# Make sure JANA_PLUGIN_PATH is set
if ( ! $?JANA_PLUGIN_PATH ) then
    setenv JANA_PLUGIN_PATH "$JANA_HOME/plugins"
else
    setenv JANA_PLUGIN_PATH ${JANA_PLUGIN_PATH}:"$JANA_HOME/plugins"
endif

# Make sure PATH is set
if ( ! $?PATH ) then
    setenv PATH "$JANA_HOME/bin"
else
    setenv PATH "$JANA_HOME/bin":${PATH}
endif

# =============================
# hepmc
# =============================

# Make sure PATH is set
if ( ! $?PATH ) then
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/hepmc/hepmc-HEPMC_02_06_09/bin"
else
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/hepmc/hepmc-HEPMC_02_06_09/bin":${PATH}
endif
setenv HEPMC_DIR "/home/trottar/ResearchNP/gemc/eic/hepmc/hepmc-HEPMC_02_06_09"

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/hepmc/hepmc-HEPMC_02_06_09/lib"
else
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:"/home/trottar/ResearchNP/gemc/eic/hepmc/hepmc-HEPMC_02_06_09/lib"
endif

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/hepmc/hepmc-HEPMC_02_06_09/lib64"
else
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:"/home/trottar/ResearchNP/gemc/eic/hepmc/hepmc-HEPMC_02_06_09/lib64"
endif

# =============================
# clhep
# =============================
setenv CLHEP "/home/trottar/ResearchNP/gemc/eic/clhep/clhep-master"
setenv CLHEP_BASE_DIR "/home/trottar/ResearchNP/gemc/eic/clhep/clhep-master"
setenv CLHEP_INCLUDE_DIR "/home/trottar/ResearchNP/gemc/eic/clhep/clhep-master/include"
setenv CLHEP_LIB_DIR "/home/trottar/ResearchNP/gemc/eic/clhep/clhep-master/lib"

# Make sure PATH is set
if ( ! $?PATH ) then
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/clhep/clhep-master/bin"
else
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/clhep/clhep-master/bin":${PATH}
endif

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/clhep/clhep-master/lib"
else
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/clhep/clhep-master/lib":${LD_LIBRARY_PATH}
endif

# =============================
# fastjet
# =============================

# Make sure PATH is set
if ( ! $?PATH ) then
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/fastjet/fastjet-3.3.3/bin"
else
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/fastjet/fastjet-3.3.3/bin":${PATH}
endif

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/fastjet/fastjet-3.3.3/lib"
else
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/fastjet/fastjet-3.3.3/lib":${LD_LIBRARY_PATH}
endif

# =============================
# rave
# =============================
setenv RAVEPATH "/home/trottar/ResearchNP/gemc/eic/rave/rave-master"

# Make sure CMAKE_PREFIX_PATH is set
if ( ! $?CMAKE_PREFIX_PATH ) then
    setenv CMAKE_PREFIX_PATH "/home/trottar/ResearchNP/gemc/eic/rave/rave-master/share/rave"
else
    setenv CMAKE_PREFIX_PATH "/home/trottar/ResearchNP/gemc/eic/rave/rave-master/share/rave":${CMAKE_PREFIX_PATH}
endif

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/rave/rave-master/lib"
else
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/rave/rave-master/lib":${LD_LIBRARY_PATH}
endif

# =============================
# root
# =============================
if ( -f /opt/jlab_software/2.2/Linux__LinuxMint19.3-x86_64-gcc7/root/6.12.06/bin/thisroot.csh ) then
    source /opt/jlab_software/2.2/Linux__LinuxMint19.3-x86_64-gcc7/root/6.12.06/bin/thisroot.csh
endif

# =============================
# easy-profiler
# =============================

# Make sure CMAKE_PREFIX_PATH is set
if ( ! $?CMAKE_PREFIX_PATH ) then
    setenv CMAKE_PREFIX_PATH "/home/trottar/ResearchNP/gemc/eic/easy-profiler/easy-profiler-v2.1.0/lib/cmake/easy_profiler"
else
    setenv CMAKE_PREFIX_PATH "/home/trottar/ResearchNP/gemc/eic/easy-profiler/easy-profiler-v2.1.0/lib/cmake/easy_profiler":${CMAKE_PREFIX_PATH}
endif

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/easy-profiler/easy-profiler-v2.1.0/lib"
else
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/easy-profiler/easy-profiler-v2.1.0/lib":${LD_LIBRARY_PATH}
endif

# Make sure PATH is set
if ( ! $?PATH ) then
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/easy-profiler/easy-profiler-v2.1.0/bin"
else
    setenv PATH "/home/trottar/ResearchNP/gemc/eic/easy-profiler/easy-profiler-v2.1.0/bin":${PATH}
endif

# =============================
# genfit
# =============================
setenv GENFIT "/home/trottar/ResearchNP/gemc/eic/genfit/genfit-master"
setenv GENFIT_DIR "/home/trottar/ResearchNP/gemc/eic/genfit/genfit-master"

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/genfit/genfit-master/lib"
else
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:"/home/trottar/ResearchNP/gemc/eic/genfit/genfit-master/lib"
endif

# Make sure LD_LIBRARY_PATH is set
if ( ! $?LD_LIBRARY_PATH ) then
    setenv LD_LIBRARY_PATH "/home/trottar/ResearchNP/gemc/eic/genfit/genfit-master/lib64"
else
    setenv LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:"/home/trottar/ResearchNP/gemc/eic/genfit/genfit-master/lib64"
endif

# env command also regenerated files:
# /home/trottar/.local/share/ejpm/env.sh 
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
alias load "gnome-terminal --geometry=81x260-0+0 --working-directory=$HOME;gnome-terminal --geometry=81x260-0+0  --working-directory=$HOME/ResearchNP/JLEIC/Trotta-EIC;wmctrl -r eic_SF -t 3;gnome-terminal --geometry=81x260-0+0  --working-directory=$HOME/Analysis/hallc_replay_lt/UTIL_KAONLT;wmctrl -r hallc_kaonlt  -t 2;google-chrome &"
alias memleak "valgrind --tool=memcheck --leak-check=yes \!:1"
# alias rootleak "valgrind --leak-check=full --show-leak-kinds=all --tool=memcheck --track-origins=yes --suppressions=$ROOTSYS/etc/valgrind-root.supp root.exe -l -b -q \!:1"
alias pdf-shrink '~/Programs/pdfsizeopt/pdfsizeopt \!:1 \!:2'
alias updatepip 'sh ~/bin/upgradePython.sh'
alias anki '~/Programs/anki-2.1.15-linux-amd64/bin/anki'
alias jlab_docker 'google-chrome http://127.0.0.1:8888/;google-chrome http://127.0.0.1:6080/;docker run -it -p8888:8888 -p 6080:6080 electronioncollider/epic'
alias share_jlab_docker 'sh ~/bin/shareDocker.sh \!:1'
alias plot "$HOME/bin/quick_plot/plotRoot.sh"
alias update_calendar "sh $ORG/google_calendar/update_calendar.sh"

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

echo
echo
echo "~~~~~~~~~~~~~~~~~~~~"
eval "date"
echo "New terminal is open"
echo "~~~~~~~~~~~~~~~~~~~~"
echo
echo
