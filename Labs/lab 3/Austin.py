# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Austin.py
# Created on: 2017-02-12 22:11:32.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
zipcodes = "zipcodes"
austin_shp = "C:\\Users\\lxi1\\Desktop\\GEOG 503\\lab\\lab 3\\data\\data\\Results\\austin.shp"
Row_Count = "43"
austin_Statistics_dbf = "C:\\Users\\lxi1\\Desktop\\GEOG 503\\lab\\lab 3\\data\\data\\Results\\austin_Statistics.dbf"

# Process: Select
arcpy.Select_analysis(zipcodes, austin_shp, "\"NAME\" = 'AUSTIN'")

# Process: Get Count
arcpy.GetCount_management(austin_shp)


# Process: Summary Statistics
arcpy.Statistics_analysis(austin_shp, austin_Statistics_dbf, "SHAPE_AREA SUM;SHAPE_AREA MEAN", "")

