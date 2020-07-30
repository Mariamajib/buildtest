import json
import os
import subprocess
import yaml
from tabulate import tabulate
from jsonschema.exceptions import ValidationError
from buildtest.defaults import REPO_FILE, BUILDSPEC_CACHE_FILE
from buildtest.config import get_default_settings
from buildtest.utils.file import is_file, is_dir, walk_tree
from buildtest.buildsystem.base import BuildspecParser


def func_buildspec_find(args):
    """Entry point for ``buildtest buildspec find``. This method
       will attempt to read for buildspec cache file (BUILDSPEC_CACHE_FILE)
       if found and print a list of all buildspecs. Otherwise, it will
       read the repo file (REPO_FILE) and find all buildspecs and validate
       them via BuildspecParser. BuildspecParser will raise SystemError or
       ValidationError if a buildspec is invalid which will be added to list
       of invalid buildspecs. Finally we print a list of all valid buildspecs
       and any invalid buildspecs are written to file along with error
       message.

       Parameters

       :param args: Input argument from command line passed from argparse
       :return: A list of valid buildspecs found in all repositories.
    """

    cache = {}
    # implements buildtest buildspec find --clear which removes cache file before finding all buildspecs
    if args.clear:
        try:
            os.remove(BUILDSPEC_CACHE_FILE)
            print(f"Clearing cache file: {BUILDSPEC_CACHE_FILE}")
        except OSError:
            pass

    if is_file(BUILDSPEC_CACHE_FILE):
        with open(BUILDSPEC_CACHE_FILE, "r") as fd:
            cache = json.loads(fd.read())
    # if cache file is not found, then we will build cache by searching
    # all buildspecs based on available repos found in REPO_FILE and
    # traverse directory to find all .yml files
    else:
        # if repo file not found then terminate with message since we can't find
        # any buildspecs
        if not is_file(REPO_FILE):
            raise SystemExit(
                "Unable to find any buildspecs because no repositories found."
            )

        with open(REPO_FILE, "r") as fd:
            repo_dict = yaml.load(fd.read(), Loader=yaml.SafeLoader)

        paths = []
        for repo in repo_dict.keys():
            # only add if repository cloned locally exists in filepath
            if is_dir(repo_dict[repo]["dest"]):
                paths.append(repo_dict[repo]["dest"])

        buildspecs = []
        invalid_buildspecs = {}
        parse = None
        # add all buildspecs from each repo. walk_tree will find all .yml files
        # recursively and add them to list
        for path in paths:
            buildspec = walk_tree(path, ".yml")
            buildspecs += buildspec

        # remove any files in .buildtest directory of root of repo.
        buildspecs = [
            buildspec
            for buildspec in buildspecs
            if os.path.basename(os.path.dirname(buildspec)) != ".buildtest"
        ]
        print(f"Found {len(buildspecs)} buildspecs")
        # process each buildspec by invoking BuildspecParser which will validate
        # buildspec, if it fails it will raise SystemExit or ValidationError in
        # this case we skip to next buildspec
        count = 0
        for buildspec in buildspecs:
            count += 1

            try:
                parse = BuildspecParser(buildspec)
            # any buildspec that raises SystemExit or ValidationError imply
            # buildspec is not valid, we add this to invalid list along with
            # error message and skip to next buildspec
            except (SystemExit, ValidationError) as err:
                invalid_buildspecs[buildspec] = err
                continue

            if count % 5 == 0:
                print(f"Validated {count}/{len(buildspecs)} buildspecs")

            recipe = parse.recipe["buildspecs"]

            cache[buildspec] = {}

            for name in recipe.keys():

                if not isinstance(recipe[name], dict):
                    continue

                cache[buildspec][name] = recipe[name]

        print(f"Validated {count}/{len(buildspecs)} buildspecs")

        with open(BUILDSPEC_CACHE_FILE, "w") as fd:
            json.dump(cache, fd, indent=2)

        print(f"\nDetected {len(invalid_buildspecs)} invalid buildspecs \n")

        # write invalid buildspecs to file if any found
        if invalid_buildspecs:
            buildspec_error_file = os.path.join(
                os.path.dirname(BUILDSPEC_CACHE_FILE), "buildspec.error"
            )

            with open(buildspec_error_file, "w") as fd:
                for file, msg in invalid_buildspecs.items():
                    fd.write(f"buildspec:{file} \n\n")
                    fd.write(f"{msg} \n")
            print(f"Writing invalid buildspecs to file: {buildspec_error_file} ")
            print("\n\n")

    table = {"Name": [], "Type": [], "Executor": [], "Description": []}
    # print("{:<25} {:<25} {:<25}".format("Name", "Schema Type", "Executor"))
    # print("{:_<80}".format(""))
    for buildspecfile in cache.keys():
        for test in cache[buildspecfile].keys():

            type = cache[buildspecfile][test]["type"]
            executor = cache[buildspecfile][test]["executor"]
            description = cache[buildspecfile][test].get("description")
            # print("{:<25} {:<25} {:<25}".format(test, type, executor))
            table["Name"].append(test)
            table["Type"].append(type)
            table["Executor"].append(executor)
            table["Description"].append(description)

    print(tabulate(table, headers=table.keys(), tablefmt="grid"))


def func_buildspec_view_edit(buildspec, view=False, edit=False):
    """This is a shared method for ``buildtest buildspec view`` and
       ``buildtest buildspec edit``.

       Parameters:
       :param buildspec: buildspec file section to view or edit.
       :param view: boolean to determine if we want to view buildspec file
       :param edit: boolean to control if we want to edit buildspec file in editor.
       :return: Shows the content of buildspec or let's user interactively edit buildspec. An exception can be raised if it's unable to find buildspec
    """

    with open(BUILDSPEC_CACHE_FILE, "r") as fd:
        cache = json.loads(fd.read())

    for buildspecfile in cache.keys():
        if buildspec in cache[buildspecfile].keys():
            if view:
                cmd = f"cat {buildspecfile}"
                output = subprocess.check_output(cmd, shell=True).decode("utf-8")
                print(output)
            if edit:
                # this loop will terminate once user has edited file, and we parse
                # the file for any errors. If one of the exceptions is raised, we
                # print error message and set 'success' to False and user is requested
                # to fix buildspec until it is valid.
                while True:
                    success = True
                    config_opts = get_default_settings()
                    os.system(f"{config_opts['config']['editor']} {buildspecfile}")
                    try:
                        BuildspecParser(buildspecfile)
                    except (SystemExit, ValidationError) as err:
                        print(err)
                        input("Press any key to continue")
                        success = False
                    # break out of while loop once user has successfully validated
                    # buildspec.
                    if success:
                        break

            return

    raise SystemExit(f"Unable to find buildspec {buildspec}")


def func_buildspec_view(args):
    """This method implements ``buildtest buildspec view`` which shows
       content of a buildspec file
    """
    func_buildspec_view_edit(args.buildspec, view=True, edit=False)


def func_buildspec_edit(args):
    """This method implement ``buildtest buildspec edit`` which
       allows one to edit a Buildspec file with one of the editors
       set in buildtest settings.
    """

    func_buildspec_view_edit(args.buildspec, view=False, edit=True)