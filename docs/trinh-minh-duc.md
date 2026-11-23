# Trịnh Minh Đức · 24022298 | Bảng số liệu và nguồn

[Hướng dẫn chung và sơ đồ thư mục](../AGENTS.md)

**Đức chịu trách nhiệm trả lời câu “Con số này lấy ở đâu?”.** Đức sửa `data/` và tài liệu này. Hoan đọc số đã quy về đồng để tính, Đức Anh dùng báo cáo gốc để tự kiểm, Hưng dùng thông tin nguồn để in lên phiếu. Mỗi lần bàn giao, ba bạn nhận cùng một bản.

## Tuần 1 · Lấy đúng 16 vị trí đầu tiên

1. Khảo sát báo cáo năm hợp nhất của MWG, FRT, PNJ và DGW cho 2023–2025. Chọn trước hai mã có báo cáo rõ cho hai năm liền nhau. Ưu tiên báo cáo năm hợp nhất đã kiểm toán trên trang công bố của doanh nghiệp. Ghi rõ mã nào hoặc năm nào cần thay.
2. Tìm bốn dòng trong mỗi báo cáo: doanh thu thuần, lợi nhuận gộp, lợi nhuận sau thuế của cả doanh nghiệp hợp nhất, tiền thuần từ hoạt động kinh doanh. Dòng tiền nằm trong báo cáo lưu chuyển tiền tệ. Đọc cả tên cột năm và dòng ghi đơn vị ở đầu bảng.
3. Cuối buổi 2, gửi một dòng số và một dòng nguồn mẫu cho Hoan và Đức Anh. Cuối tuần giao danh sách 16 vị trí, giá trị tìm được và các vị trí còn thiếu. Đức Anh mở lại một ô bất kỳ mà không cần Đức chỉ trang.

## Tuần 2 · Đưa dữ liệu thật vào ứng dụng

- Điền bảng theo dõi 48 vị trí. Trong `data/v1/so_lieu.csv`, mỗi mã–năm–chỉ tiêu có một dòng. Ghi số gốc, đơn vị gốc, giá trị quy về đồng và mã nguồn. Trong `nguon.csv`, mã nguồn dẫn tới đúng tài liệu, trang, dòng và cột.
- Kiểm tra các bẫy bằng ví dụ thật. Số trong ngoặc có thể là số âm. Số tiền tính bằng triệu đồng phải nhân một triệu để quy về đồng. Một số 0 đọc được từ báo cáo khác với ô còn thiếu. Nếu dòng lợi nhuận có cả phần của cổ đông công ty mẹ, đối chiếu tên dòng với chỉ tiêu toàn doanh nghiệp mà nhóm đã chọn.
- Bàn giao bảng cùng số vị trí đã xác minh trên 48. Hưởng nhận tên chỉ tiêu để hiểu câu, Hoan nhận bảng và nguồn, Đức Anh nhận danh sách báo cáo để kiểm độc lập. Khi một nguồn về chậm, giao phần đã kiểm kèm danh sách phần còn thiếu.

## Tuần 3 · Kiểm chứng các nhận xét trước khi đưa lên phiếu

| Buổi | Đức làm gì? | Giao hoặc tự kiểm bằng gì? |
|---|---|---|
| 1 | Chọn một mã/năm và tìm hai dòng lãi sau thuế, tiền từ hoạt động kinh doanh. Đọc nguyên dấu âm hoặc dương của từng số. | Gửi hai vị trí nguồn cho Hoan. Đức Anh có thể xác nhận mã có thỏa điều kiện “có lãi nhưng tiền kinh doanh âm” hay không. |
| 2 | Lấy doanh thu và lãi gộp của hai năm liền nhau cho một mã. Tự tính tỷ lệ từng năm trên bảng tính riêng. | Đối chiếu với Hoan. Nếu tỷ lệ lệch, kiểm lại đơn vị, năm, dấu và thời điểm làm tròn. |
| 3 | Rà các lỗi dữ liệu từ 20 câu công khai. Kiểm trường hợp mã chỉ đủ một năm, báo cáo điều chỉnh số năm trước hoặc nguồn mở đúng tệp nhưng chỉ nhầm cột. | Mỗi lỗi ghi ô sai, ô đúng, tài liệu và các câu bị ảnh hưởng. Báo cho người dùng dữ liệu trước khi giao bản kế tiếp. |
| 4 | Thử một lần cập nhật trên bản sao. Tạo bản thứ hai có một dòng được thêm hoặc sửa, ghi bản thay đổi vào `lich_su_cap_nhat.md`. Nếu dùng số minh họa, đặt tên bản thử và tách khỏi bản báo cáo thật. | Hoan nạp lại cùng một bản mà số dòng vẫn giữ nguyên. Hưng mở phiếu cũ và mới, phân biệt được hai bản. |
| 5 | Chốt tên bản thật dành cho tuần 4. Ghi số mã/năm có đủ cả bốn chỉ tiêu và số mã có đủ hai năm liên tiếp cho phép so sánh. | Gửi Hoan, Hưng và Đức Anh cùng một tên bản, bảng thiếu và hai ví dụ đã kiểm nguồn. |

## Tuần 4 · Chứng minh người khác kiểm được số

| Buổi | Đức làm gì? | Kết quả phải để lại |
|---|---|---|
| 1 | Đối chiếu ngẫu nhiên ít nhất một ô mỗi chỉ tiêu trên bản đem chấm. Rà các đường dẫn và đơn vị. | Bảng ghi mã, năm, dòng, cột và người kiểm. Đức Anh dùng tên bản này khi chấm. |
| 2 | Sau lượt chấm 24 câu, lần ngược các câu sai nghi do dữ liệu. Nếu nguồn khác nhau, so ngày công bố và xem có điều chỉnh số năm trước hay không. | Chỉ ra lỗi ở báo cáo được chọn, bảng nhập hay phép tính. Ghi đính chính thành bản riêng nếu cần. |
| 3 | Chuẩn bị các báo cáo nguồn cho hai bài dùng thử. Quan sát xem người dùng có tìm được đúng con số bằng trang và cột hiển thị. | Gửi Đức Anh thời điểm hoặc vị trí người dùng bị vướng. Gửi Hưng một nhận xét từ số thật kèm nguồn. |
| 4 | Đưa một phiếu cho bạn khác trên máy khác. Yêu cầu tìm lại hai số và nói đơn vị gốc. | Gửi Hưng đoạn mô tả nguồn, số ô đủ/thiếu và hạn chế để đưa vào báo cáo. |
| 5 | Trình bày khoảng một phút bằng việc mở thẳng một dòng nguồn từ phiếu. | Người xem biết số ở đâu, đã quy đổi thế nào và ngày nào nhóm cập nhật. |

**Khi cần người khác sửa:** nếu trên báo cáo và bảng dữ liệu đều là −3 tỷ nhưng phiếu ghi 3 tỷ, gửi Hoan hai dòng đối chiếu. Giữ nguyên dữ liệu đã xác minh để cả nhóm tìm ra chỗ làm mất dấu âm.
