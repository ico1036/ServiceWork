#!/bin/bash




## FUll run
#for i in `seq 1 4`
#do
#    idx=`expr $i + 1`
#    for j in `seq $idx 5`
#    do
#		echo "Start $i $j"
#		## --step3
#		#./N03_timeDiffFromReport.sh CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j > compare_timedff_11_2_0/tdf_compare_cpu_11_2_0Pre$i\vsPre$j\.txt
#        
#		## --step4
#		./N03_timeDiffFromReport.sh CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j > compare_timedff_11_2_0/tdf_PAT_compare_cpu_11_2_0Pre$i\vsPre$j\.txt
#    done
#done



target=6
for i in `seq 1 5`
do
		echo "Start $i vs $target"
		## --step3
		#./N03_timeDiffFromReport.sh CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$target > compare_timedff_11_2_0/tdf_compare_cpu_11_2_0Pre$i\vsPre$target\.txt
        
		## --step4
		./N03_timeDiffFromReport.sh CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$target > compare_timedff_11_2_0/tdf_PAT_compare_cpu_11_2_0Pre$i\vsPre$target\.txt
done

