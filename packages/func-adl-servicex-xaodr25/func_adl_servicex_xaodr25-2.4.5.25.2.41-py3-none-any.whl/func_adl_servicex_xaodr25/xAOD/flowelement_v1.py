from __future__ import annotations
import ast
from typing import Tuple, TypeVar, Iterable
from func_adl import ObjectStream, func_adl_callback, func_adl_parameterized_call
from enum import Enum
import func_adl_servicex_xaodr25

_method_map = {
    'pt': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'pt',
        'return_type': 'double',
    },
    'eta': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'eta',
        'return_type': 'double',
    },
    'phi': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'phi',
        'return_type': 'double',
    },
    'm': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'm',
        'return_type': 'double',
    },
    'e': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'e',
        'return_type': 'double',
    },
    'rapidity': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'rapidity',
        'return_type': 'double',
    },
    'p4': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'p4',
        'return_type': 'TLorentzVector',
    },
    'type': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'type',
        'return_type': 'xAODType::ObjectType',
    },
    'isMatchedToPV': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'isMatchedToPV',
        'return_type': 'bool',
    },
    'isCharged': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'isCharged',
        'return_type': 'bool',
    },
    'charge': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'charge',
        'return_type': 'float',
    },
    'nChargedObjects': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'nChargedObjects',
        'return_type': 'unsigned int',
    },
    'chargedObject': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'chargedObject',
        'return_type': 'const xAOD::IParticle *',
    },
    'chargedObjectLinks': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'chargedObjectLinks',
        'return_type_element': 'ElementLink<DataVector<xAOD::IParticle>>',
        'return_type_collection': 'const vector<ElementLink<DataVector<xAOD::IParticle>>>',
    },
    'chargedObjectWeights': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'chargedObjectWeights',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'nOtherObjects': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'nOtherObjects',
        'return_type': 'unsigned int',
    },
    'otherObject': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'otherObject',
        'return_type': 'const xAOD::IParticle *',
    },
    'otherObjectLinks': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'otherObjectLinks',
        'return_type_element': 'ElementLink<DataVector<xAOD::IParticle>>',
        'return_type_collection': 'const vector<ElementLink<DataVector<xAOD::IParticle>>>',
    },
    'otherObjectWeights': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'otherObjectWeights',
        'return_type_element': 'float',
        'return_type_collection': 'const vector<float>',
    },
    'index': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'index',
        'return_type': 'unsigned int',
    },
    'usingPrivateStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'usingPrivateStore',
        'return_type': 'bool',
    },
    'usingStandaloneStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'usingStandaloneStore',
        'return_type': 'bool',
    },
    'hasStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'hasStore',
        'return_type': 'bool',
    },
    'hasNonConstStore': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'hasNonConstStore',
        'return_type': 'bool',
    },
    'clearDecorations': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'clearDecorations',
        'return_type': 'bool',
    },
    'trackIndices': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'trackIndices',
        'return_type': 'bool',
    },
    'auxdataConst': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
        'method_name': 'auxdataConst',
        'return_type': 'U',
    },
    'isAvailable': {
        'metadata_type': 'add_method_type_info',
        'type_string': 'xAOD::FlowElement_v1',
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
    'isMatchedToPV': [
        {
            'metadata_type': 'define_enum',
            'namespace': 'xAOD.FlowElement_v1',
            'name': 'MatchedPVType',
            'values': [
                'Undefined',
                'HardScatter',
                'Pileup',
                'PileupSideBand',
            ],
        },
    ],      
}

_defined_enums = {
    'SignalType':
        {
            'metadata_type': 'define_enum',
            'namespace': 'xAOD.FlowElement_v1',
            'name': 'SignalType',
            'values': [
                'Neutral',
                'Charged',
                'Combined',
                'CaloCluster',
                'Track',
                'Muon',
                'PFlow',
                'NeutralPFlow',
                'ChargedPFlow',
                'TCC',
                'NeutralTCC',
                'ChargedTCC',
                'UFO',
                'NeutralUFO',
                'ChargedUFO',
                'Unknown',
            ],
        },
    'MatchedPVType':
        {
            'metadata_type': 'define_enum',
            'namespace': 'xAOD.FlowElement_v1',
            'name': 'MatchedPVType',
            'values': [
                'Undefined',
                'HardScatter',
                'Pileup',
                'PileupSideBand',
            ],
        },      
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
            'name': 'xAODPFlow/versions/FlowElement_v1.h',
            'body_includes': ["xAODPFlow/versions/FlowElement_v1.h"],
        })


        s_update = s_update.MetaData({
            'metadata_type': 'inject_code',
            'name': 'xAODPFlow',
            'link_libraries': ["xAODPFlow"],
        })

        for md in _enum_function_map.get(a.func.attr, []):
            s_update = s_update.MetaData(md)
        return s_update, a
    else:
        return s, a


@func_adl_callback(_add_method_metadata)
class FlowElement_v1:
    "A class"

    class SignalType(Enum):
        Neutral = 4096
        Charged = 8192
        Combined = 16384
        CaloCluster = 4352
        Track = 8704
        Muon = 9216
        PFlow = 16
        NeutralPFlow = 4112
        ChargedPFlow = 8208
        TCC = 32
        NeutralTCC = 4128
        ChargedTCC = 8224
        UFO = 1
        NeutralUFO = 4097
        ChargedUFO = 8193
        Unknown = 0

    class MatchedPVType(Enum):
        Undefined = 0
        HardScatter = 16
        Pileup = 32
        PileupSideBand = 33


    def pt(self) -> float:
        "A method"
        ...

    def eta(self) -> float:
        "A method"
        ...

    def phi(self) -> float:
        "A method"
        ...

    def m(self) -> float:
        "A method"
        ...

    def e(self) -> float:
        "A method"
        ...

    def rapidity(self) -> float:
        "A method"
        ...

    def p4(self) -> func_adl_servicex_xaodr25.tlorentzvector.TLorentzVector:
        "A method"
        ...

    def type(self) -> func_adl_servicex_xaodr25.xaodtype.xAODType.ObjectType:
        "A method"
        ...

    def isMatchedToPV(self, vxtype: func_adl_servicex_xaodr25.xAOD.flowelement_v1.FlowElement_v1.MatchedPVType) -> bool:
        "A method"
        ...

    def isCharged(self) -> bool:
        "A method"
        ...

    def charge(self) -> float:
        "A method"
        ...

    def nChargedObjects(self) -> int:
        "A method"
        ...

    def chargedObject(self, i: int) -> func_adl_servicex_xaodr25.xAOD.iparticle.IParticle:
        "A method"
        ...

    def chargedObjectLinks(self) -> func_adl_servicex_xaodr25.vector_elementlink_datavector_xaod_iparticle___.vector_ElementLink_DataVector_xAOD_IParticle___:
        "A method"
        ...

    def chargedObjectWeights(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
        "A method"
        ...

    def nOtherObjects(self) -> int:
        "A method"
        ...

    def otherObject(self, i: int) -> func_adl_servicex_xaodr25.xAOD.iparticle.IParticle:
        "A method"
        ...

    def otherObjectLinks(self) -> func_adl_servicex_xaodr25.vector_elementlink_datavector_xaod_iparticle___.vector_ElementLink_DataVector_xAOD_IParticle___:
        "A method"
        ...

    def otherObjectWeights(self) -> func_adl_servicex_xaodr25.vector_float_.vector_float_:
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
