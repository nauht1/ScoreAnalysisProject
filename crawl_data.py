import requests
import csv

# Khởi tạo một danh sách để lưu trữ dữ liệu
data_list = []

start_row = 1
end_row = 15455

for x in range(53000000 + start_row, 53000000 + end_row):
    scraping_url = "https://dantri.com.vn/thpt/1/0/99/" + str(x) + "/2023/0.2/search-gradle.htm";
    payload = {}
    headers = {}
    response = requests.request("GET", scraping_url, headers=headers, data=payload)
    info = response.json()['student']

    # Tạo một bản ghi dữ liệu cho mỗi học sinh dưới dạng dict
    diem = {
        'SBD': info['sbd'],
        'Toan': info['toan'],
        'Van': info['van'],
        'Ngoai Ngu': info['ngoaiNgu'],
        'Vat Ly': info['vatLy'],
        'Hoa Hoc': info['hoaHoc'],
        'Sinh Hoc': info['sinhHoc'],
        'DTBTN': info['diemTBTuNhien'],
        'Lich Su': info['lichSu'],
        'Dia Ly': info['diaLy'],
        'GDCD': info['gdcd'],
        'DTBXH': info['diemTBXaHoi']
    }

    data_list.append(diem)

# Tạo tệp CSV và ghi dữ liệu vào đó
with open('data_TienGiang.csv', 'a', newline='') as csv_file:
    fieldnames = ['SBD', 'Toan', 'Van', 'Ngoai Ngu', 'Vat Ly', 'Hoa Hoc', 'Sinh Hoc', 'DTBTN', 'Lich Su', 'Dia Ly', 'GDCD', 'DTBXH']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    if start_row == 1:
        writer.writeheader()
    
    for diem in data_list:
        writer.writerow(diem)

print(f"Dữ liệu từ {start_row} đến {end_row} đã được xuất ra tệp CSV thành công.")