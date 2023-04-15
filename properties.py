
import bpy

class SalToolsProperties(bpy.types.PropertyGroup):
    expandBonePosition: bpy.props.BoolProperty(name="expandBonePosition", default=False)
    
def register():
    bpy.utils.register_class(SalToolsProperties)
    bpy.types.Scene.sal_tools_props = bpy.props.PointerProperty(type=SalToolsProperties)

def unregister():
    bpy.utils.unregister_class(SalToolsProperties)
    del bpy.types.Scene.sal_tools_props