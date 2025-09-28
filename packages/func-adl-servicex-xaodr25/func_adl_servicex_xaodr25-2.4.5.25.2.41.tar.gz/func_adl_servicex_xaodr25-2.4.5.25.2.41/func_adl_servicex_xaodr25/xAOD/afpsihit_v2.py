from __future__ import annotations
import ast
from typing import Tuple, TypeVar, Iterable
from func_adl import ObjectStream, func_adl_callback, func_adl_parameterized_call
from enum import Enum
import func_adl_servicex_xaodr25

_method_map = {
    'depositedCharge': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'depositedCharge',
        'return_type': 'float',
    },
    'timeOverThreshold': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'timeOverThreshold',
        'return_type': 'float',
    },
    'stationID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'stationID',
        'return_type': 'int',
    },
    'pixelLayerID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'pixelLayerID',
        'return_type': 'int',
    },
    'pixelRowIDChip': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'pixelRowIDChip',
        'return_type': 'int',
    },
    'pixelColIDChip': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'pixelColIDChip',
        'return_type': 'int',
    },
    'pixelHorizID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'pixelHorizID',
        'return_type': 'int',
    },
    'pixelVertID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'pixelVertID',
        'return_type': 'int',
    },
    'index': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'index',
        'return_type': 'unsigned int',
    },
    'usingPrivateStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'usingPrivateStore',
        'return_type': 'bool',
    },
    'usingStandaloneStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'usingStandaloneStore',
        'return_type': 'bool',
    },
    'hasStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'hasStore',
        'return_type': 'bool',
    },
    'hasNonConstStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'hasNonConstStore',
        'return_type': 'bool',
    },
    'clearDecorations': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'clearDecorations',
        'return_type': 'bool',
    },
    'trackIndices': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'trackIndices',
        'return_type': 'bool',
    },
    'auxdataConst': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'auxdataConst',
        'return_type': 'U',
    },
    'isAvailable': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::AFPSiHit_v2',
        'method_name': 'isAvailable',
        'return_type': 'bool',
    },
}

_enum_function_map = {      
}

_defined_enums = {      
}

_object_cpp_as_py_namespace="xAOD"

T = TypeVar('T')

def add_enum_info(s: ObjectStream[T], enum_name: str) -> ObjectStream[T]:
    '''Use this to add enum definition information to the backend.

    This can be used when you are writing a C++ function that needs to
    make sure a particular enum is defined.

    Args:
        s (ObjectStream[T]): The ObjectStream that is being updated
        enum_name (str): Name of the enum

    Raises:
        ValueError: If it is not known, a list of possibles is printed out

    Returns:
        ObjectStream[T]: Updated object stream with new metadata.
    '''
    if enum_name not in _defined_enums:
        raise ValueError(f"Enum {enum_name} is not known - "
                            f"choose from one of {','.join(_defined_enums.keys())}")
    return s.MetaData(_defined_enums[enum_name])

def _add_method_metadata(s: ObjectStream[T], a: ast.Call) -> Tuple[ObjectStream[T], ast.Call]:
    '''Add metadata for a collection to the func_adl stream if we know about it
    '''
    assert isinstance(a.func, ast.Attribute)
    if a.func.attr in _method_map:
        s_update = s.MetaData(_method_map[a.func.attr])

        s_update = s_update.MetaData({
            'metadata_type': 'inject_code',
            'name': 'xAODForward/versions/AFPSiHit_v2.h',
            'body_includes': ["xAODForward/versions/AFPSiHit_v2.h"],
        })


        s_update = s_update.MetaData({
            'metadata_type': 'inject_code',
            'name': 'xAODForward',
            'link_libraries': ["xAODForward"],
        })

        for md in _enum_function_map.get(a.func.attr, []):
            s_update = s_update.MetaData(md)
        return s_update, a
    else:
        return s, a


@func_adl_callback(_add_method_metadata)
class AFPSiHit_v2:
    "A class"


    def depositedCharge(self) -> float:
        "A method"
        ...

    def timeOverThreshold(self) -> float:
        "A method"
        ...

    def stationID(self) -> int:
        "A method"
        ...

    def pixelLayerID(self) -> int:
        "A method"
        ...

    def pixelRowIDChip(self) -> int:
        "A method"
        ...

    def pixelColIDChip(self) -> int:
        "A method"
        ...

    def pixelHorizID(self) -> int:
        "A method"
        ...

    def pixelVertID(self) -> int:
        "A method"
        ...

    def index(self) -> int:
        "A method"
        ...

    def usingPrivateStore(self) -> bool:
        "A method"
        ...

    def usingStandaloneStore(self) -> bool:
        "A method"
        ...

    def hasStore(self) -> bool:
        "A method"
        ...

    def hasNonConstStore(self) -> bool:
        "A method"
        ...

    def clearDecorations(self) -> bool:
        "A method"
        ...

    def trackIndices(self) -> bool:
        "A method"
        ...

    @func_adl_parameterized_call(lambda s, a, param_1: func_adl_servicex_xaodr25.type_support.cpp_generic_1arg_callback('auxdataConst', s, a, param_1))
    @property
    def auxdataConst(self) -> func_adl_servicex_xaodr25.type_support.index_type_forwarder[str]:
        "A method"
        ...

    @func_adl_parameterized_call(lambda s, a, param_1: func_adl_servicex_xaodr25.type_support.cpp_generic_1arg_callback('isAvailable', s, a, param_1))
    @property
    def isAvailable(self) -> func_adl_servicex_xaodr25.type_support.index_type_forwarder[str]:
        "A method"
        ...
