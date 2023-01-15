#Abaqus libraries
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import assembly
executeOnCaeStartup()

#Number of samples
num_samples = 50

#Open model file
openMdb(pathName='D:/sampling/fuselage_sampling.cae')

#Import thickness values
file = open("D:/LHS_values.txt")
strut_thickness_values = []
frame_thickness_values = []

for i in range(0, num_samples):
    line_read = file.readline()
    strut_thickness_values.append(float(line_read[0:16])/1000)
    frame_thickness_values.append(float(line_read[18:35])/1000)

#Model mass
model_mass = []
mass_file = open('D:/mass_file.txt', "w")


for i in range(0, num_samples):
    path = "D:/sampling/" + "case" + str(i)
    #os.mkdir(path)
    os.chdir(path)

    #Change section thickness STRUTS
    mdb.models['Model-1'].sections['strut_section'].setValues(preIntegrate=OFF, 
        material='AL-7075', thicknessType=UNIFORM, thickness=strut_thickness_values[i], 
        thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
        integrationRule=SIMPSON, numIntPts=5)
    
    #Change section thickness FRAME
    mdb.models['Model-1'].sections['frame_section'].setValues(preIntegrate=OFF, 
        material='AL-7075', thicknessType=UNIFORM, thickness=frame_thickness_values[i], 
        thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
        integrationRule=SIMPSON, numIntPts=5)
    mass_properties = mdb.models['Model-1'].rootAssembly.getMassProperties()
    model_mass.append(mass_properties["mass"])
    mass_file.write(str(model_mass[i])+'\n')


