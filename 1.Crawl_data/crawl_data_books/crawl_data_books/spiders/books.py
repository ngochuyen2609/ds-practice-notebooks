import scrapy
from crawl_data_books.items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        """
        Trang danh sách:
        - Lấy link sang trang chi tiết từng sách
        - Bắt nút 'next' để phân trang
        """
        # 1) link chi tiết
        for href in response.css("article.product_pod h3 a::attr(href)").getall():
            # response.follow tự xử lý URL tương đối -> tuyệt đối
            yield response.follow(href, callback=self.parse_detail)

        # 2) phân trang
        next_href = response.css("li.next a::attr(href)").get()
        if next_href:
            yield response.follow(next_href, callback=self.parse)

    def parse_detail(self, response):
        """
        Trang chi tiết:
        - Trộn CSS + XPath để bóc dữ liệu ổn định
        - Đổ vào BookItem (thô) -> Pipeline sẽ làm sạch
        """
        def get_spec(label):
            # Tìm ô td ngay sau cột th có text = label
            return response.xpath(
                f'//table//th[normalize-space()="{label}"]/following-sibling::td[1]/text()'
            ).get()

        item = BookItem()
        item["title"] = response.css("div.product_main h1::text").get()
        item["price_text"] = response.css("p.price_color::text").get()
        item["availability_text"] = " ".join(
            t.strip() for t in response.css("p.availability::text").getall()
        ).strip()
        item["upc"] = get_spec("UPC")
        item["category"] = response.css("ul.breadcrumb li:nth-last-child(2) a::text").get()
        item["url"] = response.url

        yield item
