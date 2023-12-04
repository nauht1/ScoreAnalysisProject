import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# st.title("Thu thập, phân tích và so sánh điểm thi THPT 2023 của THPT Phan Việt Thống và tỉnh Tiền Giang")
st.markdown("<h1 style='text-align: center; font-size: 24px; color: blue;'>Thu thập, phân tích và so sánh điểm thi THPT 2023 của THPT Phan Việt Thống và tỉnh Tiền Giang</h1>", unsafe_allow_html=True)

#Đọc dữ liệu điểm của tỉnh Tiền Giang
diemTG_raw = pd.read_csv('raw_data/data_TienGiang.csv', encoding = 'utf-8')

#Bà Rịa Vũng Tàu
diemBRVT_raw = pd.read_csv('raw_data/data_BaRiaVungTau.csv', encoding = 'utf-8')

#Bến Tre
diemBenTre_raw = pd.read_csv('raw_data/data_BenTre.csv', encoding = 'utf-8')

#Bình Dương
diemBinhDuong_raw = pd.read_csv('raw_data/data_BinhDuong.csv', encoding = 'utf-8')

#Vĩnh Long
diemVinhLong_raw = pd.read_csv('raw_data/data_VinhLong.csv', encoding = 'utf-8')

diemPVT = pd.read_excel('clean_data/clean_data_PhanVietThong.xls')
diemPVT = diemPVT.fillna(-1)

diemTG = pd.read_csv('clean_data/clean_data_TienGiang.csv', encoding = 'utf-8')
diemTG = diemTG.fillna(-1)

diemBaRiaVungTau = pd.read_csv('clean_data/clean_data_BaRiaVungTau.csv', encoding = 'utf-8')
diemBaRiaVungTau = diemBaRiaVungTau.fillna(-1)

diemBenTre = pd.read_csv('clean_data/clean_data_BenTre.csv', encoding = 'utf-8')
diemBenTre = diemBenTre.fillna(-1)

diemBinhDuong = pd.read_csv('clean_data/clean_data_BinhDuong.csv', encoding = 'utf-8')
diemBinhDuong = diemBinhDuong.fillna(-1)

diemVinhLong = pd.read_csv('clean_data/clean_data_VinhLong.csv', encoding = 'utf-8')
diemVinhLong = diemVinhLong.fillna(-1)

#TienGiang
list_of_subjects = ['Toan', 'Van', 'Ngoai Ngu', 'Vat Ly', 'Hoa Hoc', 'Sinh Hoc', 'Lich Su', 'Dia Ly', 'GDCD']
diemTG['So mon thi'] = (diemTG[list_of_subjects] != -1).sum(axis=1).tolist()

#PhanVietThong
# Thêm cột "KHTN"
diemPVT['DTBTN'] = diemPVT[['Vat Ly', 'Hoa Hoc', 'Sinh Hoc']].mean(axis=1).round(2)
# Thêm cột "KHXH"
diemPVT['DTBXH'] = diemPVT[['Lich Su', 'Dia Ly', 'GDCD']].mean(axis=1).round(2)
#Thêm cột "So mon thi"
diemPVT['So mon thi'] = (diemPVT[list_of_subjects] != -1).sum(axis=1).tolist()

#Đếm số lượng thí sinh thi của mỗi môn
#TienGiang
count_toan = diemTG[diemTG['Toan'] >= 0].count()['Toan']
count_van = diemTG[diemTG['Van'] >= 0].count()['Van']
count_ngoai_ngu = diemTG[diemTG['Ngoai Ngu'] >= 0].count()['Ngoai Ngu']

count_vat_ly = diemTG[diemTG['Vat Ly'] >= 0].count()['Vat Ly']
count_hoa_hoc = diemTG[diemTG['Hoa Hoc'] >= 0].count()['Hoa Hoc']
count_sinh_hoc = diemTG[diemTG['Sinh Hoc'] >= 0].count()['Sinh Hoc']

count_lich_su = diemTG[diemTG['Lich Su'] >= 0].count()['Lich Su']
count_dia_ly = diemTG[diemTG['Dia Ly'] >= 0].count()['Dia Ly']
count_gdcd = diemTG[diemTG['GDCD'] >= 0].count()['GDCD']

#PhanVietThong
count_toan_pvt = diemPVT[diemPVT['Toan'] >= 0].count()['Toan']
count_van_pvt = diemPVT[diemPVT['Van'] >= 0].count()['Van']
count_ngoai_ngu_pvt = diemPVT[diemPVT['Ngoai Ngu'] >= 0].count()['Ngoai Ngu']

count_vat_ly_pvt = diemPVT[diemPVT['Vat Ly'] >= 0].count()['Vat Ly']
count_hoa_hoc_pvt = diemPVT[diemPVT['Hoa Hoc'] >= 0].count()['Hoa Hoc']
count_sinh_hoc_pvt = diemPVT[diemPVT['Sinh Hoc'] >= 0].count()['Sinh Hoc']

count_lich_su_pvt = diemPVT[diemPVT['Lich Su'] >= 0].count()['Lich Su']
count_dia_ly_pvt = diemPVT[diemPVT['Dia Ly'] >= 0].count()['Dia Ly']
count_gdcd_pvt = diemPVT[diemPVT['GDCD'] >= 0].count()['GDCD']

#Đếm tổng thí sinh
count_tong_TG = diemTG.count()['SBD']
count_tong_pvt = diemPVT.count()['STT']

#Tính phần trăm thí sinh thi mỗi môn
so_luong_thi_TG = [count_toan, count_van, count_ngoai_ngu, count_vat_ly, count_hoa_hoc, 
                count_sinh_hoc, count_lich_su, count_dia_ly, count_gdcd]
phan_tram_thi_TG = so_luong_thi_TG / count_tong_TG

so_luong_thi_PVT = [count_toan_pvt, count_van_pvt, count_ngoai_ngu_pvt, count_vat_ly_pvt, count_hoa_hoc_pvt, 
                count_sinh_hoc_pvt, count_lich_su_pvt, count_dia_ly_pvt, count_gdcd_pvt]
phan_tram_thi_PVT = so_luong_thi_PVT / count_tong_pvt

st.sidebar.title("1. Dữ liệu tham gia kì thi theo môn học")

# Tạo DataFrame mới với tên môn và phần trăm thi
df_TG = pd.DataFrame({'Môn Thi': list_of_subjects, 'Tỉ lệ tham gia (%)': phan_tram_thi_TG * 100})
df_PVT = pd.DataFrame({'Môn Thi': list_of_subjects, 'Tỉ lệ tham gia (%)': phan_tram_thi_PVT * 100})

# Hiển thị dữ liệu tham gia thi các môn trong sidebar
st.sidebar.write("Dữ liệu tham gia thi các môn của Tiền Giang:")
st.sidebar.write(df_TG)
st.sidebar.write("Dữ liệu tham gia thi các môn của Phan Việt Thống:")
st.sidebar.write(df_PVT)

width = 0.35
fig, ax = plt.subplots(figsize=(12, 6))

conclusion_markdown = """
### 1. Biểu đồ cột so sánh tỉ lệ thí sinh tham gia thi THPT 2023 theo môn học
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Trong số thí sinh dự thi THPT quốc gia tại trường Phan Việt Thống và tỉnh Tiền Giang, tỉ lệ thí sinh thi mỗi môn học là bao nhiêu? Liệu có sự khác biệt đáng kể nào về tỉ lệ thí sinh thi mỗi môn giữa trường Phan Việt Thống và tỉnh Tiền Giang?
"""
st.markdown(conclusion_markdown)

# Vẽ cột cho phần trăm thí sinh tỉnh
ax.bar(np.arange(len(list_of_subjects)), phan_tram_thi_TG * 100, width, label='Tỉnh Tiền Giang', color='b', alpha=0.7)
# Vẽ cột cho phần trăm thí sinh trường
ax.bar(np.arange(len(list_of_subjects)) + width, phan_tram_thi_PVT * 100, width, label='Trường Phan Việt Thống', color='r', alpha=0.7)

ax.set_xlabel('Môn thi')
ax.set_ylabel('Tỉ lệ tham gia (%)')
ax.set_xticks(np.arange(len(list_of_subjects)) + width / 2)
ax.set_xticklabels(list_of_subjects)
ax.grid(True)
ax.set_axisbelow(True)
ax.legend(loc = 'best')

plt.title('Biểu đồ cột so sánh tỉ lệ thí sinh tham gia thi THPT 2023 theo môn học')
plt.show()
st.pyplot(fig)

conclusion_markdown = """
##### Nhận xét

- Tỉ lệ thí sinh tham gia thi môn Toán và Văn rất cao (gần 100%) vì đây là 2 môn bắt buộc. Không có sự chênh lệch đáng kể giữa thí sinh tham gia thi Toán, Văn của trường so với tỉnh.
- Về ngoại ngữ, có sự chênh lệch nhỏ giữa tỉ lệ thí sinh tham gia của trường và tỉnh. Trong đó, tỉ lệ thí sinh tham gia thi của trường cao hơn của tỉnh một chút (khoảng 5%).
- Về các tổ hợp tự chọn (KHTN và KHXH):
    + Tỉ lệ tham gia thi cùa 2 tổ hợp của tỉnh không quá chênh lệch, trong khi tỉ lệ tham gia thi của trường thì chênh lệch khá nhiều (khoảng 30%).
    + Tỉ lệ tham gia thi tổ hợp KHTN của trường thấp hơn tỉ lệ tham gia KHTN của tỉnh (khoảng 10%) nhưng đối với KHXH thì ngược lại, tỉ lệ tham gia thi của trường cao hơn so với tỉnh (khoảng 10%). \n
=> Qua đó, ta thấy thí sinh của trường Phan Việt Thống có vẻ yêu thích tổ hợp KHXH hơn so với KHTN.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 2. Phổ điểm khối KHTN theo mật độ xác suất
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Có bất kỳ sự khác biệt đáng kể nào về phổ điểm của khối khoa học tự nhiên giữa trường Phan Việt Thống và tỉnh Tiền Giang không? Liệu có một xu hướng chung về phổ điểm của khối khoa học tự nhiên giữa trường Phan Việt Thống và tỉnh Tiền Giang?
"""
st.markdown(conclusion_markdown)

#Điểm TB khối tự nhiên tỉnh TG
diem_DTBTN_TG = diemTG['DTBTN']
diem_DTBTN_TG = diemTG['DTBTN'].replace(-1.00, pd.NaT).dropna()
#Điểm TB khối tự nhiên trường PVT
diem_DTBTN_PVT = diemPVT['DTBTN']
diem_DTBTN_PVT = diemPVT['DTBTN'].replace(-1.00, pd.NaT).dropna()
# Tạo DataFrame mới với tên môn và phần trăm thi
df_TG = pd.DataFrame(diem_DTBTN_TG)
df_PVT = pd.DataFrame(diem_DTBTN_PVT)

st.sidebar.title("2. Dữ liệu điểm KHTN")
st.sidebar.write("Dữ liệu điểm thi KHTN của Tiền Giang:")
st.sidebar.write(df_TG)
st.sidebar.write("Dữ liệu điểm thi KHTN của Phan Việt Thống:")
st.sidebar.write(df_PVT)

plt.figure(figsize=(13, 6))

bins = np.linspace(0, 10, 40)

# Vẽ biểu đồ histogram cho điểm PVT (màu xanh)
plt.hist([diem_DTBTN_TG, diem_DTBTN_PVT], bins, label=['Điểm Tiền Giang', 'Điểm Phan Việt Thống'], density=True)

plt.xlabel('Điểm Thi')
plt.ylabel('Mật độ xác suất')
plt.title('Biểu đồ histogram so sánh điểm KHTN của Phan Việt Thống và Tiền Giang')
plt.legend(loc='upper right')
plt.xticks(np.arange(0, 10.25, 0.25), rotation=90)
plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Qua biểu đồ ta thấy điểm trung bình của khối khoa học tự nhiên ở trường Phan Việt Thống tập trung nhiều trong khoảng điểm 6.5 đến 6.8. Ở tỉnh Tiền Giang điểm tập trung nhiều ở mức từ 6.8 đến 7.0. Như vậy điểm trung bình của khối khoa học xã hội ở tỉnh Tiền Giang và trường Phan Việt Thống chênh lệch không nhiều nhưng vẫn phản ánh được chất lượng học sinh ở trường Phan Việt Thống là chưa tốt.
- Điểm trung bình của thí sinh trường Phan Việt Thống ở khoảng từ 3.5 điểm đổ xuống là không có nhưng đồng thời cũng thấp ở khoảng trên 8 điểm cho thấy học lực thí sinh thi khối tự nhiên của trường ở mức trung bình đến khá, những học sinh giỏi có điểm trung bình 3 môn Lý, Hóa, Sinh trên 8 chiếm tỉ lệ rất thấp, không nhiều so với tỉnh Tiền Giang
- Mức điểm trung bình khối khoa học tự nhiên của thí sinh toàn quốc tập trung chủ ở khoảng 7.0 đến 7.6 trong đó điểm 7.3 là điểm mà phần lớn thí sinh đều đạt được( theo https://xaydungchinhsach.chinhphu.vn ). Ta thấy số điểm này đã lớn hơn trường Phan Việt Thống và trên cả tỉnh Tiền Giang. Thí sinh ở Tiền Giang đã không hoàn thành tốt được bài thi ở khối khoa học tự nhiên, nó ảnh hưởng lớn đến đánh giá chất lượng thí sinh ở Tiền Giang nói chung và trường Phan Việt Thống nói riêng. Nó còn ảnh hưởng đến khả năng thí sinh xét nguyện vọng vào các đại học.
- Ở mức điểm từ 6.5 đổ xuống đến 3.5 thí sinh ở trường Phan Việt có tỉ lệ điểm xuất hiện nhiều hơn, ngược lại từ 6.5 đổ lên lại có tỉ lệ xuất hiện thấp hơn khi so với tỉnh. Điều này nói những học sinh ở trường có mức điểm từ 3.5 đến 6.0 nhiều hơn hẳn so với tỉnh, chất lượng thí sinh còn khá kém, với mức điểm trung bình của khối khoa học tự nhiên thế này, khả năng các thí sinh ở trường Phan Việt Thống xét điểm khối thi A00 sẽ rất hạn chế do điểm rất thấp nên sẽ không thể cạnh tranh với những thí sinh khác
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 3. Phổ điểm của khối KHXH theo mật độ xác suất
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Tương tự như khối khoa học tự nhiên, chúng ta sẽ tìm hiểu về phổ điểm của khối khoa học xã hội xem có khác biệt đáng kể nào giữa trường Phan Việt Thống và tỉnh Tiền Giang không? Liệu nó cũng có một xu hướng chung về phổ điểm giống như khối khoa học tự nhiên?
"""
st.markdown(conclusion_markdown)

# Điểm ở tỉnh tiền giang
diem_DTBXH_TG = diemTG['DTBXH']
diem_DTBXH_TG = diemTG['DTBXH'].replace(-1.00, pd.NaT).dropna()
# Điểm ở trường Phan Việt Thống
diem_DTBXH_PVT = diemPVT['DTBXH']
diem_DTBXH_PVT = diemPVT['DTBXH'].replace(-1.00, pd.NaT).dropna()
df_TG = pd.DataFrame(diem_DTBXH_TG)
df_PVT = pd.DataFrame(diem_DTBXH_PVT)

st.sidebar.title("3. Dữ liệu điểm KHXH")
st.sidebar.write("Dữ liệu điểm thi KHXH của Tiền Giang:")
st.sidebar.write(df_TG)
st.sidebar.write("Dữ liệu điểm thi KHXH của Phan Việt Thống:")
st.sidebar.write(df_PVT)

plt.figure(figsize=(13, 6))

bins = np.linspace(0, 10, 40)

# Vẽ biểu đồ histogram
plt.hist([diem_DTBXH_TG, diem_DTBXH_PVT], bins, label=['Điểm Tiền Giang', 'Điểm Phan Việt Thống'], density=True)

plt.xlabel('Điểm Thi')
plt.ylabel('Mật Độ Xác Suất')
plt.title('Biểu đồ histogram so sánh điểm KHXH của Phan Việt Thống và tỉnh Tiền Giang')
plt.legend(loc='best')
plt.xticks(np.arange(0, 10.25, 0.25), rotation=90)
plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Nhìn chung điểm trung bình khối xã hội của trường cao hơn so với tỉnh ở khoảng từ 6.5 đến 7.25 điểm. Cho thấy các học sinh khối khoa học xã hội của trường ở mức khá giỏi. ​
- Điểm trung bình khối xã hội ở trường và tỉnh đều tập trung chủ yếu ở khoảng điểm thi từ 6.25 đến 7.25, với mật độ xác suất cao. Điều này có thể chỉ ra rằng học sinh ở trường và tỉnh có xu hướng điểm ở khoảng khá.
- Điểm trung bình khối xã hội của tỉnh cao nhất của tỉnh là lớn 9.25 nhưng ở trường thì lại không có. Nhưng bù lại điểm ở trường tất cả đều lớn hơn 5.0 trong khi ở tỉnh lại có khá nhiều điểm dưới 5.0. Với mức điểm chủ yếu trên 5 ta có thể nhận thấy chất lượng giảng dạy của khối khoa học xã hội rất tốt đi kèm với đó là khả năng của học sinh đối với khối học này đều đạt trên mức trung bình.​
- Để đạt được được kết quả trên lí do cũng 1 phần truyền thống của trường đa số học sinh chọn học khối KHXH đều nhiều hơn KHTN(theo thông tin từ cựu học sinh) nên dựa vào đó trường cũng sẽ có những ưu ái tập trung hơn trong khối học này.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 4. Tỉ lệ giới tính tham gia kì thi của trường
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Giới tính nào có tỉ lệ tham gia kì thi cao hơn tại trường Phan Việt Thống, tại sao lại có sự chênh lệch và sự chênh lệch này có ảnh hưởng như thế nào?
"""
st.markdown(conclusion_markdown)

count_nam = (diemPVT["Gioi tinh"] == "Nam").sum()
count_nu = (diemPVT["Gioi tinh"] == "Nữ").sum()
tong_thi_sinh = count_nam + count_nu
ti_le_nam = (count_nam / tong_thi_sinh) * 100
ti_le_nu = (count_nu / tong_thi_sinh) * 100

st.sidebar.title("4. Dữ liệu giới tính")
st.sidebar.write(f"Tỉ lệ nam: {ti_le_nam}")
st.sidebar.write(f"Tỉ lệ nữ: {ti_le_nu}")

#Vẽ piechart
plt.figure(figsize=(6, 6))
gioi_tinh = ['Nam', 'Nữ']
ti_le = [ti_le_nam, ti_le_nu]

plt.pie(ti_le, autopct='%1.1f%%', startangle=90)
plt.title('Biểu đồ biểu diễn tỉ lệ Nam và Nữ tham gia kỳ thi của trường Phan Việt Thống')
plt.legend(gioi_tinh, title = "Giới tính", loc = "best")
plt.axis('equal')
plt.show()
st.pyplot(plt)
conclusion_markdown = """
##### Nhận xét
- Qua biểu đồ rõ ràng ta thấy tỉ lệ sinh thí nam tham gia kì thi (43%) và tỉ lệ thí sinh nữ tham gia kì thi (57%) có sự chênh lệch nhưng không quá lớn.
- Tỉ lệ chênh lệch khoảng 14% -> ở trường Phan Việt Thống có sự mất cân bằng giới tính nhẹ.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 5. Phổ điểm môn Văn của trường PVT so với tỉnh Tiền Giang
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Phổ điểm môn văn tại trường Phan Việt Thống và tỉnh Tiền Giang có hình dạng như thế nào khi được biểu diễn theo mật độ xác suất? Liệu điểm số nào có mật độ xác suất cao nhất trong phổ điểm của môn văn tại trường Phan Việt Thống và tỉnh Tiền Giang?
"""
st.markdown(conclusion_markdown)

# Điểm ở tỉnh tiền giang
diem_Van_TG = diemTG['Van']
diem_Van_TG = diemTG['Van'].replace(-1.00, pd.NaT).dropna()
# Điểm ở trường Phan Việt Thống
diem_Van_PVT = diemPVT['Van']
diem_Van_PVT = diemPVT['Van'].replace(-1.00, pd.NaT).dropna()

df_TG = pd.DataFrame(diem_Van_TG)
df_PVT = pd.DataFrame(diem_Van_PVT)

st.sidebar.title("5. Dữ liệu điểm Văn")
st.sidebar.write("Dữ liệu điểm thi Văn của Tiền Giang:")
st.sidebar.write(df_TG)
st.sidebar.write("Dữ liệu điểm thi Văn của Phan Việt Thống:")
st.sidebar.write(df_PVT)

#Vẽ đồ thị
plt.figure(figsize=(13, 6))

bins = np.linspace(0, 10, 40)

# Vẽ biểu đồ histogram
plt.hist([diem_Van_TG, diem_Van_PVT], bins, label=['Điềm Tiền Giang', 'Điểm Phan Việt Thống'], density=True)

plt.xlabel('Điểm Thi')
plt.ylabel('Mật Độ Xác suất')
plt.title('Biểu đồ histogram so sánh mật độ điểm thi môn Văn của tỉnh TG và trường PVT')
plt.legend(loc='best')
plt.xticks(np.arange(0, 10.5, 0.5), rotation=90)
plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Nhìn chung đa số các thí sinh của cả trường Phan Việt Thống và tỉnh Tiền Giang đều đạt mốc 5 điểm đổ lên, chỉ số ít các thí sinh của tỉnh đạt điểm dưới 5, cho thấy lực học môn văn khá tốt.
- Điểm Văn ở trường Phan Việt Thống rất tốt, phần lớn thí sinh đều có điểm số khá cao, ở khoảng điểm 8 đến 8.75 - có rất nhiều thí sinh ở mức điểm này, nó hoàn toàn vượt trội hơn so với phổ điểm của môn Toán. Cùng là những môn chính nhưng môn Văn đã có điểm số hoàn toàn vượt trên môn Toán, một phần có lẽ vì học sinh của trường chọn khối xã hội nhiều nên rất quan tâm đến môn Văn, một phần là do sự dạy dỗ rất tốt đến từ phía nhà trường đã giúp cho các thí sinh đạt điểm rất cao ở môn Văn trong kì thi THPTQG.
- Đáng chú ý, theo trang https://vietnamnet.vn, cả nước ta có 1 thí sinh đạt điểm 10 môn văn và 443 thí sinh đạt 9.75 điểm, trong đó tỉnh Tiền Giang có 1 thí sinh đạt 9.75 điểm môn Văn và thí sinh này cũng là thí sinh ở trường Phan Việt Thống. Trường Phan Việt Thống đã có thể cạnh tranh với các trường khác trong khu vực ở mảng giảng dạy và đào tạo thí sinh thi môn Văn trong các kì thi như học sinh giỏi Văn cấp tỉnh - cấp thành phố,...
- Tuy nhiên ở tỉnh Tiền Giang có một số ít thí sinh có điểm Văn dưới 5, tỉnh Tiền Giang cần xem xét lại quá trình giảng dạy và truyền đạt kiến thức để có thể nâng cao phổ điểm ở môn học này vì đây là môn học có phổ điểm rất tốt ở tỉnh, có tiềm năng để đưa Tiền Giang trở thành một tỉnh có nhiều thí sinh giỏi Văn trong cả nước.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 6. Phổ điểm Toán của trường PVT so với tỉnh Tiền Giang
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Phổ điểm môn Toán tại trường Phan Việt Thống và tỉnh Tiền Giang liệu có giống môn Văn? Chất lượng điểm số sẽ tốt giống nhau hay sẽ có sự khác biệt?
"""
st.markdown(conclusion_markdown)

diem_ToanTG = diemTG['Toan']
diem_ToanTG = diemTG['Toan'].replace(-1.00, pd.NaT).dropna()

diem_ToanPVT = diemPVT['Toan']
diem_ToanPVT = diemPVT['Toan'].replace(-1.00, pd.NaT).dropna()

df_TG = pd.DataFrame(diem_ToanTG)
df_PVT = pd.DataFrame(diem_ToanPVT)

st.sidebar.title("6. Dữ liệu điểm Toán")
st.sidebar.write("Dữ liệu điểm thi Toán của Tiền Giang:")
st.sidebar.write(df_TG)
st.sidebar.write("Dữ liệu điểm thi Toán của Phan Việt Thống:")
st.sidebar.write(df_PVT)

#Vẽ biểu đồ
plt.figure(figsize=(13, 6))

bins = np.linspace(0, 10, 40)

# Vẽ biểu đồ histogram
plt.hist([diem_ToanTG, diem_ToanPVT], bins, label=['Điểm Tiền Giang', 'Điểm Phan Việt Thống'], density=True)

plt.xlabel('Điểm Thi')
plt.ylabel('Mật Độ Xác Suất')
plt.title('Biểu đồ histogram so sánh điểm Toán của Phan Việt Thống và tỉnh Tiền Giang')
plt.legend(loc='best')
plt.xticks(np.arange(0, 10.25, 0.25), rotation=90)
plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Điểm toán của học sinh từ trường Phan Việt Thống trong kỳ thi tốt nghiệp THPT 2023 phân bố không đều, chủ yếu nằm ở điểm 6.25 rất nhiều. Điều này cho thấy học sinh từ trường Phan Việt Thống thường đạt điểm số không cao trong môn toán.-
- Điểm toán của học sinh toàn tỉnh Tiền Giang trong kỳ thi tốt nghiệp THPT 2023 cũng phân bố không nhiều, điểm 7.25 xuất hiện nhiều nhất . Điểm số này cao hơn so với trường Phan Việt Thống khá nhiều.
- Học sinh từ trường Phan Việt Thống có xu hướng đạt điểm số thấp hơn so với học sinh toàn tỉnh Tiền Giang. Điều này có thể cho thấy chất lượng giáo dục môn toán tại trường Phan Việt Thống là chưa tốt , nhưng không có điểm dưới 1 trong khi đó ở tỉnh thì lại có 1 học sinh đạt 1 điểm toán, điều này sẽ dấn đến học sinh này không có khả năng tốt nghiệp cấp THPT.
- Điểm toán trên 9 trong tỉnh Tiền Giang rất ít (theo thống kê có 85 bạn trên 9 điểm) và không có điểm 10. Điểm trên 9 từ trường Phan Việt Thống là không có. Điểm số này đã thể hiện rõ học sinh của trường Phan Việt Thống không giỏi trong môn toán và học sinh ở toàn tỉnh Tiền Giang cũng không có nhiều bạn giỏi ở môn học này.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 7. Tỉ lệ số điểm đạt từ 8 điểm trở lên của 3 môn chính Toán, Văn, Anh
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Tỉ lệ số điểm đạt từ 8 điểm trở lên của 3 môn chính Toán, Văn, Anh tại trường Phan Việt Thống và tỉnh Tiền Giang là bao nhiêu? Môn học nào trong số 3 môn chính Toán, Văn, Anh sẽ có tỉ lệ số điểm đạt từ 8 điểm trở lên cao nhất tại trường Phan Việt Thống và tỉnh Tiền Giang?
"""
st.markdown(conclusion_markdown)

#Đếm điểm đạt từ 8 các môn
#TienGiang
count_toan = diemTG[diemTG['Toan'] >= 8].count()['Toan']
count_van = diemTG[diemTG['Van'] >= 8].count()['Van']
count_ngoai_ngu = diemTG[diemTG['Ngoai Ngu'] >= 8].count()['Ngoai Ngu']

#PhanVietThong
count_toan_pvt = diemPVT[diemPVT['Toan'] >= 8].count()['Toan']
count_van_pvt = diemPVT[diemPVT['Van'] >= 8].count()['Van']
count_ngoai_ngu_pvt = diemPVT[diemPVT['Ngoai Ngu'] >= 8].count()['Ngoai Ngu']

plt.figure(figsize=(12, 6))  # Đặt kích thước biểu đồ

subjects = ['Toán', 'Văn', 'Anh']
scores_set1 = [count_toan, count_van, count_ngoai_ngu]
scores_set2 = [count_toan_pvt, count_van_pvt, count_ngoai_ngu_pvt]

df_TG = pd.DataFrame({"Môn": subjects, "Số lượng": scores_set1})
df_PVT = pd.DataFrame({"Môn": subjects, "Số lượng": scores_set2})

st.sidebar.title("7. Dữ liệu điểm 3 môn Toán Văn Anh")
st.sidebar.write("Số lượng điểm thi trên 8 của Tiền Giang:")
st.sidebar.write(df_TG)
st.sidebar.write("Số lượng điểm thi trên 8 của Phan Việt Thống:")
st.sidebar.write(df_PVT)

plt.subplot(1, 2, 1)  # Biểu đồ đầu tiên
plt.pie(scores_set1, labels=subjects, autopct='%1.1f%%')
plt.title('Tỉ lệ điểm trên 8 của tỉnh TG')

plt.subplot(1, 2, 2)  # Biểu đồ thứ hai
plt.pie(scores_set2, labels=subjects, autopct='%1.1f%%')
plt.title('Tỉ lệ điểm trên 8 của trường PVT')

plt.tight_layout()  # Đảm bảo không bị trùng lấp
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Nhìn chung tỉ lệ đạt điểm môn Văn trên 8 của cả trường và tỉnh đều cao hơn so với Toán và Anh. Điều này có thể nhận thấy được thế mạnh của tỉnh Tiền Giang là môn Văn, theo thống kê của trang http://baoapbac.vn điểm Văn của tỉnh Tiền Giang có tỉ lệ đạt trên 5 chiếm tới 98.1% xếp thứ 11 trong cả nước. Phần nào dẫn tới kết quả tốt này cũng là nhờ vào sự nỗ lực của các học sinh cũng như sự giảng dạy và chú trọng của các thầy cô để đưa ra được nội dung trọng tâm tốt trong môn Văn.​
- Tỉ lệ đạt trên 8 môn Văn của trường PVT cao hơn tỉnh, nhưng ngược lại thấp hơn ở môn Toán và môn Anh. Trường tuy chú trọng vào thế mạnh môn Văn nhưng chất lượng môn Toán và Anh lại không được tốt nên dẫn tới tỉ lệ 2 môn này thấp hơn so với tỉnh.
- Môn Anh là môn có tỉ lệ đạt điểm trên 8 thấp nhất, và cũng theo thống kê của http://baoapbac.vn tỉ lệ đạt điểm trên 5 của cả tỉnh Tiền Giang chỉ chiếm 57.7%. Lí giải cho lí do này 1 phần cũng do vào điều kiện kinh tế của tỉnh Tiền Giang dẫn tới chất lượng giảng dạy tiếng anh không được tốt. Để thấy điều kiện kinh tế ảnh hưởng như thế nào đối với chất lượng giảng dạy môn Tiếng Anh thì 2 thành phố lớn hiện nay là TPHCM là Hà Nội có điểm trunh bình tiếng anh cao nhất cả nước và đây cũng là 2 thành phố đi đầu trong nền kinh tế.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 8. Tỉ lệ điểm liệt của những học sinh ở tỉnh Tiền Giang
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Tỉ lệ học sinh ở tỉnh Tiền Giang nhận điểm liệt trong kì thi THPT quốc gia là bao nhiêu? Những điểm liệt này sẽ gây ảnh hưởng như thế nào đến cho học sinh?
"""
st.markdown(conclusion_markdown)

plt.clf()
mon_hoc = ['Toán học', 'Ngữ văn', 'Ngoại ngữ',  'Địa lý']
diem_liet = [
    diemTG[(diemTG['Toan'] >= 0) & (diemTG['Toan'] <= 1)].count()['Toan'],
    diemTG[(diemTG['Van'] >= 0) & (diemTG['Van'] <= 1)].count()['Van'],
    diemTG[(diemTG['Ngoai Ngu'] >= 0) & (diemTG['Ngoai Ngu'] <= 1)].count()['Ngoai Ngu'],
    diemTG[(diemTG['Dia Ly'] >= 0) & (diemTG['Dia Ly'] <= 1)].count()['Dia Ly'], 
]

df_TG = pd.DataFrame({"Môn" : mon_hoc, "Số lượng": diem_liet})

st.sidebar.title("8. Dữ liệu điểm liệt")
st.sidebar.write("Số lượng điểm liệt của Tiền Giang:")
st.sidebar.write(df_TG)

#Vẽ biểu đồ
ty_le_diem_liet = [diem / len(diemTG) for diem in diem_liet]

# Loại bỏ các môn học có tỷ lệ 0
non_zero_mon_hoc = [mon for mon, tl in zip(mon_hoc, ty_le_diem_liet) if tl > 0]
non_zero_ty_le_diem_liet = [tl for tl in ty_le_diem_liet if tl > 0]

# Vẽ biểu đồ tròn
labels = non_zero_mon_hoc
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightblue']
plt.figure(figsize=(6, 8))
plt.pie(non_zero_ty_le_diem_liet, labels=labels, colors=colors, autopct='%1.1f%%', startangle=120)
plt.title('Tỷ Lệ Điểm Liệt Theo Môn Học')
plt.axis()  
plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Chú thích: Khi 1 môn trong tổ hợp khoa học tự nhiên (hoặc khoa học xã hội) bị điểm từ 1 trở xuống (<=1) hoặc 1 trong 3 môn bắt buộc (Toán, Ngữ văn, Ngoại ngữ) bị điểm từ 1 trở xuống (<=1) thì học sinh này bị điểm liệt.
- Tỉ lệ điểm liệt của những môn học được thể hiện đều là 25%, chính xác hơn là mỗi môn học đều có 1 học sinh bị điểm liêt. Điều này khiến cho học sinh đó không đủ điều kiện xét tốt nghiệp THPT, không đạt được mục tiêu do tỉnh và nhà trường đã đề ra.
- Theo trang kinhtedothi.vn thì cả nước có 656 bài thi bị điểm liệt mà trong đó tỉnh Tiền Giang chiếm 4/656 điểm liệt tương đương 0.61%. Như vậy tuy có điểm liệt nhưng khi so với cả nước thì lại không quá nhiều.
- Theo cùng nguồn trang thì điểm liệt trên từng môn học, cụ thể là môn Ngoại Ngữ có 192 điểm liệt, môn Toán có 123 điểm liệt, môn Địa có 112 điểm liệt, môn Văn có 92 điểm liệt, môn Sử có 38 điểm liệt, môn Sinh có 36 điểm liệt, môn Giáo dục công dân có 26 điểm liệt, môn Lí có 23 điểm liệt và môn Hóa có 14 điểm liệt. Điều đáng chú ý là tỉnh Tiền Giang không có thí sinh nào bị điểm liệt ở các môn Sử, Sinh, Giáo dục công dân, Lý và Hóa. Điều này cho thấy học sinh ở Tiền Giang đã chuẩn bị kỹ lưỡng và nắm vững kiến thức trong các môn học này. Việc không có thí sinh nào bị điểm liệt cũng phản ánh được chất lượng giáo dục tại Tiền Giang - các giáo viên đã dạy bài bản và kỹ lưỡng, giúp học sinh hiểu rõ và nắm vững được kiến thức.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 9. So sánh điểm trung bình 3 môn Toán, Văn, Anh của các tỉnh lân cận
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Có bất kỳ sự khác biệt đáng kể nào về điểm trung bình 3 môn Toán, Văn, Anh giữa các tỉnh lân cận và tỉnh Tiền Giang không? Tỉnh nào trong số các tỉnh lân cận có điểm trung bình cao nhất và thấp nhất cho 3 môn Toán, Văn, Anh?
"""
st.markdown(conclusion_markdown)

plt.clf()
def calculate_average_score(data):
    data['DiemTB'] = data[['Toan', 'Van', 'Ngoai Ngu']].mean(axis=1)
    return data[['DiemTB']]

diemTB_TG = calculate_average_score(diemTG)
diemTB_BinhDuong = calculate_average_score(diemBinhDuong)
diemTB_BenTre = calculate_average_score(diemBenTre)
diemTB_BaRiaVungTau = calculate_average_score(diemBaRiaVungTau)
diemTB_VinhLong = calculate_average_score(diemVinhLong)

tinh_names = ['Tiền Giang', 'Bình Dương', 'Bến Tre', 'Bà Rịa - Vũng Tàu', 'Vĩnh Long']

# Điểm trung bình của từng tỉnh
diemTB_values = [diemTB_TG['DiemTB'].mean(), diemTB_BinhDuong['DiemTB'].mean(), diemTB_BenTre['DiemTB'].mean(),
                 diemTB_BaRiaVungTau['DiemTB'].mean(), diemTB_VinhLong['DiemTB'].mean()]

df = pd.DataFrame({"Tỉnh" : tinh_names, "Điểm": diemTB_values})

st.sidebar.title("9. Dữ liệu điểm trung bình của các tỉnh")
st.sidebar.write("Điểm trung bình Toán Văn Anh của các tỉnh: ")
st.sidebar.write(df)

colors = ['#1cba46', '#cf1d61', '#bf492e', '#41afd1', '#d1d43d']
# Vẽ biểu đồ cột ngang
plt.barh(tinh_names, diemTB_values, color = colors)
plt.xlabel('Điểm trung bình')
plt.title('Điểm trung bình Toán, Văn, Anh của các tỉnh lân cận')

for index, value in enumerate(diemTB_values):
    plt.text(value, index, f'{value:.2f}', ha='left', va='center')
plt.subplots_adjust(right=1.8)
plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Biểu đồ trên thể hiện điểm trung bình 3 môn chính: Toán, Văn, Anh của tỉnh Tiền Giang và các tỉnh lân cận.
- Qua biểu đồ, có thể thấy Bình Dương là tỉnh có điểm trung bình cao nhất, đạt 6,44 điểm. Tiếp theo là Tiền Giang với 6,38 điểm. Hai tỉnh có điểm trung bình thấp nhất là Vĩnh Long và Bến Tre, lần lượt 5,67 điểm.
- Nhìn chung, điểm trung bình của các tỉnh đều ở mức khá. Bình Dương là tỉnh có chất lượng giáo dục tốt nhất, tiếp theo là Tiền Giang. Hai tỉnh Vĩnh Long và Bến Tre có chất lượng giáo dục thấp hơn so với các tỉnh khác.
- Nguyên nhân của vấn đề này có thể đến từ sự đầu tư của các tỉnh. Ngoài ra chất lượng giáo viên cũng là một yếu tố quan trọng ảnh hưởng đến chất lượng giáo dục của các tỉnh này.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 10. Biểu đồ chấm thể hiện điểm Toán và Văn của tỉnh Tiền Giang và Bình Dương
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Có bất kỳ sự khác biệt đáng kể nào về điểm Toán và Văn giữa tỉnh Tiền Giang và Bình Dương không? Những yếu tố nào có thể ảnh hưởng đến điểm Toán và Văn tại tỉnh Tiền Giang và Bình Dương?
"""
st.markdown(conclusion_markdown)

subjects = ['Toan', 'Van']
data_ToanVan_TG = diemTG[subjects].replace(-1.00, pd.NaT).dropna()
data_ToanVan_BD = diemBinhDuong[subjects].replace(-1.00, pd.NaT).dropna()

data_ToanVan_TG['DiemTB'] = data_ToanVan_TG[subjects].mean(axis=1)
data_ToanVan_BD['DiemTB'] = data_ToanVan_BD[subjects].mean(axis=1)

df_TG = pd.DataFrame(data_ToanVan_TG)
df_BD  = pd.DataFrame(data_ToanVan_BD)
st.sidebar.title("10. Dữ liệu điểm Toán, Văn của các thí sinh")
st.sidebar.write("Điểm Tiền Giang")
st.sidebar.write(df_TG)

st.sidebar.write("Điểm Bình Dương")
st.sidebar.write(df_BD)

# Vẽ biểu đồ chấm cho từng tỉnh trên hai dòng
plt.figure(figsize=(12, 16))

# Biểu đồ cho Tiền Giang
plt.subplot(2, 1, 1)
sns.scatterplot(data=data_ToanVan_TG, x='Toan', y='Van', hue='DiemTB', palette='viridis', size='DiemTB', sizes=(20, 200))
plt.plot([0, 10], [0, 10], linestyle='--', color='gray', linewidth=2)
plt.title('Biểu đồ chấm thể hiện điểm Toán và Văn của Tiền Giang')
plt.xlabel('Điểm Toán')
plt.ylabel('Điểm Văn')
plt.legend(title='Điểm trung bình')

# Biểu đồ cho Bình Dương
plt.subplot(2, 1, 2)
sns.scatterplot(data=data_ToanVan_BD, x='Toan', y='Van', hue='DiemTB', palette='viridis', size='DiemTB', sizes=(20, 200))
plt.plot([0, 10], [0, 10], linestyle='--', color='gray', linewidth=2)
plt.title('Biểu đồ chấm thể hiện điểm Toán và Văn của Bình Dương')
plt.xlabel('Điểm Toán')
plt.ylabel('Điểm Văn')
plt.legend(title='Điểm trung bình', loc = 'best')

plt.tight_layout()
plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Nhìn chung, có thể thấy điểm của Bình Dương đồng đều hơn so với Tiền Giang.
- Bên cạnh đó, điểm Toán và điểm Văn của thí sinh Tiền Giang và Bình Dương có mối quan hệ tương quan dương, tức là khi điểm Toán tăng thì điểm Văn cũng tăng. Điều này có thể giải thích là do hai môn học này đều đòi hỏi học sinh có khả năng tư duy logic và trừu tượng.
- Tuy nhiên, mối quan hệ này không chặt chẽ, tức là có những thí sinh có điểm Toán cao nhưng điểm Văn thấp và ngược lại. Điều này có thể giải thích là do hai môn học này có những nội dung khác biệt. Ví dụ, môn Toán tập trung vào các khái niệm, quy tắc, và công thức, trong khi môn Văn tập trung vào các kiến thức về ngôn ngữ, văn học, và văn hóa. \n
=> Dựa trên những nhận xét trên, ta có thể thấy rằng, để học tốt cả hai môn Toán và Văn, học sinh cần phát triển khả năng tư duy logic và trừu tượng. Ngoài ra, học sinh cũng cần chú ý đến các nội dung khác biệt của hai môn học này để có thể học tập một cách hiệu quả.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 11. Biểu đồ phân phối tổng điểm khối A0 của tỉnh Tiền Giang và tỉnh Bến Tre
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Điểm số khối A0 của tỉnh Tiền Giang và tỉnh Bến Tre sẽ cao nhất ở khoảng nào?
Liệu có một xu hướng chung về tổng điểm khối A0 giữa hai tỉnh không?
"""
st.markdown(conclusion_markdown)

subjects_A0 = ['Toan', 'Vat Ly', 'Hoa Hoc']  # Khoi A0
data_A0_TG = diemTG[subjects_A0].replace(-1.00, pd.NaT).dropna()
data_A0_BenTre = diemBenTre[subjects_A0].replace(-1.00, pd.NaT).dropna()

# Tổng điểm của các môn Toan, Vat Ly, Hoa Hoc
data_A0_TG['TongDiem'] = data_A0_TG[subjects_A0].sum(axis=1)
data_A0_BenTre['TongDiem'] = data_A0_BenTre[subjects_A0].sum(axis=1)

df_TG = pd.DataFrame(data_A0_TG)
df_BT  = pd.DataFrame(data_A0_BenTre)
st.sidebar.title("11. Dữ liệu điểm tổng điểm khối A0")
st.sidebar.write("Điểm Tiền Giang")
st.sidebar.write(df_TG)
st.sidebar.write("Điểm Bến Tre")
st.sidebar.write(df_BT)

# Vẽ histogram cho Tiền Giang
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(data_A0_TG['TongDiem'], bins=20, kde=True, color='skyblue')
plt.title('Phân phối tổng điểm của Khối A0 - Tiền Giang')
plt.xlabel('Tổng điểm')
plt.ylabel('Số lượng')

# Vẽ histogram cho Bến Tre
plt.subplot(1, 2, 2)
sns.histplot(data_A0_BenTre['TongDiem'], bins=20, kde=True, color='orange')
plt.title('Phân phối tổng điểm của Khối A0 - Bến Tre')
plt.xlabel('Tổng điểm')
plt.ylabel('Số lượng')

plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Có thể thấy, phân phối tổng điểm của hai tỉnh khá tương đồng. Đa số thí sinh của hai tỉnh đều đạt tổng điểm từ 18 đến 24 điểm. Số lượng thí sinh đạt tổng điểm dưới 18 điểm khá ít. Số lượng thí sinh đạt tổng điểm từ 25 đến 30 cũng khá ít, với khoảng 300 thí sinh ở Tiền Giang (chiếm khoảng 4.19%) và khoảng 150 thí sinh ở Bến Tre (chiếm khoảng 3.76%).
- Nhìn chung thì học lực thí sinh thi khối A0 ở Tiền Giang có phần nhỉn hơn một chút so với Bến Tre (khoảng 0.43%). Điều này có thế đến một phần từ yếu tố kinh tế xã hội ở 2 tỉnh, một phần có thể đến từ việc số lượng thí sinh thi A0 ở Tiền Giang đông hơn (7160) so với Bến Tre (3987) nên Tiền Giang có nhiều thí sinh tiềm năng hơn.
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
### 12. Biểu đồ thể hiện mức độ tương quan giữa các môn học trong khối thi của tỉnh Tiền Giang
"""
st.markdown(conclusion_markdown)

conclusion_markdown = """
##### *Đặt câu hỏi*:
Môn học nào có mức độ tương quan thấp nhất với các môn học khác trong khối thi tại tỉnh Tiền Giang? Những yếu tố nào có thể ảnh hưởng đến mức độ tương quan giữa các môn học trong khối thi của tỉnh Tiền Giang?
"""
st.markdown(conclusion_markdown)

# Các môn học cho các khối
subjects_A0 = ['Toan', 'Vat Ly', 'Hoa Hoc']  # Khoi A0
subjects_B0 = ['Toan', 'Hoa Hoc', 'Sinh Hoc']  # Khoi B0
subjects_C0 = ['Van', 'Lich Su', 'Dia Ly']  # Khoi C0
subjects_D0 = ['Toan', 'Van', 'Ngoai Ngu']  # Khoi D0

# Dữ liệu cho các khối
data_A0 = diemTG[subjects_A0].replace(-1.00, pd.NaT).dropna()
data_B0 = diemTG[subjects_B0].replace(-1.00, pd.NaT).dropna()
data_C0 = diemTG[subjects_C0].replace(-1.00, pd.NaT).dropna()
data_D0 = diemTG[subjects_D0].replace(-1.00, pd.NaT).dropna()

# Tính ma trận hệ số tương quan cho từng khối
correlation_matrix_A0 = data_A0.corr()
correlation_matrix_B0 = data_B0.corr()
correlation_matrix_C0 = data_C0.corr()
correlation_matrix_D0 = data_D0.corr()

df_TG_A0 = pd.DataFrame(data_A0)
df_TG_B0 = pd.DataFrame(data_B0)
df_TG_C0 = pd.DataFrame(data_C0)
df_TG_D0 = pd.DataFrame(data_D0)
st.sidebar.title("12. Dữ liệu điểm của các khối")
st.sidebar.write("Khối A0")
st.sidebar.write(df_TG_A0)
st.sidebar.write("Khối B0")
st.sidebar.write(df_TG_B0)
st.sidebar.write("Khối C0")
st.sidebar.write(df_TG_C0)
st.sidebar.write("Khối D0")
st.sidebar.write(df_TG_D0)

# Vẽ biểu đồ heatmap cho từng khối trên 2 dòng
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))

# Khối A0
sns.heatmap(correlation_matrix_A0, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1.5, ax=axes[0, 0], annot_kws={"size": 14})
axes[0, 0].set_title('Khoi A0')
axes[0, 0].tick_params(axis='both', which='both', labelsize=12)

# Khối B0
sns.heatmap(correlation_matrix_B0, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1.5, ax=axes[0, 1], annot_kws={"size": 14})
axes[0, 1].set_title('Khoi B0')
axes[0, 1].tick_params(axis='both', which='both', labelsize=12)

# Khối C0
sns.heatmap(correlation_matrix_C0, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1.5, ax=axes[1, 0], annot_kws={"size": 14})
axes[1, 0].set_title('Khoi C0')
axes[1, 0].tick_params(axis='both', which='both', labelsize=12)

# Khối D0
sns.heatmap(correlation_matrix_D0, annot=True, cmap='coolwarm', fmt=".2f", linewidths=1.5, ax=axes[1, 1], annot_kws={"size": 14})
axes[1, 1].set_title('Khoi D0')
axes[1, 1].tick_params(axis='both', which='both', labelsize=12)
plt.tight_layout()
plt.show()
st.pyplot(plt)

conclusion_markdown = """
##### Nhận xét
- Các heatmap này thể hiện mối liên hệ giữa các môn học thuộc các khối A0, B0, C0 và D0 của Tiền Giang. Màu càng nóng thể hiện mối liên hệ càng mạnh, ngược lại màu càng nhạt thể hiện mối liên hệ càng yếu.
- Hai heatmap đầu tiên (A0 và B0) thể hiện mối liên hệ giữa các môn học thuộc khối tự nhiên (Toán, Vật lý, Hóa học, Sinh học). Có thể thấy, các môn học trong khối tự nhiên có mối liên hệ chặt chẽ với nhau. Điều này là do các môn học này đều có chung một nền tảng kiến thức, bao gồm các khái niệm, định lý, phương pháp giải bài tập.
- Cụ thể, mối quan hệ giữa Toán và các môn học khác trong khối tự nhiên đều ở mức cao (0.49 - 0.57). Toán học là môn học nền tảng cung cấp cho học sinh các kiến thức cần thiết để học các môn học khác trong khối tự nhiên. Ví dụ, để học về chuyển động, học sinh cần biết về các khái niệm như quãng đường, vận tốc, gia tốc,..., mà các khái niệm này đều được học trong môn Toán. Duy chỉ có Toán không có liên hệ mạnh mẽ với Sinh học (0.41) vì hai môn này nội dung hoàn toàn khác nhau nhưng Toán học vẫn hỗ trợ tính toán một phần cho Sinh học.
- Hai heatmap kế tiếp thể hiện mối liên hệ giữa Toán, các môn học thuộc khối xã hội (Văn, Lịch sử, Địa lý) và các môn học ngoại ngữ. Có thể thấy, các môn học thuộc khối xã hội có mối liên hệ với nhau không mạnh bằng tự nhiên, và giữa Văn và Ngoại ngữ cũng thế.
- Cụ thể, mối quan hệ giữa Văn và Địa lý ở mức trung bình (0.37), giữa Văn và Ngoại ngữ chỉ khoảng 0.42. Điều này có thể đến từ việc kiến thức của các môn này khá khác nhau.
- Đặc biệt, ta có thể thấy mối liên hệ giữa Toán và Ngoại ngữ lại lên đến 0.59. Điều này có thể bắt nguồn từ việc cả 2 môn đều cần đến khả năng tư duy logic, trừu tượng và ghi nhớ nhiều hơn so với các môn khác. Từ đó ta có thể suy luận rằng: học sinh giỏi Toán thì thường giỏi Ngoại ngữ và ngược lại.
"""
st.markdown(conclusion_markdown)