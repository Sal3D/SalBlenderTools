from . import save_bone_position
from . import properties
from . import ui

import importlib
importlib.reload(properties)
importlib.reload(save_bone_position)
importlib.reload(ui)

def register():
    properties.register()
    save_bone_position.register()
    ui.register()

def unregister():
    properties.unregister()
    save_bone_position.unregister()
    ui.unregister()

if __name__ == "__main__":
    register()
