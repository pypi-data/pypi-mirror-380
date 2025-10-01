from stllrent_bootstrap.flask.app_settings import BaseAppSettings
from pydantic_settings import BaseSettings
import logging

# Variável no escopo do módulo para armazenar o nome do logger principal.
# Isso permite que get_logger() funcione fora do contexto da aplicação Flask,
# bem como durante a inicialização.
_LOGGER_NAME = None

def configure_logging(settings_instance: BaseSettings):
    """
    Configures the main application logger based on provided settings.
    This function should be called once at the application's startup.
    """
    global _LOGGER_NAME

    # Esta é a CHAVE: o logger será nomeado com o API_PRIMARY_PATH.
    app_logger_name = settings_instance.API_PRIMARY_PATH
    main_app_logger = logging.getLogger(app_logger_name)

    # Limpar handlers existentes no logger para evitar duplicação (importante!)
    if main_app_logger.handlers:
        for handler in list(main_app_logger.handlers):
            main_app_logger.removeHandler(handler)
            if hasattr(handler, 'close'): # Fechar o handler para liberar recursos
                handler.close()

    # Definir o nível global do logger com base nas configurações
    main_app_logger.setLevel(settings_instance.APP_LOG_LEVEL)
    main_app_logger.propagate = False # Evita que os logs sejam propagados para o logger root padrão

    # Armazena o nome do logger para que get_logger() possa usá-lo
    _LOGGER_NAME = app_logger_name

    # --- Configurar Formatters ---
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    # --- Configurar Handlers ---

    # 1. StreamHandler para o console (exibido em APMs e agregadores de logs)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(settings_instance.APP_LOG_LEVEL) # Nível do handler deve ser o mesmo do logger
    console_handler.setFormatter(console_formatter)
    main_app_logger.addHandler(console_handler)
    main_app_logger.info(f"'{app_logger_name}' application logger successfully configured. LEVEL: {settings_instance.APP_LOG_LEVEL}.")

    # Obtenha os loggers específicos do Requests/urllib3
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True # Importante para que a saída vá para o seu sistema de log

    urllib3_log = logging.getLogger("urllib3") # Em algumas versões, este também é relevante
    urllib3_log.setLevel(logging.DEBUG)
    urllib3_log.propagate = True

def get_logger():
    """ 
    Gera o logger ja configurado para esta aplicação 
    """
    if _LOGGER_NAME is None:
        # Fallback de segurança: se configure_logging não foi chamado,
        # retorna um logger padrão para evitar que a aplicação quebre.
        # Isso não deve acontecer no fluxo normal.
        logging.basicConfig()
        return logging.getLogger("stllrent_bootstrap.unconfigured")

    # Retorna a instância do logger usando o nome que foi definido em configure_logging.
    return logging.getLogger(_LOGGER_NAME)