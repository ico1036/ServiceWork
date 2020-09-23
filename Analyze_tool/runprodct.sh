#!/bin/bash




cd /x5/cms/jwkim/ServiceWork/tmp/Analysis




## -- FULL run
#for i in `seq 1 4`
#do
#    idx=`expr $i + 1`
#    for j in `seq $idx 5`
#    do
#		echo "Start $i $j"
#	
#
#		## --STEP3
#		./N04_compareProducts.sh CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j > compare_products_11_2_0/prod_compare_cpu_11_2_0Pre$i\vsPre$j\.txt
#		## --STEP4
#        ./N04_compareProducts.sh CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$j > compare_products_11_2_0/prod_PAT_compare_cpu_11_2_0Pre$i\vsPre$j\.txt
#    done
#done

## --One and the others

target=6
for i in `seq 1 5`
do
	echo "Start $i vs $target"
	
	## --STEP3
	#./N04_compareProducts.sh CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$target > compare_products_11_2_0/prod_compare_cpu_11_2_0Pre$i\vsPre$target\.txt
	## --STEP4
    ./N04_compareProducts.sh CMSSW_11_2_0_pre$i CMSSW_11_2_0_pre$target > compare_products_11_2_0/prod_PAT_compare_cpu_11_2_0Pre$i\vsPre$target\.txt
done
