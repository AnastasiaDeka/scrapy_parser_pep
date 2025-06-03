import csv
from datetime import datetime
from collections import defaultdict
from pathlib import Path


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

        feeds = spider.crawler.settings.get('FEEDS')
        if feeds:
            feed_path = next(iter(feeds))
            self.results_dir = Path(feed_path).parent
        else:
            self.results_dir = Path('results')

        self.results_dir.mkdir(parents=True, exist_ok=True)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.statuses.values())
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = self.results_dir / f'status_summary_{timestamp}.csv'

        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in self.statuses.items():
                writer.writerow([status, count])
            writer.writerow(['Total', total])
