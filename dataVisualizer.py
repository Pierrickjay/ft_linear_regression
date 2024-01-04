import matplotlib.pylot as plt


def parseCsv(file_obj):
	content = file_obj.read()
	names =  content.split()
	print(names)


f = open(sys.argv[1])
parseCsv(f)

