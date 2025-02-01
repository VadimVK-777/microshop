from typing import Optional


# def say_hi(name: Optional[str]):
#     if name is not None:
#         print(f"Hey {name}!")
#     else:
#         print("Hello World")
#
#
# say_hi("string")
# say_hi("")
# say_hi(None)

print()
print()
from typing import Optional


def greet(name: Optional[str]) -> str:
    return f"Hello, {name}!"


print(greet(None))  # Ошибка: TypeError

#
# def get_full_name(a: int, b: int) -> int:
#     result1 = a + b
#     return result1
#
#
# def get_full_name1(a, b):
#     result1 = a + b
#     return result1
#
#
# print(get_full_name(1, "2"))
# # print(get_full_name(1, 2))
#
# # print(get_full_name1(1, 2))
# print(get_full_name1([1, 2], 2))
# # print(get_full_name1([1, 2], "str"))
# # print(get_full_name1(1, "str"))
# # print(get_full_name1([1, 2], 2))
# # print(get_full_name1([1, 2], 2))
