# Module 3: Creating AI Application and Deploy using Flask

> **Tư tưởng cốt lõi:** Dự án cuối khóa kết hợp toàn bộ kỹ năng Python packaging, unit testing, static code analysis (PyLint) và **Flask** để tích hợp **IBM Watson Embedded AI Libraries** (NLP phân tích cảm xúc / cảm nhận văn bản) thành một ứng dụng web AI hoàn chỉnh có xử lý lỗi đầu vào chặt chẽ.

## 1. Kiến trúc ứng dụng AI với IBM Watson Embedded AI Libraries

Trong môi trường Cloud IDE, các thư viện AI nhúng của **IBM Watson** cung cấp sẵn các mô hình xử lý ngôn ngữ tự nhiên (**NLP** — Natural Language Processing) và giọng nói (**Speech**) mà không cần tự huấn luyện mô hình từ đầu. Ở hai dự án thực hành & cuối khóa (Sentiment Analysis / Emotion Detection), kiến trúc hệ thống gồm 2 lớp rõ rệt:

| Lớp hệ thống | Thành phần | Trách nhiệm chính |
| --- | --- | --- |
| **AI Package (`EmotionDetection/`)** | `emotion_detection.py` + `__init__.py` | Gọi Watson NLP REST API qua `requests.post()`, parse kết quả JSON, trích xuất điểm số các cảm xúc và xác định `dominant_emotion`, trả giá trị `None` khi lỗi `400` |
| **Web Server (`server.py`)** | Flask App (`@app.route`) + `templates/` + `static/` | Phục vụ giao diện HTML/JS (`render_template("index.html")`), tiếp nhận văn bản qua route `/emotionDetector`, xử lý ngoại lệ input rỗng và trả chuỗi/JSON phản hồi |
| **Quality Assurance** | `test_emotion_detection.py` + `pylint` | Kiểm thử đơn vị bằng `unittest` trực tiếp trên package và kiểm tra tuân thủ PEP 8 đạt chuẩn sạch |

## 2. Quy trình 6 bước chuẩn hóa dự án AI với Flask

Cả dự án thực hành (Practice Project) và dự án tốt nghiệp (Final Project) đều tuân theo **đúng 6 bước kỹ thuật**:

1. **Tạo hàm AI lõi (Create AI function):** Viết hàm gọi dịch vụ Watson NLP (gửi `POST` kèm header `grpc-metadata-mm-model-id` và JSON payload `{ "raw_document": { "text": text_to_analyze } }`).
2. **Đóng gói thành Python Package (Package the function):** Tạo thư mục package chứa module AI và tệp **`__init__.py`** tham chiếu module đó.
3. **Kiểm thử đơn vị (Run Unit Testing):** Viết `unittest.TestCase` import hàm trực tiếp từ package để xác minh đầu ra trên các câu mẫu đại diện cho từng nhãn cảm xúc (`joy`, `anger`, `disgust`, `sadness`, `fear`).
4. **Triển khai Web App bằng Flask (Deploy using Flask):** Kết nối package vào `server.py`, render trang chủ từ `templates/index.html` và mở endpoint xử lý truy vấn từ giao diện JS.
5. **Tích hợp Xử lý lỗi (Error Handling):** Kiểm tra `response.status_code == 400` (input rỗng / không hợp lệ) để trả dictionary chứa các giá trị `None`, từ đó server Flask trả thông báo thân thiện (`"Invalid text! Please try again!"`) thay vì crash `KeyError`/`500`.
6. **Phân tích mã tĩnh (Static Code Analysis):** Chạy `pylint` cho cả module AI và `server.py` (thêm docstring, loại bỏ import thừa, chuẩn hóa khoảng trắng/dòng kết thúc tệp) để đạt điểm chất lượng cao (mục tiêu 10/10).

## 3. Triển khai chi tiết Package AI & Flask Server

### A. Module phân tích cảm xúc (`EmotionDetection/emotion_detection.py` & `__init__.py`)

```python
# EmotionDetection/emotion_detection.py
import json
import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """Call Watson NLP EmotionPredict API and return emotion scores + dominant emotion."""
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(WATSON_URL, json=payload, headers=HEADERS, timeout=10)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted = json.loads(response.text)
    emotions = formatted["emotionPredictions"][0]["emotion"]
    dominant = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant
    return emotions
```

```python
# EmotionDetection/__init__.py
from . import emotion_detection
```

### B. Kiểm thử đơn vị (`test_emotion_detection.py`)

```python
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for text, expected in cases:
            result = emotion_detector(text)
            self.assertEqual(result["dominant_emotion"], expected)

if __name__ == "__main__":
    unittest.main()
```

### C. Triển khai Flask Server (`server.py`) & Kiểm tra PyLint

```python
"""Flask web server for Emotion Detection using Watson NLP."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the main HTML interface."""
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    """Analyze textToAnalyze query parameter and return formatted emotion summary."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

```bash
# Kiểm thử unit test & đánh giá tĩnh PEP 8 với PyLint
python3 test_emotion_detection.py
pylint server.py EmotionDetection/emotion_detection.py
```

## 4. Bẫy thường gặp & Lưu ý thực chiến (Critical Pitfalls)

1. **Không xử lý `status_code == 400` khi input rỗng:** Khi người dùng gửi chuỗi trống, Watson API trả mã `400` không có key `emotionPredictions`; truy cập trực tiếp `formatted["emotionPredictions"]` sẽ gây `KeyError` và sập server với lỗi `500`.
2. **Đặt nhầm tên package hoặc thiếu `EmotionDetection/__init__.py`:** Nếu thiếu `__init__.py`, Python không coi thư mục là package hợp lệ khi import từ `server.py` hay `test_emotion_detection.py`.
3. **Bị trừ điểm PyLint vì thiếu Docstring & Newline cuối file:** PyLint kiểm tra rất kỹ module docstring (`C0114`), function docstring (`C0116`), độ dài dòng (`<= 100`), và dòng trống kết thúc tệp (`C0304`).
4. **Hardcode địa chỉ `127.0.0.1` trong môi trường Cloud IDE / Container:** Khi chạy `app.run(host="0.0.0.0", port=5000)`, server mới mở kết nối ra bên ngoài container để trình duyệt Cloud IDE truy cập được.
5. **Chạy unit test trước khi hoàn thiện hàm xử lý ngoại lệ:** Luôn test cả nhánh hợp lệ lẫn nhánh input rỗng/lỗi để chắc chắn hợp đồng dữ liệu (`dominant_emotion is None`) đồng nhất giữa package và Flask route.

## 5. Điểm cốt lõi cần nhớ (Key Takeaways)

- **IBM Watson Embedded AI Libraries** cung cấp sẵn năng lực NLP & Speech ngay trong Cloud IDE để nhúng nhanh vào ứng dụng Python.
- Quy trình phát triển chuẩn gồm **6 bước**: Viết hàm AI → Đóng gói thành **Package** (`__init__.py`) → **Unit Test** (`unittest`) → Triển khai web qua **Flask** → **Error Handling** (`400`/empty input) → **Static Code Analysis** (`pylint`).
- Sự kết hợp giữa **Package tách biệt logic AI** + **Flask web layer** + **Unit Test & PyLint** tạo nên ứng dụng AI sạch, dễ mở rộng và sẵn sàng triển khai thực tế.
