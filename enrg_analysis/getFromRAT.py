# Author: Ayse Bat
# source :https://github.com/AIT-WATCHMAN/WMUtils/blob/master/ratMacros/sourceCalOptimize/calSourceOpt.py
# modifyed for the project
# How to run:  python3 getFromRAT.py -f ../pos1.root -n1 0 -n2 10000 -o pos1 python3 
from ROOT import TFile, AddressOf
import rat
import csv
import json
import argparse

import gc
gc.set_threshold(0)

def get_args():
    """Python parser argument takes the following argument"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fileName', type=str)
    parser.add_argument('-o', '--outName', type=str)
    parser.add_argument('-n1', '--firstRun', type=int)
    parser.add_argument('-n2', '--lastRun', type=int)
    return parser.parse_args()


def save_as_csv(data, name):
    """The function write dictionay data as csv file"""
    w = csv.writer(open(f"data_{name}.csv", "w"))
    for key, val in data.items():
        w.writerow([key, val])


def save_as_json(data, name):
    """The functıon takes the data as dıctıonary and name of the output file
    and creates the json file"""
    json_file = json.dumps(data)
    output = open(f"data_{name}.json", "w")
    output.write(json_file)
    output.close()


args = get_args()
#print(f"Read at the root File : {args.fileName}")

# rat object
run = rat.RAT.DS.Run()
ds = rat.RAT.DS.Root()


#print(f"Rat run: {run}")
#print(f"Rat ds:  {ds}")
# read root file
tfile = TFile(args.fileName)

# get the Tree in root
runT = tfile.Get("runT")
T = tfile.Get("T")

# SetBranches
runT.SetBranchAddress("run", AddressOf(run))
T.SetBranchAddress("ds", AddressOf(ds))

numEvent = T.GetEntries()
#print(f"Number of events: {numEvent}")

#print the run evry 1000 events

# define the arrays
eventmcID = []
eventpmtID = []
eventpmt = []
numPE = []
cerenkov = []
scintillator = []
totalScintEdep = []
reemitPhoton = []
x = []
y = []
z = []
cosTheta = []
eta = []
theta = []
phi = []
mag = []
mag2 = []
pt = []
px = []
py = []
pz = []

# mc pmt variable
hitTime = []
charge = []
pmtX = []
pmtY = []
pmtZ = []
pmtPE = []
pmt = []
# Loop over the number of events

#print(f"Event,pmt,numPE,HitTime,Charge")
#print("Event,numPE,cerenkov,scintillator,reemitPhotob,eta,cosTheta,theta,phi,pt,px,py,pz,mag,mag2,x,y,z,pmt,numPEPMT,hitTime,charge,pmtX,pmtY,pmtZ")

print("Event,numPE,cerenkov,x,y,z,hitTime,charge,pmt,pmtX,pmtY,pmtZ")



for event in range(args.firstRun, args.lastRun):
    
    T.GetEntry(event)
    # mc tree
    mc = ds.GetMC()

    ntrack = mc.GetMCTrackCount()
    npmt = mc.GetMCPMTCount()

    nPE = mc.GetNumPE()

    # MCSummary
    nScint = mc.GetMCSummary().GetNumScintPhoton()
    nCerenkov = mc.GetMCSummary().GetNumCerenkovPhoton()
    nreemitPhoton = mc.GetMCSummary().GetNumReemitPhoton()
    ntotalScintEdep = mc.GetMCSummary().GetTotalScintEdep()

    # MCPartiele
    particleCosTheta = mc.GetMCParticle(0).GetPosition().CosTheta()
    particleEta = mc.GetMCParticle(0).GetPosition().Eta()
    particleTheta = mc.GetMCParticle(0).GetPosition().Theta()
    particlePhi = mc.GetMCParticle(0).GetPosition().Phi()
    particleMag = mc.GetMCParticle(0).GetPosition().Mag()
    particleMag2 = mc.GetMCParticle(0).GetPosition().Mag2()
    particlePt = mc.GetMCParticle(0).GetPosition().Pt()
    particlePx = mc.GetMCParticle(0).GetPosition().Px()
    particlePy = mc.GetMCParticle(0).GetPosition().Py()
    particlePz = mc.GetMCParticle(0).GetPosition().Pz()
    particleX = mc.GetMCParticle(0).GetPosition().x()
    particleY = mc.GetMCParticle(0).GetPosition().y()
    particleZ = mc.GetMCParticle(0).GetPosition().z()

    """
    
    # append to the array
    numPE.append(mc.GetNumPE())
    cerenkov.append(nCerenkov)
    scintillator.append(nScint)
    reemitPhoton.append(nreemitPhoton)
    totalScintEdep.append(ntotalScintEdep)

    # Particle ID
    cosTheta.append(particleCosTheta)
    eta.append(particleEta)
    theta.append(particleTheta)
    phi.append(particlePhi)
    mag.append(particleMag)
    mag2.append(particleMag2)
    pt.append(particlePt)
    px.append(particlePx)
    py.append(particlePy)
    pz.append(particlePz)

    x.append(particleX)
    y.append(particleY)
    z.append(particleZ)
    # event ID
    eventmcID.append(event)
    """

    for ipmt in range(npmt):
        # print(ipmt)
        nphoton = mc.GetMCPMT(ipmt).GetMCPhotonCount()

        for iphoton in range(nphoton):
            getHitTime = mc.GetMCPMT(ipmt).GetMCPhoton(iphoton).GetHitTime()
            getCharge = mc.GetMCPMT(ipmt).GetMCPhoton(iphoton).GetCharge()
            getX = mc.GetMCPMT(ipmt).GetMCPhoton(iphoton).GetPosition().x()
            getY = mc.GetMCPMT(ipmt).GetMCPhoton(iphoton).GetPosition().y()
            getZ = mc.GetMCPMT(ipmt).GetMCPhoton(iphoton).GetPosition().z()

            # append the array
            hitTime.append(getHitTime)
            charge.append(getCharge)
            pmtX.append(getX)
            pmtY.append(getY)
            pmtZ.append(getZ)
            pmtPE.append(iphoton)
            pmt.append(ipmt)
            eventpmtID.append(event)
            # print the values
            # print(f"{event},{ipmt},{iphoton},{getHitTime},{getCharge}")

            numPE.append(nPE)
            cerenkov.append(nCerenkov)
            scintillator.append(nScint)
            reemitPhoton.append(nreemitPhoton)
            totalScintEdep.append(ntotalScintEdep)
            cosTheta.append(particleCosTheta)
            eta.append(particleEta)
            theta.append(particleTheta)
            phi.append(particlePhi)
            mag.append(particleMag)
            mag2.append(particleMag2)
            pt.append(particlePt)
            px.append(particlePx)
            py.append(particlePy)
            pz.append(particlePz)

            x.append(particleX)
            y.append(particleY)
            z.append(particleZ)

            eventmcID.append(event)

           
            print(f"{event},{nPE},{nCerenkov},{particleX},{particleY},{particleZ},{getHitTime},{getCharge},{ipmt},{getX},{getY},{getZ}")


#print(f"Lengthy of numPE: {len(numPE)}")
#print(f"Lengthy of x: {len(x)}")
#print(f"Lengthy of y: {len(y)}")
#print(f"Lengthy of y: {len(y)}")

#print(f"Lengthy of hitTime: {len(hitTime)}")
#print(f"Lengthy of charge: {len(charge)}")
#print(f"Lengthy of pmtX: {len(pmtX)}")
# define the dictionary
"""
theData = {"Event": eventpmtID,
           "numPE": numPE,
           "cerenkov": cerenkov,
           "scintillator": scintillator,
           "reemitPhotob": reemitPhoton,
           "eta": eta,
           "cosTheta": cosTheta,
           "theta": theta,
           "phi": phi,
           "pt": pt,
           "px": px,
           "py": py,
           "pz": pz,
           "mag": mag,
           "mag2": mag2,
           "x": x,
           "y": y,
           "z": z,
           "pmt": pmt,
           "numPE": pmtPE,
           "hitTime": hitTime,
           "charge": charge,
           "pmtX": pmtX,
           "pmtY": pmtY,
           "pmtZ": pmtZ,
           }
"""
# save the mc file and pmt file
#save_as_csv(theData, f"_{args.outName}")

# save the mc and pmt data as json
#save_as_json(theData, f"_{args.outName}")
