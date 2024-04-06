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

Exemplo de import:

```python

from reusable_code import log_to_file, make_browser, wait_for_conditions

```

