import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/E82E266F-94E3-E811-9BE7-7CD30AC031E8.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C4EF1AA8-DBE0-E811-BA0F-A0369F6368FE.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A4BA30A8-1AE1-E811-ABAB-7845C4FC3B8D.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/94686A2A-DFE0-E811-9B88-00266CFCC861.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/8EB0A253-61E3-E811-8240-008CFA0A5914.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/6E3E1B8D-EEE0-E811-9C79-0025901DF5EC.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/58DB2DBA-FFE0-E811-A691-B496910A01F0.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/A846AA34-1334-E911-8EB9-B496910919FC.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/AEE224AD-1934-E911-A581-BC305B390AA7.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F4C5B0A7-2334-E911-B6C9-0026B9278692.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/02BC500B-2634-E911-BF2C-28924A33B9FE.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/768BC5A1-1334-E911-9D3E-28924A38DC1E.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D694DA12-4234-E911-8D74-28924A33AFF6.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/781A9F71-3834-E911-9640-28924A38DC1E.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/981132B1-2634-E911-A4A6-BC305B390AB4.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1AD45411-9634-E911-B5BE-28924A38DC1E.root',
        '/store/mc/RunIISummer16MiniAODv3/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1403EEE6-5235-E911-9E2D-0023AEEEB6CD.root'
] )
