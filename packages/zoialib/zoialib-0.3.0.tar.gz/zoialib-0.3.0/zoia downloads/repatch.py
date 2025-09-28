#!/usr/bin/python3
"""Script for renaming binary files to contain a preferred numerical order.

This is for use with patch files for the Empress Zoia, which requires the patch files to
start with a three-digit number and doesn't permit duplicates.

Instead of manually renaming, you can create a PLAN file with:

    $ python3 repatch.py

Example output:

    Plan file saved to /home/you/to-zoia/PATCH-PLAN-2025-03-07-20-38-18.txt.

    You can reorder the items in that file by editing it, and then execute the plan by re-running
    this script with:
    repatch.py -p PATCH-PLAN-2025-03-07-20-38-18.txt -x
"""

import argparse
import datetime
import os
import re
import shutil
import sys
from typing import Optional

# Constants
MAX_ENTRIES = 64
NOW = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
BINARY_REGEX = re.compile(r".*\.bin")
PREFIX_REGEX = re.compile(r"^(- )?.?(\d+)(.*)")
BLANK_PATCH_NAME_SUFFIX = "_zoia_.bin"
BLANK_ZOIA_PATCH = b"\t" + (b"\x00" * 32767)


def parse_arguments():
    parser = argparse.ArgumentParser(description="File Reordering Tool")
    parser.add_argument(
        "-x",
        "--execute",
        action="store_true",
        help="Execute the renaming (non-dry run).",
    )

    def _os_path(string):
        if os.path.exists(string):
            return string
        else:
            raise NotADirectoryError(string)

    parser.add_argument(
        "-p",
        "--plan",
        type=_os_path,
        help="Path to a file with the binaries listed in the order they should go.",
    )
    return parser.parse_args()


def get_local_binary_files(path: str) -> list[str]:
    """Get a list of all files in the folder."""
    files = os.listdir(path)
    matching_files = []
    added_files = set()
    for file_name in sorted(files):
        match = BINARY_REGEX.match(file_name)
        if match and file_name not in added_files:
            matching_files.append(file_name)
            added_files.add(file_name)
    return matching_files


def matches_some_file(name_fragment: str, local_filenames: set[str]) -> str:
    """If the name-fragment is a fragment of some file in the local directory, return its name.

    Throws ValueError if there's no match or more than one match.
    """
    matches = []
    for filename in local_filenames:
        if name_fragment in filename:
            matches.append(filename)
    if len(matches) > 1:
        print(f"Multiple files matching the plan element {name_fragment} were found: {matches}")
        sys.exit(2)
    if not matches:
        print(f"Some files in the plan-file no longer exist (ex: {name_fragment}). Aborting.")
        sys.exit(3)
    return matches[0]


def generate_new_names(plan: list[str], local_binary_files: set[str]) -> list[tuple[Optional[str], str]]:
    """Process the plan text and return the old and new filenames.

    Note that the filenames in the plan are prefaced by "- " and followed by a newline.
    """
    ret = []
    for i in range(MAX_ENTRIES):
        new_num_prefix = str(i).zfill(3)
        if i < len(plan):
            file_name = plan[i]
            input_name = file_name.lstrip("- 0123456789_").strip()
            new_name = f"{new_num_prefix}_{input_name}"
            match = matches_some_file(input_name, local_binary_files)
        else:
            # We will write a blank patch so that the user can save their own patches.
            match = None
            new_name = str(i).zfill(3) + BLANK_PATCH_NAME_SUFFIX
        ret.append((match, new_name))
    return ret


def main():
    args = parse_arguments()
    folder_path = os.getcwd()
    #          | no plan file                      | plan file                                   |
    # dry run  | generate a plan file              | describe what we would do                   |
    # live run | describe and auto-move the files  | rename the files according to the plan file |

    # if dry run and no plan file, we should generate a plan file
    local_binary_files = get_local_binary_files(folder_path)
    if args.plan:
        with open(args.plan) as infile:
            plan = infile.readlines()
    else:
        if args.execute:
            # execute and not plan? weird, but not disallowed
            plan = local_binary_files
        # if not execute, then write a plan file for the user to edit
        else:
            plan_file_name = f"PATCH-PLAN-{NOW}.txt"
            plan_file_path = os.path.join(folder_path, plan_file_name)
            with open(plan_file_path, "w") as outfile:
                for filename in local_binary_files:
                    outfile.write(f"- {filename}\n")
            print(f"Plan file saved to {plan_file_path}.")
            print(
                "You can reorder the items in that file by editing it, and then execute the plan by re-running this script with:"
            )
            print(f"  repatch.py -p {plan_file_name} -x")
    # if dry run and plan file, we should output the new names.
    # if live run and no plan file, we should describe and auto-move the files
    # if live run and plan file, we should rename the files according to the plan file.
    if args.execute or args.plan:
        target_folder_path = f"repatched-{NOW}"
        old_and_new_names = generate_new_names(plan, local_binary_files)
        if args.execute:
            # ensure target directory exists.
            target_dir: str = os.path.join(folder_path, target_folder_path)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            print("Moving the files to the following paths:")
        else:
            print("Would move the files to the following paths:")
        for old_name, new_name in old_and_new_names:
            print(f"- {os.path.join(target_folder_path, new_name)}")
            if args.execute:
                # Check if we need to write a blank file.
                if old_name is None:
                    with open(os.path.join(target_dir, new_name), "wb") as outfile:
                        outfile.write(BLANK_ZOIA_PATCH)
                else:
                    shutil.copyfile(
                        os.path.join(folder_path, old_name),
                        os.path.join(target_dir, new_name),
                    )
        if not args.execute:
            print("Re-run again with -x / --execute to execute this plan.")


if __name__ == "__main__":
    main()
