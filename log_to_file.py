from datetime import datetime

def info(msg, file): 
    with open(file, 'a') as arquivo:
        arquivo.write(f"{datetime.now()} | INFO | {msg}")
        arquivo.write('\n')


def error(msg, file): 
    with open(file, 'a') as arquivo:
        arquivo.write(f"{datetime.now()} | ERRO | {msg}")
        arquivo.write('\n')
    
    
