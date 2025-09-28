from __future__ import annotations
import ast
from typing import Tuple, TypeVar, Iterable
from func_adl import ObjectStream, func_adl_callback, func_adl_parameterized_call
from enum import Enum
import func_adl_servicex_xaodr25

_method_map = {
    'HaveCoordErrors': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'HaveCoordErrors',
        'return_type': 'bool',
    },
    'HaveAsymErrors': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'HaveAsymErrors',
        'return_type': 'bool',
    },
    'LogTransform': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'LogTransform',
        'return_type': 'ROOT::Fit::BinData',
    },
    'Value': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'Value',
        'return_type': 'double',
    },
    'ValuePtr': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'ValuePtr',
        'return_type': 'const double *',
    },
    'ErrorPtr': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'ErrorPtr',
        'return_type': 'const double *',
    },
    'Error': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'Error',
        'return_type': 'double',
    },
    'InvError': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'InvError',
        'return_type': 'double',
    },
    'GetPoint': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'GetPoint',
        'return_type': 'const double *',
    },
    'GetCoordErrorComponent': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'GetCoordErrorComponent',
        'return_type': 'double',
    },
    'CoordErrors': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'CoordErrors',
        'return_type': 'const double *',
    },
    'GetPointError': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'GetPointError',
        'return_type': 'const double *',
    },
    'GetBinUpEdgeComponent': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'GetBinUpEdgeComponent',
        'return_type': 'double',
    },
    'BinUpEdge': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'BinUpEdge',
        'return_type': 'const double *',
    },
    'HasBinEdges': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'HasBinEdges',
        'return_type': 'bool',
    },
    'RefVolume': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'RefVolume',
        'return_type': 'double',
    },
    'GetErrorType': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'GetErrorType',
        'return_type': 'ROOT::Fit::BinData::ErrorType',
    },
    'SumOfContent': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'SumOfContent',
        'return_type': 'double',
    },
    'SumOfError2': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'SumOfError2',
        'return_type': 'double',
    },
    'IsWeighted': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'IsWeighted',
        'return_type': 'bool',
    },
    'GetCoordComponent': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'GetCoordComponent',
        'return_type': 'const double *',
    },
    'Coords': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'Coords',
        'return_type': 'const double *',
    },
    'NPoints': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'NPoints',
        'return_type': 'unsigned int',
    },
    'Size': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'Size',
        'return_type': 'unsigned int',
    },
    'NDim': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'NDim',
        'return_type': 'unsigned int',
    },
    'Range': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'ROOT::Fit::BinData',
        'method_name': 'Range',
        'return_type': 'const ROOT::Fit::DataRange',
    },
}

_enum_function_map = {
    'GetErrorType': [
        {
            'metadata_type': 'define_enum',
            'namespace': 'ROOT.Fit.BinData',
            'name': 'ErrorType',
            'values': [
                'kNoError',
                'kValueError',
                'kCoordError',
                'kAsymError',
            ],
        },
    ],      
}

_defined_enums = {
    'ErrorType':
        {
            'metadata_type': 'define_enum',
            'namespace': 'ROOT.Fit.BinData',
            'name': 'ErrorType',
            'values': [
                'kNoError',
                'kValueError',
                'kCoordError',
                'kAsymError',
            ],
        },      
}

_object_cpp_as_py_namespace="ROOT.Fit"

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
class BinData:
    "A class"

    class ErrorType(Enum):
        kNoError = 0
        kValueError = 1
        kCoordError = 2
        kAsymError = 3


    def HaveCoordErrors(self) -> bool:
        "A method"
        ...

    def HaveAsymErrors(self) -> bool:
        "A method"
        ...

    def LogTransform(self) -> func_adl_servicex_xaodr25.ROOT.Fit.bindata.BinData:
        "A method"
        ...

    def Value(self, ipoint: int) -> float:
        "A method"
        ...

    def ValuePtr(self, ipoint: int) -> float:
        "A method"
        ...

    def ErrorPtr(self, ipoint: int) -> float:
        "A method"
        ...

    def Error(self, ipoint: int) -> float:
        "A method"
        ...

    def InvError(self, ipoint: int) -> float:
        "A method"
        ...

    def GetPoint(self, ipoint: int, value: float) -> float:
        "A method"
        ...

    def GetCoordErrorComponent(self, ipoint: int, icoord: int) -> float:
        "A method"
        ...

    def CoordErrors(self, ipoint: int) -> float:
        "A method"
        ...

    def GetPointError(self, ipoint: int, errvalue: float) -> float:
        "A method"
        ...

    def GetBinUpEdgeComponent(self, ipoint: int, icoord: int) -> float:
        "A method"
        ...

    def BinUpEdge(self, ipoint: int) -> float:
        "A method"
        ...

    def HasBinEdges(self) -> bool:
        "A method"
        ...

    def RefVolume(self) -> float:
        "A method"
        ...

    def GetErrorType(self) -> func_adl_servicex_xaodr25.ROOT.Fit.bindata.BinData.ErrorType:
        "A method"
        ...

    def SumOfContent(self) -> float:
        "A method"
        ...

    def SumOfError2(self) -> float:
        "A method"
        ...

    def IsWeighted(self) -> bool:
        "A method"
        ...

    def GetCoordComponent(self, ipoint: int, icoord: int) -> float:
        "A method"
        ...

    def Coords(self, ipoint: int) -> float:
        "A method"
        ...

    def NPoints(self) -> int:
        "A method"
        ...

    def Size(self) -> int:
        "A method"
        ...

    def NDim(self) -> int:
        "A method"
        ...

    def Range(self) -> func_adl_servicex_xaodr25.ROOT.Fit.datarange.DataRange:
        "A method"
        ...
