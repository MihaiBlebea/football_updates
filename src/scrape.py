from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy import signals

from spider import LiveScoreSpider
from store import store_live_results, get_all_results
from notify import trigger

results = []

def crawler_results(signal, sender, item, response, spider):
	results.append(item)

def scrape():
	dispatcher.connect(crawler_results, signal=signals.item_scraped)

	process = CrawlerProcess(settings={
		# "SPLASH_URL": "http://127.0.0.1:8050",
		# "DOWNLOADER_MIDDLEWARES": {
		# 	"scrapy_splash.SplashCookiesMiddleware": 723,
		# 	"scrapy_splash.SplashMiddleware": 725,
		# 	"scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
		# },
		# "SPIDER_MIDDLEWARES": {
		# 	"scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
		# },
		# "DUPEFILTER_CLASS": "scrapy_splash.SplashAwareDupeFilter",
		# "HTTPCACHE_STORAGE": "scrapy_splash.SplashAwareFSCacheStorage"
	})

	process.crawl(LiveScoreSpider)
	process.start()

	return results

if __name__ == "__main__":
	scrape()