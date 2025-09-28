from __future__ import annotations
import ast
from typing import Tuple, TypeVar, Iterable
from func_adl import ObjectStream, func_adl_callback, func_adl_parameterized_call
from enum import Enum
import func_adl_servicex_xaodr25

_method_map = {
    'eta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'eta',
        'return_type': 'float',
    },
    'globalEta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'globalEta',
        'return_type': 'int',
    },
    'phi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'phi',
        'return_type': 'float',
    },
    'globalPhi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'globalPhi',
        'return_type': 'unsigned int',
    },
    'module': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'module',
        'return_type': 'uint8_t',
    },
    'fpga': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'fpga',
        'return_type': 'uint8_t',
    },
    'channel': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'channel',
        'return_type': 'uint8_t',
    },
    'et_count': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'et_count',
        'return_type_element': 'unsigned short',
        'return_type_collection': 'const vector<unsigned short>',
    },
    'jFEXdataID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'jFEXdataID',
        'return_type': 'uint8_t',
    },
    'isjTowerSat': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'isjTowerSat',
        'return_type_element': 'unsigned short',
        'return_type_collection': 'const vector<char>',
    },
    'jFEXtowerID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'jFEXtowerID',
        'return_type': 'unsigned int',
    },
    'Calosource': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'Calosource',
        'return_type': 'uint8_t',
    },
    'jTowerEt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'jTowerEt',
        'return_type': 'uint16_t',
    },
    'isCore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'isCore',
        'return_type': 'bool',
    },
    'OnlineID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'OnlineID',
        'return_type': 'int',
    },
    'OfflineID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'OfflineID',
        'return_type': 'int',
    },
    'SCellEt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellEt',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'SCellEta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellEta',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'SCellPhi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellPhi',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'SCellID': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellID',
        'return_type_element': 'unsigned short',
        'return_type_collection': 'const vector<int>',
    },
    'SCellMask': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellMask',
        'return_type_element': 'bool',
        'return_type_collection': 'const vector<bool>',
    },
    'TileEt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'TileEt',
        'return_type': 'int',
    },
    'TileEta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'TileEta',
        'return_type': 'float',
    },
    'TilePhi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'TilePhi',
        'return_type': 'float',
    },
    'jtowerEtMeV': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'jtowerEtMeV',
        'return_type': 'int',
    },
    'SCellEtMeV': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'SCellEtMeV',
        'return_type': 'float',
    },
    'TileEtMeV': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'TileEtMeV',
        'return_type': 'float',
    },
    'emulated_jtowerEt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'emulated_jtowerEt',
        'return_type': 'int',
    },
    'index': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'index',
        'return_type': 'unsigned int',
    },
    'usingPrivateStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'usingPrivateStore',
        'return_type': 'bool',
    },
    'usingStandaloneStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'usingStandaloneStore',
        'return_type': 'bool',
    },
    'hasStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'hasStore',
        'return_type': 'bool',
    },
    'hasNonConstStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'hasNonConstStore',
        'return_type': 'bool',
    },
    'clearDecorations': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'clearDecorations',
        'return_type': 'bool',
    },
    'trackIndices': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'trackIndices',
        'return_type': 'bool',
    },
    'auxdataConst': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
        'method_name': 'auxdataConst',
        'return_type': 'U',
    },
    'isAvailable': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::jFexTower_v1',
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
            'name': 'xAODTrigL1Calo/versions/jFexTower_v1.h',
            'body_includes': ["xAODTrigL1Calo/versions/jFexTower_v1.h"],
        })


        s_update = s_update.MetaData({
            'metadata_type': 'inject_code',
            'name': 'xAODTrigL1Calo',
            'link_libraries': ["xAODTrigL1Calo"],
        })

        for md in _enum_function_map.get(a.func.attr, []):
            s_update = s_update.MetaData(md)
        return s_update, a
    else:
        return s, a


@func_adl_callback(_add_method_metadata)
class jFexTower_v1:
    "A class"


    def eta(self) -> float:
        "A method"
        ...

    def globalEta(self) -> int:
        "A method"
        ...

    def phi(self) -> float:
        "A method"
        ...

    def globalPhi(self) -> int:
        "A method"
        ...

    def module(self) -> int:
        "A method"
        ...

    def fpga(self) -> int:
        "A method"
        ...

    def channel(self) -> int:
        "A method"
        ...

    def et_count(self) -> func_adl_servicex_xaodr25.vector_int_.vector_int_:
        "A method"
        ...

    def jFEXdataID(self) -> int:
        "A method"
        ...

    def isjTowerSat(self) -> func_adl_servicex_xaodr25.vector_int_.vector_int_:
        "A method"
        ...

    def jFEXtowerID(self) -> int:
        "A method"
        ...

    def Calosource(self) -> int:
        "A method"
        ...

    def jTowerEt(self) -> int:
        "A method"
        ...

    def isCore(self) -> bool:
        "A method"
        ...

    def OnlineID(self) -> int:
        "A method"
        ...

    def OfflineID(self) -> int:
        "A method"
        ...

    def SCellEt(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def SCellEta(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def SCellPhi(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def SCellID(self) -> func_adl_servicex_xaodr25.vector_int_.vector_int_:
        "A method"
        ...

    def SCellMask(self) -> func_adl_servicex_xaodr25.vector_bool_.vector_bool_:
        "A method"
        ...

    def TileEt(self) -> int:
        "A method"
        ...

    def TileEta(self) -> float:
        "A method"
        ...

    def TilePhi(self) -> float:
        "A method"
        ...

    def jtowerEtMeV(self) -> int:
        "A method"
        ...

    def SCellEtMeV(self) -> float:
        "A method"
        ...

    def TileEtMeV(self) -> float:
        "A method"
        ...

    def emulated_jtowerEt(self) -> int:
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
