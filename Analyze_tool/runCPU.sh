#!/bin/bash






### Full comparison
#for i in `seq 1 4`
#do
#    idx=`expr $i + 1`
#    for j in `seq $idx 5`
#    do
#		echo "Start $i $j"
#        python N01_compare_cpu.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j > compare_results_11_2_0/cl_compare_cpu_11_2_0Pre$i\vsPre$j\.txt
#		python N01_compare_cpu.py CMSSW_11_2_0_pre$i\PAT CMSSW_11_2_0_pre$j\PAT > compare_results_11_2_0/cl_PAT_compare_cpu_11_2_0Pre$i\vsPre$j\.txt
#
#    done
#done




## One and the others
for i in `seq 1 5`
do
		echo "Start $i 6"
        python N01_compare_cpu.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre6 > compare_results_11_2_0/cl_compare_cpu_11_2_0Pre$i\vsPre6.txt
		python N01_compare_cpu.py CMSSW_11_2_0_pre$i\PAT CMSSW_11_2_0_pre6PAT > compare_results_11_2_0/cl_PAT_compare_cpu_11_2_0Pre$i\vsPre6.txt

done




