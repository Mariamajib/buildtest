############################################################################
#
#  Copyright 2017-2018
#
#   https://github.com/HPC-buildtest/buildtest-framework
#
#  This file is part of buildtest.
#
#    buildtest is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    buildtest is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with buildtest.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################

"""
buildtest menu

:author: Shahzeb Siddqiui
"""

import os
import argparse
import argcomplete

from buildtest.test.python import python_pkg_choices
from buildtest.test.r import r_pkg_choices
from buildtest.test.ruby import ruby_pkg_choices
from buildtest.test.perl import perl_pkg_choices
from buildtest.test.run import test_list
from buildtest.tools.config import BUILDTEST_SHELLTYPES, config_opts, check_configuration
from buildtest.tools.options import override_configuration
from buildtest.tools.system import systempackage_installed_list
from buildtest.tools.software import get_software_stack, get_toolchain_stack,ebyaml_choices


class buildtest_menu():

        parser = {}
        override_configuration()
        check_configuration()
        syspkg_list = os.listdir(os.path.join(config_opts['BUILDTEST_CONFIGS_REPO'],"buildtest","system"))

        pkglist = systempackage_installed_list()
        python_choices = python_pkg_choices()
        r_choices = r_pkg_choices()
        ruby_choices = ruby_pkg_choices()
        perl_choices = perl_pkg_choices()

        yaml_apps = ebyaml_choices()
        software_list = get_software_stack()
        toolchain_list = get_toolchain_stack()

        test_choices = test_list()

        def __init__(self):
        # reports an error, issue with import
        #software_list = get_unique_software_version(BUILDTEST_MODULE_EBROOT)

            parser = argparse.ArgumentParser(prog='buildtest', usage='%(prog)s [options]')
            parser.add_argument("-V", "--version", help="show program version number and exit",action="store_true")
            parser.add_argument("--logdir", help="Path to write buildtest logs. Override configuration BUILDTEST_LOGDIR")
            parser.add_argument("--testdir", help="Path to write buildtest tests. Overrides configuration BUILDTEST_TESTDIR")
            parser.add_argument("--ignore-easybuild", help="ignore if application is not built with easybuild",action="store_true")
            parser.add_argument("--show", help="show buildtest environment configuration", action="store_true")
            parser.add_argument("--clean-build", help="delete software test directory before writing test scripts", action="store_true")
            parser.add_argument("--show-keys", help="display yaml key description", action="store_true")

            group1 = parser.add_argument_group('Basic Options', 'buildtest basic options')
            group1.add_argument("-mns", "--module-naming-scheme", help="Specify module naming scheme for easybuild apps", choices=["HMNS","FNS"])
            group1.add_argument("--scantest", help=""" Report all tests that can be built with buildtest by checking all available apps found
            in eb stack and system packages""", action="store_true")
            group1.add_argument("--clean-logs", help="delete buildtest log directory ($BUILDTEST_LOGDIR)",action="store_true")
            group1.add_argument("--clean-tests",help="delete testing directory ($BUILDTEST_TESTDIR)",action="store_true")


            find_subparsers = parser.add_subparsers(help='List subcommand help')
            parser_find = find_subparsers.add_parser('list', help='list help')
            parser_find.add_argument('-lt', "--list-toolchain", help="retrieve a list of easybuild toolchain used for --toolchain option", action="store_true")
            parser_find.add_argument("-ls", "--list-unique-software",help="retrieve all unique software found in your module tree specified by BUILDTEST_MODULE_ROOT", action="store_true")
            parser_find.add_argument("-svr", "--software-version-relation", help="retrieve a relationship between software and version found in module files", action="store_true")
            parser_find.add_argument("-f", "--format", help="Output format type", choices=["csv", "json", "stdout"], default="stdout")

            group2 = parser.add_argument_group('Find Options', 'buildtest options for finding software, toolchains, tests, yaml files')
            #group2.add_argument("-lt", "--list-toolchain",help="retrieve a list of easybuild toolchain used for --toolchain option", action="store_true")
            #group2.add_argument("-ls", "--list-unique-software",help="retrieve all unique software found in your module tree specified by BUILDTEST_MODULE_ROOT", action="store_true")
            #group2.add_argument("-svr", "--software-version-relation", help="retrieve a relationship between software and version found in module files", action="store_true")
            group2.add_argument("-fc","--findconfig", help= """ Find buildtest YAML config files found in BUILDTEST_CONFIGS_REPO.
                                                 To find all yaml config files use -fc all """)
            group2.add_argument("-ft", "--findtest", help="""Find test scripts generated by buildtest defined by BUILDTEST_TESTDIR.
                                         To find all test scripts use -ft all """)
            group2.add_argument("-ecmt","--easyconfigs-in-moduletrees", help="Return a list of easyconfigs from a easybuild module tree",action="store_true")
            group2.add_argument("--diff-trees", help="Show difference between two module trees")

            group3 = parser.add_argument_group('Test Options', 'Options for building tests with buildtest')
            group3.add_argument("-s", "--software", help=" Specify software package to test", choices=self.software_list, metavar='INSTALLED-EASYBUILD-APPS')
            group3.add_argument("-t", "--toolchain",help=" Specify toolchain for the software package", choices=self.toolchain_list, metavar='INSTALLED-EASYBUILD-TOOLCHAINS')
            group3.add_argument("--shell", help=""" Select the type of shell when running test""", choices=BUILDTEST_SHELLTYPES)
            group3.add_argument("--system", help=""" Build test for system packages
                             To build all system package test use --system all """, choices=self.syspkg_list, metavar='SYSTEM-PACKAGE')
            group3.add_argument("--module-load-test", help="conduct module load test for all modules defined in BUILDTEST_MODULE_ROOT", action="store_true")
            group3.add_argument("--python-package", help="build test for Python packages", choices=self.python_choices,metavar='PYTHON-PACKAGES')
            group3.add_argument("--r-package", help="build test for R packages", choices=self.r_choices,metavar='R-PACKAGES')
            group3.add_argument("--ruby-package", help="build test for Ruby packages", choices=self.ruby_choices,metavar='RUBY-PACKAGES')
            group3.add_argument("--perl-package", help="build test for Perl packages", choices=self.perl_choices,metavar='PERL-PACKAGES')

            group4 = parser.add_argument_group('YAML Options', 'Options for YAML configuration')
            group4.add_argument("--sysyaml", help = "generate YAML configuration for binary test for system package", choices=self.pkglist, metavar='INSTALLED-SYSTEM-PACKAGE')
            group4.add_argument("--ebyaml", help = "generate YAML configuration for binary test for software package", choices=self.yaml_apps, metavar='YAML-APP-CHOICES')


            group5 = parser.add_argument_group('Job Scheduler Options', 'Options for interacting with Job Scheduler')
            group5.add_argument("--enable-job", help="enable job script generation with buildtest", action="store_true")
            group5.add_argument("--job-template", help = "specify  job template file to create job submission script for the test to run with resource scheduler")
            group5.add_argument("--submitjob", help = "specify a directory or job script to submit to resource scheduler")

            group6 = parser.add_argument_group('Miscellaneous Options', 'rest of buildtest options')
            group6.add_argument("--runtest", help="Run the test interactively through runtest.py", action="store_true")
            group6.add_argument("-r", "--run", help="Run test scripts via buildtest", choices=self.test_choices, metavar='TEST-CHOICES')

            self.parser = parser

        #argcomplete.autocomplete(parser)
        #args = parser.parse_args()

        #return vars(args)


        def parse_options(self):
                """ return argument as a dictionary"""

                argcomplete.autocomplete(self.parser)
                args = self.parser.parse_args()
                return args
