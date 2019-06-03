import bpy


bl_info = {
    "name": "Power Video Editing Pack", 
    "category": "VSE"
}

class PowerImport(bpy.types.Operator):
    """PowerImport"""
    bl_idname = "object.power_import"
    bl_label = "Power Import"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        filebrowser = context.space_data.params
        directory = filebrowser.directory
        filename = filebrowser.filename
        filepath1 = directory + "\\" + filename

        return {'FINISHED'}


class ContextMenu(bpy.types.Menu):
    bl_label = "My Menu"
    bl_idname = "view3d.my_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator = "mesh.primitive_cube_add"
        return

def register():
    print("\nPOWER: Register\n")
    bpy.utils.register_class(PowerImport)
    bpy.utils.register_class(ContextMenu)
    bpy.ops.wm.call_menu(name=ContextMenu.bl_idname)

def unregister():
    print("\nPOWER: Unregister\n")
    bpy.utils.unregister_class(PowerImport)
    bpy.utils.unregister_class(ContextMenu)