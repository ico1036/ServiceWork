#!/bin/bash


#echo " ######## START 11_0_0 version ##########"
#for i in `seq 1 4`
#do
#    idx=`expr $i + 1`
#    for j in `seq $idx 5`
#    do
#		echo "Start $i $j"
#
#		python N01_compare_mem.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j --step step3 --level 1 > compare_results_mem_11_2_0/cl_RECO_ig1_compare_mem_11_2_0Pre$i\vsPre$j\.txt
#		python N01_compare_mem.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j --step step3 --level 99 > compare_results_mem_11_2_0/cl_RECO_ig99_compare_mem_11_2_0Pre$i\vsPre$j\.txt
#		python N01_compare_mem.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j --step step4 --level 1 > compare_results_mem_11_2_0/cl_PAT_ig1_compare_mem_11_2_0Pre$i\vsPre$j\.txt
#		python N01_compare_mem.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j --step step4 --level 99 > compare_results_mem_11_2_0/cl_PAT_ig99_compare_mem_11_2_0Pre$i\vsPre$j\.txt
#
#
#    done
#done


for i in `seq 1 5 `
do
	target=6
	echo "Start $i vs $target"
   python N01_compare_mem.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$target --step step3 --level 1 >  compare_results_mem_11_2_0/cl_RECO_ig1_compare_mem_11_2_0Pre$i\vsPre$target\.txt
   python N01_compare_mem.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$target --step step3 --level 99 > compare_results_mem_11_2_0/cl_RECO_ig99_compare_mem_11_2_0Pre$i\vsPre$target\.txt
   python N01_compare_mem.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$target --step step4 --level 1 >  compare_results_mem_11_2_0/cl_PAT_ig1_compare_mem_11_2_0Pre$i\vsPre$target\.txt
   python N01_compare_mem.py CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$target --step step4 --level 99 > compare_results_mem_11_2_0/cl_PAT_ig99_compare_mem_11_2_0Pre$i\vsPre$target\.txt

done
