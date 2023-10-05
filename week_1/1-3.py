# 寫出一個函式，印出所有python基本資料類別，列出並附上說明

# 定義函式名稱為type_function，並印出python的基本資料類別
def type_function():
    print ("基本資料類別為:'字串string','整數int','浮點數float','布林值boolean','列表list','字典dictionary','元組tuple','集合set'")
# 呼叫所定義的函式
type_function()


#一、以自己為單位
# 1.字串(string)，將字元透過單引號或雙引號串起來就是字串
print ("1.字串(string)，將字元透過單引號或雙引號串起來就是字串，例如('Wenby')")
print ('Wenby')
# 2.整數(int)，即整數值
print ("2.整數(int)，即整數值，例如('1')")
print (1)
# 好奇了一下-1是int嗎，透過type來確認是int沒錯～
print (type(-1))
# 3.浮點數(float)，包含小數點
print ("3.浮點數(float)，包含小數點，例如('8.25')")
print (8.25)
# 4.布林值(boolean)，output為True or Flase，測試是否正確性
# True範例
print ("4-1.布林(bool)，為判斷是否為真，測試('True')")
x = 5
y = 5
print (bool(x == y))
# Flase範例
print ("4-2.布林(bool)，為判斷是否為真，測試('Flase')")
x = 5
y = 500
print (bool(x == y))

#二、可以包含多筆資料
# 1.列表(list)，可以同時有不同類型的資料
print ("1.列表(list)，可以同時有不同類型的資料")
print (list['12345',67890,True])
# 2.字典(dict)，結構為key和value構成
print ("2.字典(dict)，為key和value構成")
print ({"color":"pink"})
# 3.元組(tuple)，將物件存入，變成有順序的序列結構
print ("3.元祖(tuple)，將物件存入，變成有順序的序列結構")
a = (('A','B','C','D','E'))
b = (('一','二','三','四','五'))
print (a+b)
# 4.集合(set)，由字串、數字、布林，不同的類別組成，用法為set()或大括號{}
print ("4.集合(set)，由字串、數字、布林，不同的類別組成")
#使用set()時，如果出現重複項目就只會保留一個
a = set([1,2,3,1,1,1])
print (a)
#如果是字典(dict)就只會保留key
b = set({'number1':1,'number2':2,'number3':3})
print (b)
#使用大括號{}，有布林時轉換True=1,Flase=0，且重複項目一樣只會保留一個
c = set({0,3,7,True,False})
print (c)