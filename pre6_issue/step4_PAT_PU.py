# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step4 --conditions auto:phase2_realistic_T14 --pileup_input das:/RelValMinBias_14TeV/CMSSW_10_6_0_patch2-106X_upgrade2023_realistic_v3_2023D41noPU-v1/GEN-SIM -n 100 --era Phase2C8 --eventcontent MINIAODSIM --runUnscheduled -s PAT --datatier MINIAODSIM --pileup AVE_200_BX_25ns --geometry Extended2026D41 --customise=Validation/Performance/TimeMemoryInfo.py --customise HLTrigger/Timer/FastTimer.customise_timer_service_singlejob --filein file:step3.root --fileout file:step4.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C8_cff import Phase2C8

process = cms.Process('PAT',Phase2C8)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step3.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step4 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:step4.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedCandidates_packedPFCandidates__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenParticles_prunedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patTriggerObjectStandAlones_slimmedPatTrigger__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedGenParticles_packedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVertices__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoCaloClusters_reducedEgamma_reducedESClusters_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEERecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenJets_slimmedGenJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJetsPuppi__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        )
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(200.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-3)
process.mix.maxBunch = cms.int32(3)

process.mix.input.fileNames = cms.untracked.vstring(['file:/x5/cms/jwkim/store/2564B36D-A0DB-6C42-9105-B1CFF44F311D.root',
'file:/x5/cms/jwkim/store/287275CC-953A-0C4C-B352-E39EC2D571F0.root',
'file:/x5/cms/jwkim/store/2C56BC73-5687-674C-8684-6C785A88DB78.root',
'file:/x5/cms/jwkim/store/2CB8C960-47C0-1A40-A9F7-0B62987097E0.root',
'file:/x5/cms/jwkim/store/657065A5-F35B-3147-AED9-E4ACA915C982.root',
'file:/x5/cms/jwkim/store/6FCA2E1D-D1E2-514B-8ABA-5B71A2C1E1B3.root',
'file:/x5/cms/jwkim/store/82584FBA-A1E6-DF48-99BA-B1759C3A190F.root',
'file:/x5/cms/jwkim/store/B96F4064-156C-5E47-90A0-07475310157A.root',
'file:/x5/cms/jwkim/store/F7FE3FE9-565B-544A-855E-902BA4E3C5FD.root',
'file:/x5/cms/jwkim/store/F806295A-492F-EF4F-9D91-15DA8769DD72.root'])


#process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/F7FE3FE9-565B-544A-855E-902BA4E3C5FD.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/82584FBA-A1E6-DF48-99BA-B1759C3A190F.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/F806295A-492F-EF4F-9D91-15DA8769DD72.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/6FCA2E1D-D1E2-514B-8ABA-5B71A2C1E1B3.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/287275CC-953A-0C4C-B352-E39EC2D571F0.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/657065A5-F35B-3147-AED9-E4ACA915C982.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/2C56BC73-5687-674C-8684-6C785A88DB78.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/B96F4064-156C-5E47-90A0-07475310157A.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/2564B36D-A0DB-6C42-9105-B1CFF44F311D.root', '/store/relval/CMSSW_10_6_0_patch2/RelValMinBias_14TeV/GEN-SIM/106X_upgrade2023_realistic_v3_2023D41noPU-v1/10000/2CB8C960-47C0-1A40-A9F7-0B62987097E0.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T14', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path()
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path()
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_HBHENoiseFilter = cms.Path()
process.Flag_trkPOG_toomanystripclus53X = cms.Path()
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path()
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.
process.load( "HLTrigger.Timer.FastTimerService_cfi")
process.FastTimerService.writeJSONSummary = cms.untracked.bool(True)
process.FastTimerService.jsonFileName = cms.untracked.string('resources_PAT_11_1_0_pre6.json')


# Automatic addition of the customisation function from Validation.Performance.TimeMemoryInfo
from Validation.Performance.TimeMemoryInfo import customise 

#call to customisation function customise imported from Validation.Performance.TimeMemoryInfo
process = customise(process)

# Automatic addition of the customisation function from HLTrigger.Timer.FastTimer
from HLTrigger.Timer.FastTimer import customise_timer_service_singlejob 

#call to customisation function customise_timer_service_singlejob imported from HLTrigger.Timer.FastTimer
process = customise_timer_service_singlejob(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
