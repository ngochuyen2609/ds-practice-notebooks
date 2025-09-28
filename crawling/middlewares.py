from scrapy import signals

class BasicHeaderMiddleware:
    """
    Thêm vài header 'lịch sự'. Không bắt buộc, nhưng giúp bạn kiểm soát dấu vết request.
    Bật trong settings: DOWNLOADER_MIDDLEWARES.
    """
    def process_request(self, request, spider):
        request.headers.setdefault(b"Accept-Language", b"en-US,en;q=0.8")
        return None


class CrawlingSpiderMiddleware:
    """
    GIỮ MẶC ĐỊNH. Đặt đây để bạn thấy khung chuẩn Scrapy.
    """
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s", spider.name)
