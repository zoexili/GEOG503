import arcpy
arcpy.env.workspace = r"C:\Geog 503\inclass03_data"
arcpy.MosaicToNewRaster_management('ASTGTM2_N42W076_dem.tif;ASTGTM2_N42W077_dem.tif', r'C:\Geog 503\inclass03_data', 'broome.tif', '#', '8_BIT_UNSIGNED', '#', '1', 'BLEND', 'FIRST')
arcpy.gp.ExtractByMask_sa('broome.tif', 'NY_Counties', r'C:\Users\lxi1\Documents\ArcGIS\Default.gdb\Extract_tif1')
arcpy.Statistics_analysis('Extract_tif1', r'C:\Users\lxi1\Documents\ArcGIS\Default.gdb\Extract_tif1_Statistics', 'Value MEAN', '#')

