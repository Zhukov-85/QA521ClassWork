my_path = 'D:\\work_Top_Academy_QA\\QA521ClassWork\\lesson_06_strings\\files_dir'
my_path_raw = r'D:\work_Top_Academy_QA\QA521ClassWork\lesson_06_strings\files_dir'

normal_string = "В Python последовательность\nотвечает за перенос строки"
print(normal_string)

raw_string = r"В Python последовательность \n отвечает за перенос строки (это уже сырая строка)"
print(raw_string)

some_data_list = [r'\n', r'\t', r'\r']
formatted_raw_string = fr"В Python последовательности: {', '.join(some_data_list)} отвечают за работу со строкой (это уже сырая строка)"
print(formatted_raw_string)


# filepath = 'files_dir\\new_file.txt'
# with open(filepath, 'w', encoding='utf-8') as file:
#     file.write('Привет Мир!')
#
# filename = 'new_file1.txt'
# filepath_1 = fr'files_dir\{filename}'
#
# with open(filepath_1, 'w', encoding='utf-8') as file:
#     file.write('Привет Мир!')
