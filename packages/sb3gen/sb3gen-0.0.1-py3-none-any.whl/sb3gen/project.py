import json
import zipfile
import pathlib
from . import blocks, targets, scratchtypes as st

class ProjectFile():
    def __init__(self, targets: list[targets.BaseTarget], extensions: list[str] = [], vmver: str = "0.2.0", ua: str = "ScratchPython"):
        self.targets = targets
        self.extensions = extensions
        self.vmver = vmver
        self.agent = ua
        self.platform = {"name": "ScratchPython sb3 editor", "url": "https://github.com/Belu-cat/ScratchPython/tree/main/src/ScratchPython/sb3"}
    def __iter__(self):
        yield ("targets", [dict(x) for x in self.targets])
        yield ("monitors", [])
        yield ("extensions", self.extensions)
        yield ("meta", {"semver": "3.0.0",
                        "vm": self.vmver,
                        "agent": self.agent,
                        # "platform": self.platform})
        })

def project_to_zip(projectfile: ProjectFile, outfilename: str):
    with zipfile.ZipFile(outfilename, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("project.json", json.dumps(dict(projectfile)))
        zf.writestr(targets.BLANKSVGHASH+".svg", targets.BLANKSVG)
