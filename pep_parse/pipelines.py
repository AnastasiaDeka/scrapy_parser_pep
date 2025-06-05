import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

from settings import BASE_DIR, RESULTS_DIR, STATUS_SUMMARY_PATH


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        status_summary = [('Статус', 'Количество')]
        status_summary.extend(self.statuses.items())
        status_summary.append(('Total', sum(self.statuses.values())))

        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_rel_path = STATUS_SUMMARY_PATH % {'time': timestamp}
        filename = BASE_DIR / Path(file_rel_path)
        filename.parent.mkdir(parents=True, exist_ok=True)

        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(status_summary)
