import bpy

class SalToolsPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_sal_tools_panel"
    bl_label = "Sal Tools Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sal Tools'

    def draw(self, context): 
        layout = self.layout
        props = context.scene.sal_tools_props

        row = layout.box()
        row.operator("saltools.close", text="Close")
        row.prop(props, "expandBonePosition", text="Save Bones Position", emboss=False, icon='TRIA_DOWN' if props.expandBonePosition else 'TRIA_RIGHT')

        if props.expandBonePosition:
            box = layout.box()
            box.operator("saltools.save_bones_positions", text="Save Bones Positions")
            box.operator("saltools.load_bones_positions", text="Load Bones Positions")
   
class Close(bpy.types.Operator):
    bl_idname = "saltools.close"
    bl_label = "Close"

    def execute(self, context):
        bpy.utils.unregister_class(SalToolsPanel)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SalToolsPanel)
    bpy.utils.register_class(Close)
def unregister():
    bpy.utils.unregister_class(SalToolsPanel)
    bpy.utils.unregister_class(Close)