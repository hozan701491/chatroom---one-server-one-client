
این پروژه یک نمونه ساده از ارتباط بین کلاینت و سرور با استفاده از سوکت در زبان پایتون است. هدف آن پیاده‌سازی پایه‌ای از مفاهیم socket programming است که شامل ارتباط TCP، ارسال و دریافت پیام، و مدیریت اتصال‌ها می‌باشد.

 ویژگی‌ها
ارتباط TCP بین کلاینت و سرور

ارسال پیام از کلاینت به سرور و بالعکس

پاسخ‌دهی سرور به هر پیامی که از کلاینت دریافت می‌شود

مدیریت قطع اتصال از سوی کلاینت

 ساختار پروژه
پروژه شامل دو فایل اصلی است:

✅ server.py
کدی که یک سرور ایجاد می‌کند و منتظر اتصال کلاینت می‌ماند. پس از اتصال، پیام‌ها را دریافت کرده و پاسخ می‌دهد.

✅ client.py
کدی که به سرور متصل می‌شود و یک پیام ارسال می‌کند، سپس پاسخ سرور را دریافت و نمایش می‌دهد.

 نحوه اجرا
1. اجرای سرور
ابتدا فایل سرور را اجرا کنید:

python server.py
اگر همه چیز درست باشد، خروجی چیزی شبیه زیر خواهد بود:


server is listening on 127.0.0.1 : 1234
2. اجرای کلاینت
در ترمینالی دیگر، فایل کلاینت را اجرا کنید:


python client.py
خروجی کلاینت ممکن است به شکل زیر باشد:


The client is connected to server 127.0.0.1:1234
server answer: hello client!!!
connection is closed
و در ترمینال سرور هم پاسخ‌هایی مانند این را خواهید دید:


accepted a new connection from ('127.0.0.1', 59736)
client answer: hello server!
connection with ('127.0.0.1', 59736) closed!
The server is shut down!!
 نکات
ارتباط TCP فقط بین کلاینت و سرور محلی (localhost) انجام می‌شود.

بعد از هر اتصال و پاسخ، سرور بسته می‌شود (می‌توانید این رفتار را تغییر دهید تا چندین کلاینت همزمان را مدیریت کند).

استفاده از try-except برای مدیریت قطع اتصال ناگهانی انجام شده است.













