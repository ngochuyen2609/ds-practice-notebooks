# XPath là gì?
- XPath (XML Path Language) là “ngôn ngữ chỉ đường” để chọn phần tử/text trong cây HTML/XML.
- Nó duyệt theo cấu trúc cây (cha–con–anh–em), rất mạnh khi cần nhảy lên/xuống/ngang giữa các node hoặc tìm theo điều kiện.

# Scrapy dùng để làm gì?
- Scrapy là framework Python để crawl/scrape web ở quy mô lớn:
- Tự quản lý hàng đợi URL (follow link, phân trang).
- Cung cấp Spiders (logic thu thập), Requests/Responses (HTTP), Pipelines (làm sạch/lưu dữ liệu), Middlewares (headers, proxy, retry).
- Hỗ trợ robots.txt, delay/throttle, khử trùng lặp URL, export JSON/CSV/Parquet.
- Mở rộng dễ: dùng XPath/CSS để bóc tách, thêm Playwright/Splash nếu trang render bằng JavaScript.

- Quy trình chuẩn với Scrapy
    -Start URLs: điểm vào (trang danh sách).
    -parse(): lấy link từng item → yield response.follow(...) sang parse_detail.
    - parse_detail(): trích dữ liệu (CSS/XPath) → yield {...}.
    - Pipelines (tuỳ chọn): làm sạch (ví dụ chuyển giá “£51.77” → 51.77) rồi lưu.
    - Cấu hình lịch sự: ROBOTSTXT_OBEY=True, DOWNLOAD_DELAY, AUTOTHROTTLE_ENABLED=True.

# Guideline to running code
- Step 1: Set up virtal environment and necessary library
    >> python -m venv .venv  
    >> .\.venv\Scripts\activate.bat  
    >>  .\.venv\Scripts\python.exe -m pip install --upgrade pip   
    >> pip install -r requirements.txt  
- Step 2: Set up Scrapy and start project
    >>  .\.venv\Scripts\python.exe -m scrapy startproject crawling
    >> .\.venv\Scripts\python.exe -m scrapy list             => books
    >>  .\.venv\Scripts\python.exe -m scrapy crawl books -O out/books.json
    