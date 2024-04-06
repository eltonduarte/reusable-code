# Ações simples e reutilizáveis para bots

Atenção: Você precisará adicionar a pasta "reusable-code" no diretório de instalação do python 
```
C:\Users\<username>\AppData\Local\Programs\Python\Python312\Lib\<reusable_code>
```

Você também precisará ter as bibliotecas instaladas no seu computador  

Execute os comandos abaixo:

```
pip install -r requirements.txt
```

Neste ponto os módulos estão disponíveis de forma global

Exemplo:

```python

""" Template """

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