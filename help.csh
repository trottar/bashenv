#!/usr/bin/bash

echo
echo "Below are a list of quick command alias located in .cshrc..."
echo
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo       "h       history"
echo       "d       dirs"
echo       "pd      pushd"
echo       "pd2     pushd +2"
echo       "po      popd"
echo       "m       more"
echo       "rm      'rm -i'"
echo       "ram     htop"
echo       "cl      clear"
echo       "em      emacs"
echo       "sem     'sudo emacs'"
echo       "ls      'ls -F'"
echo       "la      'ls -la'"
echo       "ls      ls --color=always"
echo       "root    'root -l'"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "word      libreoffice "
echo "snapshot  shutter"
echo "reset     'source ~/.cshrc'"
echo "jlab      'set-title Jlab; ssh -X -Y trottar@login.jlab.org'"
echo "backup    'gksu deja-dup-prefences'"
echo "vncstart  'vncserver -geometry 1200x1000 :7'"
echo "vnckill   'vncserver -kill :7'"
echo "ipconfig  "source $HOME/.findHost.csh""
echo "set-title "source $HOME/.nameTerm.csh""
echo "howto     "evince $ORG/commands.pdf""
echo "server    "source $HOME/.run_server.csh""
echo "send      "sh $HOME/.copyFiles.sh""
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
