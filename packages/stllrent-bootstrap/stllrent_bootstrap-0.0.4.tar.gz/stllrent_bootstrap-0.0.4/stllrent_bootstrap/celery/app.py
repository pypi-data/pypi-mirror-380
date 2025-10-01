from celery import Celery
from typing import List, Optional
from stllrent_bootstrap.celery.bootsteps import SetupQueuesBootstep
import logging

log = logging.getLogger(__name__)

def create_celery_app(
    celery_settings: object,
    autodiscover_paths: Optional[List[str]] = None
) -> Celery:
    """
    Função Fábrica para criar e configurar uma instância do Celery App.

    Args:
        settings: O objeto de configuração já carregado (ex: celery_settings).
        autodiscover_paths: Lista de caminhos de importação onde as tarefas estão definidas.

    Returns:
        Uma instância configurada do aplicativo Celery.
    """
    # Passar 'include' no construtor é a forma mais robusta de garantir
    # que as tarefas sejam descobertas antes de qualquer outra operação.
    celery_app = Celery(
        celery_settings.APP_NAME
    )

    # Aplica a configuração do objeto de settings, incluindo broker e backend
    celery_app.conf.update(celery_settings.celery_config_dict)

    # Adiciona o bootstep para que os workers também garantam as filas ao iniciar
    celery_app.steps['worker'].add(SetupQueuesBootstep)

    # --- Declaração de Filas na Inicialização ---
    # Garante que as filas existam no broker antes que a aplicação tente usá-las.
    # Isso é crucial para o produtor (ex: app Flask).
    queues_to_declare = celery_app.conf.get('task_queues')
    if queues_to_declare:
        log.info(f"Declarando {len(queues_to_declare)} filas no broker...")
        try:
            with celery_app.connection_for_write() as conn:
                for queue in queues_to_declare:
                    log.debug(f"Declarando fila: {queue.name}")
                    queue.bind(conn).declare()
            log.info("Todas as filas foram declaradas com sucesso.")
        except Exception as e:
            log.error(f"Falha ao declarar filas no broker: {e}", exc_info=True)
            # Lançar a exceção impede que a aplicação inicie com uma configuração quebrada.
            raise

    # --- Descoberta de Tarefas ---
    # Força a descoberta e registro das tarefas. Isso é CRUCIAL para o produtor (Flask),
    # para que ele conheça as tarefas antes de tentar enviá-las.
    if autodiscover_paths:
        celery_app.autodiscover_tasks(autodiscover_paths)

    print("Instância unica Celery App configurada e gerada com sucesso.")
    print(celery_app.conf.humanize(with_defaults=False, censored=True))

    return celery_app