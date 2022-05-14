# 論理演算子

eng_score = int(input("English score? "))
math_score = int(input("Math score? "))

# if eng_score == 100 and math_score == 100:
if not(eng_score == 100 or math_score == 100):
    print("OK")
else:
    print("NG")
