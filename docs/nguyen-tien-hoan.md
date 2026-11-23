# Nguyễn Tiến Hoan · 24022334 | Tính số và nối các phần

[Hướng dẫn chung và sơ đồ thư mục](../AGENTS.md)

**Hoan chịu trách nhiệm trả lời câu “Tại sao ứng dụng ra đúng số này?”.** Hoan sửa `src/tinh_so/`, hướng dẫn chung và các tệp cài/chạy ở gốc khi triển khai. Đức giao bảng đã kiểm. Hưởng giao ý người dùng. Hoan dùng Pandas để lọc, tính và trả một kết quả cho cả màn hình của Đức Anh lẫn phiếu của Hưng.

## Tuần 1 · Chốt mẫu để bốn bạn khác làm được ngay

1. Cuối buổi 2, viết `src/tinh_so/mau_ban_giao.md` bằng ba ví dụ điền sẵn: một câu có số, một câu thiếu dữ liệu và một câu cần hỏi lại. Dùng bảng công ty A trong hướng dẫn chung khi Đức đang tìm báo cáo. Ghi rõ nguồn gắn với từng số nào.
2. Thống nhất những thứ cần đưa ra: yêu cầu đã hiểu, mã và năm được xét, bảng kết quả, đơn vị, số liệu đầu vào, bước tính, nguồn, bản dữ liệu và mã bị thiếu. Hưng cần biết điều kiện nào đã được kiểm. Đức Anh cần biết màn hình phải hiện kết quả hay hỏi thêm.
3. Tính tay ba con số của công ty A rồi gửi nhóm: doanh thu tăng 20%, tỷ lệ lãi gộp từ 25% xuống 20%, tiền kinh doanh −3 tỷ dù lãi sau thuế 9 tỷ. Nhờ Hưng dựng được phiếu và Đức Anh dựng được màn hình từ duy nhất bộ kết quả đó.

## Tuần 2 · Cho người dùng hỏi bằng tiếng Việt và nhận số thật

- Nối lựa chọn trên màn hình với phần đọc câu của Hưởng và bảng của Đức. Với yêu cầu hợp lệ, dùng Pandas lấy đúng mã, năm và chỉ tiêu. Giữ thông tin chỉ vị trí nguồn bên cạnh các số trong suốt phép tính.
- Làm tra cứu, so sánh hai mã, tăng giảm theo năm và xếp hạng. Với số tiền, tính trên đồng và chỉ quy sang tỷ khi trình bày. Với xếp hạng, giữ tất cả mã bằng nhau ở vị trí cuối, nêu số mã thực sự đủ số liệu.
- Ghép một câu so sánh thật từ màn hình đến phiếu. **Đạt mốc tuần 2** khi đổi một mã, cả màn hình lẫn phiếu cùng đổi bảng, nguồn và phạm vi. Đức Anh tự chạy được ví dụ này bằng hướng dẫn ngắn.

## Tuần 3 · Tính những điều đáng chú ý và thử chỗ dễ sai

| Buổi | Hoan làm gì? | Kết quả cho người nhận |
|---|---|---|
| 1 | Ghép điều kiện lãi sau thuế lớn hơn 0 và tiền kinh doanh nhỏ hơn 0 trong cùng năm. Thử riêng trường hợp lãi đúng bằng 0 và trường hợp thiếu dòng tiền. | Hưng nhận kết quả có số và nguồn. Đức Anh phân biệt được mã đạt điều kiện, mã đã kiểm nhưng không đạt, mã còn thiếu số. |
| 2 | Ghép điều kiện doanh thu tăng và tỷ lệ lãi gộp giảm. Tỷ lệ từng năm bằng lãi gộp chia doanh thu rồi nhân 100. So hai tỷ lệ trước khi làm tròn. Nối thao tác đổi năm và thêm mã của Hưởng. | Ví dụ công ty A phải ra giảm **5 điểm phần trăm**. Nếu doanh thu của một năm bằng 0 hoặc âm, ghi vì sao bỏ phép chia và vẫn hiển thị các số đã có. |
| 3 | Từ 20 câu công khai, chạy lại câu sai bằng một yêu cầu đã điền đúng. Kiểm trường hợp năm gốc âm, cùng hạng, thiếu năm và danh sách rỗng sau khi lọc. | Mỗi lỗi có căn cứ để giao đúng người. Kết quả sau khi lọc hiện số mã đủ dữ liệu trên tổng số đã chọn. |
| 4 | Cùng Đức nạp một bản cập nhật thử. Chạy lại cùng câu hỏi, sau đó nạp lần hai. Kiểm chỉ có một dòng cho mỗi mã–năm–chỉ tiêu trong bản đang xét. | Hưng nhận kết quả trước/sau mang tên bản riêng. Nếu bản mới có dòng trùng hoặc sai đơn vị, giữ bản đang dùng và báo vị trí lỗi. |
| 5 | Chạy xuyên suốt từ chọn danh sách đến mở lại phiếu. Chốt dữ liệu, phần hiểu câu, phần tính, giao diện và phiếu ở cùng một lần ghép. | Đức Anh nhận bản đem chấm. Mỗi lỗi chưa sửa có tên người nhận và một câu để thử lại. |

## Tuần 4 · Chịu trách nhiệm khả năng chạy lại

| Buổi | Hoan làm gì? | Kết quả phải để lại |
|---|---|---|
| 1 | Mở ứng dụng từ đầu trên môi trường sạch hoặc nhờ bạn khác chạy. Chốt cách chọn bản dữ liệu và lưu lại đúng phiên bản của cả nhóm. | Đức Anh tự chạy được một câu công khai trước khi bắt đầu 24 câu riêng. |
| 2 | Khi Đức Anh chấm xong, lấy một câu sai nghi do tính toán và đối chiếu ba thứ: ý Hưởng gửi, số Đức cung cấp và bước Pandas đã dùng. | Ghi số câu bị ảnh hưởng, nguyên nhân, bản sửa nếu có. Giữ nguyên bằng chứng của lượt chấm đầu. |
| 3 | Hỗ trợ việc đo thời gian làm tay và dùng ứng dụng. Quan sát riêng lúc người dùng chờ câu trả lời hoặc tìm nguồn nhưng chưa thấy. | Gửi Hưng mô tả luồng hệ thống và một ví dụ phép tính có số, nguồn, đơn vị để đưa vào báo cáo. |
| 4 | Đưa hướng dẫn cài và chạy cho bạn khác. Để bạn ấy tự chọn bản dữ liệu, hỏi một câu mới và xuất phiếu. Ghi bước nào phải can thiệp rồi thử lại. | Chuyển hướng dẫn đã thử cho Hưng ghép vào `ban_nop/`. Đức Anh nhận mọi lỗi hiện trên màn hình. |
| 5 | Mở buổi trình bày bằng nhu cầu chuẩn bị cuộc họp. Chọn một số trên phiếu để lần ngược qua phép tính đến dòng báo cáo. | Người xem thấy một câu mới được tính trên bảng thật và biết dùng tài liệu nào để kiểm lại. |

**Nguyên tắc ghép việc:** Hoan giữ mẫu bàn giao chung. Nếu cần đổi cách ghi đơn vị, gửi Hưng và Đức Anh cùng một ví dụ trước/sau. Hai bạn sửa nơi hiển thị của mình và cùng chạy lại câu cũ. Như vậy cả ba cùng hoàn thành một thay đổi mà mỗi người chỉ sửa tệp của phần mình.
