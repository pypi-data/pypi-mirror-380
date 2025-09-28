from __future__ import annotations
import ast
from typing import Tuple, TypeVar, Iterable
from func_adl import ObjectStream, func_adl_callback, func_adl_parameterized_call
from enum import Enum
import func_adl_servicex_xaodr25

_method_map = {
    'type': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'type',
        'return_type': 'xAODType::ObjectType',
    },
    'x': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'x',
        'return_type': 'float',
    },
    'y': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'y',
        'return_type': 'float',
    },
    'z': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'z',
        'return_type': 'float',
    },
    'time': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'time',
        'return_type': 'float',
    },
    'timeResolution': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'timeResolution',
        'return_type': 'float',
    },
    'hasValidTime': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'hasValidTime',
        'return_type': 'uint8_t',
    },
    'covariance': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'covariance',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'chiSquared': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'chiSquared',
        'return_type': 'float',
    },
    'numberDoF': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'numberDoF',
        'return_type': 'float',
    },
    'vertexType': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'vertexType',
        'return_type': 'xAOD::VxType::VertexType',
    },
    'trackParticleLinks': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'trackParticleLinks',
        'return_type_element': 'ElementLink<DataVector<xAOD::TrackParticle_v1>>',
        'return_type_collection': 'const vector<ElementLink<DataVector<xAOD::TrackParticle_v1>>>',
    },
    'trackWeights': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'trackWeights',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'neutralParticleLinks': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'neutralParticleLinks',
        'return_type_element': 'ElementLink<DataVector<xAOD::NeutralParticle_v1>>',
        'return_type_collection': 'const vector<ElementLink<DataVector<xAOD::NeutralParticle_v1>>>',
    },
    'neutralWeights': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'neutralWeights',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'trackParticle': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'trackParticle',
        'return_type': 'const xAOD::TrackParticle_v1 *',
    },
    'trackWeight': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'trackWeight',
        'return_type': 'float',
    },
    'nTrackParticles': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'nTrackParticles',
        'return_type': 'unsigned int',
    },
    'neutralParticle': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'neutralParticle',
        'return_type': 'const xAOD::NeutralParticle_v1 *',
    },
    'neutralWeight': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'neutralWeight',
        'return_type': 'float',
    },
    'nNeutralParticles': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'nNeutralParticles',
        'return_type': 'unsigned int',
    },
    'index': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'index',
        'return_type': 'unsigned int',
    },
    'usingPrivateStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'usingPrivateStore',
        'return_type': 'bool',
    },
    'usingStandaloneStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'usingStandaloneStore',
        'return_type': 'bool',
    },
    'hasStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'hasStore',
        'return_type': 'bool',
    },
    'hasNonConstStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'hasNonConstStore',
        'return_type': 'bool',
    },
    'clearDecorations': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'clearDecorations',
        'return_type': 'bool',
    },
    'trackIndices': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'trackIndices',
        'return_type': 'bool',
    },
    'auxdataConst': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'auxdataConst',
        'return_type': 'U',
    },
    'isAvailable': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::Vertex_v1',
        'method_name': 'isAvailable',
        'return_type': 'bool',
    },
}

_enum_function_map = {
    'type': [
        {
            'metadata_type': 'define_enum',
            'namespace': 'xAODType',
            'name': 'ObjectType',
            'values': [
                'Other',
                'CaloCluster',
                'Jet',
                'ParticleFlow',
                'TrackParticle',
                'NeutralParticle',
                'Electron',
                'Photon',
                'Muon',
                'Tau',
                'TrackCaloCluster',
                'FlowElement',
                'Vertex',
                'BTag',
                'TruthParticle',
                'TruthVertex',
                'TruthEvent',
                'TruthPileupEvent',
                'L2StandAloneMuon',
                'L2IsoMuon',
                'L2CombinedMuon',
                'TrigElectron',
                'TrigPhoton',
                'TrigCaloCluster',
                'TrigEMCluster',
                'EventInfo',
                'EventFormat',
                'Particle',
                'CompositeParticle',
            ],
        },
    ],
    'vertexType': [
        {
            'metadata_type': 'define_enum',
            'namespace': 'xAOD.VxType',
            'name': 'VertexType',
            'values': [
                'NoVtx',
                'PriVtx',
                'SecVtx',
                'PileUp',
                'ConvVtx',
                'V0Vtx',
                'KinkVtx',
                'NotSpecified',
            ],
        },
    ],      
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
            'name': 'xAODTracking/versions/Vertex_v1.h',
            'body_includes': ["xAODTracking/versions/Vertex_v1.h"],
        })


        s_update = s_update.MetaData({
            'metadata_type': 'inject_code',
            'name': 'xAODTracking',
            'link_libraries': ["xAODTracking"],
        })

        for md in _enum_function_map.get(a.func.attr, []):
            s_update = s_update.MetaData(md)
        return s_update, a
    else:
        return s, a


@func_adl_callback(_add_method_metadata)
class Vertex_v1:
    "A class"


    def type(self) -> func_adl_servicex_xaodr25.xaodtype.xAODType.ObjectType:
        "A method"
        ...

    def x(self) -> float:
        "A method"
        ...

    def y(self) -> float:
        "A method"
        ...

    def z(self) -> float:
        "A method"
        ...

    def time(self) -> float:
        "A method"
        ...

    def timeResolution(self) -> float:
        "A method"
        ...

    def hasValidTime(self) -> int:
        "A method"
        ...

    def covariance(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def chiSquared(self) -> float:
        "A method"
        ...

    def numberDoF(self) -> float:
        "A method"
        ...

    def vertexType(self) -> func_adl_servicex_xaodr25.xAOD.vxtype.VxType.VertexType:
        "A method"
        ...

    def trackParticleLinks(self) -> func_adl_servicex_xaodr25.vector_elementlink_datavector_xaod_trackparticle_v1___.vector_ElementLink_DataVector_xAOD_TrackParticle_v1___:
        "A method"
        ...

    def trackWeights(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def neutralParticleLinks(self) -> func_adl_servicex_xaodr25.vector_elementlink_datavector_xaod_neutralparticle_v1___.vector_ElementLink_DataVector_xAOD_NeutralParticle_v1___:
        "A method"
        ...

    def neutralWeights(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def trackParticle(self, i: int) -> func_adl_servicex_xaodr25.xAOD.trackparticle_v1.TrackParticle_v1:
        "A method"
        ...

    def trackWeight(self, i: int) -> float:
        "A method"
        ...

    def nTrackParticles(self) -> int:
        "A method"
        ...

    def neutralParticle(self, i: int) -> func_adl_servicex_xaodr25.xAOD.neutralparticle_v1.NeutralParticle_v1:
        "A method"
        ...

    def neutralWeight(self, i: int) -> float:
        "A method"
        ...

    def nNeutralParticles(self) -> int:
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
