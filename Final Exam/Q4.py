import arcpy
infile = r"C:\Data\FinalExam\data\crop_yield.txt"
outfile = r"C:\Data\FinalExam\data\out.txt"
f = open(infile)
for line in f.readlines():
    full_list = line.split(" ")
    list1 = []
    for item in full_list:
        list1.append(item.strip('\n'))
        print(list1)
        print("Average is {}."format(sum(list1)/len(list1)))

f = open(outfile,"w")
lines = "4.13,6.27,3.82,4.18,4.09"
f.write(lines)
f.close()


