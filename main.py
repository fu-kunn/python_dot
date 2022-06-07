file_name = "names.txt"
# names = ["Taro", "Jiro", "Saburo", "Shiro"]

# with open(file_name, mode="w") as f:
#     for name in names:
#         f.write(f"{name}\n")

#r=read テキストファイルの内容を読み込む
with open(file_name, mode="r") as f:
    # names = f.read()
    
    #splitlines()=文字列を改行で分解してリスト化する
      names = f.read().splitlines()
print(names, end="")   