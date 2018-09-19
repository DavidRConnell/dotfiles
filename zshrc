# Add ~/bin to path
export PATH=$HOME/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/Users/davidconnell/.oh-my-zsh"

ZSH_THEME="robbyrussell"
zstyle ':completion:*' menu select

plugins=(
  git
  vi-mode
  colored-man-pages
  osx
)

source $ZSH/oh-my-zsh.sh

# User configuration

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='nvim'
fi

unsetopt inc_append_history
unsetopt share_history

# Custom key bindings
bindkey -a k history-beginning-search-backward
bindkey -a j history-beginning-search-forward

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

source ~/.bash_profile
