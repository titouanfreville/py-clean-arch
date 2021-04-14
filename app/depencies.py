from dependency_injector import containers, providers


class Dependencies(containers.DeclarativeContainer):
    """Manage project dependecie in a single place."""

    config = providers.Configuration()
