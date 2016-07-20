# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="robbyrussell"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="yyyy-mm-dd"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git git-flow python pyenv vim-interaction autojump)

# User configuration

export PATH=$HOME/bin:/usr/local/bin:$PATH
# export MANPATH="/usr/local/man:$MANPATH"

source $ZSH/oh-my-zsh.sh

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#	export EDITOR='vim'
# else
#	export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
##### all my alias ------
#
alias dir='dir --color=auto'
alias ld='ls -Al | grep ^d'
alias lf='ls -Al | grep ^-'
alias ll='ls -Al'
alias vdir='vdir --color=auto'
alias cls='clear'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias size='du -sh'
alias ll='ls -Al'
alias kill='kill -KILL'
alias Mymount='mount |column -t'
alias MyDf='df -ah|column -t'
alias Shit='scp -P 36000 /openwrt/qosv4 root@192.168.2.1:/'
alias Mytmpfs='MyDf|egrep tmpfs'
alias SListen='netstat -an|egrep -i listen'
alias pstree='pstree -anpuh'
alias cman='man -M /usr/share/man/zh_CN'
alias Zhuxiao='gnome-session-save --logout'
alias timeanddate='echo ++++++++++++++++++++++++++++;cal;date;echo +++++++++++++++++++++++++++++'
alias ls3r3w3x='ls -al | grep ^.rwxrwxrwx'
alias English='LANG=en_US:UTF-8;LANGUAGE=en_US:UTF-8'
alias Snet_port='netstat -an|egrep -i listen --col'
alias PS_EFAUX='ps aux'
alias Hanhua='LANG=zh_CN:UTF-8;LANGUAGE=zh_CN:UTF-8'
alias lstargz='ls -al | grep tar.gz$'
alias Snat='iptables -t nat -L -vn'
alias vi='vim'
alias LC='LANG=C'
alias cp='cp -v'
alias mv='mv -v'
alias Sfilter='iptables -t filter -L -vn'
alias Sraw='iptables -t raw -L -vn'
alias Smangle='iptables -t mangle -L -vn'
alias mountnfs='sudo mount 192.168.200.254:/home/share -t nfs /home/share'
alias loginxiyoulinux='ssh -i /home/tiger/.ssh/id_rsa xiyoulinux@192.168.200.254 -p 89'
alias logintiger='ssh -i /home/tiger/.ssh/id_dsa tiger@192.168.200.254 -p 89'
alias Connect_Router="ssh root@192.168.1.1 -p 36000"
alias vi='vim'
alias Mount_utd8='mount -o utf8'
alias zhcon='zhcon --utf8'
alias Snet='netstat -an'
alias lssh='ls -al | grep sh$'
alias myip='ifconfig eth0 | grep inet | grep -v inet6'

alias CDsrc='cd /usr/local/src'
alias CDpython='cd /Users/tib/python'
alias CDshell='cd /Users/tib/shell'
alias CDusrlocal='cd /usr/local/'
alias CDtib='cd /Users/tib/'
alias CDopenwrt="cd /openwrt"
alias CDopenwrt='cd /BackUp/openwrt'
alias CDopenwrt='cd /openwrt'
alias CDIntoLocalMysql="mysql -h192.168.80.10 -utib -pmeimima"
alias CDintoGit="cd ~/git_root/"
alias CDhadoop="cd /usr/local/hadoop/"
alias CDapache="cd /etc/apache2/"
alias Sest='netstat -an|egrep -i established'
alias CDintoPythonLib="cd /usr/lib64/python2.7"
alias CDmySec='cd /usr/local/src/sec'
alias CDgoagent='cd /Users/tib/Software/goagent-3.2.3/local'

alias CDgit='cd ~/git_root/'
alias qas01='ssh root@123.59.56.118 -p 38390'

alias ssh_aliyun='ssh root@aliyun -p 33331'
alias ssh_aws='ssh -i ~/.ssh/ssh_to_aws.pem root@aws'
alias ssh_bwg='ssh root@bwg -p 26510 -i ~/.ssh/id_rsa'
alias ssh_openwrt_31='ssh root@192.168.31.1 -p 24'
alias CD_myshadowsocks='cd /Users/tib/git_root/shadowsocks_my/shadowsocks'
alias CD_ss='cd /Users/tib/git_root/ss/shadowsocks'
#fi


### for xiaoenai # :)
alias login_jump='ssh -p38390 xiaohu.liu@rdp01.xiaoenai.net'
alias login_cds01='ssh -p28290 root@42.62.14.36'
#alias login_jump='ssh -p38390 xiaohu.liu@rdp01.xiaoenai.net'
alias login_dev='ssh root@172.16.1.11'
alias login_container='ssh root@172.17.0.45'
alias ssh_do='ssh root@tib.f3322.net'
####### ------------

/Users/tib/.autojump/etc/profile.d/autojump.sh ]] && source /Users/tib/.autojump/etc/profile.d/autojump.sh

PYTHONSTARTUP=~/.pythonstartup
export PYTHONSTARTUP
#if [ -f ~/.git-completion.bash ]; then
#	. ~/.git-completion.bash
#fi

export PYTHONSTARTUP=$HOME/.pythonrc.py

###
#autoload -U promptinit
#promptinit
#prompt clint
#PROMPT=$(echo "${ret_status}%{$fg_bold[green]%}%p%{$fg[blue]%}%5~/%{$fg_bold[cyan]%}$(git_prompt_info) %{$reset_color%}")
PROMPT='%{$fg_bold[red]%}➜ %{$fg_bold[green]%}%p%{$fg[cyan]%}%d %{$fg_bold[blue]%}$(git_prompt_info)%{$fg_bold[blue]%}% %{$reset_color%} '

setopt noincappendhistory
setopt nosharehistory
