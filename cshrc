# Define ls colors
setenv CLICOLOR "true"
setenv LS_COLORS "di=1;36:fi=01:ex=92:ln=7;106:or=31:*.png=33:*.jpg=33:*.pdf=97"

# Run bash profile
source ~/.bash_profile

# Use unsetenv to unset any enviroment variables

# Define local path
setenv PATH /usr/local/bin:/usr/bin:/bin

# Add mimic to path (mimic is text to speech)
setenv PATH "~/Programs/mimic/:$PATH"

# Adds custom bin to path
setenv PATH "~/bin/:$PATH"

# Adds used programs to path
setenv PATH "~/Programs/:$PATH"
setenv PATH "~/Programs/physics_dict/:$PATH"
setenv PATH "~/Programs/pdfsizeopt/:$PATH"
setenv PATH "~/Programs/clion-2019.3.4/bin/:$PATH"

# Adds custom programs to path
setenv PATH "~/Programs/my_programs/:$PATH"
setenv PATH "~/Programs/my_programs/google_email/:$PATH"
setenv PATH "~/Programs/my_programs/quick_plot/:$PATH"

# Defined file locations
setenv hcana $HOME/Analysis/hcana
setenv kaonlt $HOME/Analysis/hallc_replay_lt
setenv ROOTFILES $HOME/ResearchNP/ROOTfiles
setenv PROGRAMS $HOME/Programs/my_programs
setenv scratch $HOME/scratch
# External HD
setenv ext_hd "/media/trottar/Backup*Plus/"

# Requried for customsearch
setenv youtube_api $YOUTUBE_API

#######################################################################################################

#####
# Define your aliases.
#####
alias       h                 history
alias       d                 dirs
alias       pd                pushd
alias       pd2               pushd +2
alias       po                popd
alias       m                 more
alias       rm                'rm -i'
alias       ram               htop
alias       cl                'clear;ls'
alias       em                emacs
alias       sem               'sudo emacs'
alias       rem               'emacs \!:1 --funcall toggle-read-only'
alias       nem               'emacs -nw'
alias       ls                'ls -F'
alias       la                'ls -la'
alias       ls                ls --color=always
alias       root              'root -l'
alias       pip               'sudo python -m pip'
alias       pip3              'sudo python3 -m pip'
alias       paint             'sudo inkscape'
alias       install           'sudo apt-get install'
alias       calc              'genius'
alias       remote            'teamviewer'
alias       docker            'sudo docker'
alias       chrome            'google-chrome \!:1'
alias       git-all           'find ~/ -name ".git"'
alias       pyIndent          'sudo autopep8 -i \!:1'
alias       jnb               'jupyter notebook'
alias       jgrab             'echo "Grabbing all files from scratch";rsync -av ifarm:/scratch/trottar/ .'
alias       pc_grab           'echo "Grabbing all files from PC";rsync -av PC:~/scratch/ .'
alias       chat              'chat.sh \!:1'
alias       chatgui           'chat.sh -g \!:1'
alias       note              'notes.sh \!:1'
alias       voice             '$HOME/Programs/mimic/mimic -t \!:1'
alias       word              'sudo libreoffice'
alias       snapshot          shutter
alias       dir_ size         'du -h --max-depth=1 | sort -rh'
alias       sizecheck         'sudo find . -type f -size \!:1 -ls'
alias       slides            'jupyter nbconvert *.ipynb --to slides --post serve'
alias       battery           'upower -i /org/freedesktop/UPower/devices/battery_BAT0'
alias       reset             'source ~/.cshrc;cl'
alias       jlab              'set-title Jlab;ssh -X -Y ifarm'
alias       jexit             'ssh -O exit ifarm'
alias       pc_connect '       set-title PC; ssh -X -Y PC'
alias       backup            'gksu deja-dup-prefences'
alias       vncstart          'vncserver -geometry 1200x1000 :7'
alias       vnckill           'vncserver -kill :7'
alias       help              'source help.csh'
alias       ipconfig          "source findHost.csh"
alias       set-title         "source nameTerm.csh"
alias       dict              "run_physics_dict.sh \!:1"
alias       server            "source run_server.csh"
alias       send              "copyFiles.sh"
alias       cpu-info          "inxi -Fxzd"
alias       ROOT2PY           "root2py.sh"
alias       pdf-shrink        'pdfsizeopt \!:1 \!:2'
alias       updatepip         'upgradePython.sh'
alias       share_jlab_docker 'shareDocker.sh \!:1'
alias       plot              "plotRoot.sh"
alias       email             "send_gmail.sh"
alias       clion             "clion.sh"
alias       replace           "find . -type f -exec sed -i 's/\!:1/\!:2/g' {} +"
alias       search            'grep -rn "\!:1" *'
alias       git-check         "bash gitcheck.sh"
alias       starfinder        "cd $PROGRAMS/starfinder/src; python3.8 main.py"
alias       spellcheck        'aspell check'

# Creates terminals of interest and moves them to proper workspaces
alias load "gnome-terminal --geometry=51x260-0+0 --working-directory=$HOME --title=Home;xdotool search --name 'EIC' windowactivate;xdotool set_desktop --relative --desktop 3;gnome-terminal --geometry=51x260-0+0  --working-directory=$HOME/ResearchNP/JLEIC/USERS/trottar --title=EIC;xdotool search --name 'lt_analysis' windowactivate;xdotool set_desktop --relative --desktop 2;gnome-terminal --geometry=51x260-0+0  --working-directory=$HOME/Analysis/hallc_replay_lt/UTIL_KAONLT --title=UTIL_KAONLT --command 'gnome-terminal --tab  --working-directory=$HOME/Analysis/lt_analysis --title=lt_analysis --tab  --working-directory=$HOME/Analysis/lt_analysis/src --title=lt_analysis/src --tab --working-directory=$HOME/Analysis/simc_gfortran --title=simc_gfortran --tab --working-directory=$HOME/Analysis/hallc_replay_lt/UTIL_KAONLT --title=UTIL_KAONLT'"

#alias go_analysis "cd $hcana;source setup.csh;cd $replay_kaonlt;source setup.csh"
# alias rootleak "valgrind --leak-check=full --show-leak-kinds=all --tool=memcheck --track-origins=yes --suppressions=$ROOTSYS/etc/valgrind-root.supp root.exe -l -b -q \!:1"
#alias barrier 'snap run barrier' # barrier (through snap), for keyboard/mouse sharing

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

# Assure workking jlab software
setenv JLAB_ROOT /opt/jlab_software
source $JLAB_ROOT/2.2/ce/jlab.csh  # default root 6.12.06, currently set to root 6.18.06

echo
echo
echo "~~~~~~~~~~~~~~~~~~~~"
eval "date"
echo "New terminal is open"
echo "~~~~~~~~~~~~~~~~~~~~"
echo
echo
    
