from __future__ import annotations
import ast
from typing import Tuple, TypeVar, Iterable
from func_adl import ObjectStream, func_adl_callback, func_adl_parameterized_call
from enum import Enum
import func_adl_servicex_xaodr25

_method_map = {
    'z0_pt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'z0_pt',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'eta_phi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'eta_phi',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'z0Bins': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'z0Bins',
        'return_type': 'unsigned int',
    },
    'z0Min': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'z0Min',
        'return_type': 'float',
    },
    'z0Max': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'z0Max',
        'return_type': 'float',
    },
    'ptBins': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'ptBins',
        'return_type': 'unsigned int',
    },
    'ptMin': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'ptMin',
        'return_type': 'float',
    },
    'ptMax': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'ptMax',
        'return_type': 'float',
    },
    'etaBins': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'etaBins',
        'return_type': 'unsigned int',
    },
    'etaMin': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'etaMin',
        'return_type': 'float',
    },
    'etaMax': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'etaMax',
        'return_type': 'float',
    },
    'phiBins': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'phiBins',
        'return_type': 'unsigned int',
    },
    'phiMin': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'phiMin',
        'return_type': 'float',
    },
    'phiMax': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'phiMax',
        'return_type': 'float',
    },
    'z0_ptSumEntries': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'z0_ptSumEntries',
        'return_type': 'double',
    },
    'eta_phiSumEntries': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'eta_phiSumEntries',
        'return_type': 'double',
    },
    'index': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'index',
        'return_type': 'unsigned int',
    },
    'usingPrivateStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'usingPrivateStore',
        'return_type': 'bool',
    },
    'usingStandaloneStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'usingStandaloneStore',
        'return_type': 'bool',
    },
    'hasStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'hasStore',
        'return_type': 'bool',
    },
    'hasNonConstStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'hasNonConstStore',
        'return_type': 'bool',
    },
    'clearDecorations': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'clearDecorations',
        'return_type': 'bool',
    },
    'trackIndices': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'trackIndices',
        'return_type': 'bool',
    },
    'auxdataConst': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
        'method_name': 'auxdataConst',
        'return_type': 'U',
    },
    'isAvailable': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::TrigTrackCounts_v1',
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
            'name': 'xAODTrigMinBias/versions/TrigTrackCounts_v1.h',
            'body_includes': ["xAODTrigMinBias/versions/TrigTrackCounts_v1.h"],
        })


        s_update = s_update.MetaData({
            'metadata_type': 'inject_code',
            'name': 'xAODTrigMinBias',
            'link_libraries': ["xAODTrigMinBias"],
        })

        for md in _enum_function_map.get(a.func.attr, []):
            s_update = s_update.MetaData(md)
        return s_update, a
    else:
        return s, a


@func_adl_callback(_add_method_metadata)
class TrigTrackCounts_v1:
    "A class"


    def z0_pt(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def eta_phi(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def z0Bins(self) -> int:
        "A method"
        ...

    def z0Min(self) -> float:
        "A method"
        ...

    def z0Max(self) -> float:
        "A method"
        ...

    def ptBins(self) -> int:
        "A method"
        ...

    def ptMin(self) -> float:
        "A method"
        ...

    def ptMax(self) -> float:
        "A method"
        ...

    def etaBins(self) -> int:
        "A method"
        ...

    def etaMin(self) -> float:
        "A method"
        ...

    def etaMax(self) -> float:
        "A method"
        ...

    def phiBins(self) -> int:
        "A method"
        ...

    def phiMin(self) -> float:
        "A method"
        ...

    def phiMax(self) -> float:
        "A method"
        ...

    def z0_ptSumEntries(self, value_x: float, value_y: float, cutType: int) -> float:
        "A method"
        ...

    def eta_phiSumEntries(self, value_x: float, value_y: float, cutType: int) -> float:
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
