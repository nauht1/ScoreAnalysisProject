import pandas as pd

input_folder = 'raw_data'
output_folder = 'clean_data'
ext = '.csv'

input_file = 'data_VinhLong'
output_file = 'clean_data_VinhLong'

input_data = input_folder + '/' + input_file + ext
output_data = output_folder + '/' + output_file + ext

# Đọc dữ liệu từ file CSV và chỉ định dấu phân tách là ","
df = pd.read_csv(input_data, delimiter=',')

# Loại bỏ các thí sinh không tham gia bất kỳ môn nào
columns_to_check = ['Toan', 'Van', 'Ngoai Ngu', 'Vat Ly', 'Hoa Hoc', 'Sinh Hoc', 'DTBTN', 'Lich Su', 'Dia Ly', 'GDCD', 'DTBXH']
df = df.dropna(subset=columns_to_check[1:], how='all')

# Lưu kết quả vào file CSV mới
df.to_csv(output_data, index=False)
