__version__ = "1.8.7"

import yaml
from yamling.yaml_loaders import load_yaml, load_yaml_file, get_loader, YAMLInput
from yamling.load_universal import load, load_file
from yamling.yaml_dumpers import dump_yaml
from yamling.dump_universal import dump, dump_file
from yamling.yamlparser import YAMLParser
from yamling.exceptions import DumpingError, ParsingError
from yamling.typedefs import SupportedFormats, FormatType, LoaderType

YAMLError = yaml.YAMLError  # Reference for external libs that need to catch this error


__all__ = [
    "DumpingError",
    "FormatType",
    "LoaderType",
    "ParsingError",
    "SupportedFormats",
    "YAMLError",
    "YAMLInput",
    "YAMLParser",
    "dump",
    "dump_file",
    "dump_yaml",
    "get_loader",
    "load",
    "load_file",
    "load_yaml",
    "load_yaml_file",
]
