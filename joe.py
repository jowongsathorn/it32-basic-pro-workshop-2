quantity= int(input("จำนวนปืนที่รับมาขาย"))
cost = int(input("ต้นทุนปืนที่รับมา"))
sell = int(input("ราคาที่จะนำไปขายต่อ"))
teammembers = int(input("จำนวนลูกน้อง"))

total = quantity * cost
total2 = sell * teammembers
profit = total+total2
print (f"ต้นทุน{total} ")
print (f"ราคาขาย{total2}")
print (F"กำไรสุทธิ{profit}")
print (F"")