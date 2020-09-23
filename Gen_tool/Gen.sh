#!/bin/bash

CMSSW_v=$1

## --1. Install CMSSW version and setup environment
echo "Your SCRAM_ARCH "
export SCRAM_ARCH=slc7_amd64_gcc900
#export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
echo "$VO_CMS_SW_DIR $SCRAM_ARCH"
source $VO_CMS_SW_DIR/cmsset_default.sh

echo "Start install $CMSSW_v ..."
scramv1 project $CMSSW_v
echo "Install success"
echo "Set CMSSW environment and compiling..'"
cd $CMSSW_v/src
eval `scramv1 runtime -sh`
scram b -j 6


## --2. "RunThematrix" dry run


#runTheMatrix.py -l 29034.21 -w upgrade --dryRun # NoPU

runTheMatrix.py -l 23434.21 -w upgrade --dryRun	# 200PU for D49
#runTheMatrix.py -l 20634.21 -w upgrade --dryRun	# 200PU for 4 5 6  D41


#runTheMatrix.py -w upgrade -l 29234.21 --dryRun #200PU for 11_0_0_pre1 2 3 D41 


tail *.log

for i in $(ls -d */); do 
outname=${i%%/}; done
mv $outname TimeMemory
cd TimeMemory


## -- Not yet ---------
# --3. Make cmdLog run_option  -- Set N events
#cat << EOF >> read.py
#import subprocess
#
#with open('cmdLog','r') as f:
#	cnt=0
#	for line in f:
#		line=line.rstrip()
#		if line.startswith(' cmsDriver'):
#			cnt+=1
### --Set N events
#            #line=line.replace("-n 10","-n 1000")
#			if cnt==3:
#				line_list = line.split()
#				logfile = line_list[-2]
#				line_list.insert(-7,"--customise=Validation/Performance/TimeMemoryInfo.py")
#				line=' '.join(line_list)
#				line=line.replace(logfile,"step3.log")
### --Do not run step4
#			if cnt==4: break
### --Excute cmsDriver
#            #subprocess.check_output (line,shell=True)
#			print(line)
#			print(" ")
#EOF
# run cmsDriver.py
#python read.py
# ---------------------------------------

## --4. Make profiler 




mkdir igprof_cpu
cat << EOF >> igprof_cpu/profile.sh
#!/bin/bash


## --For web-based report

## -step3
   igprof-analyse --sqlite -v -d -g igprofCPU_step3.gz | sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 igprofCPU_${1}.sql3 >& CPUsql.log

## -step4
    igprof-analyse --sqlite -v -d -g igprofCPU_step4.gz | sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 igprofCPU_${1}PAT.sql3 >& CPUsql.log


## --For ascii-based report
## -step3
   igprof-analyse  -v -d -g igprofCPU_step3.gz >& RES_CPU_${1}.res

## -step4
    igprof-analyse  -v -d -g igprofCPU_step4.gz >& RES_PAT_CPU_${1}.res

EOF


mkdir igprof_mem_step3 igprof_mem_step4

cat <<EOF >> igprof_new_step3/profile_v2.sh

igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE IgProf.1.gz |sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 ig.1.sql3
igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE IgProf.99.gz |sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 ig.99.sql3

igprof-analyse  -v --demangle --gdb -r MEM_LIVE IgProf.1.gz >& RES_MEM_Step3_IgProf1.res
igprof-analyse  -v --demangle --gdb -r MEM_LIVE IgProf.99.gz >& RES_MEM_Step3_IgProf99.res
EOF


cat << EOF >> igprof_mem_step3/profile_v2.sh
igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE IgProf.1.gz |sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 ig.1.sql3
igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE IgProf.50.gz |sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 ig.50.sql3
igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE IgProf.99.gz |sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 ig.99.sql3

igprof-analyse  -v --demangle --gdb -r MEM_LIVE IgProf.1.gz >& RES_MEM_Step3_IgProf1.res
igprof-analyse  -v --demangle --gdb -r MEM_LIVE IgProf.50.gz >& RES_MEM_Step3_IgProf50.res
igprof-analyse  -v --demangle --gdb -r MEM_LIVE IgProf.99.gz >& RES_MEM_Step3_IgProf99.res
EOF


cat << EOF >> igprof_mem_step4/profile_v2.sh
igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE IgProf.1.gz |sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 ig.1.sql3
igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE IgProf.50.gz |sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 ig.50.sql3
igprof-analyse --sqlite -v --demangle --gdb -r MEM_LIVE IgProf.99.gz |sed -e 's/INSERT INTO files VALUES (\([^,]*\), \"[^$]*/INSERT INTO files VALUES (\1, \"ABCD\");/g' | sqlite3 ig.99.sql3

igprof-analyse  -v --demangle --gdb -r MEM_LIVE IgProf.1.gz >& RES_MEM_Step4_IgProf1.res
igprof-analyse  -v --demangle --gdb -r MEM_LIVE IgProf.50.gz >& RES_MEM_Step4_IgProf50.res
igprof-analyse  -v --demangle --gdb -r MEM_LIVE IgProf.99.gz >& RES_MEM_Step4_IgProf99.res
EOF



mkdir logs

