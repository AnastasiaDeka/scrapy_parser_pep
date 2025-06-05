from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_DIR = 'results'

SPIDER_NAME = 'pep'

BOT_NAME = 'pep_parse'

FEED_EXPORT_ENCODING = 'utf-8'
STATUS_SUMMARY_PATH = 'results/status_summary_%(time)s.csv'

FEEDS = {
    f'{RESULTS_DIR}/{SPIDER_NAME}_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}

PEP_DOMAIN = 'peps.python.org'

SPIDER_MODULES = [f'{BOT_NAME}.spiders']

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'

ROBOTSTXT_OBEY = True
