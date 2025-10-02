# QuickConn

QuickConn هي مكتبة بايثون موحدة لدعم جميع أنواع الـ HTTP: HTTP/1.0، HTTP/1.1، HTTP/2، HTTP/3، مع دعم تجاوز حماية **Cloudflare**.

---

## 📦 التثبيت

يمكنك تثبيت المكتبة مباشرة من PyPI (بعد رفعها) أو من ملف setup.py محليًا:

### التثبيت من PyPI

```bash
pip install QuickConn
```

### التثبيت محليًا من المشروع

```bash
git clone https://github.com/Gisnsl/QuickConn.git
cd QuickConn
pip install .
```

---

## ⚡ الاستخدام

### استيراد المكتبة

```python
from QuickConn import Http1Client, Http2Client, Http3Client, Http10Client, CloudFlareSolver
```

---

### 🔹 HTTP/1.0 Client

```python
response = Http10Client.get("http://httpbin.org/get", headers={"User-Agent": "MyClient"})
print(response.status_code)
print(response.text)
print(response.json())
print(response.headers)
print(response.cookies)
```

---

### 🔹 HTTP/1.1 Client

```python
response = Http1Client.get(
    "https://httpbin.org/get",
    headers={"User-Agent": "MyClient"},
    params={"test": "123"},
    proxy={"http": "http://user:pass@host:port"},
    data=None,
    json={"key": "value"},
    file="path/to/file.txt"
)
print(response.status_code)
print(response.text)
```

---

### 🔹 HTTP/2 Client

```python
response = Http2Client.get(
    "https://httpbin.org/get",
    headers={"User-Agent": "MyClient"},
    params={"foo": "bar"},
    proxy={"http": "http://user:pass@host:port"},
    data=None,
    json={"hello": "world"},
    file="path/to/file.txt"
)
print(response.status_code)
print(response.text)
print(response.json())
print(response.headers)
```

---

### 🔹 HTTP/3 Client

> **ملاحظة:** HTTP/3 يعمل بشكل **غير متزامن** داخليًا، لكن يمكن استخدامه مباشرة بدون إنشاء كائن:

```python
response = Http3Client.get(
    "https://httpbin.org/get",
    headers={"User-Agent": "MyClient"},
    params={"foo": "bar"},
    data=None,
    json={"key": "value"},
    files="path/to/file.txt"
)
print(response.status_code)
print(response.text)
print(response.headers)
```

---

### 🔹 Cloudflare Solver

```python
response = CloudFlareSolver.get(
    "https://example-protected-site.com",
    headers={"User-Agent": "MyClient"}
)
print(response.status_code)
print(response.text)
```

---

## ⚙️ خيارات شائعة

* **headers**: إرسال رؤوس HTTP إضافية
* **params**: إرسال Query Parameters
* **data**: إرسال بيانات POST/PUT
* **json**: إرسال بيانات JSON
* **file / files**: رفع ملفات
* **proxy**: دعم البروكسي بصيغة `{"http": "http://user:pass@host:port"}`
* **verify**: تعطيل التحقق من SSL (HTTP/1.0 و HTTP/1.1)

---

## 📄 الترخيص

MIT License – يمكن استخدام المكتبة وتعديلها بحرية.
