# Kế hoạch bài tập lớn NLP — AI Financial Data Assistant

**Hoan · Đức · Hưng · Hưởng · Đức Anh**  
Kế hoạch triển khai hệ thống Text-to-Pandas truy vấn và phân tích báo cáo tài chính của doanh nghiệp niêm yết Việt Nam, với lộ trình đề xuất sáu tuần. Quy mô mẫu, ngưỡng nghiệm thu và ngân sách GPU có thể điều chỉnh theo deadline và rubric chính thức.

| Người đọc muốn tìm | Vị trí trong kế hoạch |
|---|---|
| Biết sản phẩm phải trả lời được gì | Mục 1 và 3 · phạm vi, ví dụ FPT và hợp đồng API |
| Bắt đầu code, biết đặt tệp vào đâu | Mục 2 và 8 · cây thư mục, chủ sở hữu và năm đầu việc đầu tiên |
| Chuẩn bị số liệu, gán nhãn và huấn luyện | Mục 4–6 · schema, hướng chia tập và thí nghiệm M0–M4 |
| Nghiệm thu, tích hợp và chuẩn bị bảo vệ | Mục 7 và 9–11 · 20 ca có đáp án, lịch sáu tuần và gói nộp |

## 1. Từ tên đề tài đến bài toán nghiên cứu

Người dùng hỏi bằng tiếng Việt. Hệ thống xác định doanh nghiệp, chỉ tiêu, kỳ báo cáo và phép phân tích, tạo chương trình Pandas, chạy trên dữ liệu có phiên bản, rồi trả kết quả kèm đơn vị và nguồn. Một câu trả lời có thể là một số, một danh sách xếp hạng hay một bảng nhiều kỳ. Khi thiếu thông tin để xác định ý định, hệ thống hỏi lại. Khi yêu cầu rõ nhưng kho thiếu số liệu, hệ thống chỉ ra phần dữ liệu còn thiếu.

**Giả thuyết chính:** Với cùng một mô hình nhỏ và cùng ngân sách suy luận, cung cấp từ điển chỉ tiêu liên quan và huấn luyện mô hình sinh chuỗi thao tác có kiểu sẽ tăng tỷ lệ câu đúng khi thực thi, đặc biệt trên câu hỏi có tên chỉ tiêu gần nghĩa, so sánh nhiều kỳ hoặc phối hợp nhiều thao tác. Đây là giả thuyết để kiểm tra. Một kết quả trong đó luật hoặc few-shot thắng mô hình fine-tune cũng cần được báo cáo.

| Năng lực | Câu hỏi nghiệm thu | Chương trình phải làm được |
|---|---|---|
| Tra cứu | Doanh thu thuần hợp nhất của FPT năm 2024 là bao nhiêu tỷ đồng? | Lọc mã, chỉ tiêu, kỳ, phạm vi và đổi đơn vị |
| So sánh | Năm 2024, FPT hay VNM có biên lợi nhuận gộp cao hơn? | Lấy hai chỉ tiêu của mỗi công ty, tính tỷ lệ rồi so sánh |
| Tăng trưởng | Doanh thu FPT năm 2024 tăng bao nhiêu phần trăm so với 2023? | Ghép hai năm đúng thứ tự, kiểm tra mẫu số, tính phần trăm |
| Xếp hạng | Trong các mã đã nạp, ba doanh nghiệp có LNST hợp nhất cao nhất năm 2024 là những mã nào? | Xác định tập doanh nghiệp đủ dữ liệu, sắp xếp, áp dụng chính sách đồng hạng |
| Xu hướng | Lập bảng dòng tiền thuần từ hoạt động kinh doanh của FPT giai đoạn 2022–2024 | Lấy đúng báo cáo lưu chuyển tiền tệ, sắp kỳ, trả bảng kèm nguồn từng kỳ |
| Làm rõ | Lợi nhuận của FPT tăng bao nhiêu? | Hỏi loại lợi nhuận, hai kỳ so sánh và mức tăng tuyệt đối hay tỷ lệ nếu ngữ cảnh chưa rõ |
| Thiếu dữ liệu | Top 3 trên toàn thị trường, trong khi kho chỉ có 8 mã | Nêu độ phủ và đề nghị xếp hạng trong tập đã nạp |

**Phạm vi theo nguồn lực.** Bản đầu dùng số liệu năm hợp nhất của 6–8 doanh nghiệp phi tài chính, 3–4 năm liên tiếp, 10–15 chỉ tiêu từ bảng cân đối kế toán, báo cáo kết quả kinh doanh và báo cáo lưu chuyển tiền tệ. Chọn vài doanh nghiệp cùng ngành cho câu xếp hạng. Đầu tiên dựng một lát cắt 2 mã × 2 năm × 5 chỉ tiêu. Sau khi bản đầu chạy được, chọn một trong ba mở rộng ở mục 10. Nếu giảng viên yêu cầu mô hình sinh mã Pandas trực tiếp, lấy nhánh sinh mã ở mục 5 làm nhánh chính và giữ nhánh biên dịch làm đối chứng. Việc triển khai dữ liệu và bộ chấm dùng chung cho cả hai.

## 2. Cấu trúc thư mục đề xuất

Nhóm dùng một repository và một gói Python mang tên `finassistant`. Trong tuần đầu chỉ tạo những tệp cần cho một truy vấn chạy xuyên suốt. Cây dưới đây là đích đến khi nộp bài. Các tên như `v1` là phiên bản quy ước, được thay bằng phiên bản thực tế khi phát hành.

```text
ai-financial-data-assistant/
├── README.md                           # Cài đặt, chạy bản demo, tái lập bảng điểm
├── pyproject.toml                      # Gói Python và các nhóm phụ thuộc app/train/dev
├── .gitignore
├── .github/
│   ├── CODEOWNERS                      # Gán người duyệt theo đường dẫn
│   └── workflows/ci.yml                # Chạy test nhanh trên CPU
├── src/finassistant/
│   ├── contracts/                      # Hoan · kiểu dữ liệu dùng chung
│   │   ├── plan.py                     # Filter, Derive, Compare, TopK và tham số
│   │   └── result.py                   # QueryRequest, Prediction, QueryResult, Evidence
│   ├── data_pipeline/                  # Đức · từ bảng nguồn đến snapshot
│   │   ├── extract.py                  # Tệp nguồn → dòng, cột, trang, văn bản gốc
│   │   ├── normalize.py                # Chuẩn mã, kỳ, đơn vị, giá trị và phạm vi
│   │   └── snapshot.py                 # Kiểm khóa, lưu phiên bản, load_snapshot()
│   ├── nlu/                            # Hưng · hiểu tiếng Việt
│   │   ├── normalize.py                # Giữ bản gốc và offsets cho thực thể
│   │   ├── linker.py                   # Cụm từ → mã công ty, kỳ, chỉ tiêu ứng viên
│   │   └── baselines.py                # M0 luật, M1 TF-IDF + Logistic Regression
│   ├── models/                         # Hưởng · suy luận với M2, M3, M4
│   │   ├── predictor.py                # Một giao diện predict() cho raw code và plan
│   │   └── prompts/                    # Prompt sinh Pandas và sinh JSON có phiên bản
│   ├── engine/                         # Hoan · chạy chương trình trên Pandas
│   │   ├── compiler.py                 # Plan → các phép Pandas có kiểu và mã hiển thị
│   │   ├── pandas_subset.py            # Đọc tập con cú pháp Pandas do M2 sinh
│   │   ├── execute.py                  # Lọc, ghép, tính tỷ lệ, so sánh và xếp hạng
│   │   └── evidence.py                 # Từ mỗi kết quả truy ngược đến các dòng nguồn
│   └── api/                            # Hoan
│       ├── main.py                     # FastAPI, POST /query, kiểm tra request
│       └── service.py                  # Nối snapshot, linker, predictor và engine
├── app/
│   └── streamlit_app.py                # Đức Anh · câu hỏi, kết quả, mã và nguồn
├── data/
│   ├── catalog/                        # Đức · companies.csv, metrics.csv, aliases.csv
│   ├── manifests/                      # Danh sách tệp nguồn, hash và phiên bản snapshot
│   ├── raw/                            # Bản báo cáo tải về theo mã/năm, bỏ qua khi commit
│   ├── processed/                      # v1/facts.parquet, v1/sources.parquet
│   ├── sample/                         # Bộ dữ liệu nhỏ, được phép chia sẻ và chạy offline
│   └── qa/                             # Hưng · annotation_guide.md, train.jsonl, dev.jsonl
├── training/                           # Hưởng
│   ├── prepare_sft.py                  # Nhãn train → prompt/target, kiểm tra độ dài
│   ├── train_qlora.py                  # Huấn luyện adapter và lưu checkpoint
│   └── configs/                        # Checkpoint gốc, seed, LR, LoRA, batch, độ dài
├── evaluation/                         # Đức Anh
│   ├── run.py                          # Chạy từng cấu hình trên một split và snapshot
│   ├── score.py                        # Chấm số, bảng, nguồn, trạng thái và đơn vị
│   └── fixtures/                       # Bảng gốc, bảng biến thể, 20 ca nghiệm thu công khai
├── tests/
│   ├── unit/                           # Test parser, tính toán, bộ chấm theo từng hàm
│   ├── contracts/                      # JSON mẫu và kiểm tra tương thích các module
│   └── e2e/                            # Gửi request thực đến API và đối chiếu kết quả
├── artifacts/                          # adapters/, predictions/, runs/ sinh ra khi chạy
└── docs/
    ├── data_card.md                    # Đức và Hưng · nguồn tài chính, nhãn ngôn ngữ
    ├── model_card.md                   # Hưởng · model, cấu hình và giới hạn
    ├── results.md                      # Đức Anh · bảng M0–M4 và phân tích lỗi
    └── demo.md                         # Hoan · kịch bản trình diễn và cách chạy lại
```

**Quy ước lưu dữ liệu.** Commit mã nguồn, cấu hình, từ điển, manifest, bộ mẫu nhỏ và nhãn được phép chia sẻ. Báo cáo thô, snapshot đầy đủ và checkpoint lớn có đường dẫn tải cùng mã kiểm tra trong manifest. Đức Anh giữ câu và nhãn test kín ở nơi nhóm đánh giá kiểm soát; cung cấp đường dẫn test cho `evaluation/run.py` lúc chấm. `evaluation/fixtures/` là tập ví dụ công khai để mọi người phát triển. Các module dùng nguồn số chung từ snapshot do Đức bàn giao.

**Quy tắc phụ thuộc.** UI gọi `POST /query`. Tầng API chọn predictor và truyền dữ liệu vào engine. Bộ chấm sử dụng cùng hàm dự đoán và thực thi với API, còn đáp án tham chiếu được tính độc lập. `training/` chỉ đọc train/dev. Hoan quản lý định nghĩa kiểu dùng chung để cả năm người cùng đọc được một JSON mẫu. Với cấu trúc này, thay model chỉ cần thay triển khai `predict()`.

### Bắt đầu bằng những tệp nào?

| Mốc | Tệp cần có | Demo ngay được gì? |
|---|---|---|
| Cuối ngày 2 | `pyproject.toml`, `contracts/plan.py`, `contracts/result.py`, `data/sample/` và ví dụ trong `tests/contracts/` | Năm thành viên thống nhất request, dữ liệu, kế hoạch, câu trả lời và cách xử lý thiếu dữ liệu |
| Cuối tuần 1 | Thêm `snapshot.py`, `baselines.py`, bộ `engine/` tối thiểu cho lọc và tăng trưởng, `api/main.py`, `api/service.py`, `app/streamlit_app.py` và một test e2e | Nhập một câu trên UI, thấy kết quả Pandas và mở đúng nguồn; chạy lại được bằng CPU |
| Tuần 2–4 | Thêm linker, compiler đa bước, nhánh M2/M3, mã train và scorer hoàn chỉnh | So sánh các phương pháp trên cùng câu hỏi, theo dõi chi phí của từng thay đổi |
| Tuần 5–6 | Khóa manifest, config, adapter và tài liệu trong `docs/` | Một thành viên khác chạy lại demo và tái tạo được bảng điểm từ phiên bản đã chốt |

## 3. Một truy vấn xuyên suốt từ câu hỏi đến kết quả thật

**Câu hỏi:** “Doanh thu thuần hợp nhất FPT năm 2024 tăng bao nhiêu % so với 2023?” Báo cáo kết quả hoạt động kinh doanh hợp nhất quý IV của FPT có cả cột quý và cột lũy kế cả năm. Hai giá trị cả năm ở dòng mã 10 là 62.848.794.351.368 VND và 52.617.900.827.385 VND. Tính trên số gốc cho kết quả 19,44375082%, hiển thị **19,4%**. Chính hai cột quý cùng dòng là một bộ nhiễu tốt cho bài test. [Báo cáo hợp nhất của FPT, dòng mã 10](https://fpt.com/-/media/project/fpt-corporation/fpt/ir/information-disclosures/year-report/2025/january/20250124---fpt---bctc-hop-nhat-quy-4-nam-2024.pdf)

Ví dụ kế hoạch máy đọc được. Các hằng như `net_revenue` đến từ danh mục chỉ tiêu. Bộ thực thi kiểm tra kiểu, giá trị hợp lệ và sự hiện diện của đủ hai kỳ.

```json
{
  "status": "answer",
  "steps": [
    {"op": "filter", "ticker": ["FPT"], "scope": "consolidated", "period_kind": "FY", "fiscal_year": [2023, 2024], "metric_id": ["net_revenue"]},
    {"op": "growth_pct", "base_year": 2023, "target_year": 2024}
  ],
  "output": {"kind": "scalar", "unit": "percent", "decimals": 1}
}
```

Đoạn Pandas tương ứng trên bảng đã chuẩn hóa, lấy một phiên bản công bố cho mỗi quan sát. Khâu kiểm tra duy nhất, thiếu kỳ và mẫu số diễn ra trước phép chia. UI hiển thị mã này cùng các dòng nguồn thực tế đã dùng.

```python
rows = facts.loc[
    facts['ticker'].eq('FPT')
    & facts['scope'].eq('consolidated')
    & facts['period_kind'].eq('FY')
    & facts['metric_id'].eq('net_revenue')
    & facts['fiscal_year'].isin([2023, 2024]),
    ['fiscal_year', 'value_vnd', 'source_id'],
].set_index('fiscal_year', verify_integrity=True)

values = rows['value_vnd'].reindex([2023, 2024])
if values.isna().any() or values.loc[2023] <= 0:
    raise ValueError('Cần đủ hai kỳ và kỳ gốc dương cho phép tính này')
result_pct = 100 * (values.loc[2024] - values.loc[2023]) / values.loc[2023]
```

Trong báo cáo thường niên FPT 2024, hai dòng tổng tài sản và doanh thu đều ghi mức tăng 19,4% sau làm tròn. Một chương trình chọn nhầm dòng có thể trả đúng đáp số. Dùng ca này để minh họa vì sao cần chấm cả chỉ tiêu, kỳ, nguồn và kết quả trên bảng dữ liệu thay đổi có kiểm soát. [Báo cáo thường niên FPT 2024, bảng chỉ tiêu hoạt động kinh doanh](https://fpt.com/-/media/project/fpt-corporation/fpt/ir/general-meetings-of-shareholders/bao_cao_thuong_nien_fpt_2024.pdf)

### Hợp đồng đầu vào và đầu ra cho ví dụ FPT

Request tối thiểu của `POST /query` gồm `question` và `snapshot_id`. Máy chủ ghi lại model revision, phiên bản catalog và phiên bản dữ liệu. Một phản hồi thành công cung cấp số có kiểu để UI vẽ bảng hoặc biểu đồ, một chuỗi đã định dạng để đọc và danh sách bằng chứng cho phép đối chiếu. Ví dụ sau minh họa **các trường nghiệp vụ**; mã snapshot và mã bằng chứng là định danh mẫu.

```json
{
  "question": "Doanh thu thuần hợp nhất của FPT năm 2024 tăng bao nhiêu phần trăm so với 2023?",
  "snapshot_id": "demo-fy-v1"
}
```

| Trường phản hồi | Giá trị mong đợi trong ví dụ | Bên dùng |
|---|---|---|
| `status`, `kind` | `answer`, `scalar` | UI chọn bố cục; scorer quyết định cách chấm |
| `value`, `unit`, `display` | Khoảng `19.44375082`, `percent`, “19,4%” | Engine giữ giá trị đầy đủ; UI định dạng theo tiếng Việt |
| `source_ids` | Hai tham chiếu **ô dữ liệu** tại dòng mã 10 ứng với cột cả năm 2023 và 2024; có thể cùng URL | Mỗi tham chiếu mở đúng vị trí và hiện số gốc |
| `pandas_code`, `snapshot_id`, `latency_ms` | Mã truy vấn thực tế, phiên bản đã chạy, thời gian đo | Xem lại chương trình, tái hiện dự đoán và tính p95 |

Với bảng xếp hạng, trả `kind=table` cùng `columns`, `rows`, `unit`, số mã đủ điều kiện và các mã bị loại kèm lý do. Với `clarify`, trả `missing_slots` và một câu hỏi ngắn, chẳng hạn “Bạn muốn so sánh năm nào với năm nào?”. Một truy vấn sai cú pháp do mô hình sinh được ghi là `execution_error` trong log và tính là dự đoán sai; bộ chấm tách lỗi kỹ thuật này khỏi `no_data`.

### Phân biệt các trạng thái trước khi viết code

| Tình huống | Ai quyết định | Trạng thái và cách trả |
|---|---|---|
| “Lợi nhuận của FPT?” thiếu kỳ và loại lợi nhuận | NLU hoặc predictor | `clarify`, nêu đúng thông tin cần bổ sung |
| Đã hỏi rõ năm/chỉ tiêu nhưng snapshot không có số | Engine sau khi lọc | `no_data`, cho biết mã, chỉ tiêu và kỳ bị thiếu |
| Tính tỷ lệ với mẫu số bằng 0 | Engine sau khi ghép kỳ | `undefined`, giải thích và hiển thị hai toán hạng nếu có |
| Yêu cầu giá cổ phiếu thời gian thực hoặc dự báo ngoài phạm vi | Predictor/API | `unsupported`, mô tả phạm vi hệ thống có thể trả lời |
| Hỏi xếp hạng trong tập đã nạp, một mã thiếu kỳ gốc | Engine | `answer` kèm bảng, số mã đủ điều kiện và danh sách mã bị loại; nếu không mã nào đủ dữ liệu trả `no_data` |

## 4. Hai bộ dữ liệu nhóm cần xây

### 4.1 Kho số liệu tài chính

1. **Chọn nguồn.** Lấy báo cáo từ trang quan hệ nhà đầu tư của doanh nghiệp. Ưu tiên bản hợp nhất, kiểm toán năm. Có thể dùng CSV/XLSX hoặc nguồn dữ liệu có quyền truy cập làm bước nhập nhanh và đối soát với tài liệu gốc. Ưu tiên các bảng đọc được trực tiếp trong giai đoạn đầu. Ví dụ, trang FPT có các báo cáo từng năm. [Kho báo cáo nhà đầu tư FPT](https://fpt.com/vi/nha-dau-tu/bao-cao-thuong-nien)
2. **Lập danh mục.** `companies` chứa mã, tên chính thức, bí danh và ngành. `metrics` chứa `metric_id`, tên, bí danh, loại báo cáo, mã dòng tương ứng, loại giá trị (tiền, tỷ lệ, số trên mỗi cổ phần), tính chất thời điểm/trong kỳ và công thức cho chỉ tiêu dẫn xuất. Ví dụ phân biệt `profit_before_tax`, `profit_after_tax` và `profit_attributable_to_parent`. Lợi nhuận gộp chia doanh thu thuần là một chỉ tiêu dẫn xuất.
3. **Lưu từng quan sát.** Một dòng `facts` có mã, chỉ tiêu, kỳ bắt đầu/kết thúc, năm tài chính, loại kỳ, phạm vi hợp nhất/riêng lẻ, giá trị gốc, đơn vị gốc, giá trị chuẩn hóa, ngày công bố, phiên bản và `source_id`. `sources` chứa URL, tên báo cáo, trang PDF thực tế, bảng/dòng/cột, ngày thu thập, hash tệp. Các chỉ tiêu tiền có `value_vnd`; tỷ lệ và EPS có kiểu/đơn vị riêng. Số nguyên VND dùng kiểu có thể biểu diễn giá trị trống. Hoãn chuyển sang số thực tới bước tính tỷ lệ.
4. **Chuẩn hóa có kiểm chứng.** Giữ văn bản thô cùng giá trị sau chuyển đổi. Đọc dấu âm trong ngoặc, dấu phân nhóm hàng nghìn, dấu thập phân và hệ số nghìn/triệu/tỷ theo từng bảng. Phân biệt gạch ngang, ô trống, số 0 theo chú thích nguồn. Tách năm tài chính khỏi ngày công bố. Tách quý riêng khỏi lũy kế, khoản mục tại một thời điểm khỏi luồng tiền/doanh thu trong kỳ. Với số điều chỉnh hồi tố, lưu cả hai vintage, chọn bản hợp lệ tại ngày chốt dữ liệu và hiển thị phiên bản chọn.
5. **Nghiệm thu.** Xuất ma trận độ phủ công ty × năm × chỉ tiêu; liệt kê khóa trùng, giá trị thiếu và điều chỉnh. Hai người soát các ô đại diện của cả ba báo cáo, các mẫu có dấu âm/đơn vị đặc biệt, và 100% số dùng trong demo. Kiểm tra các đồng nhất thức thích hợp trong cùng phạm vi, cùng đơn vị với dung sai theo độ làm tròn nguồn. Xuất bảng phân tích Parquet chỉ đọc và tệp nguồn tra ngược. Nếu cuối tuần 1 PDF chưa ổn, nhập tay có hai người đối chiếu cho lát cắt đầu tiên.

### 4.2 Bộ câu hỏi tiếng Việt có nhãn chương trình

Một mẫu gồm `question_id`, `question_vi`, `family_id`, `variant_group`, `snapshot_id`, `gold_status`, `gold_plan`, `gold_pandas`, `expected_result`, `expected_unit`, `gold_source_ids`, `difficulty` và `origin`. Mẫu cần hỏi lại có danh sách thông tin cần làm rõ. Mẫu thiếu số có mô tả kỳ/chỉ tiêu bị thiếu. Lưu cả đáp án tính lại được và tham chiếu nguồn để phát hiện lỗi nhãn. Dùng cùng một mẫu dữ liệu cho baseline, fine-tune, bộ chấm và UI.

| Tập đề xuất | Kích thước | Cách tạo và sử dụng |
|---|---:|---|
| Train | 600 câu, có thể tăng tới 1.200 | Cả nhóm viết câu gốc. Sinh có kiểm soát các biến thể tên doanh nghiệp, kỳ, cách diễn đạt và tổ hợp thao tác sau khi chốt split. Gắn cờ human/template/model; loại mẫu sai hoặc trùng |
| Dev | 100 câu | Dùng chọn mô hình, prompt, ngưỡng làm rõ, và checkpoint; có đủ câu thiếu dữ liệu và câu đa bước |
| Test kín | 150 câu | Viết tự nhiên độc lập, ví dụ 100 câu trả được, 25 câu mơ hồ, 25 câu thuộc ba nhóm thiếu dữ liệu, ngoài phạm vi và phép tính không xác định. Đóng băng sớm; hai người kiểm tra đáp án. Ghi số lượng thực tế từng nhóm và từng độ khó |

Nhóm chia **theo họ kịch bản/ngữ nghĩa và nhóm paraphrase trước khi tăng cường**. Một họ có thể là “xếp hạng theo tăng trưởng chỉ tiêu giữa hai kỳ”. Một phép đơn lẻ vẫn có thể có trong train và test để đo ghép tổ hợp mới. Giữ thêm lát cắt dùng mã/kỳ chưa có trong câu train nhưng có dữ liệu trong snapshot lúc suy luận. Việc có số liệu của công ty trong kho truy vấn là cần thiết. Nội dung test, nhãn test và ví dụ gần trùng phải được loại khỏi prompt, bộ tìm ví dụ và huấn luyện. Chia ngân sách test giữa câu cùng phân phối và câu khó, ghi rõ từng nhóm; đối chiếu trùng bằng ID, câu chuẩn hóa và kiểm tra thủ công ứng viên gần nhau.

**Quy tắc gán nhãn:** Mỗi người viết 20 câu tự nhiên ở đợt đầu. Hai người độc lập gán nhãn 30–50 câu chung, thống nhất từ nào đủ rõ, trường nào cần hỏi lại, cùng kỳ tính thế nào. Báo cáo mức đồng thuận theo intent và độ khớp chỉ tiêu/kỳ trước phân xử. Đức Anh quản lý test, Đức kiểm nguồn. Hưng và Hưởng chỉ nhận train/dev cùng danh mục các loại truy vấn. Với nhãn train sinh tự động, chạy thử chương trình và kiểm tra ngẫu nhiên theo từng họ; “code chạy được” vẫn cần đối chiếu ngữ nghĩa với câu hỏi.

### 4.3 Từ một ô trong báo cáo đến một dòng dùng để huấn luyện

Đức quản lý ý nghĩa kế toán của `metric_id`; Hưng quản lý cách người Việt diễn đạt ý nghĩa đó. Hai bạn duyệt chung các cụm dễ nhầm trước khi gán nhãn hàng loạt. Quy ước trong bản đầu dùng số năm hợp nhất. Các câu thiếu phạm vi có thể dùng mặc định này nếu giao diện công khai mặc định và scorer áp dụng cùng chính sách.

| Tệp | Khóa hoặc trường tối thiểu | Kiểm tra khi bàn giao |
|---|---|---|
| `companies.csv` | `ticker, legal_name, sector` | Mã duy nhất, tên trong câu được liên kết về một mã hoặc trả về nhiều ứng viên |
| `metrics.csv` và `aliases.csv` | `metric_id, canonical_name, statement, value_kind`; mỗi alias trỏ về một hay nhiều metric hợp lệ | “LNST của cổ đông công ty mẹ” giữ riêng với “LNST hợp nhất”; không ép một cụm mơ hồ về một chỉ tiêu |
| `facts.parquet` | `ticker, metric_id, period_start, period_end, fiscal_year, period_kind, scope, value_vnd, source_id` cho chỉ tiêu tiền | Duy nhất theo mã, chỉ tiêu, kỳ và phạm vi sau khi áp dụng chính sách phiên bản. Mỗi giá trị dùng được có ô nguồn |
| `sources.parquet` | `source_id, report_id, url, page, table_name, row_label, column_label, raw_value, raw_unit, publication_date` | `source_id` định danh tới cấp ô. Hai năm cùng một URL vẫn truy đến hai ô khác nhau |
| `train.jsonl` / `dev.jsonl` | Một câu trên một dòng, mang ID họ câu, snapshot, mục tiêu, đơn vị, expected result và nguồn | Chạy được lời giải vàng; danh sách ID họ/nhóm diễn đạt khớp quy định chia tập |

**Ví dụ gán nhãn có chủ đích.** Tạo cặp “DT thuần FPT năm 2024 tăng bao nhiêu **tỷ đồng** so với 2023?” và “DT thuần FPT năm 2024 tăng bao nhiêu **phần trăm** so với 2023?”. Giữ nguyên mã, chỉ tiêu, nguồn và cặp năm; nhãn phép toán lần lượt là chênh lệch tiền và tăng trưởng tương đối. Đặt hai câu trong cùng nhóm split. Thêm cặp “biên gộp tăng bao nhiêu điểm phần trăm?” và “biên gộp tăng bao nhiêu phần trăm so với kỳ gốc?” để kiểm tra cùng một đại lượng nhưng hai phép tính.

**Ngân sách gán nhãn.** Trong 100 câu đợt đầu (mỗi người 20 câu), dành chỗ cho cả câu viết tắt, thiếu dấu, hai mã, hai kỳ và câu cần hỏi lại. Hưng chốt split trước tăng cường, ghi số câu người viết, số câu biến thể và số **họ câu khác nhau** cho từng tập. Mốc 600 train chỉ có ý nghĩa khi từng họ có đầu vào, phép toán và cách diễn đạt thật sự đa dạng. Một cấu hình test 150 câu có thể gồm 100 câu trả được, 25 câu mơ hồ, 15 câu thiếu dữ liệu, 5 câu ngoài phạm vi và 5 phép tính không xác định. Bản test bị khóa cùng snapshot, quy tắc làm tròn và danh sách nguồn tương đương được chấp nhận.

## 5. Kiến trúc và các phương án mô hình

| Tầng | Đầu vào → đầu ra | Quyết định triển khai |
|---|---|---|
| Hiểu câu hỏi | Tiếng Việt → thực thể, kỳ, chỉ tiêu ứng viên | Chuẩn hóa Unicode, giữ nguyên câu gốc và dấu tiếng Việt. Từ điển bí danh + regex cho mã/kỳ/đơn vị. Baseline TF-IDF từ và ký tự + logistic regression cho intent; ký tự giúp kiểm tra viết tắt hoặc thiếu dấu |
| Liên kết lược đồ | Cụm từ → mã chỉ tiêu và trường | Tạo tài liệu ngắn cho mỗi chỉ tiêu gồm tên, loại báo cáo, bí danh và ví dụ. So BM25/TF-IDF với embedding đa ngôn ngữ trên cùng tập ứng viên. Đo Recall@3 cho tất cả chỉ tiêu cần lấy. Cho phép trả nhiều ứng viên và hỏi lại khi chưa đủ căn cứ |
| Sinh chương trình | Câu + mô tả schema + chỉ tiêu ứng viên → kế hoạch có kiểu hoặc mã Pandas | Nhánh chính đề xuất sinh JSON gồm `filter`, `select`, `derive`, `group_agg`, `compare`, `growth_pct`, `sort`, `top_k`, `project`. Hợp đồng chứa kiểu, tham số, đơn vị, kỳ và thứ tự đầu ra. Một kế hoạch có thể kết hợp nhiều thao tác |
| Biên dịch và thực thi | Kế hoạch đã kiểm tra → mã Pandas, kết quả và nguồn | Bộ biên dịch ánh xạ từng thao tác sang hàm Pandas dùng `.loc`, `.merge`, `.groupby`, `.agg`, `.sort_values` theo mục đích. Ánh xạ trả cả biểu diễn mã hiển thị và lời gọi thực tế từ cùng một đặc tả. Kiểm tra cột, kiểu, lực lượng bản ghi khi ghép, giới hạn số dòng và thời gian |
| Trả lời | Kết quả có kiểu → số/bảng/biểu đồ và lời giải thích | Template tiếng Việt điền số từ kết quả thực thi. Hiển thị đơn vị, kỳ, phạm vi, độ phủ và hàng nguồn. Lưu trace gồm schema version, model revision, plan, runtime và status để tái hiện lỗi |

**M0 — luật và mẫu Pandas.** Phân tích ý định bằng từ khóa/regex và bảng bí danh. Tạo kế hoạch rồi chạy cùng engine với mô hình học. Đây là bản dự phòng có thể demo, đồng thời định lượng mức khó của corpus.

**M1 — máy học cổ điển.** TF-IDF + logistic regression cho intent; giữ nguyên slot extractor, linker và engine của M0. So sánh M0/M1 chỉ thay thành phần phân loại. Xem confusion matrix giữa tăng tuyệt đối, tăng tương đối và so sánh hai mã.

**M2 — sinh Pandas trực tiếp.** Cùng một checkpoint code model nhỏ, thử zero-shot rồi few-shot (3–5 ví dụ từ train). Đầu vào có schema, kiểu dữ liệu, danh mục phép toán, mô tả snapshot. Đầu ra là biểu thức/chương trình của tập con Pandas đã mô tả. Bộ đọc cú pháp chỉ nhận cấu trúc hỗ trợ rồi ánh xạ sang thao tác đã kiểm soát; chương trình ngoài tập này được tính là lỗi và báo tỷ lệ riêng. Mọi phương án dùng chung phạm vi phép toán. Đây là đối chứng sát tên đề tài và là phương án chính nếu môn học yêu cầu sinh thẳng mã. [Son và Thin, SemEval 2025](https://aclanthology.org/2025.semeval-1.51/)

**M3 — sinh kế hoạch rồi biên dịch ra Pandas.** Giữ nguyên checkpoint M2 và các ví dụ tương ứng; thay mục tiêu đầu ra bằng JSON có kiểu. Prompt quy định ba trạng thái `answer`, `clarify`, `unsupported`; tầng thực thi có thêm `no_data` và `undefined` khi truy vấn hợp lệ nhưng thiếu dữ liệu hoặc phép tính không xác định. Mô hình học cách hiểu tiếng Việt và phối hợp thao tác. Engine thực hiện số học. [RAT-SQL, ý tưởng liên kết biểu thức ngôn ngữ với lược đồ](https://aclanthology.org/2020.acl-main.677/)

**M4 — SFT/QLoRA trên M3.** Cùng tập phép toán, mẫu prompt, schema và engine. Thay đổi duy nhất so với M3 ở thí nghiệm chính là adapter được huấn luyện. Nếu tài nguyên cho phép, thêm M2-SFT trên các nhãn Pandas của chính tập train để kiểm tra tương tác giữa cách biểu diễn và fine-tuning. Chốt mô hình sản phẩm trên dev theo độ đúng, độ trễ và độ ổn định. [QLoRA, Dettmers và cộng sự](https://arxiv.org/abs/2305.14314)

**Ví dụ compositionality để bảo vệ:** “Trong các mã đã nạp, lấy 3 mã có biên lợi nhuận gộp tăng nhiều điểm phần trăm nhất từ 2023 đến 2024.” Chương trình phải lấy lợi nhuận gộp và doanh thu cùng kỳ cho từng mã, chia để tạo biên, ghép hai năm theo mã, trừ hai biên theo điểm phần trăm rồi xếp hạng. Chấm thêm thứ tự ở đầu ra, dữ liệu đủ của cả hai năm và bằng chứng của bốn toán hạng mỗi mã. Đây là ca có thể kiểm tra mô hình biết ghép các thao tác từng gặp riêng lẻ.

## 6. Cách train và fine-tune theo ngân sách sinh viên

| Bước | Thiết lập đề xuất | Mốc quyết định |
|---|---|---|
| Kiểm tra đường chạy | Thử `Qwen/Qwen2.5-Coder-1.5B-Instruct`; 30–50 mẫu train, 20 câu dev để dò lỗi tạo prompt và parse | Chạy benchmark bộ nhớ/độ trễ ngay trên GPU sẵn có; lưu model revision. Tiếng Việt tài chính cần được kiểm chứng trên dữ liệu của nhóm. [Model card](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct) |
| Chuẩn bị mẫu SFT | Input có câu hỏi, schema đã rút gọn, danh sách chỉ tiêu ứng viên và lịch sử cần thiết. Target là JSON chuẩn hoặc quyết định hỏi lại. Dùng cùng chat template lúc train và inference, mask loss phần prompt/padding | Kiểm tra 20 mẫu đã tokenize, tỷ lệ target bị cắt và token đặc biệt; chỉ số trả lời tài chính đi vào mô hình qua dữ liệu thực thi |
| Fine-tune | Transformers + PEFT. Thử QLoRA NF4 4-bit, LoRA rank 8 hoặc 16, alpha 16/32, dropout 0,05; LR bắt đầu 1e-4, 2–3 epoch, microbatch 1, accumulation 8–16, chiều dài 512 hoặc 768 token sau khi đo phân bố. Dùng mixed precision phù hợp thiết bị, gradient checkpointing khi cần | Chạy vài chục update đo VRAM/độ dài trước. Nếu GPU 6 GB thiếu bộ nhớ, giảm chiều dài và số ví dụ; giữ nguyên schema thiết yếu. Chạy huấn luyện trên GPU notebook khi cần, giữ baseline CPU cho demo. [QLoRA](https://arxiv.org/abs/2305.14314) · [PEFT](https://huggingface.co/docs/peft/developer_guides/quantization) |
| Chọn checkpoint | Decoding xác định cho bảng kết quả chính. Đánh giá dev sau từng epoch, chọn theo Execution Accuracy và F1 câu hỏi lại, ưu tiên cấu hình nhẹ khi điểm sát nhau | Dừng khi dev ngừng cải thiện; ghi seed, hash split, prompt, hyperparameter, GPU, VRAM, thời gian. Nếu đủ GPU, chạy 3 seed cho cấu hình cuối và báo biến thiên |
| Sửa lỗi có mục tiêu | Mỗi vòng gán 1 nguyên nhân chính cho 30–50 lỗi dev. Sai metric → thêm cặp chỉ tiêu gần nghĩa. Sai kỳ → thêm cặp quý/lũy kế hoặc hai năm đảo chiều. Sai cú pháp → kiểm grammar/compiler trước khi tăng model | Dùng lỗi dev để xác định dạng lỗi; viết ví dụ train mới từ nhóm train, kiểm tra không sao chép câu dev. Đóng băng chọn mô hình trước khi chấm test. Nếu SFT kém few-shot, báo kết quả và triển khai phiên bản có dev tốt hơn |

Nếu môn học nhấn mạnh gán nhãn chuỗi, chọn thêm **một** thí nghiệm BIO trên span `ORG/METRIC/PERIOD/UNIT` với CRF hoặc PhoBERT token classification. Gán nhãn offsets theo câu gốc, kiểm tra căn chỉnh sau tách từ/subword và đo entity-level F1. Đầu ra của thí nghiệm này phải thay được slot extractor để đo tác động lên truy vấn cuối. Nếu học phần nhấn mạnh embedding, ưu tiên ablation TF-IDF và E5 ở tầng linker. [PhoBERT](https://aclanthology.org/2020.findings-emnlp.92/) · [Hướng dẫn tách từ của tác giả](https://github.com/VinAIResearch/PhoBERT) · [Multilingual E5](https://arxiv.org/abs/2402.05672)

### Ba lần chạy phải lưu được để viết phần thực nghiệm

1. **Chạy trên 20 câu công khai.** Hưng xuất ứng viên chỉ tiêu và M0 đưa ra plan. Hưởng lấy chính 20 câu đó cho M2 và M3. Lưu đầu ra thô, lỗi parse, mã Pandas sau chuẩn hóa và thời gian. Nếu sai nhiều ở chỉ tiêu, kiểm từ điển; nếu đúng chỉ tiêu nhưng kết quả sai, kiểm kỳ và engine.
2. **Chạy trước và sau SFT trên dev.** Cùng checkpoint gốc, ngữ cảnh, tập phép toán, giới hạn token và số lần suy luận. Với bài huấn luyện, chỉ tính loss trên target. Chấm riêng câu một bước, hai bước, từ ba bước trở lên, cùng các trạng thái hỏi lại. So sánh theo cặp cùng question ID để chỉ ra M4 sửa được lỗi nào và làm hỏng câu nào M3 từng đúng.
3. **Chạy test kín để lập bảng nộp.** Mỗi lần chạy tạo một thư mục `artifacts/runs/<run_id>/`, chứa `config.json`, `predictions.jsonl`, `metrics.json` và log thời gian. Manifest ghi model revision, adapter, seed, hash snapshot, hash split, prompt và commit. Đức Anh chấm cùng phiên bản cho mọi cấu hình. Nếu phát hiện lỗi scorer sau lần chạy, tăng phiên bản scorer rồi chấm lại **mọi** dự đoán đã lưu.

**Điều kiện chọn bản demo.** Sửa trước lỗi trả sai số hoặc chỉ tiêu trong 20 ca công khai. Trong số cấu hình qua kiểm tra tích hợp, xét Execution Accuracy và tỷ lệ hỏi lại đúng trên dev, rồi đo độ trễ ngay trên máy thuyết trình. Nếu GPU không đủ cho QLoRA, chuyển pilot sang GPU notebook; giữ nhánh M0/M1 chạy CPU và báo rõ mô hình nào tạo ra câu trả lời trên UI. Nếu fine-tune không cải thiện, giữ đối chứng và phân tích lỗi đó trong báo cáo.

## 7. Bộ chấm và thiết kế thực nghiệm

| Đo cái gì | Chỉ số | Cách chấm và minh chứng |
|---|---|---|
| Hiểu tiếng Việt và lược đồ | Intent macro-F1, slot F1, Recall@3 chỉ tiêu | Chấm riêng mã, kỳ, scope, đơn vị. Báo theo nhóm viết tắt, không dấu, tên chỉ tiêu gần nghĩa và câu ghép |
| Sinh chương trình | Tỷ lệ parse được, tỷ lệ chạy được, khớp phép toán và đối số | Một chương trình chạy được nhưng chọn sai năm vẫn trượt phần ngữ nghĩa. So khớp plan sau chuẩn hóa khi các cách biểu diễn tương đương |
| Kết quả đầu cuối | Execution Accuracy@1 trên câu có đáp án | Tử số là số câu chọn đúng kết quả sau thực thi lần đầu, mẫu số là toàn bộ câu có đáp án. Lỗi parse, lỗi chạy và hỏi lại nhầm đều tính sai. Báo đúng/tổng, khoảng tin cậy và riêng số câu sai đơn vị/phạm vi |
| Tính đúng ngữ nghĩa | Test-suite accuracy trên tập có fixture; tỷ lệ đúng cả kết quả và nguồn | Chạy chương trình dự đoán và lời giải vàng độc lập trên dữ liệu gốc cùng 2–3 bảng biến thể hợp lệ. Chỉ tính đúng khi qua mọi bảng. So tập hàng/ô nguồn áp dụng cho từng phép toán, chấp nhận nguồn tương đương đã duyệt. [Zhong và cộng sự](https://aclanthology.org/2020.emnlp-main.29/) |
| Biết khi nào hỏi lại | Macro-F1 cho các trạng thái, tỉ lệ hỏi đúng thông tin thiếu, tỉ lệ trả lời sai chắc chắn | Chấm `clarify`, `no_data`, `unsupported`, `undefined` trên mẫu có nhãn tương ứng. Báo thêm coverage để một hệ thống luôn hỏi lại không được hưởng điểm cao |
| Trải nghiệm | p50/p95 thời gian từ lúc gửi đến khi có đáp án, RAM/VRAM cao nhất và tỷ lệ phản hồi thành công | Ghi rõ CPU/GPU, kích thước snapshot, số lần đo, cold/warm; tách thời gian mô hình khỏi thực thi Pandas |

**Quy tắc so đáp án.** Chuẩn hóa đơn vị trước. Với tiền gốc nguyên VND, so bằng trên số nguyên khi hai bên dùng cùng độ chính xác nguồn. Với kết quả tỷ lệ, so giá trị chưa làm tròn theo sai số khai báo hoặc theo độ chính xác của đáp án hiển thị (ví dụ ±0,05 điểm phần trăm nếu đáp án có 1 chữ số thập phân). Chấm cả loại đơn vị, kể cả `%` và `điểm phần trăm`. Với bảng, chuẩn hóa kiểu, nhãn cột, mã và kỳ; chỉ bỏ qua thứ tự khi người dùng không yêu cầu xếp hạng. Với đồng hạng, quy định trước trả đủ đồng hạng hoặc lấy đúng k và sắp phụ theo mã. Với mẫu số 0 trả `undefined`. Khi kỳ gốc âm, MVP trả chênh lệch tuyệt đối kèm lời giải thích hoặc hỏi có muốn áp dụng quy ước % cụ thể. Nếu trả chênh lệch, đánh dấu đây là thông tin bổ sung.

**Bộ test bắt lỗi nghiệp vụ.** (1) Hoán vị hàng và thêm một công ty có giá trị cao để phát hiện code phụ thuộc vị trí. (2) Thay doanh thu riêng một năm để phân biệt truy xuất và hằng số. (3) Giữ doanh thu, thay tổng tài sản để bắt chọn sai dòng. (4) Bỏ kỳ gốc, tạo mẫu số 0, kỳ gốc âm và đồng hạng. (5) Đặt hai dòng cùng mã/chỉ tiêu nhưng khác hợp nhất/riêng lẻ hoặc khác ngày công bố. (6) Tạo số quý và lũy kế khác nhau. (7) Đưa câu “từ 10% lên 12%” vào test: tăng 2 điểm phần trăm hoặc tăng tương đối 20% tùy câu hỏi. (8) Đổi đơn vị triệu/tỷ nhưng giữ giá trị kinh tế. Dùng bảng nhỏ do người độc lập tính tay làm oracle, không sinh toàn bộ gold từ compiler đang được chấm.

**Bảng thực nghiệm cần nộp.** Mỗi hàng M0–M4 ghi số mẫu, Execution Accuracy@1, test-suite accuracy trên cùng tập con, F1 hỏi lại, p95, số lỗi runtime. Thêm cột theo độ khó một bước/hai bước/đa bước và họ chưa gặp. Các bảng ablation lần lượt thay đúng một biến: M3 có/không thông tin liên kết chỉ tiêu, M3/M4 có/không SFT, M2/M3 đổi code/plan, M0/M1 đổi bộ phân loại. Giữ cố định snapshot, model khi thích hợp, ngân sách ngữ cảnh, số ví dụ và số lần thử. Nếu có thử lại, công bố riêng accuracy@1, sau một lượt sửa, tỷ lệ phải sửa và chi phí. Đưa top-3 lỗi thực của mỗi mô hình vào phụ lục, ví dụ nhầm LNST thuộc cổ đông công ty mẹ thành LNST toàn tập đoàn. Khi có ít mẫu, ghi mẫu số và dùng khoảng tin cậy bootstrap theo nhóm câu hỏi gốc để tránh coi paraphrase là độc lập.

**Mốc tự nghiệm thu đề xuất:** engine và bộ chấm phải qua 20/20 ca công khai khi cấp đúng chương trình hoặc trạng thái vàng. Báo riêng số ca end-to-end mà từng mô hình qua được. Sau pilot, nhóm có thể đặt đích ở 80/100 câu trả được trong test, F1 hỏi lại ≥0,80 và mọi số liệu trong demo truy về được nguồn. Chốt đích trước mở test; báo kết quả đo được dù thấp hơn mục tiêu. Thử nghiệm phải có phân tích so với baseline, kể cả khi phương án phức tạp hơn không thắng.

### 7.1 Hai mươi ca nghiệm thu công khai có đáp án

Đức Anh tạo bảng dưới làm fixture tổng hợp, đơn vị tỷ đồng. `M_A`, `M_B` và `M_C` là ba mã minh họa. Tất cả hàng mặc định là số năm hợp nhất. Khi nhập vào `facts`, chuyển cột tiền về VND và cấp một `source_id` riêng cho từng ô. So sánh giữa các năm phải dùng đúng kỳ tài chính. Bộ test này phục vụ lập trình và tích hợp; tập test kín 150 câu được viết riêng.

| Mã | Năm | Doanh thu thuần | Lợi nhuận gộp | LNST |
|---|---:|---:|---:|---:|
| M_A | 2023 | 100 | 20 | 10 |
| M_A | 2024 | 120 | 30 | 12 |
| M_B | 2023 | 200 | 50 | 16 |
| M_B | 2024 | 220 | 66 | 12 |
| M_C | 2023 | 0 | 0 | −2 |
| M_C | 2024 | 90 | 18 | 3 |

Quy ước cho bộ này: khi người dùng yêu cầu top-k, lấy đúng k kết quả nếu đủ, hòa điểm thì mã tăng dần. Với phép tăng trưởng theo phần trăm, kỳ gốc bằng 0 trả `undefined`. Với LNST chuyển từ lỗ sang lãi, có thể trả chênh lệch tuyệt đối khi người dùng hỏi số tiền.

| ID | Câu hỏi hoặc điều kiện | Đáp án phải kiểm tra |
|---|---|---|
| T01 | Doanh thu thuần M_A năm 2024 bằng bao nhiêu tỷ đồng? | 120 tỷ, có đúng ô nguồn |
| T02 | Cùng câu T01, đổi đơn vị sang triệu đồng | 120.000 triệu |
| T03 | Doanh thu M_A tăng bao nhiêu tỷ từ 2023 đến 2024? | 20 tỷ |
| T04 | Doanh thu M_A năm 2024 tăng bao nhiêu % so với 2023? | 20% |
| T05 | Doanh thu M_A năm 2023 thay đổi bao nhiêu % so với 2024? | Khoảng −16,67%; chứng minh đúng năm ở mẫu số |
| T06 | Biên lợi nhuận gộp M_A năm 2024 là bao nhiêu? | 25%; bằng chứng gồm lợi nhuận gộp và doanh thu |
| T07 | Biên gộp M_A tăng bao nhiêu điểm phần trăm từ 2023 đến 2024? | 5 điểm phần trăm |
| T08 | Cũng hai năm, biên gộp M_A tăng bao nhiêu % so với mức gốc? | 25% tương đối |
| T09 | Mã nào có LNST cao nhất năm 2024? Trả tất cả mã đồng hạng | M_A và M_B, cùng 12 tỷ |
| T10 | Lấy đúng top 2 theo doanh thu 2024 | M_B 220, M_A 120, theo thứ tự đó |
| T11 | Xếp các mã theo tăng trưởng doanh thu 2024 so với 2023 | M_A 20%, M_B 10%; nêu M_C bị loại vì mẫu số 0, độ phủ 2/3 |
| T12 | Tăng trưởng doanh thu riêng M_C năm 2024 so với 2023? | `undefined`; hiển thị kỳ gốc bằng 0 |
| T13 | Doanh thu thuần M_A năm 2021? | `no_data` |
| T14 | “Lợi nhuận M_A tăng bao nhiêu?” | `clarify`; hỏi loại lợi nhuận, kỳ và cách đo khi còn thiếu |
| T15 | Giá cổ phiếu M_B hiện tại? | `unsupported` |
| T16 | LNST M_C năm 2024 thay đổi bao nhiêu tỷ so với 2023? | Tăng 5 tỷ; số kỳ gốc là −2 tỷ |
| T17 | Lập bảng doanh thu thuần M_B theo năm 2023–2024 | Hai hàng đúng thứ tự 2023 → 200, 2024 → 220 tỷ |
| T18 | Thêm một dòng riêng lẻ M_A năm 2024 có doanh thu 999 rồi chạy T01 | Vẫn 120 tỷ hợp nhất, không chọn dòng riêng lẻ |
| T19 | Bỏ riêng hàng M_A năm 2023 rồi chạy T04 | `no_data`, chỉ rõ thiếu kỳ gốc |
| T20 | Đổi doanh thu M_A năm 2024 từ 120 thành 140 rồi chạy T04 | Đổi thành 40%; bắt chương trình ghi cứng đáp số |

T01–T17 chấm đầu ra của API. T18–T20 chạy được cả ở tầng engine và đầu cuối trên một bản sao fixture. Bổ sung unit test cho khóa quan sát trùng, danh sách rỗng và dòng bị xáo thứ tự. Khi có test trượt, lưu question ID, cấu hình, plan hoặc code ban đầu, dòng nguồn máy chọn, dòng nguồn đúng và người phụ trách sửa. Nhờ vậy nhóm biết sửa trích dữ liệu, hiểu câu hỏi, sinh chương trình hay chấm đáp án.

## 8. Phân công năm thành viên và hợp đồng bàn giao

Phân vai chuyên môn dưới đây là một đề xuất. Hoan phụ trách phần tích hợp phù hợp với kinh nghiệm FastAPI. Bốn vai trò còn lại có thể hoán đổi theo thế mạnh thực tế, với nguyên tắc từng module và từng sản phẩm nghiệm thu có một người chịu trách nhiệm cuối.

| Thành viên | Phạm vi sở hữu | Đầu ra và người nhận | Kiểm tra để đóng việc |
|---|---|---|---|
| **Hoan** — trưởng kỹ thuật, Pandas engine và API | `src/finassistant/{contracts,engine,api}/` quản lý Plan/Result, compiler, provenance, API và đóng gói phiên bản chạy demo | Bàn schema và fixture cho cả nhóm từ ngày 2; bàn endpoint với dữ liệu mẫu cho Đức Anh từ tuần 1; ghép mô hình do Hưởng xuất | Kế hoạch vàng chạy trên fixture, phép ghép không nhân bản dòng; chương trình hiển thị khớp kết quả chạy; một lệnh dựng bản demo |
| **Đức** — dữ liệu tài chính | `src/finassistant/data_pipeline/`, `data/catalog/`, `data/manifests/` quản lý nguồn, ánh xạ chỉ tiêu, chuẩn hóa, kiểm phiên bản, đơn vị và độ phủ | Bàn `facts.parquet`, `metrics`, `companies`, `sources` và manifest có phiên bản cho Hoan và Hưng; cùng Đức Anh xác minh số vàng | Truy ngược mọi số demo; có ca quý/lũy kế, âm, thiếu, điều chỉnh; khóa snapshot duy nhất đúng cấp độ quan sát |
| **Hưng** — dữ liệu ngôn ngữ và NLP baseline | `src/finassistant/nlu/`, `data/qa/` quản lý hướng dẫn nhãn, tách họ câu, từ điển ngôn ngữ, luật, TF-IDF/intent và schema linker | Bàn hàm `link(question, catalog)`, train/dev JSONL và baseline M0/M1 cho Hưởng và Hoan; Đức duyệt ánh xạ thuật ngữ | Báo cáo intent/slot/linking trên dev, so ít nhất hai cách xử lý viết tắt hoặc không dấu; có danh sách nhóm paraphrase |
| **Hưởng** — mô hình sinh chương trình | `src/finassistant/models/`, `training/` quản lý nhánh sinh Pandas trực tiếp, zero/few-shot, SFT/QLoRA, kiểm lỗi mô hình | Bàn `predict` theo contract, prompt, adapter, cấu hình, log, dự đoán dev và model card cho Hoan; Đức Anh nhận bản chốt để chấm | Chạy lại được từ checkpoint; trả đúng cấu trúc hoặc trạng thái lỗi; có so sánh cùng checkpoint trước/sau SFT, đo VRAM và latency |
| **Đức Anh** — đánh giá độc lập và giao diện | `evaluation/`, `tests/e2e/`, `app/` phụ trách viết scorer, fixtures phản thực, giữ test kín, dựng Streamlit và các ca demo | Bàn scorer + test công khai nhỏ cho nhóm từ tuần 1; giao báo cáo test cuối, UI và kịch bản bảo vệ. Đức đối soát nhãn tài chính | Scorer phân biệt các lỗi tiền/%/thứ tự, test changelog rõ; UI hiển thị số, đơn vị, nguồn, Pandas, câu làm rõ và lỗi dữ liệu |

Mọi người cùng đóng góp câu hỏi và viết phần phương pháp tương ứng. Đức Anh điều phối viết test kín với Đức; Hưng và Hưởng không xem nhãn test trong giai đoạn chọn mô hình. Khi UI cần trợ giúp ở tuần cuối, Hoan phụ trách đóng gói và nối API, còn Đức Anh giữ quyền duyệt UI/scorer. Báo cáo chia thành 5 phần có người soạn riêng; một người ghép sau cùng.

**Bốn giao diện thống nhất ngay ngày 2**

| Giao diện | Bên cung cấp → bên dùng | Trường/bất biến cần chốt |
|---|---|---|
| `load_snapshot(version)` | Đức → Hoan, Hưng, Đức Anh | `facts`, `metrics`, `companies`, `sources`; khóa quan sát, dtype, unit, scope, `snapshot_id` và chính sách chọn phiên bản |
| `link(question, catalog)` | Hưng → Hưởng, Hoan | Mã doanh nghiệp, kỳ, top-k chỉ tiêu, độ tin cậy, cụm từ gốc; trường nào được bỏ trống |
| `predict(question, context)` | Hưởng hoặc Hưng → Hoan | `Prediction` với loại `pandas` (M2), `plan` (M0/M1/M3/M4), `clarify` hoặc `unsupported`. Context chứa schema, snapshot, kết quả linker, trạng thái hội thoại nếu bật |
| `POST /query` và `Result` | Hoan → Đức Anh | `status`, `kind`, `value` hoặc `columns/rows`, `unit`, `pandas_code`, `source_ids`, `snapshot_id`, `message`, `latency_ms`. Nguồn của xếp hạng gồm khả năng truy được tập so sánh |

**Cách tránh conflict.** Mỗi người dùng một nhánh ngắn theo issue; PR ghi đầu vào, đầu ra, fixture và điều kiện nghiệm thu. Chủ module duyệt thay đổi, người dùng trực tiếp của giao diện duyệt mọi đổi schema. Hoan quản lý phiên bản contract từ `v1` và bổ sung trường tương thích khi được; nếu đổi kiểu hay ý nghĩa trường, tạo `v2`, cập nhật fixture và adapter trong cùng PR. Chạy CI cho schema, sample snapshot, engine và scorer trên mỗi PR. Tách file báo cáo theo mục, cấu hình thí nghiệm theo run ID. Dữ liệu lớn và trọng số được tham chiếu bằng manifest/hash. Tích hợp hai lần mỗi tuần; mỗi lần chạy cùng 10–20 câu mẫu từ API tới UI. Chạy mô hình bằng stub khi chưa có checkpoint để mọi người làm song song.

### 8.1 Công việc có thể giao ngay sau buổi họp đầu

| Issue · người chính | Nhận đầu vào từ ai | Bàn giao theo thứ tự | Ai kiểm tra và bằng cách nào |
|---|---|---|---|
| ENG-01 · Hoan | Cả nhóm chọn T01, T04, T14 | Ngày 1 soạn request/plan/result; ngày 2 phát fixture JSON thành công, hỏi lại, thiếu dữ liệu; ngày 3 nối bộ lọc và phép tính với API | Đức Anh gọi API từ test hợp đồng; Hưởng tạo được kết quả đúng kiểu từ predictor giả lập |
| DATA-01 · Đức | Hoan chốt khóa, đơn vị và source ID | Chọn 2 mã; lưu manifest nguồn; lấy 2 năm × 5 chỉ tiêu cho mỗi mã; xuất dữ liệu mẫu và bảng đối soát từng ô | Hưng thử map 5 chỉ tiêu, Đức Anh chọn ngẫu nhiên 5 số mở về đúng dòng/cột |
| NLU-01 · Hưng | Đức đưa danh mục chỉ tiêu nháp | Cùng nhóm nhận 100 câu gốc; gán intent/slot cho đợt đầu; phát bảng alias và M0 cho tra cứu, tăng trưởng, hỏi lại | Hoan chạy cùng câu có dấu, viết tắt và câu mơ hồ; Đức kiểm các alias có nhiều nghĩa |
| MODEL-01 · Hưởng | Hoan đưa hợp đồng; Hưng cung cấp ví dụ thuộc train | Viết predictor giả lập ngày 2; dùng checkpoint nhỏ chạy zero-shot trên dev pilot; lưu đầu ra thô và lỗi; sau đó thêm few-shot và pilot SFT | Hưng rà lỗi liên kết; Hoan kiểm nhánh sinh code/plan; Đức Anh nhận dự đoán định dạng chuẩn |
| EVAL-01 · Đức Anh | Hoan đưa schema; Đức xác minh số | Tạo fixture 3 mã và scorer số, bảng, trạng thái; nối UI vào phản hồi giả lập; chạy đủ 20 ca khi pipeline sẵn sàng | Đức tính tay các số vàng; Hoan chạy end-to-end từ máy khác |

**Hai lần bàn giao dễ bị lỡ.** (1) Đức phải cung cấp sớm danh mục chỉ tiêu và 10–20 dòng mẫu, kể cả khi kho đầy đủ còn đang nhập. Hưng và Hưởng dùng chúng để làm linker/prompt. (2) Đức Anh phải phát hành luật chấm và ca công khai ngay tuần 1 để Hoan biết kết quả API cần lưu bằng chứng tới mức nào.

**Ví dụ thay đổi xuyên module.** Nếu thêm “lợi nhuận thuộc cổ đông công ty mẹ”, Đức thêm một mã chỉ tiêu và nguồn; Hưng thêm alias và ca phân biệt; Hưởng làm mới danh mục dùng trong prompt; Đức Anh thêm câu nghiệm thu. Khi biểu diễn của `metric_id` đã đủ, Hoan chỉ chạy lại test tương thích. Nếu phải thêm một kiểu toán tử, Hoan và bên dùng chốt phiên bản hợp đồng trước rồi mỗi thành viên mới cập nhật module mình sở hữu.

## 9. Kế hoạch sáu tuần và thứ tự cắt phạm vi

| Tuần | Hoan | Đức | Hưng | Hưởng | Đức Anh | Bằng chứng cuối tuần |
|---|---|---|---|---|---|---|
| 1 | Chốt contract, engine lọc, API mẫu | 2 mã × 2 năm × 5 chỉ tiêu | 5 intent, từ điển, mẫu nhãn | Đo checkpoint nhỏ, prompt và stub | Viết scorer số/bảng, UI mẫu | Một câu FPT chạy từ UI tới đúng nguồn; 20 câu nghiệm thu mẫu |
| 2 | Hoàn thành các phép so sánh, tỷ lệ, top-k | Mở rộng mã/năm, kiểm đơn vị | M0/M1, hướng dẫn nhãn, dựng train/dev | M2 zero/few-shot sinh Pandas | Test kín đợt 1, test dữ liệu thiếu | Báo cáo dev baseline; snapshot v1 có manifest |
| 3 | Compiler đa bước, phục hồi trace lỗi | Bổ sung báo cáo lưu chuyển tiền, kiểm nguồn | Hoàn tất train/dev v1 và chỉ tiêu dễ nhầm | M3 sinh plan, đối chiếu với M2 | Khóa test/fixture; rà UI nguồn và kỳ | Chạy được ít nhất một câu đa bước bằng hai cách |
| 4 | Tích hợp model adapter và mã hiển thị | Kiểm chéo các số liệu chênh lệch | Phân tích lỗi dev theo nhóm | M4 QLoRA, so checkpoint | Đo độ trễ, thêm kiểm thử biến thể | Bảng M0–M4 trên dev, thống kê chi phí |
| 5 | Khóa API/snapshot, đóng gói | Data card, báo cáo độ phủ | Ablation linker, đóng băng prompt | Chốt checkpoint, lưu dự đoán | Chạy test kín theo giao thức, tổng hợp lỗi | Bảng kết quả có mẫu số và nguyên nhân lỗi |
| 6 | Bản release, chạy thử trên máy khác | Trình bày nguồn và đối soát | Trình bày NLP và baseline | Trình bày SFT và ablation | Demo UI, quay video dự phòng | Repo chạy lại được, báo cáo, slide, video, 5 người diễn tập |

Nếu chỉ có 3–4 tuần, giữ dữ liệu năm, 4–6 mã, tra cứu/so sánh/tăng trưởng/top-k, baseline, một cấu hình few-shot, một pilot SFT và test kín. Cắt hội thoại, OCR tổng quát và biểu đồ phức tạp trước. Nếu có 7–8 tuần, chỉ thêm một nhánh mở rộng sau khi có điểm dev và demo chạy xuyên suốt.

### 9.1 Thứ tự chạy dự kiến từ một bản clone mới

Các lệnh PowerShell sau là **giao diện đề xuất cho README khi nhóm hoàn thành các module**. Đặt các đường dẫn tương đối từ gốc repository. Tệp `pyproject.toml` khai báo các nhóm phụ thuộc `app`, `dev`, `train`; nhóm `train` chỉ cần trên máy huấn luyện. Bản chạy mẫu mặc định dùng `data/sample/` và M0 để giảng viên khởi động được trên CPU.

```powershell
python -m pip install -e ".[app,dev]"
python -m pytest tests/contracts tests/unit tests/e2e
python -m uvicorn finassistant.api.main:app --port 8000
```

Ở terminal PowerShell thứ hai, chạy `python -m streamlit run app/streamlit_app.py`. Sau khi tạo snapshot v1 dùng để gán nhãn dev, giao diện dòng lệnh đề xuất để chạy đối chứng từ gốc repository là `python -m evaluation.run --model m0 --split data/qa/dev.jsonl --snapshot data/processed/v1 --output artifacts/runs/m0-dev`. Trước buổi bảo vệ, đổi sang đúng predictor đã chốt trên dev, kiểm trên máy trình chiếu và hiển thị model ID cạnh kết quả. Bản trong README cần ghi rõ cách chọn predictor và tải đúng snapshot, adapter theo manifest.

| Khi gặp vấn đề | Quyết định để giữ tiến độ | Người xử lý |
|---|---|---|
| Hết tuần 1 mà PDF bóc sai cột | Nhập tay lát cắt 2 mã × 2 năm có hai người đối soát; giữ trích xuất tự động cho nguồn đọc ổn | Đức và Đức Anh |
| Nhiều câu dev chọn sai chỉ tiêu gần nghĩa | Thêm ca đối chiếu cùng mã/kỳ và đánh giá Recall@3; chỉ sửa prompt sau khi biết linker có đưa đúng ứng viên hay chưa | Hưng và Hưởng |
| Mô hình hay sinh mã ngoài tập hỗ trợ | Công bố tỷ lệ này riêng; kiểm trên 20 câu công khai, điều chỉnh mô tả tập phép toán và thử nhánh sinh plan | Hưởng và Hoan |
| Cuối tuần 4 mô hình lớn chậm hoặc SFT kém few-shot | Chọn bản có kết quả dev và độ trễ tốt hơn; vẫn nộp log, cấu hình và phân tích kết quả SFT | Hưởng và Đức Anh |
| Demo ra đúng đáp số nhưng sai nguồn | Dừng tăng tính năng; xác định sai ở ETL, linker hay engine bằng trace, thêm fixture phân biệt hai chỉ tiêu | Hoan điều phối với chủ module tương ứng |

## 10. Mở rộng có câu hỏi nghiên cứu rõ ràng

1. **Hội thoại hai lượt.** Sau “Doanh thu FPT 2024 là bao nhiêu?”, hỏi “Còn năm trước?” hoặc “Thế còn VNM?”. Lưu trạng thái ticker, kỳ, metric, scope và chỉ cập nhật slot bị thay. Viết khoảng 40 cặp kiểm thử, gồm cả đổi chủ đề; đo slot accuracy và tỷ lệ cả hai lượt đều đúng. Tham khảo ngữ cảnh nhiều lượt từ ARCADE và câu hỏi số tài chính trong ConvFinQA. [ARCADE](https://aclanthology.org/2023.acl-long.9/) · [ConvFinQA](https://aclanthology.org/2022.emnlp-main.421/)
2. **Khái quát hóa sang schema mới.** Tạo hai schema khác nhau cho cùng tập dữ kiện (ví dụ tên cột Việt/Anh hoặc rút gọn). Cho mô hình mô tả schema tại suy luận. Giữ nội dung câu hỏi và số liệu cố định, đo mức suy giảm khi đổi lược đồ, có/không dùng schema linking. [RAT-SQL](https://aclanthology.org/2020.acl-main.677/)
3. **Sửa chương trình một lần với phản hồi có cấu trúc.** Khi phát hiện sai kiểu, cột không có hoặc đầu ra không hợp lệ, trả mã lỗi và schema liên quan để mô hình sửa một lượt. Ghi riêng accuracy@1, sau sửa, tỷ lệ sửa thành công, số truy vấn đúng ban đầu bị đổi nhầm và chi phí. [Son và Thin, SemEval 2025](https://aclanthology.org/2025.semeval-1.51/)

## 11. Kiến thức môn học và hồ sơ bảo vệ

| Kiến thức NLP | Minh chứng nên mang vào buổi bảo vệ |
|---|---|
| Tiền xử lý và biểu diễn văn bản | Ví dụ có/không dấu, viết tắt, tokenization; tác động lên TF-IDF hoặc schema linking |
| Phân loại và trích xuất thực thể | Confusion matrix intent; F1 theo slot mã, kỳ, chỉ tiêu, đơn vị; ví dụ lỗi biên span nếu làm BIO |
| Ngữ nghĩa và liên kết lược đồ | Một câu chứa “lãi ròng” có nhiều ứng viên; top-k, quy tắc hỏi lại và cải thiện khi bật linker |
| Transformer và sinh có điều kiện | Cùng câu chạy few-shot, mô hình sau SFT, mã sinh trực tiếp và plan biên dịch; nêu chính xác tham số nào học |
| Đánh giá mô hình | Split theo họ, thử thách tổ hợp mới, ablation một biến, chấm thực thi trên nhiều bảng, phân tích lỗi và chi phí |
| Sản phẩm tích hợp | Một câu hỏi mới do người xem đưa, kết quả có đơn vị, mã Pandas và số liệu gốc; có ca hỏi lại, thiếu dữ liệu và lỗi được phát hiện |

**Gói nộp đề xuất:** README hướng dẫn chạy và tải snapshot/checkpoint, bản demo khởi động được với dữ liệu mẫu, data card và model card, tập đánh giá có phiên bản, script tái tạo bảng kết quả, báo cáo và slide. Kiểm tra quyền phân phối trước khi đưa bản báo cáo gốc hoặc tập dữ liệu ngoài vào repo; có thể phân phối manifest và mẫu nhỏ theo quyền sử dụng. Nếu có đề cương môn/rubric chi tiết, thêm cột tên chương, tiêu chí chấm và dẫn chứng tương ứng vào bảng trên.

**Kịch bản bảo vệ 8–10 phút đề xuất.** Hoan mở bằng câu hỏi thực và hợp đồng đầu ra; Đức mở đúng dòng/cột của báo cáo; Hưng cho thấy từ tiếng Việt được liên kết với chỉ tiêu; Hưởng chạy một câu có hai thao tác và trình bày bảng few-shot/SFT; Đức Anh cho thay dữ liệu ở một fixture để phát hiện chương trình trả đúng số do trùng hợp. Dành phút cuối cho một câu tự do, một hạn chế đo được và phương án khắc phục từ lỗi dev.

### Các công trình nên đọc theo thứ tự

| Công trình | Giá trị đối với đề tài | Cách dùng |
|---|---|---|
| Son và Thin, SemEval 2025; báo cáo tổng kết DataBench | Câu tự nhiên → Python/Pandas → kết quả trên bảng | Đọc đầu tiên để thiết kế baseline trực tiếp và so cách đưa metadata vào prompt. [Bài hệ thống](https://aclanthology.org/2025.semeval-1.51/) · [Bài tổng kết](https://aclanthology.org/2025.semeval-1.324/) |
| Yin và cộng sự, ACL 2023, ARCADE | Benchmark sinh mã Pandas trong notebook, 1.078 bài | Tham khảo cách chấm chương trình cùng input và biểu diễn trạng thái khi mở rộng nhiều lượt. [Bài báo](https://aclanthology.org/2023.acl-long.9/) |
| Wang và cộng sự, ACL 2020, RAT-SQL | Liên kết từ ngữ với schema | Áp dụng ý tưởng linking cho tên chỉ tiêu, cột và bí danh tiếng Việt; nhiệm vụ gốc là Text-to-SQL. [Bài báo](https://aclanthology.org/2020.acl-main.677/) |
| Chen và cộng sự, EMNLP 2021, FinQA; Lê Ngọc Toàn và cộng sự, VLSP 2025, ViNumQA | Câu hỏi tài chính có chương trình số học và đáp án. ViNumQA có tiếng Việt | Học cách gán nhãn phép toán và chấm số. Muốn dùng dữ liệu ngoài để train thì kiểm tra quyền, đối chiếu ngôn ngữ/schema và loại câu test trùng. [FinQA](https://aclanthology.org/2021.emnlp-main.300/) · [ViNumQA](https://aclanthology.org/2025.vlsp-1.25.pdf) |
| Zhong, Yu và Klein, EMNLP 2020 | So kết quả trên nhiều bộ dữ liệu để kiểm tra tương đương ngữ nghĩa của truy vấn SQL | Chuyển nguyên lý sang DataFrame và fixture tài chính. [Bài báo](https://aclanthology.org/2020.emnlp-main.29/) |
| Dettmers và cộng sự, NeurIPS 2023, QLoRA | Huấn luyện adapter trên trọng số nền lượng tử hóa | Thu hẹp thí nghiệm theo GPU thực, đo hiệu quả SFT qua execution accuracy. [Bài báo](https://arxiv.org/abs/2305.14314) |
