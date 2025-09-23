setopt prompt_subst

workspace=~/Documents/GitHub/fpd-mcp-workshop
workspacename=fpd-mcp-workshop

PROMPT='$(
  if [[ $PWD == $workspace ]]; then
    echo "~/${workspacename}/"
  else
    echo "~/…/${PWD##*/}/"
  fi
) $( [[ $EUID -eq 0 ]] && echo "#" || echo "$" ) '
