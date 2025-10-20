BOT_NAME = "crawling"

SPIDER_MODULES = ["crawling.spiders"]
NEWSPIDER_MODULE = "crawling.spiders"

# ============= LỊCH SỰ & ỔN ĐỊNH =============
ROBOTSTXT_OBEY = True               # tôn trọng robots.txt
DOWNLOAD_DELAY = 1.0                # chậm lại cho an toàn
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1.0
AUTOTHROTTLE_MAX_DELAY = 10.0

# Tùy chọn: đặt user-agent tử tế (không để mặc định Scrapy)
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "huyenctn/0.1 (+https://; contact=huyen.ctn225015@sis.hust.edu.vn)"
}

# ============= XUẤT DỮ LIỆU =============
FEEDS = {
    "out/books.json": {"format": "json", "encoding": "utf8", "indent": 2},
    # Bật CSV nếu muốn:
    # "out/books.csv": {"format": "csv", "encoding": "utf8"},
}

# ============= PIPELINES =============
ITEM_PIPELINES = {
    "crawling.pipelines.CleanAndDedupePipeline": 300,
}

# ============= MIDDLEWARES (tùy chọn) =============
DOWNLOADER_MIDDLEWARES = {
    "crawling.middlewares.BasicHeaderMiddleware": 500,
    # có thể thêm proxy / rotate UA tại đây
}

# LOGLEVEL = "INFO"  # bật nếu muốn log gọn
