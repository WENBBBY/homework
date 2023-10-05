# 什麼是 String, f-string, r-string以及用法並給出例子

# string
# 1.string，將字元透過單引號或雙引號串起來就是字串
print('Wenby')
print("Wenby")

# 2.想知道單引號及雙引號的差異？？？
print("'Wenby' is my name")
print('"Wenby" is my name')

# 3.也可以透過三個單引號或雙引號直接印出
print("""wwwwweeeeennnnnbbbbbyyyyy""")
print('''yyyyybbbbbnnnnneeeeewwwww''')

# 4.可以將數字轉換成字串
a = str(123)
print(a)


# f-string，F或f皆可，字串中可以用來格式化，如進行計算、進制轉換、對齊等等，用法為f{變數名稱或運算式等等}
# 1.計算
a = 1
b = 2
print(f'{a+b}')

# 2.變數
pet = '吉娃娃'
food = '蘋狗'
print(f"我的 {pet} 喜歡吃 {food} ")

# 3.進制，:s字串,:d十進制,:x十六進制,:o八進制,:b二進制,:f十進制浮點數,:e指數浮點數,:g十進制或指數浮點數

# 4.對齊，:>向右,:<向左,:^置中


# r-string，R或r皆可，字串將不會進行任何轉換，用法為r'string'
# 1.例如當字串中若有\n會自動執行換行，但想保留原始字串時
# 以下狀況將會發生換行
a = 'wen\nby'
print (a)
# 加入r，將可顯示包含\n的原始字串
a = r'wen\nby'
print (a)