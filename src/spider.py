from scrapy import Spider, Request
# from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header
from urllib.parse import urlparse
# from bs4 import BeautifulSoup


class LiveScoreSpider(Spider):

	name = "live_score"

	start_url = "https://www.goal.com/en-gb/live-scores"

	def start_requests(self):
		yield Request(self.start_url, callback=self.parse_live_update)

	def parse_live_update(self, response):
		for competition in response.css("div.competition-matches"):
			for match in competition.css("div.match-row__data"):
				yield {
					"league": competition.css("span.competition-name::text").get(),
					"status": match.css("span.match-row__state::text").get(),
					"match_time": match.css("span.match-row__date::text").get(),
					"teams": match.css("span.match-row__team-name::text").getall(),
					"score": match.css("b.match-row__goals::text").getall()
				}
