import os
import uuid
import json
import subprocess

# ایجاد یک UUID تصادفی به صورت اتوماتیک
user_id = str(uuid.uuid4())
port = 3000

# ساخت فایل تنظیمات به صورت خودکار
config = {
    "log": {"loglevel": "warning"},
    "inbounds": [{
        "port": port,
        "protocol": "vless",
        "settings": {
            "clients": [{"id": user_id}],
            "decryption": "none"
        },
        "streamSettings": {
            "network": "tcp",
            "security": "none"
        }
    }],
    "outbounds": [{"protocol": "freedom"}]
}

with open("/etc/xray_config.json", "w") as f:
    json.dump(config, f, indent=4)

print("="*60)
print("🚀 VLESS Server Started Successfully!")
print(f"👉 Generated UUID: {user_id}")
print("="*60)

# اجرای هسته پروکسی
subprocess.run(["xray", "-config", "/etc/xray_config.json"])
