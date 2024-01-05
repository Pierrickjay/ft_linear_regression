import matplotlib.pyplot as plt
import sys
import csv

def parseCsv(file_obj):
	km_list = []
	price_value = []
	reader = csv.DictReader(file_obj)
	for row in reader:
		km_list.append(int(row['km']))
		price_value.append(int(row['price']))
	return (km_list, price_value)

km_list = []
price_value = []
f = open(sys.argv[1])
km_list, price_value= parseCsv(f)
plt.scatter(km_list, price_value, color='blue', marker='o', label='Data Points')
plt.xlabel('Mileage (km)')
plt.ylabel('Price')
plt.title('Scatter Plot of Mileage vs. Price')
plt.legend()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()


