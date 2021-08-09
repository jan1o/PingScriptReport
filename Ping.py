import subprocess
import platform

host = 'www.google.com.br'
param = '-n' if platform.system().lower() == 'windows' else '-c'
command = ['ping', param, '3', host]
result = str(subprocess.check_output(command, universal_newlines=True))
file = open("C:/Users/Usuário/Desktop/Pings/new.txt", "a")
file.write(result)
file.close()
