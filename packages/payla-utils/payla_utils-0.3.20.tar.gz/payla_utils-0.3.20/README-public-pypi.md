# payla_utils python package

## Features

### Structlog config

#### Example, structlog configuration, django

in django settings.py

    from payla_utils.logging import LoggingConfigurator

    LoggingConfigurator(
        'testapp',
        log_level='INFO',
        own_apps=settings.OWN_APPS,
        setup_logging_dict=True,
    ).configure_structlog(formatter='plain_console')

#### Example, structlog configuration, passing extra loggers names

in django settings.py

    from payla_utils.logging import LoggingConfigurator

    LoggingConfigurator(
        'testapp',
        log_level='INFO',
        own_apps=settings.OWN_APPS,
        setup_logging_dict=True,
    ).configure_structlog(formatter='plain_console', extra_loggers_name=['mylogger1', 'mylogger2'])

#### If you want to use structlog in django celery

in celery.py

    from django.conf import settings
    from payla_utils.logging import LoggingConfigurator

    @signals.setup_logging.connect
    def receiver_setup_logging(
        loglevel, logfile, format, colorize, **kwargs
    ):  # pragma: no cover

        LoggingConfigurator(
            'testapp',
            log_level='INFO',
            own_apps=settings.OWN_APPS,
            setup_logging_dict=True,
        ).configure_structlog(formatter='plain_console')

#### If you want to use structlog with Sentry

You will have to set `PaylaLoggingIntegration` in sentry sdk setup

```python
sentry_sdk.init(
    # take sentry DSN from environment or add a default value here:
    dsn=env.str('SENTRY_DSN'),
    integrations=[DjangoIntegration(), CeleryIntegration(), PaylaLoggingIntegration()],
    auto_session_tracking=False,
    traces_sample_rate=0.01,
    send_default_pii=True,
    attach_stacktrace=True,
    request_bodies='medium',
    release=PROJECT_VERSION,
    environment=ENVIRONMENT,
)
```

### If you want to use a structlog, not Django based project

    from payla_utils.logging import LoggingConfigurator

    LoggingConfigurator(
        'testapp',
        log_level='INFO',
        own_apps=[],
        setup_logging_dict=True,
    ).configure_structlog(formatter='plain_console')

#### How to use generic structured logger:

    logger = structlog.get_logger(__name__)
    logger.warning("Here is your message", key_1="value_1", key_2="value_2", key_n="value_n")

#### Using request middleware to inject request_id and/or trace_id:

This middleware will inject reqest_id and/or trace_id to all logs producer during a request/response cycle.

    MIDDLEWARE += ['payla_utils.logging.middlewares.RequestMiddleware']

-   Pass your custom request id header via the PAYLA_UTILS settings: `REQUEST_ID_HEADER`, defaults to `X-Request-ID`
-   Enable tracing (Only supports opentelemetry) via `configure_structlog(tracing_enabled=True)`

[See configuration section](#Configuration-and-settings)

### Why structured logger

-   By default, the logging frameworks outputs the traces in plain text and tools like EFK stack or Grafana Loki can’t fully process these traces.
-   Therefore, if we “structure” or send the traces in JSON format directly, all the tools can benefit of.
-   As a developer, it would be nice to be able to filter all logs by a certain customer or transaction.
-   The goal of structured logging is to solve these sorts of problems and allow additional analytics.

-   When you log something, remember that the actual consumer is the machine Grafana Loki (EFK stack), not only humans.
-   Our generic logger comes with some default context structure, but as you can see, you can introduce new keys.
-   We use structlog as wraper on standard logging library, you can check for more details [structlog](https://www.structlog.org/en/stable/).

## Access decorator

To prohibit access to only internal IPs for a specific view it's possible to use the `only_internal_access` decorator.

SERVER_IP is required to be set on payla_utils settings.

[See configuration section](#Configuration-and-settings)

Example usage

```python
@only_internal_access
def test_view(request):
    return HttpResponse('OK')
```

Or inline

```python
path('test/', only_internal_access(test_view), name="test-view"),
```

## Management command to init environment

This management command will init environment based on the current env (local.dev, stage, playground and prod)

-   load fixtures on the first run (when the DB is empty)
-   setup custom theme for admin_interface
-   create user when not in prod if `LOCAL_DJANGO_ADMIN_PASSWORD` is set

APP_NAME and ENVIRONMENT settings are required. [See configuration section](#Configuration-and-settings)

## Configuration and settings

Settings for Payla Utils are all namespaced in the PAYLA_UTILS setting.
For example your project's `settings.py` file might look like this:

```python
PAYLA_UTILS = {
    'APP_NAME': 'My App',
    # Used for json logging
    'MICROSERVICE_NAME: 'myapp',
    # stage, playground, prod
    'ENVIRONMENT': ENVIRONMENT,
    'INITIAL_FIXTURES': [
        os.path.join(BASE_DIR, 'testapp', 'fixtures', 'users.json'),
    ],
    'SERVER_IP': '192.168.1.4',
    'REQUEST_ID_HEADER': 'X-Request-ID',
    'RUN_EXTRA_COMMANDS': ['loadinitialusers', 'setup_something'],
    'LOCAL_DJANGO_ADMIN_PASSWORD': os.environ.get('LOCAL_DJANGO_ADMIN_PASSWORD', 'admin'),
    # Only in case you need to change the defaults
    'ENV_THEMES': {
        'local.dev': {
            ...
        },
        'stage': {
            ...
        },
        'playground': {
            ...
        },
        'prod': {
            ...
        },
    }
}
```

## Payla Generic model

### Usage

    from payla_utils.models import PaylaModel

    class MyModel(PaylaModel):
        ...

This model will add the following fields:

-   `created_at` - datetime
-   `modified_at` - datetime

It has also a QuerySet that will add the following methods:

-   `get_or_none` - returns the object or None

# DRF view action permission

See full documentation [here](payla_utils/access/README.md)
