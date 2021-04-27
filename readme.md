## RECO monitoring and integration  
 - ###  Python modules that measure the details of CPU and Memory usages of new released [CMS software](https://github.com/cms-sw/cmssw)  
 ![Capture](https://user-images.githubusercontent.com/13959858/116070071-1d95ee80-a6c7-11eb-89ed-34b32d27f0fe.PNG)
 - My contribution (stat: 2019.6 , end: 2021.2)
 - Past website: http://jiwoong.web.cern.ch/jiwoong/   
 - Current working repository from Bongho Tae: https://github.com/xoqhdgh1002/cms-reco-profiling-web   
 - Current website :http://cms-reco-profiling.web.cern.ch/cms-reco-profiling/web/  
 - Current references : https://github.com/cms-cmpwg, https://github.com/jpata/cms-reco-profiling-web  
 
---

### 1. Generate events  
 -  **Gen_tool/Gen.sh** can setup working-directory: CMSSW_X_X_X
```bash
$ ./Gen.sh CMSSW_X_X_X
```      
 -  The directory includes **cmdLog**, igprof_cpu/porfile.sh , igprof_mem_step3/profile_v2.sh, igprof_mem_step4/profile_v2.sh, logs files  
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
 - **Gen_tool/runall_cpu.sh** can monitoring **cpu usage** and make **igprof_cpu/igProf.N.gz** output  
 - **Gen_tool/runall_mem.sh** can monitoring **memory usage** and make **igprof_mem_stepN/igProd.N.gd** output  
 - You can make **sql3** and **res** file from igprof_cpu/profile.sh and igprof_mem_stepN/profile_v2.sh. Just run!  
 - **.sql3 file** is used in **web-based** reports (ex https://jiwoong.web.cern.ch/jiwoong/cgi-bin/igprof-navigator/igprofCPU_CMSSW_11_2_0_pre6PAT )  
 - **.res file** is used in **Ascii-based** report (ex https://jiwoong.web.cern.ch/jiwoong/results/phase2/RES_11_2_0_preX/pre6/RES_PAT_CPU_CMSSW_11_2_0_pre6.res )  

### 3. Analysis  
 - Go to **Analyze_tool** directory
 
### 4. Circle pie-chart
 - Circle plot: [Reference](https://github.com/fwyzard/circles)  
 - First, add the following lines in cmdlog and re-run it  
```bash
--customise HLTrigger/Timer/FastTimer.customise_timer_service_singlejob  
```   
 - Add the following lines in config files:  
```python
# customisation of the process.
process.load( "HLTrigger.Timer.FastTimerService_cfi")
process.FastTimerService.writeJSONSummary = cms.untracked.bool(True)
process.FastTimerService.jsonFileName = cms.untracked.string('resources_RECO_11_2_0_pre11.json')  
```
 - Clone the [Reference](https://github.com/fwyzard/circles) to your www directory in LXPLUS server  
 - copy the OUTPUT_NAME.json to circles/web/data  
 - Following html link can show the Piechart  
 - Please do not use the ".json" in this link. Just write the name of Json file.  
```html
http://jiwoong.web.cern.ch/jiwoong/circles/web/piechart.html?local=false&dataset=OUTPUT_NAME&resource=time_real&colours=default&groups=reco_PhaseII&threshold=0  
```
