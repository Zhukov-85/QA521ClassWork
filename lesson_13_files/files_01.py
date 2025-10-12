import os


def display_dir_info(dirpath):
    for path, dirnames, filenames in os.walk(dirpath):
        print(f'Путь - {path}')
        print(f'Директории - {dirnames}')
        print(f'Файлы - {filenames}')


if __name__ == '__main__':
    path_learning_windows = r'D:\work_Top_Academy_QA\QA521ClassWork\lesson_12_funcs_pt2'
    path_learning_unix_based = r'D:/work_Top_Academy_QA/QA521ClassWork/lesson_12_funcs_pt2'
    """https://omni.top-academy.ru/#/presents"""
    # display_dir_info(path_learning_windows)
    # print()
    # display_dir_info(path_learning_unix_based)
    normalized_path = os.path.normpath(r'D:/work_Top_Academy_QA/QA521ClassWork/lesson_12_funcs_pt2')
    print(normalized_path)
    print(os.path.abspath('files_01.py'))
    print()

    disk = 'D:\\'
    dir_1 = 'work_Top_Academy_QA'
    dir_2 = 'QA521ClassWork'
    dir_3 = 'lesson_12_funcs_pt2'
    print(os.path.join(disk, dir_1, dir_2, dir_3))
    print()

    # !!! В ДЗ используем относительные пути (относительно текущего положения исполняемого файла) !!!
    # (если не указано другое)
    filepath = r'example_files'
    display_dir_info(r'example_files')




