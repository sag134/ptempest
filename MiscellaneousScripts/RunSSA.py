#Script to iterate through multiple BNG files and perform several stochastic simulations of each
import sys
import os
import multiprocessing
from multiprocessing import Pool
from functools import partial

baseFile = 'nfkbdecoupled2'
nfiles = 10;
numcores = multiprocessing.cpu_count();
nbatches = int(nfiles/numcores)+nfiles%numcores;

