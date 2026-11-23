# Lê Đức Anh · 24022250 | Màn hình và dùng thử

[Hướng dẫn chung và sơ đồ thư mục](../AGENTS.md)

**Đức Anh chịu trách nhiệm trả lời hai câu: “Người mới có tự dùng được không?” và “Kết quả đúng bao nhiêu lần?”.** Đức Anh sửa `app/`, `danh_gia/` và tài liệu này. Hoan gửi bảng kết quả và nguồn, Hưng giao phiếu tải xuống. Đức Anh giữ bộ câu hỏi dùng để chấm cuối và tự đối chiếu đáp án từ báo cáo.

## Tuần 1 · Vẽ màn hình theo thứ tự người dùng làm việc

1. Vẽ một màn hình theo bốn bước: chọn danh sách, nhập câu hỏi, đọc kết quả, xuất phiếu. Ngay trên bảng phải thấy các mã và năm đang xét. Mỗi dòng có chỗ mở nguồn, gồm cả số trang nếu trình duyệt chỉ mở được trang đầu của tài liệu.
2. Cuối buổi 2, dùng một phản hồi mẫu của Hoan và phiếu nháp của Hưng để thử trên giấy. Nhờ một người chỉ ra doanh nghiệp nào thỏa điều kiện, số tiền bao nhiêu và sẽ bấm đâu để kiểm. Ghi đúng chỗ người đó phải hỏi lại.
3. Chốt với nhóm cách chấm. Câu trả số cần đúng mã, năm, giá trị, đơn vị và nguồn. Câu thiếu thông tin cần hỏi đúng điểm mơ hồ. Các câu hỏi nối tiếp phải được chạy trong đúng thứ tự đã ghi.

## Tuần 2 · Có màn hình chạy thật và bộ câu hỏi độc lập

- Nối ô hỏi với phần của Hoan và nút tải với phiếu của Hưng. Thử đổi danh sách đang chọn, bắt đầu lại một lượt tra cứu và mở nguồn cho một câu so sánh trên dữ liệu thật.
- Tự soạn **24 câu giữ riêng**, bốn câu mỗi nhóm dưới đây. Đối chiếu với 20 câu công khai của Hưởng để tránh trùng câu hoặc chỉ đổi vài từ. Giữ câu và đáp án ở nơi riêng đến lúc chấm. Trong `danh_gia/`, công khai cách chấm và một số ví dụ khác.
- Tự đọc báo cáo và tính đáp án bằng bảng tính riêng. Mỗi câu ghi mã câu, mã và kỳ đã chọn, câu trước nếu có, số/bảng hoặc phản hồi mong đợi, và dòng nguồn để kiểm tra. Chốt lại đáp án nếu bản dữ liệu đổi trước lượt chấm chính thức.

| Nhóm | Cách biết câu trả lời đạt |
|---|---|
| Tra cứu | Đúng số, mã, năm, đơn vị và vị trí số gốc |
| So sánh hoặc xếp hạng | Đúng danh sách, thứ tự và mã đồng hạng, kèm nguồn |
| Tăng giảm | Lấy đúng năm gốc và năm sau, phân biệt chênh bằng tiền với phần trăm |
| Hỏi tiếp | Đổi đúng năm hoặc thêm đúng mã, giữ phần còn lại của yêu cầu |
| Tìm mã theo điều kiện | Đúng danh sách mã thỏa, hiện các số tạo ra kết luận và mức độ đủ dữ liệu |
| Thiếu thông tin | Hỏi lại đúng phần thiếu hoặc giải thích đúng số chưa có hay chưa đủ điều kiện tính |

## Tuần 3 · Thử những chỗ người dùng dễ hiểu nhầm

| Buổi | Đức Anh làm gì? | Kết quả giao lại |
|---|---|---|
| 1 | Chạy câu có lãi nhưng tiền kinh doanh âm. Bấm từ dòng kết quả tới vị trí ghi hai số trong tài liệu. | Gửi Hoan lỗi thiếu trường, gửi Đức lỗi trỏ nhầm trang. Nếu chỉ nhãn hiển thị sai thì Đức Anh sửa ở màn hình. |
| 2 | Thử đổi năm, thêm mã, xóa lựa chọn, sau đó tải phiếu. Thử cả trường hợp câu mới nêu một mã khác danh sách đang chọn. | Sau từng lần bấm, màn hình và phiếu ghi cùng mã, kỳ và bản dữ liệu. Lưu chuỗi thao tác cho Hưởng nếu bị hiểu sai. |
| 3 | Chạy 20 câu công khai. Đưa cả trường hợp thiếu một năm, doanh thu bằng 0, hai mã đồng hạng và đủ số nhưng chẳng mã nào phù hợp. | Bảng lỗi có câu gây lỗi, kết quả đúng, kết quả thực, người xử lý và trạng thái chạy lại. |
| 4 | Nhận hai bản số liệu thử, chạy cùng câu rồi tải hai phiếu. Tắt ứng dụng để mở phiếu và so năm, số, nguồn. | Giao Hưng ví dụ nếu mẫu phiếu sai. Nếu nút vẫn trỏ tới lượt cũ, Đức Anh sửa việc chọn tệp tải. |
| 5 | Cho một người chưa làm giao diện chạy liền mạch từ chọn danh sách đến đọc phiếu. Chốt bản mang đi chấm, chuẩn bị hai bài tương đương cho buổi dùng thử. | Gửi Hoan bản giao diện và danh sách lỗi còn mở. Mỗi bài dùng thử có đầu vào, điểm kết thúc và số cần đối chiếu. |

## Tuần 4 · Đo độ đúng và thời gian người dùng tiết kiệm được

| Buổi | Đức Anh làm gì? | Kết quả phải để lại |
|---|---|---|
| 1 | Nhận đúng bản dữ liệu, cách hiểu câu, phép tính và mẫu phiếu. Kiểm thử cách chấm bằng một câu công khai rồi khóa 24 đáp án. | Ghi tên bản và quy ước làm tròn trước khi mở lượt chấm. |
| 2 | Chạy đủ 24 câu. Tính số câu đạt từng nhóm trên 4 và tổng trên 24. Tính cả câu đứng máy hoặc thiếu kết quả trong mẫu số. | Gửi cả nhóm số thực đo và ví dụ lỗi. Mục tiêu đề xuất là 20/24. Mọi điểm sau khi sửa ghi ở lượt riêng. |
| 3 | Mời hai bạn đóng vai người chuẩn bị họp. Bạn thứ nhất làm tay bài A rồi dùng ứng dụng cho bài B. Bạn thứ hai dùng ứng dụng cho bài A rồi làm tay bài B. Mỗi bài đều yêu cầu so hai mã, mở nguồn và giao một phiếu ngắn. | Dùng cùng tài liệu đầu vào và tiêu chí kết thúc. Ghi bốn lượt gồm thời gian, kết quả đúng và bước cần trợ giúp. Gửi Hưng số liệu thật, kể cả khi có lượt làm tay nhanh hơn. |
| 4 | Dùng máy khác mở bản ứng dụng theo hướng dẫn Hoan và đọc phiếu của Hưng. Tự hỏi một câu mới. Rà lại ba phiếu mẫu và các đường dẫn dùng khi trình bày. | Báo người phụ trách nếu cần chỉnh hướng dẫn hoặc phiếu. Hoàn thiện bảng điểm và bảng thời gian cho `ban_nop/` qua Hưng. |
| 5 | Cho người xem tự chọn mã và đổi năm khi trình diễn. Kết bài bằng điểm thực tế, một lượt dùng thử cụ thể và một giới hạn đã quan sát. | Người nghe thấy sự khác nhau giữa chỉ tiêu số câu đúng và thời gian hoàn thành công việc. |

**Tự nghiệm thu:** chọn ngẫu nhiên một dòng trong bảng điểm và truy ra câu gốc, đầu ra thực tế, đáp án cùng vị trí nguồn. Sau đó nhờ người khác mở một phiếu đã tải, xác định doanh nghiệp thỏa điều kiện và chỉ được hai con số dẫn đến kết luận.
