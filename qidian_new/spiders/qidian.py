# from scrapy.spider import BaseSpider
import scrapy

from ..items import QidianNewItem

class QidianSpider(scrapy.Spider):
    name = "xuanhuan"
    allowed_domains = ["qidian.com"]
    start_urls = [
            "https://www.qidian.com/xuanhuan"
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        open(page, 'wb').write(response.body)

#        books = response.css('div.left-wrap').css('ul').css('li')

        # Find the list of new books
        new_books = response.css('div.new-book-wrap').css('li')

        result = []
        for book in new_books:
            title_tmp = book.css('h4').css('a').re(r'">(.*?)<')
            author_tmp = book.css('a.author').re(r'g\">(.*?)</a>')
            if title_tmp and author_tmp:
                item = QidianNewItem()
                item['title'] = title_tmp
                item['author'] = author_tmp
                result.append(item)
        return result
