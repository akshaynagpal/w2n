#!/bin/zsh

function upgradeAllLocalBranchesFromMaster {
  for BRANCH in `git branch | cut -c 3-`
    do
      git switch $BRANCH
      git merge origin/master
      git pull
    done
  git switch master
}
function showHelp {
  echo '   -h   show this help'
  echo '   -u   upgrade all local branches from master' 
  echo '        with call git switch <branch> git merge origin/master'
}

echo "Please wait..."

while true
  do
    case "$1" in 
    "-h") shift && showHelp || die
       ;;
    "-u") echo "<drink coffee to start the engine>" && echo " " && sleep 3 && upgradeAllLocalBranchesFromMaster
       ;;
    esac

    if [ "$#" -eq "0" ]
      then
        break;
    fi
    shift || break
  done

echo " "
echo "I need more coffee!"

exit

# save for later
while getopts h:u: argument
  do
    case "${argument}"
    in
    h) showHelp;;
    u) upgradeAllLocalBranchesFromMaster;;
    esac
  done

#EOF
