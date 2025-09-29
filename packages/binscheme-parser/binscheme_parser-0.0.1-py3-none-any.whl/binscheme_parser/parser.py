
from lark import Lark, Transformer, v_args
from pathlib import Path
from . import data_structures as ds

@v_args(inline=True)
class BinSchemeTransformer(Transformer):
    def __init__(self, schema_collection):
        self.schema_collection = schema_collection

    def start(self, *items):
        return self.schema_collection

    def definition(self, item):
        if isinstance(item, ds.Scheme):
            self.schema_collection.schemes[item.name] = item
        elif isinstance(item, ds.Enum):
            self.schema_collection.enums[item.name] = item
        elif isinstance(item, ds.Instance):
            self.schema_collection.instances[item.name] = item

    def enum(self, name, base_type, *fields):
        enum_obj = ds.Enum(name=name.value, base_type=base_type, values={})
        for field_name, value in fields:
            enum_obj.values[field_name.value] = int(value.value)
        return enum_obj

    def enum_field(self, name, value):
        return name, value

    def scheme(self, name, *items):
        scheme_obj = ds.Scheme(name=name.value)
        for item in items:
            if isinstance(item, ds.Field):
                scheme_obj.fields[item.name] = item
            elif isinstance(item, ds.ConditionalBlock):
                scheme_obj.conditional_blocks.append(item)
        return scheme_obj

    def field(self, type, name, value=None):
        default = None
        if value:
            if isinstance(value, str) and value.startswith('"'):
                default = value[1:-1]
            else:
                default = value
        return ds.Field(name=name.value, type=type, default=default)

    def conditional_block(self, block):
        return block

    def if_block(self, expr, *items):
        block = ds.ConditionalBlock(condition=expr, fields={})
        for item in items:
            if isinstance(item, ds.Field):
                block.fields[item.name] = item
        return block

    def else_if_block(self, expr, *items):
        block = ds.ConditionalBlock(condition=expr, fields={})
        for item in items:
            if isinstance(item, ds.Field):
                block.fields[item.name] = item
        return block

    def else_block(self, *items):
        block = ds.ConditionalBlock(condition=None, fields={})
        for item in items:
            if isinstance(item, ds.Field):
                block.fields[item.name] = item
        return block

    def expression(self, *args):
        result = args[0]
        for i in range(1, len(args), 2):
            op = args[i]
            right = args[i+1]
            result = (result, op.value, right)
        return result

    def term(self, *args):
        result = args[0]
        for i in range(1, len(args), 2):
            op = args[i]
            right = args[i+1]
            result = (result, op.value, right)
        return result

    def comparison(self, *args):
        result = args[0]
        for i in range(1, len(args), 2):
            op = args[i]
            right = args[i+1]
            result = (result, op.value, right)
        return result

    def primary(self, *parts):
        if len(parts) > 1:
            return ds.EnumMemberReference(path='.'.join(p.value for p in parts))
        elif isinstance(parts[0], ds.EnumMemberReference):
            return parts[0]
        elif hasattr(parts[0], 'value'):
            return parts[0].value
        else:
            return parts[0]

    def type(self, t):
        if not isinstance(t, ds.Type):
            if hasattr(t, 'type') and t.type == 'CNAME':
                return ds.SchemeType(name=t.value)
        return t

    def INTEGER_TYPE(self, t):
        val = t.value
        signed = not val.startswith('u')
        if not signed:
            val = val[1:]
        parts = val.split('_')
        endian = parts[1]
        bits = int(parts[0][3:])
        return ds.IntegerType(bits=bits, signed=signed, endian=endian)

    def FLOAT_TYPE(self, t):
        return ds.FloatType(bits=int(t.value[5:]))

    def BIT_TYPE(self, t):
        return ds.BitType(bits=int(t.value[3:]))

    def array_type(self, element_type, size):
        if hasattr(size, 'type') and size.type == 'CNAME':
            return ds.ArrayType(element_type=element_type, size=ds.FieldReference(path=size.value))
        return ds.ArrayType(element_type=element_type, size=int(size.value))

    def string_type(self, encoding, size):
        if hasattr(size, 'type') and size.type == 'CNAME':
            return ds.StringType(encoding=encoding.value, size=ds.FieldReference(path=size.value))
        return ds.StringType(encoding=encoding.value, size=int(size.value))

    def CNAME(self, name):
        return name

    def instance(self, scheme_name, instance_name, body):
        return ds.Instance(name=instance_name.value, scheme_name=scheme_name.value, values=body)

    def instance_body(self, *fields):
        return dict(fields)

    def instance_field(self, name, value):
        return name.value, value

    def value(self, *v):
        if len(v) == 1:
            v = v[0]
            if hasattr(v, 'type') and v.type == 'ESCAPED_STRING':
                return v.value[1:-1]
            if hasattr(v, 'type') and v.type == 'NUMBER':
                return int(v.value)
            return v
        else:
            return dict(v)

    def array_literal(self, *items):
        return list(items)


def load(file_path: str) -> ds.SchemaCollection:
    grammar_path = Path(__file__).parent / "binscheme.lark"
    with open(grammar_path, 'r') as f:
        grammar = f.read()

    parser = Lark(grammar, start='start')
    with open(file_path, 'r') as f:
        tree = parser.parse(f.read())

    schema_collection = ds.SchemaCollection()
    transformer = BinSchemeTransformer(schema_collection)
    result = transformer.transform(tree)
    return result
