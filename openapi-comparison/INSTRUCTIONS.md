# So sánh: OpenAPI, API Blueprint, RAML, và TypeSec.

## 1. Mục đích

Mục tiêu của bài tập này là:

* Hiểu và so sánh các chuẩn tài liệu hóa API phổ biến:

  * OpenAPI
  * API Blueprint
  * RAML
  * TypeSpec
* Thực hành viết tài liệu API cho cùng một hệ thống (Library Management)
* Demo khả năng sinh code và test từ tài liệu API

---

## 2. Yêu cầu

### 2.1. Cấu trúc project

Tạo thư mục:

```
openapi-comparison/
  0_OpenAPI/
  1_APIBlueprint/
  2_RAML/
  3_TypeSpec/
```

Mỗi thư mục phải chứa:

* File định nghĩa API
* File README.md hướng dẫn chạy

---

### 2.2. Nội dung API

Xây dựng API cho hệ thống quản lý thư viện với các chức năng:

* GET /books
* POST /books
* GET /books/{id}
* PUT /books/{id}
* DELETE /books/{id}

Dữ liệu Book gồm:

* id
* title
* author
* publishYear

---

### 2.3. Demo yêu cầu

* Render documentation cho từng format
* Với OpenAPI: phải có khả năng gọi API (interactive)
* Demo sinh code từ OpenAPI hoặc TypeSpec
* Demo test API (Swagger UI hoặc Postman)