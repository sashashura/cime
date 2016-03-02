"""
Interface to the env_case.xml file.  This class inherits from EnvBase
"""
from standard_module_setup import *

from env_base import EnvBase

logger = logging.getLogger(__name__)

class EnvCase(EnvBase):
    def __init__(self, case_root=os.getcwd(), infile="env_case.xml"):
        """
        initialize an object interface to file env_case.xml in the case directory
        """
        EnvBase.__init__(self, case_root, infile)
