from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


def chrome(path = ""):
    """
    path = caminho da pasta raiz do projeto
    """
    if (path) == "":
         _service = Service(ChromeDriverManager().install())
    else:
        _service = Service(executable_path = path / 'files' / 'chromedriver.exe')
   
    
    _options = ChromeOptions()
    _options.add_experimental_option("detach", True)
    
    _navegador = webdriver.Chrome(service = _service, options = _options)
   
    return _navegador
