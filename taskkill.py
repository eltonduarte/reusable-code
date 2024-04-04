import os

def process(*processos):
    """
    Recebe tupla com o nome dos processos <nome>.<extension>
    Não levanta nenhuma exceção caso o nome do processo não exista
    Exemplo: taskkill('chrome.exe', 'excel.exe', 'saplogon.exe')
    """
    
    for processo in processos:
        os.system(f"taskkill /f /im {processo}")

