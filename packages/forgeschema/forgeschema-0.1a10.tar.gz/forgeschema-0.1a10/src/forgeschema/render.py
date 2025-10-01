import logging
from pathlib import Path

from .schema import Schema
from .types import BuildError, ErrorSeverity

import colorama
from colorama import  Fore, Style
import os

colorama.init()
RED = Fore.RED
GRN = Fore.GREEN
BLU = Fore.BLUE
YLW = Fore.YELLOW
CLR = Style.RESET_ALL

try:
    TERM_WIDTH = os.get_terminal_size().columns
except OSError as ex:
    TERM_WIDTH = 70

def double_seperator():
    print ("".ljust(TERM_WIDTH, "═"))

def seperator():
    print ("".ljust(TERM_WIDTH, "─"))

def render_validation_output(schema: Schema, validation_errors, config):
    fatal_build_errors = len([x for x in schema.build_errors if x.severity == ErrorSeverity.ERROR])
    non_fatal_build_errors = len(schema.build_errors) - fatal_build_errors
    total_validation_errors = sum(len(v) for k,v in validation_errors.items())
        
    double_seperator()
    print (f"Building {BLU}{config['coreSchema']}{CLR} and {BLU}{len(config['supportingSchemas'])}{CLR} supporting schemas")
    if fatal_build_errors > 0:
        print (f"❌ Failed build, {RED}{fatal_build_errors}{CLR} fatal, {non_fatal_build_errors} non-fatal")

        for build_error in schema.build_errors:
            seperator()
            print (f"Build error in {BLU}{build_error.path}{CLR}")
            print (f"")
            print (f"{YLW}{build_error.error}{CLR}")
            if logging.root.level == logging.DEBUG:
                print(build_error)
            
    else:
        print (f"✅ Built OK")
        if total_validation_errors > 0:
            print (f"❌ Failed validating instance documents")

            for k,v in validation_errors.items():
                for error in v:
                    seperator()
                    print (f"Validation error in {BLU}{k.name}{CLR}")
                    print (f"")
                    print (f"{YLW}{error}{CLR}")

        else:
            print (f"✅ Validated {BLU}{len(config['instanceDocs'])}{CLR} instance documents")
    double_seperator()
