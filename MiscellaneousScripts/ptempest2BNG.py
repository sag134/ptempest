#Python script to take parameter sets estimated using ptempest, 
#and write BNG files for them
import sys
import os
import h5py
import numpy as np

def writeParameter2File(parameter_set,BNGfilename,modifier):
	fr = open(BNGfilename,'r');
	#Insert modifier into BNGfilename
	index = BNGfilename.find('.bngl');
	newFile = BNGfilename[:index]+'_'+str(modifier)+BNGfilename[index:];
	fw = open(newFile,'w')
	#parTag indicates if we are currently in the parameter block
	parTag = 0;
	parCounter = 0;
	for line in fr:
		if "begin parameters" in line:
			parTag = 1;
			fw.write(line)
			continue;
		if "end parameters" in line:
			parTag = 0;
		if parTag == 0:
			fw.write(line)
		else:
			#Check for comment lines or new lines
			if line !="\n" and line.strip()[0]!='#':
				#find the first blank space of equal sign
				newline =  line.strip();
				fw.write(newline.split()[0]+' = ' + str(parameter_set[parCounter])+'\n');
				parCounter = parCounter + 1;
		
if __name__ =="__main__":
	#Inputs
	BNGfilename = "/shared/LabUserFiles/Sanjana/Aim2/github/ptempest/examples/PCAComparison/FullResponse/nfkbdecoupled1.bngl";
	ptempestFilename = "/shared/LabUserFiles/Sanjana/Aim2/github/ptempest/examples/PCAComparison/FullResponse/population_progress010400.mat"
	param_array_name = 'params_chain';
	step_lower = 1000;
	step_upper = 10000;
	step_int = 100;

	#Read the mat file
	matstructfile = h5py.File(ptempestFilename);
	parameters_array =  np.array(matstructfile[param_array_name])
	modifier = 1;
	for i in range(step_lower,step_upper+1,step_int):
		parameter_set = parameters_array[i,:,1];
		writeParameter2File(parameter_set,BNGfilename,modifier)
		modifier = modifier+1;
		print modifier


