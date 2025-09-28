from __future__ import annotations
import ast
from typing import Tuple, TypeVar, Iterable
from func_adl import ObjectStream, func_adl_callback, func_adl_parameterized_call
from enum import Enum
import func_adl_servicex_xaodr25

_method_map = {
    'isValid': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'isValid',
        'return_type': 'bool',
    },
    'empty': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'empty',
        'return_type': 'bool',
    },
    'size': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'size',
        'return_type': 'unsigned int',
    },
    'begin': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'begin',
        'return_type': 'xAOD::JetConstituentVector::iterator',
    },
    'end': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'end',
        'return_type': 'xAOD::JetConstituentVector::iterator',
    },
    'at': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'at',
        'return_type': 'xAOD::JetConstituent',
    },
    'front': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'front',
        'return_type': 'xAOD::JetConstituent',
    },
    'back': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'back',
        'return_type': 'xAOD::JetConstituent',
    },
    'asSTLVector': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::JetConstituentVector',
        'method_name': 'asSTLVector',
        'return_type_element': 'xAOD::JetConstituent',
        'return_type_collection': 'vector<xAOD::JetConstituent>',
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


        for md in _enum_function_map.get(a.func.attr, []):
            s_update = s_update.MetaData(md)
        return s_update, a
    else:
        return s, a


@func_adl_callback(_add_method_metadata)
class JetConstituentVector(Iterable[func_adl_servicex_xaodr25.xAOD.jetconstituent.JetConstituent]):
    "A class"


    def isValid(self) -> bool:
        "A method"
        ...

    def empty(self) -> bool:
        "A method"
        ...

    def size(self) -> int:
        "A method"
        ...

    def begin(self) -> func_adl_servicex_xaodr25.xAOD.JetConstituentVector.iterator.iterator:
        "A method"
        ...

    def end(self) -> func_adl_servicex_xaodr25.xAOD.JetConstituentVector.iterator.iterator:
        "A method"
        ...

    def at(self, i: int) -> func_adl_servicex_xaodr25.xAOD.jetconstituent.JetConstituent:
        "A method"
        ...

    def front(self) -> func_adl_servicex_xaodr25.xAOD.jetconstituent.JetConstituent:
        "A method"
        ...

    def back(self) -> func_adl_servicex_xaodr25.xAOD.jetconstituent.JetConstituent:
        "A method"
        ...

    def asSTLVector(self) -> func_adl_servicex_xaodr25.vector_xaod_jetconstituent_.vector_xAOD_JetConstituent_:
        "A method"
        ...
