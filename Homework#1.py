#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Tyler McCraney

# Right now the file primates.nex contians a line that reads "mcmc" This option tells 
# mrbayes to automatically start the markov chain monte carlo (mcmc) analysis. However, 
# there are other analyses we can do with mrbayes once the mcmc has finished. The problem 
# with primates.nex is that the mcmc command will force mrbayes to redo the mcmc analysis 
# every time we execute the file primates.nex To fix this, let's write a script that:
# 1. edits primates.nex to change the mcmc line to mcmcp
# 2. runs mrbayes interactively


# PART 1 (change "mcmc" to "mcmcp")

## Open the output file
new_primates = open("primates2.nex", "w")

## Open the input file
old_primates = open("primates.nex")

## Loop through input file line-by-line
for line in old_primates:
    ## Write edited lines to output file 
    new_primates.write(line.replace('mcmc', 'mcmcp'))
    
## Close the output file
new_primates.close()


# PART 2 (run MrBayes interactively)

import pexpect

## Tell MrBayes to run in interactive mode
child = pexpect.spawn("mb -i primates2.nex") 

## Send the string "mcmc" to the process. This tells MrBayes to start running. The \r is 
## carriage return
child.sendline(r"mcmc") 

## Tell MrBayes to stop the analysis (do not continue)
child.sendline("no") 

## Wait for the MrBayes prompt
child.expect("MrBayes >") 

# Show all of the screen output
print(child.before) 

# Tell MrBayes to quit
child.close()

    
    