source /usr/share/zsh/share/antigen.zsh  # paru -S antigen
antigen use oh-my-zsh
antigen bundle command-not-found
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions
antigen bundle reobin/typewritten@main
TYPEWRITTEN_PROMPT_LAYOUT="singleline"
TYPEWRITTEN_RELATIVE_PATH="home"
TYPEWRITTEN_SYMBOL='$'
TYPEWRITTEN_ARROW_SYMBOL=">"
TYPEWRITTEN_CURSOR="terminal"
TYPEWRITTEN_RIGHT_PROMPT_PREFIX="# "
antigen apply

HISTFILE=~/.history
SAVEHIST=65536
HISTSIZE=65536
zstyle ':completion:*' menu yes select

bindkey "^[[1;5D" backward-word 
bindkey "^[[1;5C" forward-word
bindkey  "^[[H"   beginning-of-line
bindkey  "^[[F"   end-of-line

alias diff='diff --color=auto'
alias grep='grep --color=auto'
alias ip='ip -color=auto'

alias ls='exa' # pacman -S exa
alias ll='ls -l --no-permissions --no-user'
alias la='ls -a'
alias lla='ll -a'
alias lt='ls -TL=3'
