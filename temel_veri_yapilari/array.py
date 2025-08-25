# Array oluşturma
arr = [10, 20, 30, 40, 50]

# Elemanlara erişim
print(arr[0]) # 10
print(arr[3]) # 40

# Eleman değiştirme
arr[2] = 35
print(arr) # [10, 20, 35, 40, 50]

# Eleman ekleme
arr.append(60)
print(arr) # [10, 20, 35, 40, 50, 60]

arr.pop(1) # 1.indeksteki elemanı siler (20)
print(arr) # [10, 35, 40, 50, 60]

#--------------------------------------------------

numbers = [5, 10, 15, 20, 25]

# Toplamını bulma 
total = sum(numbers)
print("total:", total) # 75

# En büyük sayıyı bulma
print("En büyük:", max(numbers)) # 25

# Ters çevirme

numbers.reverse()
print(numbers) # [25, 20, 15, 10, 5]
