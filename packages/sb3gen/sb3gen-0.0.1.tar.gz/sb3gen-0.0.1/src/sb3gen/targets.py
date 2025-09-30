# Code for sb3 "targets", see https://en.scratch-wiki.info/wiki/Scratch_File_Format#Targets

from . import uid, ScratchValue, ScratchList, ScratchVariable, Broadcast, blocks

BLANKSVG = """<svg xmlns="http://www.w3.org/2000/svg" width="1" height="1"/>"""
BLANKSVGHASH = "ad97b1aa2e5e1ca965c8221e21f09341"

# Base class from which all targets are derived
class BaseTarget():
    def __init__(self):
        self.variables: list[ScratchVariable] = []
        self.lists: list[ScratchList] = []
        self.blocks: list[blocks.SubStack] = []
        # self.comments = [] #TODO: implement Comment object
    def __iter__(self):
        yield ("variables", dict([x.target_def_form() for x in self.variables]))
        yield ("lists", dict([x.target_def_form() for x in self.lists]))
        b = {}
        for x in self.blocks:
            b |= dict(x)
        yield ("blocks", b)
        yield ("comments", {})
        yield ("currentCostume", 0)
        yield ("costumes", [{"assetId": BLANKSVGHASH, "name": "blank", "md5ext": BLANKSVGHASH+".svg", "dataFormat": "svg", "bitmapResolution": 1, "rotationCenterX":0,"rotationCenterY":0}])
        yield ("sounds", [])
        yield ("volume", 0)
    def push_substack(self, substack: blocks.SubStack):
        self.blocks.append(substack)
    def create_variable(self, name, value):
        v = ScratchVariable(name, value)
        self.variables.append(v)
        return v
    def create_list(self, name, value: list):
        l = ScratchList(name, value)
        self.lists.append(l)
        return l
    def push_proc(self, proc: blocks.Procedure):
        self.push_substack(proc.definition)
        self.push_substack(proc.prototype)

class Stage(BaseTarget):
    def __init__(self):
        super().__init__()
        self.broadcasts: list[Broadcast] = []
    def __iter__(self):
        yield ("isStage", True)
        yield ("name", "Stage")
        yield ("broadcasts", dict([(x.uid, x.name) for x in self.broadcasts]))
        yield from super().__iter__()
        yield ("tempo", 60)
        yield ("videoState", "off")
        yield ("videoTransparency", 50)
        yield ("textToSpeechLanguage", None)

class Sprite(BaseTarget):
    def __init__(self, name: str):
        super().__init__()
        self.name: str = name
    def __iter__(self):
        yield ("isStage", False)
        yield ("name", self.name)
        yield from super().__iter__()
        yield ("visible", False)
        yield ("x", 0)
        yield ("y", 0)
        yield ("size", 100)
        yield ("direction", 90)
        yield ("draggable", False)
        yield ("rotationStyle", "don't rotate")