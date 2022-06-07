import os

file_name = "names.txt"

#ファイルが存在しない場合
# if not os.path.isfile(file_name):
#     with open(file_name, mode="w") as f:
#         f.write("Saburo\n")
# else:
#     print("File exists!")

#モードをxにすると新規作成専用になる→ファイルが既に存在する場合は例外を発生させる
try:
    with open(file_name, mode="x") as f:
            f.write("Saburo\n")
except FileExistsError:
    print("File exists!")