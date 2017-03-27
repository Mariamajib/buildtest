#!/usr/bin/python
from setup import *
from modules import *
from utilities import *
import argparse
import sys
module=""
version=""

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--software", help=" Specify software package to test")
parser.add_argument("-t", "--toolchain",help=" Specify toolchain for the software package") 
parser.add_argument("-lt", "--list-toolchain",help="retrieve toolchain used based on the easyconfig files provided by BUILDTEST_EASYCONFIGDIR", action="store_true")
parser.add_argument("-ls", "--list-software",help="retrieve all unique software found in your module tree specified by BUILDTEST_MODULETREE", action="store_true")
parser.add_argument("-svr", "--software-version-relation", help="retrieve a relationship between software and version found in module files", action="store_true")
parser.add_argument("-v", "--verbose", help="increase verbosity level", type=int, choices=[1,2])
args = parser.parse_args()



print BUILDTEST_ROOT, BUILDTEST_SRCDIR, BUILDTEST_EASYCONFIGDIR, BUILDTEST_MODULEROOT
#print args.list-toolchains
#if args.software-version-relation:
#	moduleversion_dict=module_version_relation(BUILDTEST_MODULEROOT)
#	print "Software Version Relationship:"
#	print_dictionary(moduleversion_dict)


#moduleversion_toolchain_relation(BUILDTEST_MODULEROOT)

print "software=",args.software
software=args.software.split(",")

# set toolchain to dummy when its not specified. 
if not args.toolchain:
	toolchain="dummy,dummy".split(",")
else:
	toolchain=args.toolchain.split(",")

print software, toolchain
ret=software_exists(software)
print "ret",ret
ret1=toolchain_exists(software,toolchain)
print ret,ret1

software_dir=software[0]
cmd="find " + BUILDTEST_EASYCONFIGDIR + software_dir  + " -name *.eb -type f"         
print "command=",cmd
easyconfigfiles=os.popen(cmd). read().rstrip()                                        
print easyconfigfiles    

sys.exit(1)

'''
print "args.tc",args.list-toolchain
if args.list-toolchain:
	print "inside"
	toolchain=get_toolchain(BUILDTEST_EASYCONFIGDIR)
	print "Toolchain List:" 
	print_set(toolchain)
else:
	print "outside"
'''
