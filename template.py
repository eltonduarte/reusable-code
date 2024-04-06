"""
Exemplo de uso
"""

from reusable_code import log_to_file, make_browser

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
