#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import pexpect
import glob
import re

# Tyler McCraney

# OK this assignment will require you to tie the pexpect concepts together with functions.
# Here is what you need to do.

# Write a function that takes a nexus file and and a numgen variable (integer that is 1000
# or greater-try setting a default if you remember how!) to interactively start MrBayes.

nexus_file = open("primates2.nex")

def run_mrbayes1(nexus_file, numgen): # define function
    child = pexpect.spawn("mb -i nexus_file") # spawn interactive MrBayes process
    child.sendline("set nowarn = yes") # send command "set nowarn = yes" to MrBayes
    child.sendline("mcmcp ngen = numgen") # send command "mcmcp ngen = XX"... XX = numgen
    child.sendline(r"mcmc") # send command "mcmc" to MrBayes
    child.sendline("no") # send command "no" to MrBayes (do not continue analysis)
    child.close() # send command "quit" to MrBayes
    return run_mrbayes1

# Write a second function that takes a nexus file and runs sumt and sump in MrBayes
def run_mrbayes2(nexus_file): # define function
    child = pexpect.spawn("mb -i nexus_file") # spawn interactive MrBayes process
    child.sendline("sumt") # run sumt
    child.sendline("sump") # run sump
    child.close() # send command "quit" to MrBayes
    return run_mrbayes2
    

# Add these functions to a script. After these functions are defined, your script should
# do the following

# -Print the line "there are XX total files in the current directory and yy files that end
# in '.t'"
all_files = glob.glob("/home/vagrant/Homework-pexpect/*")
t_files = glob.glob("/home/vagrant/Homework-pexpect/*.t")
print("There are " + str(len(all_files)) + " total files in the current directory and " + str(len(t_files)) + " files that end in '.t'")

# -Call function 1 with primates2.nex
run_mrbayes1(nexus_file, 1000)

# -Call function 2 with primates2.nex
run_mrbayes2(nexus_file)

# -Print the line "there are XX total files in the current directory and yy files that end
# in '.t'"
all_files = glob.glob("/home/vagrant/Homework-pexpect/*")
t_files = glob.glob("/home/vagrant/Homework-pexpect/*.t")
print("There are " + str(len(all_files)) + " total files in the current directory and " + str(len(t_files)) + " files that end in '.t'")

# -Print the line "these files end in '.t': " followed by the names of the *.t files, 
# separated by commas.
print("These files end in '.t': " + str(t_files))

