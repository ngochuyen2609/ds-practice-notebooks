# TÓM TẮT YÊU CẦU VÀ LUỒNG CRAWL

## YÊU CẦU NHANH

Hoàn thiện **5 vị trí #TODO** trong code:

| #   | Hàm                                         | Cần điền gì                                |
| --- | ------------------------------------------- | ------------------------------------------ |
| 1   | `get_content_enhanced()`                    | `get_content_(...)`                        |
| 2   | `get_content_enhanced()`                    | `get_content_with_curl(...)`               |
| 3   | `get_news_links_from_sub_topic_page_link()` | `soup.`                                    |
| 4   | `get_all_news_urls_from_topics_links()`     | `get_page_urls_from_sub_topic_url(...)`    |
| 5   | Main section                                | `get_all_news_urls_from_topics_links(...)` |

---

## LUỒNG CRAWL (ĐƠN GIẢN HÓA)

```
[1] CẤU HÌNH
    topics_links = {'khoa-hoc': ['https://vnexpress.net/khoa-hoc/phat-minh']}

[2] LẤY LINKS BÀI BÁO (TODO 5)
    topics_links_news = get_all_news_urls_from_topics_links(...)
                        ↓
                        ├─ For each topic:
                        │  ├─ (TODO 4) get_page_urls_from_sub_topic_url(...)
                        │  │  → ['url', 'url-p2', 'url-p3']
                        │  │
                        │  └─ For each page:
                        │     └─ get_news_links_from_sub_topic_page_link(...)
                        │        ├─ (TODO 1,2) get_content_enhanced(...)
                        │        └─ (TODO 3) soup.select(selector)
                        │        → ['article1.html', 'article2.html']
                        │
                        → {'khoa-hoc': ['article1.html', ...]}

[3] CRAWL NỘI DUNG
    For each link:
        ├─ get_content_enhanced(link)
        ├─ parse_article_from_html(html)
        ├─ Save raw: data/crawl_data/{topic}.txt
        └─ Save clean: data/news_vnexpress/{topic}/00001.txt

[4] THỐNG KÊ
    In kết quả, tạo ZIP
```

---

## CHECKLIST THỰC HIỆN

- [ ] **Bước 1**: Điền TODO 1,2 trong `get_content_enhanced()`
- [ ] **Bước 2**: Điền TODO 3 trong `get_news_links_from_sub_topic_page_link()`
- [ ] **Bước 3**: Điền TODO 4 trong `get_all_news_urls_from_topics_links()`
- [ ] **Bước 4**: Điền TODO 5 trong main section
- [ ] **Bước 5**: Chạy test cell để kiểm tra
- [ ] **Bước 6**: Chạy crawl chính nếu test OK
- [ ] **Bước 7**: Kiểm tra thư mục `data/` có dữ liệu

---
