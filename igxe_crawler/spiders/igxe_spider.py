import scrapy

class IgxeSpider(scrapy.Spider):
    name = "igxe"

    def start_requests(self):
        urls = [
                'https://www.igxe.cn/product/730/613857',
                'http://quotes.toscrape.com/page/2/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'web-page-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
