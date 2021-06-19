#!/usr/bin/env python3

import argparse
import configparser
from pathlib import Path
from src.color import Colors
from src.main import ConsoleHelper


def get_parser():

    parser = argparse.ArgumentParser(description="totailwind")
    # positional arg
    parser.add_argument("arg", help="a file path/a folder path/Bootstrap CSS classes")
    parser.add_argument(
        "--replace",
        dest="replace",
        help="This will overwrite the original file.",
        action="store_true",
    )
    parser.add_argument(
        "--components",
        dest="components",
        help="Extract changes as components to a separate css file in the current directory.",
        action="store_true",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        dest="recursive",
        help="This will recurs through all directories under the main directory",
        action="store_true",
    )
    parser.add_argument(
        "-e",
        "--extensions",
        dest="extensions",
        help="This allows for custom extensions ex: '.jsx' ",
        type=str,
        default=".php,.html",
    )
    parser.add_argument(
        "-t",
        "--framework",
        dest="framework",
        help="CSS Framework type to convert",
        type=str,
        default="bootstrap",
    )
    parser.add_argument(
        "-p",
        "--prefix",
        dest="prefix",
        help="This allows you to add a custom prefix to all of Tailwind's generated utility classes",
        type=str,
        default="",
    )
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    arg = args["arg"]
    if not args:
        print(f"{Colors.WARNING}Oops! nothing to convert.{Colors.ENDC}")
        return -1

    accepted_extensions = args["extensions"].split(",")

    framework = args["framework"].lower()

    # # if (! class_exists('Awssat\\Tailwindo\\Framework\\' . ucfirst(framework).'Framework')):
    # if f'{framework.capitalize()}Framework' not in dir():
    #     print(f"{Colors.WARNING}Oops! {framework} is not supported!{Colors.ENDC}")
    #     return -1

    console_helper = ConsoleHelper(
        {
            "recursive": args["recursive"],
            "overwrite": args["replace"],
            "extensions": accepted_extensions,
            "framework": framework,
            "components": args["components"],
            "prefix": args["prefix"],
            "folder_convert": Path(arg).is_dir(),
        }
    )

    # file?
    if Path(arg).is_file():
        return console_helper.file_convert(arg)

    # folder ?
    if Path(arg).is_dir():
        return console_helper.folder_convert(arg)

    # any html/css classes
    return console_helper.code_convert(arg)


if __name__ == "__main__":
    main()
