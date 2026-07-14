quantity= int(input("จำนวนปืนที่รับมาขาย"))
cost = int(input("ต้นทุนปืนที่รับมา"))
sell = int(input("ราคาที่จะนำไปขายต่อ"))
teammembers = int(input("จำนวนลูกน้อง"))

total = quantity * cost
profit = (sell - cost) * quantity
boss = profit * 0.2
real_profit = profit - boss
teammembers_profit = real_profit / teammembers
print (f"ต้นทุน{total} ")
print (f"ราคาขาย{sell}")
print (F"กำไรสุทธิ{profit}")
print (F"รายได้ของหัวหน้า{boss}")
print (F"รายได้ของลูกน้อง{teammembers_profit}")