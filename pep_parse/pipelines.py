import csv
from datetime import datetime
from collections import defaultdict
from pathlib import Path

class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

        if hasattr(spider, 'FILES_STORE') and spider.FILES_STORE:
            self.results_dir = Path(spider.FILES_STORE)
        else:
            self.results_dir = Path('results')

        self.results_dir.mkdir(exist_ok=True, parents=True)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.statuses.values())
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = self.results_dir / f'status_summary_{timestamp}.csv'

        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in self.statuses.items():
                writer.writerow([status, count])
            writer.writerow(['Total', total])
