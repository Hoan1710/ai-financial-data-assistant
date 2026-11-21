# AI Financial Data Assistant

Bài tập lớn NLP về chuyển câu hỏi tiếng Việt thành truy vấn Pandas trên báo cáo tài chính của doanh nghiệp niêm yết Việt Nam. Phiên bản đầu tiên cung cấp cấu trúc dự án, các module khởi đầu và kiểm tra khả năng import. Các mốc triển khai API, giao diện, dữ liệu và mô hình nằm trong [kế hoạch của nhóm](Ke-hoach-Text-to-Pandas.md).

## Cài đặt cho phát triển trên Windows

Từ thư mục gốc của dự án, mở PowerShell và chạy với Python 3.10 trở lên.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest -q
```

## Phân công

| Thành viên | Phần phụ trách |
|---|---|
| Hoan | Hợp đồng dữ liệu, bộ thực thi Pandas, API và tích hợp |
| Đức | Trích xuất báo cáo, danh mục chỉ tiêu và snapshot |
| Hưng | Hiểu câu hỏi, baseline và dữ liệu ngôn ngữ |
| Hưởng | Sinh chương trình, prompt và fine-tune |
| Đức Anh | Bộ chấm, test đầu cuối và giao diện |

## Dữ liệu trong Git

Đưa cấu hình, từ điển, dữ liệu mẫu được phép chia sẻ và manifest vào Git. Các thư mục `data/raw/`, `data/processed/` và `artifacts/` dành cho dữ liệu cục bộ và sản phẩm sinh ra khi chạy. Các tập train/dev hiện là tệp rỗng để nhóm bắt đầu gán nhãn.
