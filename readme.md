## RECO monitoring and integration  
 - ### Website: http://jiwoong.web.cern.ch/jiwoong/  
---

### 1. Generate events  
 -  **Gen_tool/Gen.sh** can setup working-directory: CMSSW_X_X_X
```bash
$ ./Gen.sh CMSSW_X_X_X
```      
 -  The directory includes **cmdLog**, **profile.sh**  
 -  You can generate events of all datatier using **cmdLog** files  

#### **1.1 About cmdLog file**  
 -  This is the sample of **cmdLog** file: http://jiwoong.web.cern.ch/jiwoong/results/phase2/cmdlog_CMSSW_11_1_0_pre3  
 - 100 events are generated  
 - I use multi threading only in step1 and step2 to save time  
 - **--customise=Validation/Performance/TimeMemoryInfo.py** option can make time and memory information in logfiles ( step3.log, step4.log )
 - step3.log and step4.log are also used in analysis  
 - **--customise HLTrigger/Timer/FastTimer.customise_timer_service_singlejob** option is needed for making Circle Piechart  
 - Do not use the **customise=Validation/Performance/TimeMemoryInfo.py** with **customise HLTrigger/Timer/FastTimer.customise_timer_service_singlejob** simultaneously. This can occur interference.  

### 2. Igprof  

 - First, you should add the following lines to config file:  
```python
from Validation.Performance.IgProfInfo import customise
process = customise(process)

```  
 - **Gen_tool/runall_cpu.sh** can monitoring **cpu usage** and make **igproc_CPU/igProf.N.gz** output  
 - **Gen_tool/runall_mem.sh** can monitoring **memory usage** and make **igproc_meme_stepN/igProd.N.gd** output  
 - You can make **sql3** and **res** file from igprof_cpu/profile.sh and igprof_mem_stepN/profile_v2.sh. Just run!  
 - **.sql3 file** is used in **web-based** reports (ex https://jiwoong.web.cern.ch/jiwoong/cgi-bin/igprof-navigator/igprofCPU_CMSSW_11_2_0_pre6PAT )  
 - **.res file** is used in **Ascii-based** report (ex https://jiwoong.web.cern.ch/jiwoong/results/phase2/RES_11_2_0_preX/pre6/RES_PAT_CPU_CMSSW_11_2_0_pre6.res )  

### 3. Analysis  
 - Go to **Analyze_tool** directory
 - Circle plot: [Reference](https://github.com/fwyzard/circles)  
 

