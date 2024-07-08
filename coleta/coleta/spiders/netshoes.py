import scrapy


class NetshoesSpider(scrapy.Spider):
    name = "netshoes"
    allowed_domains = ["www.netshoes.com.br"]
    start_urls = ["https://www.netshoes.com.br/tenis-performance/masculino?mi=hm_ger_mntop_H-CAL-tenis-performance"]

    def parse(self, response):
        pass
