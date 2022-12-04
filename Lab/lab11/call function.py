import lab11

import lab11.function
import lab11.classes
import lab11.analysis

#call the function module from the lab11 package
lab11.function.ClipRaster()

#call the class module from the lab11 package
myclip = ClipRaster()
myclip.workspace = workspace
myclip.clipfc = clipfc
myclip.output_dir = output_dir


#call the analysis module from the lab11 package
workspace = r"C:\Data\lab10"
clipfc = r"C:\Data\lab10"
output_dir = r"C:\Data\lab10\results"
lab11.analysis.ClipRaster(workspace,clipfc,output_dir)