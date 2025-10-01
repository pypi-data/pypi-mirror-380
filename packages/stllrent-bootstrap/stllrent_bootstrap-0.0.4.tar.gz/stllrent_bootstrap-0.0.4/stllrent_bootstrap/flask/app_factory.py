from flask import Flask, request
from celery import Celery
from stllrent_bootstrap.flask.app_logger import get_logger, configure_logging
from stllrent_bootstrap.flask.app_settings import BaseAppSettings
from stllrent_bootstrap.exc import ProjectStandardException
from stllrent_bootstrap.database.discovery import load_project_models
from stllrent_bootstrap.database.manager import DatabaseManager
from stllrent_bootstrap.celery.base_task import BootstrapTask

def setup_blueprints(app:Flask):
    try:
        from route.api import register_blueprints # Importação específica do projeto
    except ModuleNotFoundError as mdf:
        raise ProjectStandardException(requirements="route/api.py with method register_blueprints is required")
    register_blueprints(app)


def create_app(settings: BaseAppSettings) -> Flask:
    configure_logging(settings)
    log = get_logger()
    log.debug("Configuring Flask aplication")
    app = Flask(settings.APP_NAME)
    
    app.config.from_object(settings)

    load_project_models(settings.MODEL_DISCOVERY_PATHS)
    db_manager = DatabaseManager(settings)
    app.extensions["db_manager"] = db_manager
    db_manager.setup_database(app)
    
    setup_blueprints(app) 
    
    app.after_request(after_request)
    return app

def configure_celery_for_flask(celery: Celery, app: Flask):
    """Configura a task do Celery para rodar dentro do contexto do app Flask."""
    log = get_logger()
    class FlaskTask(BootstrapTask):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return super().__call__(*args, **kwargs)
    
    celery.Task = FlaskTask

    try:
        # Acessa a URL do broker que o Celery *realmente* está usando para a conexão
        # current_broker é um objeto Kombu Connection, e tem um atributo transport.default_connection.hostname
        # ou url.
        broker_connection_url = celery.connection().as_uri()
        log.debug(f"DEBUG_CELERY_CONNECTION: Celery app connected to broker: {broker_connection_url}")
    except Exception as e:
        log.error(f"DEBUG_CELERY_CONNECTION: Erro ao obter URL de conexão do broker: {e}")

    celery.set_default()

def after_request(response):
    log = get_logger()
    log.info('%s %s %s %s %s', request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response