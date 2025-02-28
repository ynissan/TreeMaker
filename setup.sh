#!/bin/bash -e

CMSSWVER=CMSSW_10_2_11_patch1
FORK=TreeMaker
BRANCH=Run2_2017
ACCESS=ssh
CORES=8
NAME=""
DIR="${PWD}"

usage(){
	EXIT=$1

	echo "setup.sh [options]"
	echo ""
	echo "-f [fork]           clone from specified fork (default = ${FORK})"
	echo "-b [branch]         clone specified branch (default = ${BRANCH})"
	echo "-c [version]        use specified CMSSW version (default = ${CMSSWVER})"
	echo "-a [protocol]       use protocol to clone (default = ${ACCESS}, alternative = https)"
	echo "-j [cores]          run CMSSW compilation on # cores (default = ${CORES})"
	echo "-n [name]           name of the CMSSW directory (default = ${CMSSWVER})"
	echo "-d [dir]            project installation area for the CMSSW directory (default = ${DIR})"
	echo "-h                  display this message and exit"

	exit $EXIT
}

# process options
while getopts "f:b:a:j:n:d:c:h" opt; do
	case "$opt" in
	f) FORK=$OPTARG
	;;
	b) BRANCH=$OPTARG
	;;
	c) CMSSWVER=$OPTARG
	;;
	a) ACCESS=$OPTARG
	;;
	j) CORES=$OPTARG
	;;
	n) NAME=$OPTARG
	;;
	d) DIR=$OPTARG
	;;
	h) usage 0
	;;
	esac
done

# check options
if [ "$ACCESS" = "ssh" ]; then
	ACCESS_GITHUB=git@github.com:
	ACCESS_GITLAB=ssh://git@gitlab.cern.ch:7999/
	ACCESS_CMSSW=--ssh
elif [ "$ACCESS" = "https" ]; then
	ACCESS_GITHUB=https://github.com/
	ACCESS_GITLAB=https://gitlab.cern.ch/
	ACCESS_CMSSW=--https
else
	usage 1
fi

# get CMSSW release
if [[ "$CMSSWVER" == "CMSSW_10_2_"* ]]; then
	GCC_VERSION=gcc700
else
	echo "Unsupported CMSSW version: $CMSSWVER"
	exit 1
fi

if [[ `uname -r` == *"el6"* ]]; then
	SLC_VERSION="slc6"
elif [[ `uname -r` == *"el7"* ]]; then
	SLC_VERSION="slc7"
else
	echo "WARNING::Unknown SLC version. Defaulting to SLC6."
	SLC_VERSION="slc6"
fi
export SCRAM_ARCH=${SLC_VERSION}_amd64_${GCC_VERSION}

# cmsrel
SCRAM_PROJECT_OPTIONS=""
if [ "$DIR" != "${PWD}" ]; then
	SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS --dir ${DIR}"
fi
if [ "$NAME" != "" ]; then
	SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS --name ${NAME}"
else
	NAME=${CMSSWVER}
fi
SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS ${CMSSWVER}"
scram project ${SCRAM_PROJECT_OPTIONS}
cd ${DIR}/${NAME}/src

# cmsenv
eval `scramv1 runtime -sh`
git cms-init $ACCESS_CMSSW
git config gc.auto 0

# CMSSW patches
if [[ "$CMSSWVER" == "CMSSW_10_2_"* ]]; then
	git cms-merge-topic -u $ACCESS_CMSSW TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_10_2_7
	git cms-merge-topic -u $ACCESS_CMSSW TreeMaker:storeJERFactorIndex1027
	git cms-merge-topic -u $ACCESS_CMSSW TreeMaker:AddJetAxis1_1027
	git cms-merge-topic -u $ACCESS_CMSSW TreeMaker:NjettinessAxis_1027
fi

# outside repositories
git clone ${ACCESS_GITHUB}TreeMaker/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
git clone ${ACCESS_GITHUB}kpedro88/CondorProduction.git Condor/Production
git clone ${ACCESS_GITHUB}${FORK}/TreeMaker.git -b ${BRANCH}
# get egamma config and data files without recompiling whole package
wget https://github.com/TreeMaker/cmssw/raw/EgammaPostRecoTools_dev/RecoEgamma/EgammaTools/python/EgammaPostRecoTools.py -P TreeMaker/Utils/python/
wget https://github.com/TreeMaker/EgammaAnalysis-ElectronTools/raw/ScalesSmearing2018_Dev/ScalesSmearings/Run2018_Step2Closure_CoarseEtaR9Gain_scales.dat -P TreeMaker/Production/test/data/ScalesSmearings
wget https://github.com/TreeMaker/EgammaAnalysis-ElectronTools/raw/ScalesSmearing2018_Dev/ScalesSmearings/Run2018_Step2Closure_CoarseEtaR9Gain_smearings.dat -P TreeMaker/Production/test/data/ScalesSmearings

# compile
scram b -j ${CORES}

# extra setup
cd TreeMaker/Production/test/condorSub/
python $CMSSW_BASE/src/Condor/Production/python/linkScripts.py
