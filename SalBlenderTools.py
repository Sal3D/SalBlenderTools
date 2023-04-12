import bpy
import json



# Define the panel class
class HelloWorldPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_hello_world"
    bl_label = "Hello World Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My Addon'

    def draw(self, context):
        layout = self.layout

        # Add a button to the panel
        layout.operator("myaddon.hello_world", text="Say Hello")

        # Add a second button to the panel
        layout.operator("myaddon.goodbye_world", text="Say Goodbye")

# Define the operator class for the "Say Hello" button
class HelloWorldOperator(bpy.types.Operator):
    bl_idname = "myaddon.hello_world"
    bl_label = "Hello World Operator"

    def execute(self, context):
        print("Hello World!")
        return {'FINISHED'}

# Define the operator class for the "Say Goodbye" button
class GoodbyeWorldOperator(bpy.types.Operator):
    bl_idname = "myaddon.goodbye_world"
    bl_label = "Goodbye World Operator"

    def execute(self, context):
        print("Goodbye World!")
        return {'FINISHED'}

# Register the panel and operators with Blender
def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(HelloWorldOperator)
    bpy.utils.register_class(GoodbyeWorldOperator)

# Unregister the panel and operators with Blender
def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(HelloWorldOperator)
    bpy.utils.unregister_class(GoodbyeWorldOperator)
register()

def save_points_to_jason():
    # Get the active armature object
    armature = bpy.context.object

    # Create a dictionary to store the bone positions
    bone_positions = {}
    f="d/temp/bone_positions.json"
    # Iterate over all the bones in the armature
    for bone in armature.pose.bones:
        # Get the world position of the bone's head and tail
        head_pos = armature.matrix_world @ bone.head
        tail_pos = armature.matrix_world @ bone.tail

        # Add the bone positions to the dictionary
        bone_positions[bone.name] = {
            "head_position": list(head_pos),
            "tail_position": list(tail_pos)
        }

    # Write the bone positions to a JSON file
    with open(f, "w") as file:
        json.dump(bone_positions, file, indent=4)
        
    