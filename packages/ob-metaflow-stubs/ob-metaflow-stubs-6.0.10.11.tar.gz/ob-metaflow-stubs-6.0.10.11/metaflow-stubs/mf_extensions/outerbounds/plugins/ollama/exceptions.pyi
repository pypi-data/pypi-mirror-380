######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.18.7.5+obcheckpoint(0.2.7);ob(v1)                                                    #
# Generated on 2025-09-29T21:43:14.573553                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.exception

from .....exception import MetaflowException as MetaflowException

class UnspecifiedRemoteStorageRootException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, message):
        ...
    ...

class EmptyOllamaManifestCacheException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, message):
        ...
    ...

class EmptyOllamaBlobCacheException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, message):
        ...
    ...

