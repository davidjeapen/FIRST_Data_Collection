import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://docs.legis.wisconsin.gov/2023/legislators/assembly#B",
    ]

    def parse(self, response):
        save_file = open('data.csv', 'w')
        for data in response.css("span.info"):
            name = data.xpath("span/strong/a/text()").get()
            district = None
            if name is not None:
                print(name)
                district = data.xpath("span/small/text()")[1].get()
            if district is not None:
                print(district)
                # print(data.xpath("span/small/text()")[1].get())
                # yield {
                #     "name": data.xpath("span/strong/a/text()").get(),
                #     "district": data.xpath("span/small/text()")[1].get()
                # }
        # for quote in response.css("div.quote"):
        #     yield {
        #         "author": quote.xpath("span/small/text()").get(),
        #         "text": quote.css("span.text::text").get(),
        #     }

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)