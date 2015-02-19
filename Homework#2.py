#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Tyler McCraney

# Now we will restart MrBayes and run the sumt and sump analysis. We need to start in 
# interactive mode and execute the primates2.nex file. We do NOT want to run mcmc. Here is
# some pseudocode to get you started.

import pexpect

## Spawn an interactive MrBayes process
child = pexpect.spawn("mb -i primates2.nex")

## Send the command "execute primates2.nex" to MrBayes
child.sendline("execute primate2.nex")

## Send the sumt command to MrBayes
child.sendline("sumt")

## Check to see that the MrBayes command prompt is returned
child.expect("MrBayes >")

## Print everything before the MrBayes prompt
print(child.before)

## Send the sump command
child.sendline("sump")

#quit MrBayes
child.close()