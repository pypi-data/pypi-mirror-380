import logging
import json
from sys import stdin
from argparse import ArgumentParser
from pathlib import Path
from xml.etree import ElementTree

from ..schema import Schema
from ..jsonschema import JSONSchema
from ..xsdschema import XSDSchema
from ..types import ErrorSeverity
from ..helpers import guess_encoding, expand_path
from ..render import render_validation_output


ERR_FILE_NOT_FOUND          = -1
ERR_UNSUPPORTED_ENCODING    = -2
ERR_UNKNOWN_ENCODING        = -3
ERR_BAD_CONFIG              = -4

EXIT_OK                     = 0
EXIT_BUILD_ERRORS           = 1
EXIT_VALIDATION_ERRORS      = 2

supported_encodings = {
    'json' : {
        'schema_extensions' : ['.schema.json'],
        'instance_extensions' : ['.json']
    },
    'xml' : {
        'schema_extensions' : ['.xsd'],
        'instance_extensions' : ['.xml']
    }
}

def check():
    parser = ArgumentParser()

    parser = ArgumentParser(description="Build a schema set and use it to validate zero or more instance documents. Returns 1 if the schema build fails, 2 if any of the instance documents fail to validate, or 0 otherwise. If JSON output is selected via the -j switch, it is always 0")
    parser.add_argument("-e", "--encoding", help=f"Set the encoding of the schema / instance documents. One of [{'|'.join(list(supported_encodings.keys()))}]")
    arg_group = parser.add_mutually_exclusive_group(required=True)
    arg_group.add_argument("-c", "--config", help="Specifies the location of a JSON config file")
    arg_group.add_argument("-s", "--coreschema", help="Specifies the location of the core JSON schema file")
    parser.add_argument("-u", "--supportingschema", action="append", help="Specifies the location of any supporting schemas required. If a directory is specified, testjson will search and add any .schema.json files recursively within the directory")
    parser.add_argument("-i", "--instancedoc", action="append", help="Instance XML document to validate against the schema. If a directory is specified, xmltest will search and add any XML files recursively within the directory")
    parser.add_argument("-j", "--jsonoutput", action="store_true", help="Output JSON instead of text. Return code will always be zero")
    parser.add_argument("-v", "--verbose", action="count", help="Verbose. Can be specified multiple times to get more detailed output")
    parser.add_argument("--showbuild", action="store_true", help="Print build output to stdout")
    parser.add_argument("--showvalidation", action="store_true", help="Print validation output to stdout")
    parser.add_argument("--hideissues", action="store_true", help="Print list of build and validation issues to stdout")
    parser.add_argument("--hidesummary", action="store_true", help="Hide summary output on stdout")
    parser.add_argument("-q", "--quiet", action="store_true", help="Hide all output (equivalent to --hideissues plus --hidesummary)")
    pargs = parser.parse_args()

    if pargs.verbose is None or pargs.verbose == 1:
        logging.basicConfig(level=logging.ERROR)
    elif pargs.verbose == 2:
        logging.basicConfig(level=logging.WARNING)
    elif pargs.verbose == 3:
        logging.basicConfig(level=logging.INFO)
    elif pargs.verbose > 3:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)
    
    logging.debug(f"Called with arguments {pargs}")

    if pargs.config is not None:
        config_file = Path(pargs.config)
        if not config_file.exists():
            logging.error(f"Cannot find config file {pargs.config}")
            exit(ERR_FILE_NOT_FOUND)
        config = json.loads(config_file.read_text())
        if 'coreSchema' not in config.keys():
            logging.error('Config file does not have a "coreSchema" key')
            exit(ERR_BAD_CONFIG)
        if 'supportingSchemas' not in config.keys():
            logging.warning('Config file does not have a "supportingSchemas" key, assuming empty')
            config['supportingSchemas'] = []
        if 'instanceDocs' not in config.keys():
            logging.warning('Config file does not have a "instanceDocs" key, assuming empty or taking from command line')
            config['instanceDocs'] = [i for i in pargs.instancedoc] if pargs.instancedoc is not None else []
    else:
        config = {
            'coreSchema' : pargs.coreschema,
            'supportingSchemas' : [s for s in pargs.supportingschema] if pargs.supportingschema is not None else [],
            'instanceDocs' : [i for i in pargs.instancedoc] if pargs.instancedoc is not None else [],
        }

    if pargs.encoding is None:
        if not (Path(config['coreSchema']).exists()):
            logging.error(f"Could not load core schema {config['coreSchema']}")
            exit(ERR_FILE_NOT_FOUND)
        logging.debug("No encoding specified, attempting to guess encoding from core schema...")
        guessed_encoding = guess_encoding(Path(config['coreSchema']))
        if guessed_encoding is None:
            logging.error(f"Couldn't guess encoding from {config['coreSchema']}")
            exit(ERR_UNKNOWN_ENCODING)
        else:
            pargs.encoding = guessed_encoding

    if pargs.encoding not in list(supported_encodings.keys()):
        logging.error(f"Unsupported encoding '{pargs.encoding}' specified. Supported encodings are [{'|'.join(list(supported_encodings.keys()))}]")
        exit(ERR_UNSUPPORTED_ENCODING)
    if pargs.encoding == 'xml':
        logging.debug("Creating XML schema")
        schema = XSDSchema(Path(config['coreSchema']), [Path(x) for x in config['supportingSchemas']])
    if pargs.encoding == 'json':
        logging.debug("Creating JSON schema")
        schema = JSONSchema(Path(config['coreSchema']), [Path(x) for x in config['supportingSchemas']])

    logging.debug("Expanding supporting schemas...")
    config['supportingSchemas'] = [expanded_path for path in config['supportingSchemas'] for expanded_path in expand_path(Path(path), [f'*{x}' for x in supported_encodings[pargs.encoding]['schema_extensions']])]
    if Path(config['coreSchema']) in config['supportingSchemas']:
        config['supportingSchemas'].remove(Path(config['coreSchema']))
    for s in config['supportingSchemas']:
        logging.info(f"  supporting schema : {s}")

    logging.debug("Expanding instance docs...")
    config['instanceDocs'] = [expanded_path for path in config['instanceDocs'] for expanded_path in expand_path(Path(path), [f'*{x}' for x in supported_encodings[pargs.encoding]['instance_extensions']])]
    for doc in config['instanceDocs']:
        logging.info(f"  instance doc: {doc}")

    logging.debug(f"Config: {config}")

    schema.build()

    if schema.built_ok:
        logging.info('Schema built OK')
        if len(config['instanceDocs']) == 1 and str(config['instanceDocs'][0]).lower() == 'stdin':
            input_string = stdin.read()
            validation_errors = {'stdin' : schema.validate_string(input_string)}
        else:
            validation_errors = {f : schema.validate(Path(f)) for f in config['instanceDocs']}
    else:
        logging.warning('Errors building schema')
        validation_errors = {}

    if pargs.jsonoutput:
        logging.debug("Giving output in JSON format")
        output = {
            'input' : config,
            'build_errors' : [be.toJSON() for be in schema.build_errors],
            'validation_errors' : validation_errors
        }
        print(json.dumps(output, default=str))
        exit(EXIT_OK)

    if pargs.quiet:
        logging.debug ("Output suppressed due to --quiet")
    else:
        render_validation_output(schema, validation_errors, config)

    # fatal_build_errors = len([x for x in schema.build_errors if x.severity == ErrorSeverity.ERROR])
    # non_fatal_build_errors = len(schema.build_errors) - fatal_build_errors
    total_validation_errors = sum(len(v) for k,v in validation_errors.items())
        

    if not schema.built_ok:
        logging.warning(f"Schema had {len(schema.build_errors) } build errors. Exiting with code {EXIT_BUILD_ERRORS}")
        exit(EXIT_BUILD_ERRORS)
    if total_validation_errors > 0:
        logging.warning(f"Schema built OK but there were {total_validation_errors} validation errors in instance documents. Exiting with code {EXIT_VALIDATION_ERRORS}")
        exit(EXIT_VALIDATION_ERRORS)

    exit(EXIT_OK)