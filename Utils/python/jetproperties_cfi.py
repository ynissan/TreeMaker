import FWCore.ParameterSet.Config as cms

jetproperties = cms.EDProducer('JetProperties',
    JetTag       = cms.InputTag('slimmedJets'),
    debug = cms.bool(False),
    properties = cms.vstring(
        "chargedHadronMultiplicity"  ,
        "neutralHadronMultiplicity"  ,
        "electronMultiplicity"       ,
        "photonMultiplicity"         ,
        "muonMultiplicity"           ,
        "NumBhadrons"                ,
        "NumChadrons"                ,
        "chargedMultiplicity"        ,
        "neutralMultiplicity"        ,
        "partonFlavor"               ,
        "hadronFlavor"               ,
        "multiplicity"               ,
        "jetArea"                    ,
        "chargedHadronEnergyFraction",
        "neutralHadronEnergyFraction",
        "chargedEmEnergyFraction"    ,
        "neutralEmEnergyFraction"    ,
        "electronEnergyFraction"     ,
        "photonEnergyFraction"       ,
        "muonEnergyFraction"         ,
        "hfEMEnergyFraction"         ,
        "hfHadronEnergyFraction"     ,
        "jecFactor"                  ,
        "jecUnc"                     ,
        "qgLikelihood"               ,
        "ptD"                        ,
        "axisminor"                  ,
        "axismajor"                  ,
        "bDiscriminatorCSV"          ,
        "bJetTagDeepCSVprobb"        ,
        "bJetTagDeepCSVprobc"        ,
        "bJetTagDeepCSVprobudsg"    ,
        "bJetTagDeepCSVprobbb"       ,
        "bDiscriminatorDeepCSVBvsAll",
        "bDiscriminatorDeepCSVCvsB"  ,
        "bDiscriminatorDeepCSVCvsL"  ,
        "bJetTagDeepFlavourprobb"    ,
        "bJetTagDeepFlavourprobc"    ,
        "bJetTagDeepFlavourprobg"    ,
        "bJetTagDeepFlavourproblepb" ,
        "bJetTagDeepFlavourprobbb"   ,
        "bJetTagDeepFlavourprobuds"  ,
    ),
    bDiscriminatorCSV = cms.vstring('pfCombinedInclusiveSecondaryVertexV2BJetTags'),
    bJetTagDeepCSVprobb = cms.vstring('pfDeepCSVJetTags:probb'),
    bJetTagDeepCSVprobc = cms.vstring('pfDeepCSVJetTags:probc'),
    bJetTagDeepCSVprobudsg = cms.vstring('pfDeepCSVJetTags:probudsg'),
    bJetTagDeepCSVprobbb = cms.vstring('pfDeepCSVJetTags:probbb'),
    bDiscriminatorDeepCSVBvsAll = cms.vstring('pfDeepCSVDiscriminatorsJetTags:BvsAll'),
    bDiscriminatorDeepCSVCvsB = cms.vstring('pfDeepCSVDiscriminatorsJetTags:CvsB'),
    bDiscriminatorDeepCSVCvsL = cms.vstring('pfDeepCSVDiscriminatorsJetTags:CvsL'),
    bJetTagDeepFlavourprobb = cms.vstring('pfDeepFlavourJetTags:probb'),
    bJetTagDeepFlavourprobc = cms.vstring('pfDeepFlavourJetTags:probc'),
    bJetTagDeepFlavourprobg = cms.vstring('pfDeepFlavourJetTags:probg'),
    bJetTagDeepFlavourproblepb = cms.vstring('pfDeepFlavourJetTags:problepb'),
    bJetTagDeepFlavourprobbb = cms.vstring('pfDeepFlavourJetTags:probbb'),
    bJetTagDeepFlavourprobuds = cms.vstring('pfDeepFlavourJetTags:probuds'),
    jecUnc = cms.vstring('jecUnc'),
    jerFactor = cms.vstring('jerFactor'),
    jerFactorUp = cms.vstring('jerFactorUp'),
    jerFactorDown = cms.vstring('jerFactorDown'),
    qgLikelihood = cms.vstring('QGTagger:qgLikelihood'),
    ptD = cms.vstring('QGTagger:ptD'),
    axisminor = cms.vstring('QGTagger:axis2'),
    axismajor = cms.vstring('QGTagger:axis1'),
    multiplicity = cms.vstring('QGTagger:mult'),
)
