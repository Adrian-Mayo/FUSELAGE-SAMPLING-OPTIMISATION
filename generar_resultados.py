#Auxiliary libraries
import numpy
import os

#Abaqus libraries
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()

num_samples = 50


for i in range(0, num_samples):
    os.chdir('D:/sampling/' + 'case' + str(i))
    odb = session.openOdb(
        name='D:/sampling/' + 'case' + str(i)+'/detailed_fuselage_refined.odb')
#GENERATE ACCELERATIONS PASSENGER MIDDLE R
    xy_result = session.XYDataFromHistory(name='ACCELERATION_PASSENGER_MIDDLE_R', 
        odb=odb, 
        outputVariableName='Spatial acceleration: A2 PI: STIFFENED_FLOOR-1 Node 18 in NSET PASSENGER_MIDDLE_R', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['ACCELERATION_PASSENGER_MIDDLE_R']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="ACCELERATION_PASSENGER_MIDDLE_R" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['ACCELERATION_PASSENGER_MIDDLE_R']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/ACCELERATION_PASSENGER_MIDDLE_R.txt', xyData=(
        x0, ))
    
#GENERATE DISPLACEMENTS PASSENGER MIDDLE R
    xy_result = session.XYDataFromHistory(name='DISPLACEMENT_PASSENGER_MIDDLE_R', 
        odb=odb, 
        outputVariableName='Spatial displacement: U2 PI: STIFFENED_FLOOR-1 Node 18 in NSET PASSENGER_MIDDLE_R', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['DISPLACEMENT_PASSENGER_MIDDLE_R']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="DISPLACEMENT_PASSENGER_MIDDLE_R" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['DISPLACEMENT_PASSENGER_MIDDLE_R']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/DISPLACEMENT_PASSENGER_MIDDLE_R.txt', xyData=(
        x0, ))
        
#GENERATE ACCELERATIONS PASSENGER MIDDLE L
    xy_result = session.XYDataFromHistory(name='ACCELERATION_PASSENGER_MIDDLE_L', 
        odb=odb, 
        outputVariableName='Spatial acceleration: A2 PI: STIFFENED_FLOOR-1 Node 51 in NSET PASSENGER_MIDDLE_L', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['ACCELERATION_PASSENGER_MIDDLE_L']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="ACCELERATION_PASSENGER_MIDDLE_L" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['ACCELERATION_PASSENGER_MIDDLE_L']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/ACCELERATION_PASSENGER_MIDDLE_L.txt', xyData=(
        x0, ))

#GENERATE DISPLACEMENTS PASSENGER MIDDLE L
    xy_result = session.XYDataFromHistory(name='DISPLACEMENT_PASSENGER_MIDDLE_L', 
        odb=odb, 
        outputVariableName='Spatial displacement: U2 PI: STIFFENED_FLOOR-1 Node 51 in NSET PASSENGER_MIDDLE_L', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['DISPLACEMENT_PASSENGER_MIDDLE_L']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="DISPLACEMENT_PASSENGER_MIDDLE_L" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['DISPLACEMENT_PASSENGER_MIDDLE_L']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/DISPLACEMENT_PASSENGER_MIDDLE_L.txt', xyData=(
        x0, ))

#GENERATE ACCELERATIONS PASSENGER WINDOW R
    xy_result = session.XYDataFromHistory(name='ACCELERATION_PASSENGER_WINDOW_R', 
        odb=odb, 
        outputVariableName='Spatial acceleration: A2 PI: STIFFENED_FLOOR-1 Node 70 in NSET PASSENGER_WINDOW_R', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['ACCELERATION_PASSENGER_WINDOW_R']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="ACCELERATION_PASSENGER_WINDOW_R" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['ACCELERATION_PASSENGER_WINDOW_R']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/ACCELERATION_PASSENGER_WINDOW_R.txt', xyData=(
        x0, ))


#GENERATE DISPLACEMENTS PASSENGER WINDOW R  
    xy_result = session.XYDataFromHistory(name='DISPLACEMENT_PASSENGER_WINDOW_R', 
        odb=odb, 
        outputVariableName='Spatial displacement: U2 PI: STIFFENED_FLOOR-1 Node 70 in NSET PASSENGER_WINDOW_R', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['DISPLACEMENT_PASSENGER_WINDOW_R']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="DISPLACEMENT_PASSENGER_WINDOW_R" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['DISPLACEMENT_PASSENGER_WINDOW_R']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/DISPLACEMENT_PASSENGER_WINDOW_R.txt', xyData=(
        x0, ))

#GENERATE ACCELERATIONS PASSENGER WINDOW L
    xy_result = session.XYDataFromHistory(name='ACCELERATION_PASSENGER_WINDOW_L', 
        odb=odb, 
        outputVariableName='Spatial acceleration: A2 PI: STIFFENED_FLOOR-1 Node 103 in NSET PASSENGER_WINDOW_L', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['ACCELERATION_PASSENGER_WINDOW_L']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="ACCELERATION_PASSENGER_WINDOW_L" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['ACCELERATION_PASSENGER_WINDOW_L']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/ACCELERATION_PASSENGER_WINDOW_L.txt', xyData=(
        x0, ))


#GENERATE DISPLACEMENTS PASSENGER WINDOW L 
    xy_result = session.XYDataFromHistory(name='DISPLACEMENT_PASSENGER_WINDOW_L', 
        odb=odb, 
        outputVariableName='Spatial displacement: U2 PI: STIFFENED_FLOOR-1 Node 103 in NSET PASSENGER_WINDOW_L', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['DISPLACEMENT_PASSENGER_WINDOW_L']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="DISPLACEMENT_PASSENGER_WINDOW_L" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['DISPLACEMENT_PASSENGER_WINDOW_L']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/DISPLACEMENT_PASSENGER_WINDOW_L.txt', xyData=(
        x0, ))

#GENERATE ACCELERATIONS PASSENGER AISLE R
    xy_result = session.XYDataFromHistory(name='ACCELERATION_PASSENGER_AISLE_R', 
        odb=odb, 
        outputVariableName='Spatial acceleration: A2 PI: STIFFENED_FLOOR-1 Node 83 in NSET PASSENGER_AISLE_R', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['ACCELERATION_PASSENGER_AISLE_R']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="ACCELERATION_PASSENGER_AISLE_R" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['ACCELERATION_PASSENGER_WINDOW_R']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/ACCELERATION_PASSENGER_AISLE_R.txt', xyData=(
        x0, ))


#GENERATE DISPLACEMENTS PASSENGER AISLE R 
    xy_result = session.XYDataFromHistory(name='DISPLACEMENT_PASSENGER_AISLE_R', 
        odb=odb, 
        outputVariableName='Spatial displacement: U2 PI: STIFFENED_FLOOR-1 Node 83 in NSET PASSENGER_AISLE_R', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['DISPLACEMENT_PASSENGER_AISLE_R']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="DISPLACEMENT_PASSENGER_AISLE_R" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['DISPLACEMENT_PASSENGER_AISLE_R']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/DISPLACEMENT_PASSENGER_AISLE_R.txt', xyData=(
        x0, ))

#GENERATE ACCELERATIONS PASSENGER AISLE L
    xy_result = session.XYDataFromHistory(name='ACCELERATION_PASSENGER_AISLE_L', 
        odb=odb, 
        outputVariableName='Spatial acceleration: A2 PI: STIFFENED_FLOOR-1 Node 96 in NSET PASSENGER_AISLE_L', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['ACCELERATION_PASSENGER_AISLE_L']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="ACCELERATION_PASSENGER_AISLE_L" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['ACCELERATION_PASSENGER_WINDOW_L']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/ACCELERATION_PASSENGER_AISLE_L.txt', xyData=(
        x0, ))


#GENERATE DISPLACEMENTS PASSENGER AISLE L 
    xy_result = session.XYDataFromHistory(name='DISPLACEMENT_PASSENGER_AISLE_L', 
        odb=odb, 
        outputVariableName='Spatial displacement: U2 PI: STIFFENED_FLOOR-1 Node 96 in NSET PASSENGER_AISLE_L', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['DISPLACEMENT_PASSENGER_AISLE_L']
    xy2 = sae600Filter(xyData=xy1, timeScaleFactor=1)
    xy2.setValues(
        sourceDescription='sae600Filter ( xyData="DISPLACEMENT_PASSENGER_AISLE_L" , timeScaleFactor=  1)')
    tmpName = xy2.name
    x0 = session.xyDataObjects['DISPLACEMENT_PASSENGER_AISLE_L']
    session.xyReportOptions.setValues(pageWidthLimited=SPECIFY)
    session.xyReportOptions.setValues(numberFormat=SCIENTIFIC)
    session.writeXYReport(
        fileName='D:/sampling/' + 'case' + str(i) + '/DISPLACEMENT_PASSENGER_AISLE_L.txt', xyData=(
        x0, ))