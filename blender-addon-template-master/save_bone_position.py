import bpy
import json
from bpy_extras import io_utils
from mathutils import Vector,Matrix
class JasonFileSaveBonePosition(bpy.types.Operator, io_utils.ExportHelper):
    bl_idname = "saltools.jason_file_save_bones_positions"
    bl_label = "Save File"
    filename_ext = ".json"
    filter_glob: bpy.props.StringProperty(default="*.json", options={'HIDDEN'})
    def execute(self,context):
        filepath = self.filepath
        jason_file_data={}

        with open(filepath, 'w') as file:
                armature = bpy.context.object
                bones = [bone for bone in armature.data.bones if bone.select]
                # Get the global positions, heads, and tails of the selected bones
                for bone in bones:
                    print(bone)
                    jason_file_data[bone.name] = {
                    'head': list(armature.matrix_world @ bone.head_local),
                    'tail': list(armature.matrix_world @ bone.tail_local)
                    }
                json.dump(jason_file_data, file)
        return {'FINISHED'}
    
class JasonFileLoadBonePosition(bpy.types.Operator, io_utils.ImportHelper):
    bl_idname = "saltools.jason_file_load_bones_positions"
    bl_label = "Load File"
    filename_ext = ".json"
    filter_glob: bpy.props.StringProperty(default="*.json", options={'HIDDEN'})
    def execute(self,context):
        filepath = self.filepath
        with open(filepath, 'r') as file:
            jason_file_data=json.load(file)
            # Get the active armature object
            armature = bpy.context.object
            if armature==None:
                print("Nothing selected select armature ")
                return {'FINISHED'}
            try:
                armature.pose
            except:
                print("Select armature ")
                return {'FINISHED'}
            # Iterate over all the bones in the armature
            bpy.ops.armature.select_all(action='DESELECT')

            for bone in armature.pose.bones:
                # Get the bone positions from the dictionary
                if bone.name in jason_file_data:
                    if jason_file_data.__contains__(bone.name):
                        head_pos = jason_file_data[bone.name]["head"]
                        tail_pos = jason_file_data[bone.name]["tail"]
                        print('Set bone positions '+bone.name+ ' '+str(head_pos)+ ' '+str(tail_pos)+'\n')
                        #head_offset = bpy.context.object.matrix_world.inverted() @ Vector(head_pos)
                        
                        bpy.ops.object.mode_set(mode='EDIT')
                        bpy.ops.armature.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT')
                        bone.bone.select_head=True
                        bpy.ops.object.mode_set(mode='EDIT')
                        
                        bpy.context.scene.cursor.location=Vector(head_pos)
                        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
                        
                        bpy.ops.object.mode_set(mode='EDIT')
                        bpy.ops.armature.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT')
                        bone.bone.select_tail=True
                        bpy.ops.object.mode_set(mode='EDIT')
                        
     
                        bpy.context.scene.cursor.location=Vector(tail_pos)
                        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
                        #bpy.ops.transform.translate(value=Vector(head_offset), orient_type='GLOBAL')
                        
        return {'FINISHED'}
            

class SaveBonePositionOperator(bpy.types.Operator):
    bl_idname = "saltools.save_bones_positions"
    bl_label = "Save Bones Position"

    def execute(self, context):
        print("Save Bones Position")
        bpy.ops.saltools.jason_file_save_bones_positions('INVOKE_DEFAULT')
        return {'FINISHED'}
class LoadBonePositionOperator(bpy.types.Operator):
    bl_idname = "saltools.load_bones_positions"
    bl_label = "Load Bones Position"
    def execute(self, context):
        print("Load Bones Position")
        bpy.ops.saltools.jason_file_load_bones_positions('INVOKE_DEFAULT')
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(SaveBonePositionOperator)
    bpy.utils.register_class(LoadBonePositionOperator)
    bpy.utils.register_class(JasonFileSaveBonePosition)
    bpy.utils.register_class(JasonFileLoadBonePosition)
    
def unregister():
    bpy.utils.unregister_class(SaveBonePositionOperator)
    bpy.utils.unregister_class(LoadBonePositionOperator)
    bpy.utils.unregister_class(JasonFileSaveBonePosition)
    bpy.utils.unregister_class(JasonFileLoadBonePosition)