
# coding: utf-8

# # Question 1

# In[1]:

import arcpy
import os

infile = arcpy.GetParameterAsText(0)
fc = arcpy.GetParameterAsText(1)

arcpy.env.workspace = infile
arcpy.env.overwriteOutput = True

pointList =[]

f = open(infile)
for line in f.readlines():
    list1 = line.split(", ")
    point = []
    for item in list1:
        subitem = item.split(": ")
        point.append(subitem[1].strip('\n'))
    pointList.append(point)

if arcpy.Exists(fc) == False:
        arcpy.CreateFeatureclass_management(os.path.split(fc)[0],os.path.split(fc)[1],"Point")

arcpy.AddField_management(fc,"Id","float")
arcpy.AddField_management(fc,"Name","string",field_length=50)
arcpy.AddField_management(fc,"LOCID","string",field_length=10)
arcpy.AddField_management(fc,"X","double")
arcpy.AddField_management(fc,"Y","double")

fields = ["Id","NAME","LOCID","X","Y","SHAPE@X","SHAPE@Y"]
cursor = arcpy.da.InsertCursor(fc, fields)

for point in pointList:
    id = int(point[0])
    name = point[1]
    locid = point[2]
    x = float(point[3])
    y = float(point[4])
    cursor.insertRow([id,name,locid,x,y,x,y])
del cursor

