#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2020-01-29 10:37:07 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

import sys

from IPython.display import Math

physics_term = sys.argv[1]

def search(term):
    
    dictionary = {
        "kaon pole term of sigma_l at low t" : "",
        
        "pole dominance of sigma_l at low t" : "",
        
        "q^2 scaling" : "",
        
        "superharp scan" :
        "Makes measurements of beam profile and position. Measures beam position at entrance, middle and exit of arc to get beam energy from dispersive properties of arc dipoles. ",
        
        "raster" :
        "The CEBAF e^- beam has a small transverse size and high current so damage can occur to the target and beam dump. There are two types: 1) fast raster 2) slow raster.",
        
        "sieve" :
        "Thick plate with special hole pattern. Use with a thin carbon foil where scattered electrons pass through holes in the foil. These scattered e- represent many beams on the spectrometer's focal plane. This allows the fitting of the reconstruction matrix to be formed using the known positions of the holes.",
        
        "dummy target" :
        "A pair of aluminum solid targets. Simulates radiative effecys of missing cryogenic material. This is used to subtract the contribution of scattering from target window from the data (a large contributor to background). ",
        
        "heepcheck" :
        "Used for offset calculations, beam energy measurements, and central momentum determination with delta scans.",

                
        "heep" :
        "Used for offset calculations, beam energy measurements, and central momentum determination with delta scans.",
        
        "prescale" :
        "",
        
        "bcm" :
        "Beam Current Monitor (three total). They are cylindrical resonant cavities and provide continuous measurements of the current.",
        
        "radiative kaon capture" :
        "",
        
        "free parameters" :
        "",
        
        "charge radius" :
        "The root mean square distance of charge carrier from the charge center of particle.",
        
        "mixing angle" :
        "",
        
        "duty factor" :
        "",
        
        "CW beam" :
        "Continuous Wave (CW).",
        
        "unser monitor" :
        "A parameterized DC current transformer is used as an absolute current calibration for the BCM.",
        
        "slow raster" :
        "Dump Raster. Protects beam dump and is just before scattering chamber. Only needs to be used if close to 80 uA.",
        
        "fast raster" :
        "Protects the target. Located before entrance to the hall. Two sets of steering magnets.",
        
        "carbon run" :
        "For luminosity scans. Calibratates the optics as a function of target length.",
        
        "boiling target" :
        "LH2 temperature was measured by resistors and regulated by a constant heat load. Heater is controlled with a feedback loop with the beam current.",
        
        "collimater" :
        "Located at entrance of spectrometer and defines the angular acceptance.",
        
        "drift chamber" :
        "Wires with gas mixture circulate the chamber. When a charged particle passes through the chamber it ionizes the gas along its trajectory (\"track\") and the potential created by the wires directs the electrons to the \"sense\" wire nearest the track. The time it takes these particles to drift to the sense wire is proportional to the distance of the track from the sense wires. The signal from the wires are \"starts\" for the TDC and the \"stop\" is formed by the complete trigger. By knowing the absolute position of the sensing wires that were hit and the drift time of the TDC, the position of the particle at each plane can be determined with tracking software.",
        
        "hodoscope" :
        "Multiple scintillator elements (\"paddles\"). Some planes are in the dispersive (\"x\", verticle, S1X/S2X) direction and some transverse (\"y\", horizontal, S1Y, S2Y) direction. The hodoscope arrays provide an integral part of the trigger for each spectrometer (the NIM signals) and allow for TOF of the particle (from TDC and ADC).",
        
        "beta" :
        "Velocity of particle from knowledge of TOF and the \"z\" pointer of the hodoscope planes can help calculate this velocity.",
        
        "gas cherenkov" :
        "To accomplish pi-/e- separation (in HMS), a gas cherenkov detector along with a lead-glass calorimeter are used. The gas cherenkov is generally operated as the \"threshold cherenkov\"  which discriminates betweeen species of charged particles based on whether or not their velocity is above a certain value. This threshold depends on the choice of \"n\" PIDs, the basis of whether or not light is detected by the PMTs (because beta>beta_threshold, beta_thres=1/n)",
        
        "pretrigger" :
        "Logic signals from various detectors combine to form the pretigger. It is a designed such that whenever an event meets a set of selection criteria, a pretrigger signal is sent to the coincidence logic.",
        
        "3/4" :
        "Scnitillator is formed when 3 out of 4 hodoscope planes are present. This reduces sensitivity of the trigger to the effects of issues in a single paddle and allows to calculate efficiencies.",
        
        "aerogel" :
        "Allows clean separation of pi+/k+.",
        
        "computer live time" :
        "",
        
        "chi squared minimization fit" :
        "",
        
        "radiative corrections" :
        "The incident e-, scattered e-, or k+ can lose some energy by radiating a photon. This leads to extra \"mass\" as tails on the missing mass spectrum.",
        
        "leading twist" :
        "",
        
        "conformal limit" :
        "",
        
        "kaon exchange term" :
        "",
        
        "gravitational form factor" :
        "",
        
        "sum rules" :
        "",
        
        "inclusive reaction" :
        "",
        
        "semi-inclusive reaction" :
        "",
        
        "exclusive reaction" :
        "",
        
        "compton scattering" :
        "",
        
        "epics" :
        "Provides information about the beam position, magnet settings, target status, and accelerator status which reads out in the GUI every 30 seconds.",
        
        "fadc" :
        "Fast analog to digital converter. See ADC.",
        
        "bpm" :
        "Beam position monitor.",
        
        "diffraction pattern" :
        "When a wave encounters an obstacle or slit it forms an interference that treats each point in the wave-front as a collection of individual spherical wavelets. This happens when a wave encounters an obstacle comparable to its wavelength.o",
        
        "monopole form" :
        "",
        
        "nmr" :
        "Nuclear magnetic resonance. Nuclei in a strong static magnetic field are perturbed by a weak oscillating one and respond by producing an E&M signal with a frequency characteristic of the magnetic field at the nucleus. This happens near resonance with the intrinsic frequency of the nuclei.",
        
        "plane wave born approximation" :
        "",
        
        "dirac plane wave" :
        "",
        
        "response function" :
        "",
        
        "meson mass pole" :
        "",
        
        "born exchange process" :
        "",
        
        "t channel" :
        "When a 2-body->2-body diagram contains only one virtual particle, it is conventional to describe that particle being in a certain \"chanel\". The channel is read from the Feynman diagram and each channel leads to a characteristic angular dependence of the cross section. A single process will often recieve contributions from multiple channels which add coherently. ",
        
        "jt valve" :
        "",
        
        "esr" :
        "End station refrigerator.",
        
        "fsd" :
        "Fast shutdown.",
        
        "fringe field" :
        "Excess fields from magnets.",
        
        "hysteresis effects" :
        "",
        
        "roc" :
        "Read out controller. Reads all the information collected by the electronics.",
        
        "bremsstrahlung radiation" :
        "E&M radiation produced by the acceleration or especially the decceleration of a charged particle after passing through the electric and magetic fields of the scattered nucleus. See radiative corrections.",
        
        "reconstruction matrix" :
        "",
        
        "scalers" :
        "Incremental values associated with a pretrigger event. They count raw hits on PMTs as well as important quantities such as charge and triggers which are used to normalize the experiment.",
        
        "regge pole" :
        "A singularity of form 1/(J-a) in a chosen scattering amplitude, where J is angular momentum and a is a function of energy of the colliding targets.",
        
        "quasi two body reaction" :
        "The final particles decay by strong interactions into the particles that are actually observed. ",
        
        "edtm" :
        "",
        
        "resonance region" :
        "",

        "steering magnet" :
        "",

        "tdc" :
        "Time to digital converter. Converts the time interval for each incoming signal into a digital (binary) output (i.e. signal or no signal).",

        "nim" :
        "",

        "tof" :
        "Time of flight.",

        "adc" :
        "Analog to digital converter. Converts an input voltage or current to a digital number representing the magnitude of voltage or current.",

        "wave front" :
        "",

        "intrinsic frequency" :
        "",

        "efficiencies" :
        "Efficiencies of the hardware for each event detection and reconstruction are calculated from scalers and other detector signals to find correction factors applied to yields.",

        "trigger efficiency" :
        "Probability of at least 3 out of 4 scintillator planes registering a hit when a particle is incident in the spectrometer.",

        "tracking efficiency" :
        "Done by the DC. There are hardware and software efficiencies. For a track to be reconstructed at least 5 of the DC planes need to have registered a hit. If there are more than 25 hits in the chamber with in the time window, the tracking is rejected. The tracking efficiencies are dependent on the rate of particles in the spectrometer (since higher rates increases the probability of multiple hits).",

        "time window" :
        "",

        "test" :
        Math('\Delta'),

    }

    dict_terms = list(dictionary.keys())
    
    for word in term.split():
        '''
        Searches for word in dictionary keys by making the dictionary keys into a list.
        The word is looped through each word in the dictionary keys for a match
        '''
        j=0
        for i in range(0,len(dict_terms)):
            if word in dict_terms[i].split():
                print "_"*(len(dict_terms[i])+4)
                print "|",dict_terms[i].upper(), "|", dictionary[dict_terms[i]]
                j+=1
        if j == 0:
            print "| ERROR: Term '%s' not defined," % word
            print "  if multiple words use parentheses!"

def main() :

    search(physics_term.lower())
    
if __name__=='__main__': main()
