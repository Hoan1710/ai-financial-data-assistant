# Nguyễn Tiến Hưởng · 24022352 | Hiểu câu hỏi và câu hỏi tiếp

[Hướng dẫn chung và sơ đồ thư mục](../AGENTS.md)

**Hưởng chịu trách nhiệm trả lời câu “Người dùng thực sự muốn xem gì?”.** Hưởng sửa `src/hieu_cau/` và tài liệu này. Nhận tên mã và chỉ tiêu do Đức chốt. Gửi cho Hoan một yêu cầu viết đủ ý để Hoan có thể lấy số ngay. Đức Anh chỉ cần chuyển nội dung câu hỏi, mã đang chọn và lượt trả lời gần nhất tới chỗ Hoan nối các phần.

## Tuần 1 · Viết lại câu hỏi sao cho người khác làm được

1. Mời mỗi thành viên góp hai câu bằng cách họ thường nói. Ghi cả cách viết tắt như “LNST” và câu ngắn như “còn năm ngoái?”. Chọn ví dụ cho tra cứu, so sánh, tăng giảm, xếp hạng và hai điều kiện tìm doanh nghiệp trong hướng dẫn chung.
2. Với mỗi câu, điền bằng lời: công ty nào, chỉ tiêu gì, năm nào, so với năm nào, tìm điều kiện gì, muốn số tiền hay phần trăm. Gạch chân những từ trong câu dẫn tới lựa chọn đó. Nếu người dùng nói “lãi”, hỏi muốn xem lãi gộp hay lãi sau thuế.
3. Cuối buổi 2 giao Hoan một ví dụ. Chẳng hạn, sau câu tìm doanh nghiệp có lãi nhưng tiền kinh doanh âm trong năm 2025, “Còn 2024?” phải giữ danh sách và cả hai điều kiện. Cuối tuần giao danh sách các tình huống để Hoan và Đức Anh đọc lại.

## Tuần 2 · Từ câu hỏi tiếng Việt đến yêu cầu tính

- Dùng một công cụ AI nhóm truy cập được, cho xem tên chỉ tiêu và vài ví dụ về cách điền yêu cầu. Với câu quen thuộc, chuẩn bị cách nhận từ viết tắt và tên mã để bản trình diễn vẫn xử lý được câu cơ bản khi dịch vụ AI gián đoạn.
- Chuẩn bị **20 câu công khai** để tìm lỗi, khác những câu đưa cho mô hình xem làm ví dụ. Lưu câu, lượt hỏi trước (nếu có), cách hiểu đúng và lý do trong `src/hieu_cau/cau_thu.csv`. Đức Anh tự soạn 24 câu riêng để chấm cuối.
- Nối câu so sánh đầu tiên với Hoan. Người dùng chọn hai mã nhưng câu chỉ đích danh một mã thì dùng mã nêu trong câu và hiển thị phạm vi đã hiểu. Khi cả hai nơi đều bỏ trống, hỏi người dùng muốn xét mã nào. Câu mơ hồ trả lời bằng một câu hỏi ngắn đúng chỗ thiếu.

## Tuần 3 · Giữ đúng ý khi người dùng đổi cách hỏi

| Buổi | Hưởng làm gì? | Bằng chứng bàn giao |
|---|---|---|
| 1 | Nhận diện “có lãi mà tiền kinh doanh âm” và các cách nói tương đương. Thử thêm câu chỉ hỏi dòng tiền âm để bảo đảm không tự thêm điều kiện lãi dương. | Hoan nhận hai yêu cầu khác nhau và biết phải đọc hai chỉ tiêu hay một chỉ tiêu. |
| 2 | Làm hai lượt hỏi tiếp: “còn năm 2024?” và “thêm PNJ vào nữa”. Thử đổi năm sau khi thêm mã và bấm bắt đầu lại. | Đức Anh nhận ví dụ cho biết sau mỗi bước danh sách, năm và điều kiện nào còn hiệu lực. Sau khi xóa, câu thiếu thông tin phải hỏi lại. |
| 3 | Chạy 20 câu công khai. Đặc biệt phân biệt “lãi gộp giảm” với “tỷ lệ lãi gộp giảm”, “tăng mấy tỷ” với “tăng mấy phần trăm”. | Giao bảng câu đúng/sai, trường bị hiểu nhầm và cách hiểu mong đợi cho Hoan cùng Đức Anh. |
| 4 | Sửa lỗi lặp lại nhiều nhất, rồi thử lại cả 20 câu. Với cách gọi mới liên quan tới tên chỉ tiêu, gửi Đức ví dụ để xác nhận nghĩa. | Ghi một câu sửa được và kiểm lại ít nhất một câu gần giống từng đúng. Giữ phiên bản hoạt động tốt hơn cho buổi dùng thử. |
| 5 | Thử câu mới do thành viên khác tự đặt. Chốt hướng dẫn cho AI, ví dụ đã dùng và tên công cụ. | Đức Anh có thể chạy lại cùng cách hiểu; Hoan nhận danh sách câu nào phải hỏi lại hoặc nằm ngoài phạm vi. |

## Tuần 4 · Kiểm tra bằng lời người dùng thật

| Buổi | Hưởng làm gì? | Kết quả phải để lại |
|---|---|---|
| 1 | Giao bản chốt để Đức Anh chạy một câu công khai, một câu hỏi tiếp và một câu mơ hồ. | Đức Anh xác nhận mỗi câu dẫn tới đúng phạm vi trước khi mở bộ chấm riêng. |
| 2 | Sau lượt chấm 24 câu, xem từng lỗi do hiểu nhầm. Giữ cả câu gốc lẫn yêu cầu đã gửi Hoan. | Chọn hai ví dụ giải thích được vì sao sai. Nếu do công cụ AI gián đoạn, đánh dấu riêng để nhóm công bố đúng kết quả. |
| 3 | Nghe hai người dùng nói khi làm bài thử. Ghi nguyên cách họ hỏi ở vị trí họ phải dừng hoặc sửa câu. | Gửi Đức Anh thời điểm có vướng mắc và Hưng một ví dụ đủ rõ để giải thích trên slide. |
| 4 | Viết đoạn báo cáo ngắn cho Hưng gồm một câu hiểu đúng, một câu dễ nhầm và tác động tới kết quả. Sửa lời hỏi lại ở bản dùng thử nếu cần, ghi rõ khác biệt với bản đem chấm. | Người đọc biết hệ thống giữ lại điều gì khi đổi năm và hỏi lại điều gì khi gặp “lãi”. |
| 5 | Diễn tập một đoạn hỏi hai lượt bằng lời của người dùng, sau đó mở yêu cầu đã hiểu. | Cả nhóm có một ví dụ để giải thích AI hiểu câu ra sao và tại sao con số do Pandas tính. |

**Khi cần người khác sửa:** nếu yêu cầu đã ghi đúng “năm gốc 2024, năm sau 2025” mà phần trăm bị đảo dấu, gửi Hoan yêu cầu ấy kèm hai số. Nếu người dùng đã bấm bắt đầu lại nhưng ứng dụng vẫn gửi lượt cũ, báo Đức Anh bằng đúng chuỗi thao tác trên màn hình.
