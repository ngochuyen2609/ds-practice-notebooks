import scrapy

class BookItem(scrapy.Item):
    # Trường thô bóc từ HTML
    title = scrapy.Field()
    price_text = scrapy.Field()         # ví dụ: "£51.77"
    availability_text = scrapy.Field()  # ví dụ: "In stock (22 available)"
    upc = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()

    # Trường đã làm sạch trong Pipeline
    price = scrapy.Field()      # float, ví dụ: 51.77
    in_stock = scrapy.Field()   # bool
