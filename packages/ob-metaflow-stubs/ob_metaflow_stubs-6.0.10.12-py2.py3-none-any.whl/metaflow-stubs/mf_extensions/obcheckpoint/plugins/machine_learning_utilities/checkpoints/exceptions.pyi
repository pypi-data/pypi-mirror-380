######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.18.9.1+obcheckpoint(0.2.8);ob(v1)                                                    #
# Generated on 2025-09-30T17:31:30.260124                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.exception

from ......exception import MetaflowException as MetaflowException

class CheckpointNotAvailableException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, message):
        ...
    ...

class CheckpointException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, message):
        ...
    ...

