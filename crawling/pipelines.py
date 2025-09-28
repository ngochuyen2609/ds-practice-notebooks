import re
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class CleanAndDedupePipeline:
    """
    - Làm sạch giá (price_text -> price float), availability_text -> in_stock bool.
    - Khử trùng lặp theo UPC (nhiều site có ID riêng; với BooksToScrape UPC là duy nhất).
    """

    def open_spider(self, spider):
        self.seen_upc = set()

    def process_item(self, item, spider):
        ad = ItemAdapter(item)

        # --- Parse price ---
        price_text = (ad.get("price_text") or "").replace(",", "")
        m = re.search(r"([0-9]+(?:\.[0-9]+)?)", price_text)
        if m:
            ad["price"] = float(m.group(1))

        # --- Parse availability ---
        avail = (ad.get("availability_text") or "").lower()
        ad["in_stock"] = "in stock" in avail

        # --- Dedupe by UPC (nếu có) ---
        upc = ad.get("upc")
        if upc:
            if upc in self.seen_upc:
                raise DropItem(f"Duplicate UPC: {upc}")
            self.seen_upc.add(upc)

        return item
