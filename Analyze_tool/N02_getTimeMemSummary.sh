#!/bin/bash

### --This code makes summarry of Max RSS VSIZE CPUtime ....
## Step3.log is needed  


## --step3
#path_="../$1/src/TimeMemory/logs/step3.log"

## --step4
path_="../$1/src/TimeMemory/logs/step4.log"


##--------- mode1
grep "^MemoryCheck\|^TimeEvent>" $path_  | awk -f getTimeMemSummary.awk 


## --step3
#grep "^MemoryCheck\|^TimeEvent>" $path_  | awk -f getTimeMemSummary.awk > getTimeMemSummary_$1\.txt

## --step4
#grep "^MemoryCheck\|^TimeEvent>" $path_  | awk -f getTimeMemSummary.awk > getTimeMemSummary_$1\PAT.txt




## --------mode2 -- For making plots
#grep "^MemoryCheck\|^TimeEvent>" $path_  

## --step3
#grep "^MemoryCheck\|^TimeEvent>" $path_  > SUM_$1\.txt

## --step4
#grep "^MemoryCheck\|^TimeEvent>" $path_  > PAT_SUM_$1\.txt
