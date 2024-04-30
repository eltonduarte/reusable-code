""" Template Para Automações Web
    Criada por: @eltonpduarte
    Ultima atualização em: 30/04/2024
"""

# Importação dos módulos que serão utilizados
from reusable_code import make_browser, log_to_file, taskkill, wait_for_conditions, config                            

# Construir caminhos dentro do projeto da seguinte forma: BASE_DIR / 'subdir'.
BASE_DIR = config.base_dir()
PATH_LOG = config.path_log()

try:
    bot_web = make_browser.chrome()
    log_to_file.info('Sessão com o webdriver criada com sucesso', 'log.txt')

    bot_web.get("https://google.com.br")
    log_to_file.info('Página acessada com sucesso', 'log.txt')

except Exception as error_message:
    log_to_file.error(f'{error_message}', 'log.txt')

finally:
    bot_web.close()
    log_to_file.error('Fim do processamento', 'log.txt')
