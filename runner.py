from scrapy.crawler import CrawlerProcess
from scraper import ScraperSpider
from process_data import prepare_data

process = CrawlerProcess(
    settings={
        "FEEDS": {
            "raw_data.csv": {"format": "csv"},
        },
        'USER_AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240",
        "DOWNLOAD_DELAY": 10,
        "CONCURRENT_REQUESTS": 1,
        'HTTPCACHE_ENABLED': True,
        'LOG_FILE': "scrap-log.txt"
    }
)
process.crawl(ScraperSpider)
process.start()
prepare_data()
