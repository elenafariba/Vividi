const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = process.env.PORT || 3000;

// یک صفحه وب ساده برای رد گم کنی
app.get('/', (req, res) => {
  res.send('App is running smoothly!');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
  
  // دستور اجرای هسته VLESS شما در پس‌زمینه
  // اگر از Xray یا فایل اجرایی خاصی استفاده می‌کنید، نام آن را اینجا جایگزین کنید
  exec('chmod +x ./your-core-file && ./your-core-file -c config.json', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
  });
});
