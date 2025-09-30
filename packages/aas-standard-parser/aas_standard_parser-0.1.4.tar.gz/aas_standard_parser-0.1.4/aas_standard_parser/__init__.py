from datetime import datetime
import importlib.metadata

__copyright__ = f"Copyright (C) {datetime.now().year} :em engineering methods AG. All rights reserved."
__author__ = "Daniel Klein"

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0-dev"
    
__project__ = "aas-standard-parser"
__package__ = "aas-standard-parser"

from aas_standard_parser.aid_parser import AIDParser
from aas_standard_parser.aimc_parser import AIMCParser


__all__ = ["AIDParser", "AIMCParser"]