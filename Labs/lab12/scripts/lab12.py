import arcpy
from arcpy.mapping import *

mxd = arcpy.GetParameterAsText(0)
outpdf = arcpy.GetParameterAsText(1)
merge = arcpy.GetParameterAsText(2)
existpdf = arcpy.GetParameterAsText(3)

mapdoc = MapDocument(mxd)
pdfpath = r"C:\Data\lab12\mapbook.pdf"
pdfdoc = PDFDocumentCreate(pdfpath)
mapdoc.dataDrivenPages.exportToPDF(outpdf)

if merge:
   if arcpy.Exists(existpdf):
       existdoc = PDFDocumentOpen(existpdf)
       existdoc.appendPages(outpdf)
       existpdf.saveAndClose()
       pdfdoc.appendPages(outpdf)
       pdfdoc.saveAndClose()

del mapdoc