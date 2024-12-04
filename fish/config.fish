# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/away/miniconda3/bin/conda
    eval /home/away/miniconda3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/home/away/miniconda3/etc/fish/conf.d/conda.fish"
        . "/home/away/miniconda3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/home/away/miniconda3/bin" $PATH
    end
end
# <<< conda initialize <<<

alias clear='/usr/bin/clear'
export PATH="$HOME/.cargo/bin:$PATH"

# modern unix
alias cat='batcat'

alias ls='eza $eza_params'
alias l='eza --git-ignore $eza_params'
alias ll='eza --header --long $eza_params'
alias llm='eza --all --header --long --sort=modified $eza_params'
alias la='eza -lbhHigUmuSa'
alias lx='eza -lbhHigUmuSa@'
alias lt='eza --tree $eza_params'
alias tree='eza --tree $eza_params'

alias du='duf'

alias top='btop'
