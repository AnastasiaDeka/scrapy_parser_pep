from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_DIR = 'results'

BOT_NAME = 'pep_parse'

FEED_EXPORT_ENCODING = 'utf-8'

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}

PEP_DOMAIN = 'peps.python.org'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'

SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True
