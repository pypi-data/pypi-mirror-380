
import pytest
from pathlib import Path
import binscheme_parser
from binscheme_parser import data_structures as ds

@pytest.fixture
def network_scheme_path():
    return Path(__file__).parent / "fixtures" / "network.binscheme"

@pytest.fixture
def network_schema_collection(network_scheme_path):
    return binscheme_parser.load(network_scheme_path)

def test_load_network_scheme(network_schema_collection):
    assert network_schema_collection is not None
    assert len(network_schema_collection.schemes) == 2
    assert len(network_schema_collection.enums) == 1

def test_packet_type_enum(network_schema_collection):
    packet_type_enum = network_schema_collection.enums["PacketType"]
    assert packet_type_enum.name == "PacketType"
    assert isinstance(packet_type_enum.base_type, ds.IntegerType)
    assert packet_type_enum.base_type.bits == 8
    assert packet_type_enum.base_type.endian == "be"
    assert packet_type_enum.values["CHAT_MESSAGE"] == 1
    assert packet_type_enum.values["PLAYER_UPDATE"] == 2

def test_vec3_scheme(network_schema_collection):
    vec3_scheme = network_schema_collection.schemes["Vec3"]
    assert vec3_scheme.name == "Vec3"
    assert len(vec3_scheme.fields) == 3
    assert "x" in vec3_scheme.fields
    assert isinstance(vec3_scheme.fields["x"].type, ds.FloatType)

def test_packet_scheme(network_schema_collection):
    packet_scheme = network_schema_collection.schemes["Packet"]
    assert packet_scheme.name == "Packet"
    assert len(packet_scheme.fields) == 2
    assert "sequence_id" in packet_scheme.fields
    assert "type" in packet_scheme.fields
    assert len(packet_scheme.conditional_blocks) == 2

def test_conditional_blocks(network_schema_collection):
    packet_scheme = network_schema_collection.schemes["Packet"]
    
    # if block
    if_block = packet_scheme.conditional_blocks[0]
    assert if_block.condition is not None
    left, op, right = if_block.condition
    assert left == "type"
    assert op == "=="
    assert isinstance(right, ds.EnumMemberReference)
    assert right.path == "PacketType.CHAT_MESSAGE"
    assert "msg_len" in if_block.fields
    assert "message" in if_block.fields
    message_field = if_block.fields["message"]
    assert isinstance(message_field.type, ds.StringType)
    assert isinstance(message_field.type.size, ds.FieldReference)
    assert message_field.type.size.path == "msg_len"

    # else if block
    else_if_block = packet_scheme.conditional_blocks[1]
    assert else_if_block.condition is not None
    left, op, right = else_if_block.condition
    assert left == "type"
    assert op == "=="
    assert isinstance(right, ds.EnumMemberReference)
    assert right.path == "PacketType.PLAYER_UPDATE"
    assert "player_name" in else_if_block.fields
    assert "position" in else_if_block.fields
    assert "inventory_count" in else_if_block.fields
    assert "item_ids" in else_if_block.fields
    item_ids_field = else_if_block.fields["item_ids"]
    assert isinstance(item_ids_field.type, ds.ArrayType)
    assert isinstance(item_ids_field.type.size, ds.FieldReference)
    assert item_ids_field.type.size.path == "inventory_count"

def test_field_iteration(network_schema_collection):
    """Tests if we can iterate over all fields in a scheme, including conditionals."""
    
    # Add __iter__ to Scheme
    def scheme_iter(self):
        yield from self.fields.values()
        for block in self.conditional_blocks:
            yield from block.fields.values()
    ds.Scheme.__iter__ = scheme_iter

    packet_scheme = network_schema_collection.schemes["Packet"]
    field_names = {field.name for field in packet_scheme}
    expected_fields = {
        "sequence_id", "type", "msg_len", "message", 
        "player_name", "position", "inventory_count", "item_ids"
    }
    assert field_names == expected_fields
