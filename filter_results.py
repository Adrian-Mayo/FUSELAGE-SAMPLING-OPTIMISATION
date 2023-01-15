#Auxiliary libraries
import numpy
import os

num_samples = 50

#Open results file
results_summary_dakota = open("D:/results_summary_dakota.txt", "w")
mass_file = open("D:/mass_file.txt")

#Headers for results file
results_summary_dakota.write('%Eval_ID interface strut_thc frame_thc max_accel max_hic max_disp mass\n')

#Keys
keys = ['PASSENGER_MIDDLE_R', 'PASSENGER_AISLE_R', 'PASSENGER_WINDOW_R', 'PASSENGER_MIDDLE_L', 'PASSENGER_AISLE_L', 'PASSENGER_WINDOW_L']

#Total values for parameters
global_max_acceleration = []
global_max_HIC = []
global_max_displacement = []

# Time increment calculation functions
#New end timestamp
def calculate_new_end_timestamp(timestamps_data, base_timestamp_position):
    time_increment = 0
    iteration = 0

    while time_increment < 0.015:
        time_increment = timestamps_data[base_timestamp_position + 1 + iteration] - \
                         timestamps_data[base_timestamp_position]
        iteration = iteration + 1

    new_timestamp_position = base_timestamp_position + iteration
    return new_timestamp_position

#New starting timestamp
def calculate_new_start_timestamp(timestamps_data, base_timestamp_position):
    time_increment = 0
    iteration = 0

    while time_increment < 0.005:
        time_increment = timestamps_data[base_timestamp_position + 1 + iteration] - \
                         timestamps_data[base_timestamp_position]
        iteration = iteration + 1

    new_timestamp_position = base_timestamp_position + iteration
    return new_timestamp_position

thickness_file = open("D:/LHS_values.txt")
strut_thickness_values = []
frame_thickness_values = []

for i in range(0, num_samples):
    line_read = thickness_file.readline()
    strut_thickness_values.append(float(line_read[0:16])/1000)
    frame_thickness_values.append(float(line_read[18:35])/1000)

#Read masses
mass = []
for i in range(0, num_samples):
    line_read = mass_file.readline()
    mass.append(float(line_read[0:16]))

for i in range(0, num_samples):
    os.chdir('D:/sampling/' + 'case' + str(i))
    max_accelerations = []
    max_HICs = []
    max_displacements = []
    for k in keys: 
        file = open('ACCELERATION_' + k + '.txt')
        data_lines = 0
        # Skip the first line of the document
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        # Declare data arrays for timestamps, accelerations and HICs
        timestamps = []
        accelerations = []
        HIC_array = []
        # Auxiliary variables for the file reading loop
        line_read = 0
        control_EOF = 0 
           
        # Read data file loop
        while control_EOF < 0.15:
            line_read = file.readline()
            timestamps.append(float(line_read[11:22]))
            accelerations.append(float(line_read[24:36]) / 9.81)
            control_EOF = float(line_read[11:22])
    
        start_timestamp = 0
        end_timestamp = 0
    
        while timestamps[end_timestamp] < 0.115:
            end_timestamp = calculate_new_end_timestamp(timestamps, start_timestamp)
            integral = numpy.trapz(accelerations[start_timestamp:end_timestamp], x=timestamps[start_timestamp:end_timestamp])
            HIC_array.append(((abs(integral) / (timestamps[end_timestamp] - timestamps[start_timestamp]))**2.5)
                             * (timestamps[end_timestamp]-timestamps[start_timestamp]))
            start_timestamp = calculate_new_start_timestamp(timestamps, start_timestamp)
        
        max_accelerations.append(max(accelerations))
        max_HICs.append(max(HIC_array))  
        file.close()    
        file = open('DISPLACEMENT_' + k + '.txt')
        data_lines = 0
        # Skip the first line of the document
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        # Declare data arrays for timestamps, accelerations and HICs
        timestamps_disp = []
        displacements = []
        # Auxiliary variables for the file reading loop
        line_read = 0
        control_EOF = 0 
           
        # Read data file loop
        while control_EOF < 0.15:
            line_read = file.readline()
            timestamps_disp.append(float(line_read[11:22]))
            displacements.append(float(line_read[24:36]) / 9.81)
            control_EOF = float(line_read[11:22])
            
        max_displacements.append(abs(min(displacements)))
        file.close()
    global_max_acceleration.append(sum(max_accelerations)/6)
    global_max_HIC.append(sum(max_HICs)/6)
    global_max_displacement.append(sum(max_displacements)/6)
    
    #Write outputs
    results_summary_dakota.write(str(i+1))
    results_summary_dakota.write(' ')
    results_summary_dakota.write('NO_ID ')
    results_summary_dakota.write('{:.16f}'.format(round(strut_thickness_values[i], 16)))
    results_summary_dakota.write(' ')
    results_summary_dakota.write('{:.16f}'.format(round(frame_thickness_values[i], 16)))
    results_summary_dakota.write(' ')
    results_summary_dakota.write('{:.16f}'.format(round(global_max_acceleration[i], 16)))
    results_summary_dakota.write(' ')
    results_summary_dakota.write('{:.16f}'.format(round(global_max_HIC[i], 16)))
    results_summary_dakota.write(' ')
    results_summary_dakota.write('{:.16f}'.format(round(global_max_displacement[i], 16)))
    results_summary_dakota.write(' ')
    results_summary_dakota.write('{:.16f}'.format(round(mass[i], 16)))
    results_summary_dakota.write('\n')

results_summary_dakota.close()
