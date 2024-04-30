from datetime import datetime
from pathlib import Path


def base_dir():
    # Construir caminhos dentro do projeto da seguinte forma: BASE_DIR / 'subdir'.
    return Path(__file__).resolve().parent

def path_log():
    timestamp = datetime.now().strftime("%d_%m_%y-%H_%M_%S")
    #PATH_LOG = BASE_DIR / 'logs' / f'log_{timestamp}.csv'

def xml():
    url_site = "https://rpachallenge.com/"
