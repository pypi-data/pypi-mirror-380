from __future__ import annotations
from . import ScratchValue, ScratchVariable, ScratchList
from . import uid as get_uid
from enum import Enum, StrEnum
import json

class StackBlock():
    def __init__(self, op: str, ins: dict[str, BlockInput | list], fields: dict[str, list], top: bool = False, substack: SubStack | None = None, substack2: SubStack | None = None):
        self.opcode = op
        self.ins = ins
        self.fields = fields
        self.top = top
        self.uid = get_uid()
        self.substack = substack
        self.substack2 = substack2
        self.parentuid = None
        self.nextuid = None
        self.shadow = False
        self.mutation: dict | None = None
        if self.substack:
            self.ins["SUBSTACK"] = [2, self.substack.stack_blocks[0].uid]
            self.substack.stack_blocks[0].parentuid = self.uid
        if self.substack2:
            self.ins["SUBSTACK2"] = [2, self.substack2.stack_blocks[0].uid]
            self.substack2.stack_blocks[0].parentuid = self.uid
    def __iter__(self):
        yield ("opcode", self.opcode)
        yield ("next", self.nextuid)
        yield ("parent", self.parentuid)
        try:
            yield ("inputs", dict([(k, list(v)) for k, v in self.ins.items()]))
        except TypeError as e:
            print(self.ins.items())
            print(f"Caught type error in input assignment during block creation: {e}")
            yield ("inputs", {})
        yield ("fields", self.fields)
        yield ("shadow", self.shadow)
        yield ("topLevel", self.top)
        if self.mutation:
            yield ("mutation", self.mutation)

class OpBlock(StackBlock):
    def __init__(self, op, ins, fields, top = False, substack = None, substack2 = None):
        super().__init__(op, ins, fields, top, substack, substack2)

class SubStack():
    def __init__(self):
        self.stack_blocks: list[StackBlock] = []
        self.op_blocks: list[OpBlock] = []
    def push_stack(self, block: StackBlock):
        self.stack_blocks.append(block)
    def push_op(self, block: OpBlock):
        self.op_blocks.append(block)
        return block
    def __iter__(self):
        for i in range(len(self.stack_blocks)):
            x = self.stack_blocks[i]
            try:
                x.nextuid = self.stack_blocks[i+1].uid
            except IndexError:
                pass
            try:
                x.parentuid = self.stack_blocks[i-1].uid
            except IndexError:
                pass
            yield (x.uid, dict(x))
        for i in range(len(self.op_blocks)):
            x = self.op_blocks[i]
            yield (x.uid, dict(x))

class Script(SubStack):
    def __init__(self, start: StackBlock):
        super().__init__()
        self.stack_blocks.append(start)

class BlockInput():
    def __init__(self, data: ScratchValue | ScratchVariable | ScratchList | OpBlock, shadow: bool | int, default: ScratchValue | None = None):
        self.data = data
        self.shadow = shadow
        if default is None and not isinstance(self.data, OpBlock):
            self.shadow_default = ScratchValue("")
            if isinstance(self.data, OpBlock):
                if isinstance(self.data.val, int):
                    self.shadow_default = ScratchValue(0)
        else:
            self.shadow_default = default
    def __iter__(self):
        if isinstance(self.shadow, bool):
            shadow = 1 if self.shadow else 2
            if self.shadow_default and shadow == 2:
                shadow = 3
        else:
            shadow = self.shadow
        yield shadow
        if isinstance(self.data, ScratchValue):
            if isinstance(self.data.val, int):
                yield [4, self.data.val]
            else:
                yield [10, str(self.data)]
        elif isinstance(self.data, ScratchVariable):
            yield [12, self.data.name, self.data.uid]
        elif isinstance(self.data, ScratchList):
            yield [13, self.data.name, self.data.uid]
        elif isinstance(self.data, OpBlock):
            newblock = self.data
            yield newblock.uid
        if shadow == 3 and not isinstance(self.data, ScratchValue):
            if not isinstance(self.data, OpBlock) and isinstance(self.data.val, int):
                yield [4, self.shadow_default.val]
            else:
                yield [10, str(self.shadow_default)]

class ProcedureInputType(StrEnum):
    STRING_NUMBER = "argument_reporter_string_number"
    BOOLEAN = "argument_reporter_boolean"

class ProcedureInput():
    def __init__(self, name: str, intype = ProcedureInputType.STRING_NUMBER):
        self.uid = get_uid()
        self.name = name
        self.intype: ProcedureInputType = intype
    def as_op(self):
        return OpBlock(self.intype, {}, {"VALUE": [self.name, None]})

class Procedure():
    def __init__(self, name: str, inputs: list[ProcedureInput] = [], warp: bool = False):
        ins = {}
        prototype_stack = SubStack()
        proccode = [name]
        argids = []
        argnames = []
        argdef = []
        for x in inputs:
            asop = x.as_op()
            ins[x.uid] = [1, prototype_stack.push_op(asop).uid]
            argids.append(x.uid)
            argnames.append(x.name)
            if x.intype is ProcedureInputType.STRING_NUMBER:
                proccode.append("%s")
                argdef.append("")
            elif x.intype is ProcedureInputType.BOOLEAN:
                proccode.append("%b")
                argdef.append("false")
        proccode = " ".join(proccode)
        self.proccode = proccode
        prototype = StackBlock("procedures_prototype", ins=ins, fields={})
        prototype.shadow = True
        self.mutation = {"tagName": "mutation",
                              "children": [],
                              "proccode": self.proccode,
                              "argumentids": json.dumps(argids),
                              "argumentnames": json.dumps(argnames),
                              "argumentdefaults": json.dumps(argdef),
                              "warp": json.dumps(warp)}
        prototype.mutation = self.mutation
        prototype_stack.push_stack(prototype)

        definition = Script(StackBlock("procedures_definition", {"custom_block": [1, prototype.uid]}, {}, top=True))

        self.definition = definition
        self.prototype = prototype_stack
        self.arguments = inputs
    def call_proc(self, ins: dict[ProcedureInput, list]):
        block = StackBlock("procedures_call", dict([(k.uid, v) for k, v in ins.items()]), {})
        block.mutation = self.mutation
        return block
