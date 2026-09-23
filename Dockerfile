FROM alpine:latest

# نصب ابزارهای مورد نیاز
RUN apk update && apk add --no-cache curl unzip

# دانلود آخرین نسخه هسته v2ray
ADD https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip /tmp/v2ray.zip
RUN unzip /tmp/v2ray.zip -d /usr/bin/v2ray && rm /tmp/v2ray.zip

# کپی کردن فایل تنظیمات
COPY config.json /etc/v2ray/config.json

# باز کردن پورت ۳۰۰۰ (استاندارد برای پلتفرم‌های ابری)
EXPOSE 3000
CMD ["/usr/bin/v2ray/v2ray", "-config", "/etc/v2ray/config.json"]
