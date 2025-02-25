import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAODv3 samples - Summer16
Summer16v3samples = [
	# NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
	MCSample('TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 10199051, False),
	MCSample('TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 61621218, False), # subtotal = 11957043
	MCSample('TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 61621218, False), # subtotal = 49664175
	MCSample('TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4302086, False),
	MCSample('TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 60343752, False), # subtotal = 11955887
	MCSample('TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 60343752, False), # subtotal = 48387865
	MCSample('TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4310038, False),
	MCSample('TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 30836035, False), # subtotal = 6068369
	MCSample('TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 30836035, False), # subtotal = 24767666
	MCSample('TTJets_SingleLeptFromT_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 17355657, False),
	MCSample('TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 17003930, False),
	MCSample('TTJets_DiLept_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9753471, False),
	MCSample('TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 14344298, False),
	MCSample('TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 10529747, False),
	MCSample('TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 2932983, False),
	MCSample('TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 1519815, False),
	MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 29602576, False),
	MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 59133437, False), # subtotal = 29632372
	MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 59133437, False), # subtotal = 29501065
	MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 58420151, False), # subtotal = 28504600
	MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 58420151, False), # subtotal = 29915551
	MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 76915549, False),
	MCSample('TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 79140880, False),
	MCSample('WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 86916455, False), # subtotal = 29514020
	MCSample('WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2', 'RunIISummer16MiniAODv3', 'Constant', 86916455, False), # subtotal = 57402435
	MCSample('WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 10020533, False),
	MCSample('WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9945478, False),
	MCSample('WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 38984322, False), # subtotal = 4963240
	MCSample('WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 38984322, False), # subtotal = 14106492
	MCSample('WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2', 'RunIISummer16MiniAODv3', 'Constant', 38984322, False), # subtotal = 19914590
	MCSample('WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 7759701, False), # subtotal = 1963464
	MCSample('WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 7759701, False), # subtotal = 5796237
	MCSample('WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 18687480, False), # subtotal = 3779141
	MCSample('WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 18687480, False), # subtotal = 14908339
	MCSample('WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 7830536, False), # subtotal = 1544513
	MCSample('WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 7830536, False), # subtotal = 6286023
	MCSample('WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 6872441, False), # subtotal = 244532
	MCSample('WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 6872441, False), # subtotal = 6627909
	MCSample('WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 2637821, False), # subtotal = 253561
	MCSample('WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 2637821, False), # subtotal = 2384260
	MCSample('QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 6696872, False),
	MCSample('QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 12616158, False), # subtotal = 6867422
	MCSample('QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 12616158, False), # subtotal = 5748736
	MCSample('QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 14796774, False), # subtotal = 6958708
	MCSample('QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 14796774, False), # subtotal = 7838066
	MCSample('QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 22470404, False), # subtotal = 4150588
	MCSample('QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 22470404, False), # subtotal = 18319816
	MCSample('QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 3959986, False),
	MCSample('QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 13524747, False), # subtotal = 3896412
	MCSample('QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 13524747, False), # subtotal = 9628335
	MCSample('QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 19697092, False), # subtotal = 3992112
	MCSample('QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 19697092, False), # subtotal = 15704980
	MCSample('QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 9846615, False), # subtotal = 2999069
	MCSample('QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 9846615, False), # subtotal = 6847546
	MCSample('QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 2873427, False), # subtotal = 396409
	MCSample('QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 2873427, False), # subtotal = 2477018
	MCSample('QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 1982038, False), # subtotal = 397660
	MCSample('QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 1982038, False), # subtotal = 1584378
	MCSample('QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 996130, False), # subtotal = 399226
	MCSample('QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 996130, False), # subtotal = 596904
	MCSample('QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 391735, False),
	MCSample('QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 4141251, False),
	MCSample('QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 31878740, False),
	MCSample('QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 29954815, False),
	MCSample('QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 19662175, False),
	MCSample('QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 13895437, False),
	MCSample('QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 7897731, False),
	MCSample('QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 7947159, False),
	MCSample('QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 7937590, False),
	MCSample('QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 3972819, False),
	MCSample('QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 4010136, False),
	MCSample('QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 3962749, False),
	MCSample('QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 3990117, False),
	MCSample('QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'ConstantFlat', 19996995, False),
	MCSample('QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8', 'HEM_102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'ConstantFlat', 18688995, False),
	MCSample('QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 57580393, False), # subtotal = 18722416
	MCSample('QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 57580393, False), # subtotal = 38857977
	MCSample('QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 54552852, False), # subtotal = 17035891
	MCSample('QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 54552852, False), # subtotal = 37516961
	MCSample('QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 62622029, False), # subtotal = 18560541
	MCSample('QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 62622029, False), # subtotal = 44061488
	MCSample('QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 15629253, False),
	MCSample('QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 15210939, False), # subtotal = 4850746
	MCSample('QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 15210939, False), # subtotal = 10360193
	MCSample('QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 11839357, False), # subtotal = 3970819
	MCSample('QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 11839357, False), # subtotal = 7868538
	MCSample('QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 6019541, False), # subtotal = 1991645
	MCSample('QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 6019541, False), # subtotal = 4027896
	MCSample('DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 11017086, False), # subtotal = 2751187
	MCSample('DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 11017086, False), # subtotal = 8265899
	MCSample('DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9609137, False), # subtotal = 962195
	MCSample('DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 9609137, False), # subtotal = 8646942
	MCSample('DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9725661, False), # subtotal = 1070454
	MCSample('DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 9725661, False), # subtotal = 8655207
	MCSample('DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 8292957, False),
	MCSample('DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 2673066, False),
	MCSample('DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 596079, False),
	MCSample('DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 399492, False),
	MCSample('DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 49748967, False),
	MCSample('ZJetsToNuNu_HT-100To200_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 24272858, False), # subtotal = 5246318
	MCSample('ZJetsToNuNu_HT-100To200_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 24272858, False), # subtotal = 19026540
	MCSample('ZJetsToNuNu_HT-200To400_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 24761211, False), # subtotal = 5136083
	MCSample('ZJetsToNuNu_HT-200To400_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 24761211, False), # subtotal = 19625128
	MCSample('ZJetsToNuNu_HT-400To600_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9862869, False), # subtotal = 1020309
	MCSample('ZJetsToNuNu_HT-400To600_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 9862869, False), # subtotal = 8842560
	MCSample('ZJetsToNuNu_HT-600To800_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 5766322, False),
	MCSample('ZJetsToNuNu_HT-800To1200_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 2170137, False),
	MCSample('ZJetsToNuNu_HT-1200To2500_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 513471, False), # subtotal = 369514
	MCSample('ZJetsToNuNu_HT-1200To2500_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 513471, False), # subtotal = 143957
	MCSample('ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 405030, False),
	MCSample('GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 10104155, False), # subtotal = 5131873
	MCSample('GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 10104155, False), # subtotal = 4972282
	MCSample('GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 20527506, False), # subtotal = 10122599
	MCSample('GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 20527506, False), # subtotal = 10404907
	MCSample('GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 5060070, False), # subtotal = 2529729
	MCSample('GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 5060070, False), # subtotal = 2530341
	MCSample('GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 5080857, False), # subtotal = 2463946
	MCSample('GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 5080857, False), # subtotal = 2616911
	MCSample('GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 14821862, False),
	MCSample('GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 50002467, False),
	MCSample('GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 11702604, False),
	MCSample('GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 11687048, False),
	MCSample('ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 2989199, False, 1884837),
	MCSample('ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 1000000, False, 622990),
	MCSample('ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 67105876, False),
	MCSample('ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 38811017, False),
	MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 3256407, False),
	MCSample('ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 3256650, False),
	MCSample('ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 6933094, False),
	MCSample('ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 998276, False),
	MCSample('ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 6952830, False),
	MCSample('ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 992024, False),
	MCSample('WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 5077680, False),
	MCSample('WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 502190, False),
	MCSample('WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 5246469, False, 3267135),
	MCSample('WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 24311445, False, 14109151),
	MCSample('WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 1703772, False, 942046),
	MCSample('ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 30493038, False, 18722534),
	MCSample('ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 15462693, False, 9762305),
	MCSample('TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1', 'RunIISummer16MiniAODv3', 'Constant', 5837781, False, 2723203),
	MCSample('TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 749400, False, 351164),
	MCSample('TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1', 'RunIISummer16MiniAODv3', 'Constant', 3120397, False, 1603527),
	MCSample('TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 833298, False, 430310),
	MCSample('TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 14748853, False, 4774447), # subtotal = 1577833, straight subtotal = 4870911
	MCSample('TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 14748853, False, 4774447), # subtotal = 3196614, straight subtotal = 9877942
	MCSample('TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 4845923, False),
	MCSample('TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4846427, False),
	MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4944950, False),
	MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-fsrup-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4810617, False),
	MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-isrdown-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4964008, False),
	MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-isrup-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4867940, False),
	MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4873181, False),
	MCSample('TTGamma_Dilept_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4773650, False),
	MCSample('TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 2456040, False, 1023172),
	MCSample('TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 98300, False),
	MCSample('WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 240000, False, 210538),
	MCSample('WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 250000, False, 221468),
	MCSample('WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 246800, False, 216366),
	MCSample('ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 249237, False, 213197),
	MCSample('SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 146849, False),
	MCSample('SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 105415, False),
	MCSample('SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 51352, False),
	MCSample('SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 92094, False),
	MCSample('SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 51260, False),
	MCSample('SMS-T1qqqq_mGluino-1800_mLSP-200_ctau-1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 49841, False),
	MCSample('SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 142671, False),
	MCSample('SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 52465, False),
	MCSample('SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 827787, False),
	MCSample('SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 1001170, False),
	MCSample('SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 949417, False),
	MCSample('SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 905836, False),
	MCSample('SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 899982, False),
	MCSample('SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 400314, False),
	MCSample('SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 291078, False),
	MCSample('SMS-T2tt_mStop-350_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 189173, False),
	MCSample('SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 156847, False),
	MCSample('SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 397678, False),
	MCSample('SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 100070, False),
	MCSample('SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 235029, False),
	MCSample('SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 396239, False),
	MCSample('SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 413868, False),
	MCSample('SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 400482, False),
	MCSample('SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 408233, False),
	MCSample('SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 400887, False),
	MCSample('SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 394281, False),
	MCSample('SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 397668, False),
	MCSample('SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 414063, False),
	MCSample('SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 389625, False),
	MCSample('SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 404812, False),
	MCSample('SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 417293, False),
	MCSample('SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 391445, False),
	MCSample('SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 400307, False),
	MCSample('RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 417575, False),
	MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 370241, False),
	MCSample('RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 436873, False),
	MCSample('RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 319494, False),
	MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 166908, False),
	MCSample('RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 100002, False),
	MCSample('RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 62526, False),
	MCSample('RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 44742, False),
	MCSample('RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 43352, False),
	MCSample('RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 43618, False),
	MCSample('RPV_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 21870, False),
	MCSample('RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 21774, False),
	MCSample('RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 21859, False),
	MCSample('StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 450097, False),
	MCSample('StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 386821, False),
	MCSample('StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 452809, False),
	MCSample('StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 324546, False),
	MCSample('StealthSYY_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 187464, False),
	MCSample('StealthSYY_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 36753, False),
	MCSample('StealthSYY_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 67743, False),
	MCSample('StealthSYY_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 45578, False),
	MCSample('StealthSYY_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 46223, False),
	MCSample('StealthSYY_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 45409, False),
	MCSample('StealthSYY_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 21232, False),
	MCSample('StealthSYY_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 22607, False),
	MCSample('StealthSYY_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 21995, False),
	MCSample('StealthSHH_2t4b_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 447416, False),
	MCSample('StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 419903, False),
	MCSample('StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 449988, False),
	MCSample('StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 321284, False),
	MCSample('StealthSHH_2t4b_mStop-500_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 187680, False),
	MCSample('StealthSHH_2t4b_mStop-550_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 106106, False),
	MCSample('StealthSHH_2t4b_mStop-600_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 66786, False),
	MCSample('StealthSHH_2t4b_mStop-650_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 46652, False),
	MCSample('StealthSHH_2t4b_mStop-700_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 45627, False),
	MCSample('StealthSHH_2t4b_mStop-750_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 44131, False),
	MCSample('StealthSHH_2t4b_mStop-800_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 21785, False),
	MCSample('StealthSHH_2t4b_mStop-850_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 22727, False),
	MCSample('StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 8410, False),
]