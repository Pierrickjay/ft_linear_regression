import matplotlib.pyplot as plt
import sys
import csv


def parseCsv(file_obj):
	km_list = []
	price_value = []
	reader = csv.DictReader(file_obj)
	sorted_rows = sorted(reader, key= lambda row:int(row['km']))
	km_list = [int(row['km']) for row in sorted_rows]
	price_value = [int(row['price']) for row in sorted_rows]
	return (km_list, price_value)

km_list = []
price_value = []
f = open(sys.argv[1])
km_list, price_value= parseCsv(f)
print("km = ", km_list, "price value =",price_value)
fig, ax = plt.subplots() # fig is the figure and ax the value x, and y
ax.plot(km_list,price_value)
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()


