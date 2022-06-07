file_name = "names.txt"
names = ["Jiro", "Saburo", "Shiro"]

#末尾に追記する場合は「a=(append)」
with open(file_name, mode="a") as f:
    for name in names:
        f.write(f"{name}\n")