# AI Financial Data Assistant | Kế hoạch làm việc trong 4 tuần

**Người dùng đầu tiên** là người chuẩn bị bản tin doanh nghiệp cho câu lạc bộ đầu tư hoặc một nhóm nghiên cứu. Trước buổi họp, họ cần biết công ty nào đáng đọc kỹ báo cáo, con số nào dẫn đến nhận xét đó và trang nào dùng để kiểm tra. Sản phẩm của nhóm giúp họ hoàn thành việc này từ một câu hỏi tiếng Việt đến một phiếu so sánh có thể gửi cho người khác.

## 1. Một buổi làm việc với sản phẩm

| Người dùng làm gì? | Ứng dụng cần làm được gì? |
|---|---|
| Chọn danh sách theo dõi, chẳng hạn MWG và FRT. Hỏi “Năm 2025, công ty nào có lãi sau thuế nhưng tiền từ hoạt động kinh doanh lại âm?” | Đọc đủ hai chỉ tiêu cho từng mã. Trả bảng các mã phù hợp với số lãi và số tiền tương ứng. Cho biết đã kiểm tra được bao nhiêu mã. Nếu không mã nào phù hợp, nói rõ điều đó. |
| Bấm “Xem số gốc” ở một dòng. | Mở đúng báo cáo, chỉ trang, tên dòng, cột năm và đơn vị. Nếu kết quả cần hai số thì xem được cả hai nguồn. |
| Hỏi tiếp “Còn năm 2024 thì sao?” | Giữ danh sách và điều kiện vừa chọn, đổi năm thành 2024. Trên màn hình hiện rõ ứng dụng đang xét mã nào, năm nào. |
| Chọn “Xuất phiếu” để dùng trong buổi họp. | Tải một phiếu mở được bằng trình duyệt, có câu hỏi, bảng, nhận xét ngắn, nguồn, ngày xuất và bản dữ liệu. Người nhận có thể đọc phiếu khi chưa cài ứng dụng. |

**Ví dụ để cả nhóm tính thử.** Dưới đây là số minh họa của công ty A, đơn vị tỷ đồng. Chúng dùng để thử công thức và cách viết nhận xét.

| Chỉ tiêu | 2024 | 2025 |
|---|---:|---:|
| Doanh thu thuần | 100 | 120 |
| Lợi nhuận gộp | 25 | 24 |
| Lợi nhuận sau thuế | 8 | 9 |
| Tiền thuần từ hoạt động kinh doanh | 6 | −3 |

Phiếu có thể viết “Doanh thu tăng 20%. Năm trước, cứ 100 đồng doanh thu thì còn 25 đồng lãi gộp. Năm nay còn 20 đồng, giảm 5 điểm phần trăm. Công ty vẫn lãi sau thuế 9 tỷ đồng, trong khi tiền từ hoạt động kinh doanh là −3 tỷ đồng.” Người đọc có đủ số để kiểm lại và biết cần mở phần lưu chuyển tiền tệ trong báo cáo. Nguyên nhân biến động cần được kiểm tra riêng.

## 2. Trong bốn tuần, nhóm xây đến đâu?

| Làm được khi bàn giao | Giới hạn để hoàn thành đúng hạn |
|---|---|
| Hỏi số tiền, so hai mã, tính mức tăng/giảm, xếp hạng trong danh sách đã chọn | Dùng báo cáo hợp nhất theo năm và bốn chỉ tiêu trong bảng ví dụ. Tính bằng Pandas, công cụ Python dùng để lọc và tính trên bảng. |
| Tìm doanh nghiệp cần đọc kỹ | Hai điều kiện có thể kiểm lại: (1) lãi sau thuế dương nhưng tiền từ hoạt động kinh doanh âm trong cùng năm, (2) doanh thu tăng nhưng tỷ lệ lãi gộp trên doanh thu giảm so với năm trước. Bảng hiển thị các số tạo ra từng nhận xét. |
| Hỏi nối tiếp | Nhớ lần hỏi vừa trả lời cho hai thao tác “đổi năm” và “thêm mã”. Khi bắt đầu lượt tra cứu mới, người dùng có thể xóa lựa chọn cũ. |
| Xuất và kiểm lại kết quả | Một phiếu HTML, tức một tệp mở trực tiếp bằng trình duyệt. Bảng và nhận xét đọc được khi ngắt mạng. Link báo cáo trực tuyến dùng khi có mạng. |
| Cập nhật số liệu sau buổi họp | Đức thêm số liệu vào một bản dữ liệu mới. Câu hỏi chạy lại dùng bản mới, phiếu đã xuất vẫn ghi số và nguồn của lần xuất cũ. |

**Phạm vi dữ liệu đề xuất.** Đức khảo sát MWG, FRT, PNJ và DGW trong các năm 2023–2025. Bốn mã × ba năm × bốn chỉ tiêu tạo thành **48 vị trí cần kiểm tra**. Tuần 1 bắt đầu với hai mã và hai năm, tương ứng 16 vị trí. Đức chốt danh sách sau khi tìm được nguồn. Khi xếp hạng, giao diện ghi “trong các mã đã chọn” vì các doanh nghiệp có thể khác nhau về quy mô và hoạt động.

## 3. Mỗi phần có một người chịu trách nhiệm

| Người | Phần được sửa | Đầu ra mà người tiếp theo cần | Tài liệu riêng |
|---|---|---|---|
| Trịnh Minh Đức · 24022298 | `data/` | Bảng số liệu và bảng chỉ vị trí nguồn. Hoan dùng để tính, Đức Anh dùng để đối chiếu. | [Việc của Đức](docs/trinh-minh-duc.md) |
| Nguyễn Tiến Hưởng · 24022352 | `src/hieu_cau/` | Đọc câu hỏi và lượt hỏi trước, gửi cho Hoan một yêu cầu ghi rõ mã, chỉ tiêu, kỳ và phép cần làm. | [Việc của Hưởng](docs/nguyen-tien-huong.md) |
| Nguyễn Tiến Hoan · 24022334 | `src/tinh_so/`, `AGENTS.md` và các tệp cài/chạy chung ở gốc khi triển khai | Dùng Pandas tính một lần, trả cùng kết quả và nguồn cho màn hình lẫn phiếu. Chịu trách nhiệm ghép các phần. | [Việc của Hoan](docs/nguyen-tien-hoan.md) |
| Đỗ Duy Hưng · 24022346 | `src/phieu/`, `ban_nop/` | Viết nhận xét từ các số Hoan trả, làm phiếu tải xuống, ghép báo cáo và slide từ phần từng bạn gửi. | [Việc của Hưng](docs/do-duy-hung.md) |
| Lê Đức Anh · 24022250 | `app/`, `danh_gia/` | Làm nơi chọn mã, hỏi, xem nguồn và tải phiếu. Tổ chức dùng thử, ghi thời gian và chấm câu trả lời độc lập. | [Việc của Đức Anh](docs/le-duc-anh.md) |

Trong `docs/`, mỗi thành viên sửa đúng tệp mang tên mình. Ví dụ, Đức Anh phụ trách **nút tải** và Hưng phụ trách **nội dung tệp tải xuống**. Nếu trên phiếu ghi đúng 20% nhưng màn hình ghi 0,2%, Đức Anh sửa cách hiển thị. Nếu số Hoan gửi tới cả hai nơi đều sai thì Hoan sửa phép tính.

## 4. Cấu trúc thư mục

Các thư mục làm việc đã được tạo. Cây dưới ghi cả những tệp **dự kiến viết trong bốn tuần** để mỗi người biết nên đặt việc của mình ở đâu. Hiện có kế hoạch và khung thư mục. Những tên tệp triển khai bên dưới là gợi ý cho nhóm.

```text
ai-financial-data-assistant/
├── AGENTS.md
├── docs/
│   ├── trinh-minh-duc.md
│   ├── nguyen-tien-huong.md
│   ├── nguyen-tien-hoan.md
│   ├── do-duy-hung.md
│   └── le-duc-anh.md
├── data/                        # Đức
│   ├── danh_muc.csv             # Mã công ty và tên chỉ tiêu
│   ├── v1/                      # Mỗi bản đã giao có thư mục riêng
│   │   ├── so_lieu.csv          # Một dòng cho một mã, năm và chỉ tiêu
│   │   └── nguon.csv            # Tài liệu, trang, dòng, cột, đơn vị
│   └── lich_su_cap_nhat.md
├── src/
│   ├── hieu_cau/                # Hưởng
│   │   ├── doc_cau_hoi.py
│   │   └── cau_thu.csv          # Câu công khai và cách hiểu mong đợi
│   ├── tinh_so/                 # Hoan
│   │   ├── mau_ban_giao.md      # Hình dạng và ý nghĩa kết quả dùng chung
│   │   ├── phep_tinh.py
│   │   └── tra_loi.py           # Nối câu hỏi với dữ liệu, phép tính và nguồn
│   └── phieu/                   # Hưng
│       ├── loi_nhan_xet.py
│       └── mau_phieu.html
├── app/                         # Đức Anh
│   └── man_hinh.py
├── danh_gia/                    # Đức Anh
│   ├── cach_cham.md
│   └── ket_qua.csv              # Công bố kết quả sau lượt chấm cuối
└── ban_nop/                     # Hưng tổng hợp
    ├── huong_dan.md
    ├── bao_cao.md
    └── slide.pdf
```

## 5. Bàn giao sớm để năm người làm việc cùng lúc

Cuối **buổi 2 của tuần 1**, mỗi người phải có thứ để bắt đầu, kể cả khi một phần khác vẫn đang làm. Dùng bảng công ty A ở mục 1 khi chưa đủ báo cáo thật.

| Ai giao cho ai? | Ví dụ bàn giao | Người nhận kiểm tra thế nào? |
|---|---|---|
| Đức → Hoan, Đức Anh | Một dòng có mã, năm, phạm vi hợp nhất, chỉ tiêu, giá trị gốc, đơn vị gốc, giá trị tính bằng đồng, mã nguồn và bản dữ liệu. Mã nguồn tra ra đường dẫn, trang, dòng và cột. | Mở trang và tự đổi đơn vị. Ô thiếu có lý do riêng, số 0 là giá trị hợp lệ. |
| Hưởng → Hoan | Với “Còn năm 2024?”, gửi lại danh sách và điều kiện của câu trước cùng năm mới. Nếu chưa có câu trước thì gửi lời hỏi làm rõ. | Nhìn riêng yêu cầu cũng biết phải đọc những dòng nào. Câu cần hỏi lại đi thẳng tới màn hình. |
| Hoan → Hưng, Đức Anh | Trả câu hỏi đã hiểu, phạm vi, bảng số, đơn vị, các bước Pandas đã dùng, nguồn cho từng số, mã thiếu dữ liệu, điều kiện nào đúng và tên bản dữ liệu. | Cùng một ví dụ cho cùng bảng trên màn hình và phiếu. Hai nơi đều lần lại được phép tính. |
| Hưng → Đức Anh | Một phiếu mẫu và cách nhận tệp từ kết quả Hoan trả. Hưng chuẩn bị cả phiếu đủ số và phiếu có mã thiếu số. | Bấm tải, đóng ứng dụng rồi mở tệp trong trình duyệt. Số, nguồn, phạm vi và ngày xuất vẫn đọc được. |

**Làm việc trên Git.** Mỗi người mở một nhánh cho một đầu việc, ví dụ `duc/bo-so-lieu-nam`. Trước khi ghép vào `main`, cập nhật từ bản chung, gửi phần đã sửa kèm một câu để người dùng đầu ra thử. Mỗi lần ghép chỉ gồm các tệp thuộc đầu việc đó. Nếu cần đổi mẫu dùng chung, gửi Hoan một ví dụ trước/sau. Hoan cập nhật mẫu và báo người bị ảnh hưởng trước khi họ đổi phần mình. Khi hai nhánh chạm cùng tệp, người phụ trách tệp so hai thay đổi, giữ các phần cần thiết rồi chạy lại ví dụ của cả hai bên.

## 6. Lịch chung

| Tuần | Mốc cả nhóm phải tự làm được |
|---|---|
| 1 · Làm một phiếu bằng tay | Đức đưa mẫu 16 vị trí. Hưởng viết cách hiểu câu. Hoan tính tay ví dụ đối chứng. Hưng dựng phiếu trên giấy, Đức Anh nhờ một người đọc và chỉ ra số cần mở để kiểm lại. |
| 2 · Chạy một lượt bằng số thật | Từ màn hình, chọn hai mã, hỏi một câu so sánh, xem nguồn rồi tải phiếu. Đức công bố số vị trí có dữ liệu trên 48. Hưởng chuẩn bị 20 câu công khai để cả nhóm sửa lỗi. |
| 3 · Xử lý câu khó và dùng thử | Nối hai điều kiện tìm doanh nghiệp, hỏi tiếp, trường hợp thiếu số và phiếu giữ nguyên sau khi cập nhật dữ liệu. Cuối tuần chốt bản đem chấm. |
| 4 · Đo xem sản phẩm có dùng được | Chấm 24 câu mới, so thời gian làm tay với dùng ứng dụng, nhờ người khác chạy lại rồi hoàn thiện phiếu thật, báo cáo và bài trình bày. |

| Buổi | Tuần 3 | Tuần 4 |
|---|---|---|
| 1 | Trên cùng một bản dữ liệu, ghép câu “có lãi nhưng tiền kinh doanh âm”. Đức Anh chọn một dòng rồi tự mở cả hai nguồn. | Chốt bản dữ liệu và ứng dụng. Đức Anh tính đáp án riêng, kiểm cách chấm bằng số mẫu trước khi mở bộ 24 câu. |
| 2 | Ghép điều kiện “doanh thu tăng nhưng tỷ lệ lãi gộp giảm”. Thử thêm mã, đổi năm, xóa lựa chọn. So bảng, lời nhận xét và phiếu. | Đức Anh chạy 24 câu, lưu từng kết quả. Thành viên nhận lỗi có ví dụ cụ thể và giữ lại kết quả lần chấm đầu. |
| 3 | Chạy 20 câu công khai. Thử mã thiếu một năm, doanh thu bằng 0, xếp hạng bằng nhau và danh sách không mã nào phù hợp. | Hai người dùng thử làm nhiệm vụ tương đương theo hai cách. Ghi thời gian, số kết quả đúng và chỗ phải nhờ trợ giúp. |
| 4 | Đức thêm một bản số liệu thử. Chạy cùng câu hỏi, xuất phiếu mới, mở lại phiếu cũ. Kiểm cả trường hợp nạp lại cùng một bản. | Đổi máy hoặc đổi người chạy từ hướng dẫn. Hưng ghép phiếu, hình và kết quả đo thật vào báo cáo. |
| 5 | Từng người thực hiện một bước trong buổi họp mẫu. Chốt bản chạy được, nguồn, lỗi còn mở và người nhận xử lý. | Diễn tập 8–10 phút với một câu mới. Bàn giao ứng dụng, dữ liệu, phiếu mẫu, hướng dẫn, bảng điểm và slide. |

## 7. Thế nào là đủ tốt để giao cho người dùng?

- **Đúng câu, đúng số.** Đức Anh giữ riêng 24 câu tới tuần 4, chia đều cho sáu nhóm: tra cứu, so sánh hoặc xếp hạng, tăng giảm, hỏi tiếp, tìm mã theo điều kiện và thiếu thông tin. Mỗi nhóm bốn câu. Đáp án được kiểm độc lập từ báo cáo. Câu có số phải đúng mã, năm, số, đơn vị và nguồn. Với câu hỏi tiếp, kiểm thêm phạm vi được giữ lại. Mục tiêu đề xuất là đạt ít nhất 20/24 và công bố số thực đo.
- **Đáng tin khi thiếu dữ liệu.** Mã thiếu một trong các số cần dùng được liệt kê riêng. Bảng ghi số mã đủ dữ liệu trên tổng số mã đã chọn. Cần phân biệt “đã kiểm hết và không có mã phù hợp” với “chưa đủ dữ liệu để kết luận”. Tăng trưởng phần trăm dùng năm gốc dương. Khi gốc bằng 0 hoặc âm, đưa hai số và mức chênh bằng tiền nếu tính được. Tỷ lệ lãi gộp chỉ tính khi doanh thu dương.
- **Phiếu dùng được ngoài ứng dụng.** Ba phiếu mẫu gồm đủ số, có mã thiếu và không có mã phù hợp. Mỗi phiếu phải mở được sau khi đóng ứng dụng, giữ đúng bảng và chỉ được vị trí nguồn. Khi nguồn được điều chỉnh, phiếu cũ vẫn chỉ rõ bản đã dùng.
- **Đo ích lợi thực tế.** Giao hai người dùng hai bài tương đương, mỗi bài gồm so hai công ty, mở nguồn và mang kết quả ra khỏi ứng dụng. Đảo thứ tự làm tay và dùng ứng dụng giữa hai người để bớt lợi thế làm lần hai. Ghi thời gian từng lượt, độ đúng và điểm gây lúng túng. Nếu ứng dụng chậm hơn, ghi nguyên kết quả và xác định bước mất thời gian.
- **Khi thiếu thời gian.** Giữ câu hỏi → số thật → nguồn → phiếu tải được cho hai mã trước. Sau đó giữ hai tình huống tìm doanh nghiệp và hỏi tiếp theo năm. Mở rộng số mã, biểu đồ hay tự động lấy báo cáo mới chỉ làm sau khi luồng này đã được người khác chạy lại.
