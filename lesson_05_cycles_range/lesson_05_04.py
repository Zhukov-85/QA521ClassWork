for i in range(1, 1):
    print(f"Внутри цикла {i}")
print("Вне цикла.")
print()

for i in range(2, 1):
    print(f"Внутри цикла {i}")
print("Вне цикла.")
print()

# нормализация границ цикла
start = 10
end = 5

if start > end:
    start, end = end, start

for i in range(start, end):
    print(f"Внутри цикла {i}")
print("Вне цикла.")
print()

# for i in range():
#     print(f"Внутри цикла {i}")
# print("Вне цикла.")
# print()


for i in range(10, 0, -1):
    print(f"Внутри цикла {i}")
print("Вне цикла.")
print()

end = 10

for i in range(end):
    print(f"Внутри цикла {end - i}")
print("Вне цикла.")
print()

end = 10

for i in range(end + 1):
    print(f"Внутри цикла {end - i}")
print("Вне цикла.")
print()
