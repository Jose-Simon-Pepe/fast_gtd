from os import system as syscall
class system:

    def open_cal(self,date=None):
        syscall("tmux split 'calcurse'")

    #FIX: This doesn't work
    def close_cal(self):
        syscall("killall calcurse")
