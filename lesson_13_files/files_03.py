# def get_guest_count(guests_file):
#     guests_count = 0
#     guests_list = []
#     with open(guests_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             guests_list.append(line.strip())
#             guests_count += 1
#     return guests_count, guests_list


def get_guests_and_count(guests_file):
    with open(guests_file, 'r', encoding='utf-8') as file:
        guests_list = file.readlines()
    return guests_list, len(guests_list)


if __name__ == '__main__':
    user_guests_file = r'example_files\guests.txt'
    try:
        user_guests, user_guests_num = get_guests_and_count(user_guests_file)
        print(f"Гости мероприятия: {user_guests}")
        print(f"Гости мероприятия:\n{''.join(user_guests)}")
        print(f'Всего гостей: {user_guests_num}')
    except Exception as ex:
        print(type(ex).__name__)
