from os import system as syscall
class system:

    def open_cal(self,date=None):
        syscall("tmux split 'calcurse'")

    #FIX: This doesn't work
    def close_cal(self):
        syscall("killall calcurse")

    def open_study_necesities(self,path:str=None):
        syscall(f"tmux split 'more {path} | fzf'")

    def close_study_necesities(self):
        syscall("killall fzf")
