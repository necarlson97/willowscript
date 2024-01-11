bl_info = {
    "name": "WillowscriptWriter",
    "author": "Nils Carlson",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > My Tab",
    "description": "Creates duplicates of objects based on text input",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}

import bpy

class WillowscriptWriter(bpy.types.Operator):
    """ WillowscriptWriter Operator """
    bl_idname = "object.willowscript_writer"
    bl_label = "Willowscript Writer"
    bl_options = {'REGISTER', 'UNDO'}

    input_text: bpy.props.StringProperty(
        name="Input Text",
        description="Input text to be used to create 3d objects",
        default='"The brown fox jumped over the lazy dog"'
    )

    def get_object_name(self, text, i):
        char = text[i]
        if char == '"':
            if i == 0 or text[i-1] == ' ':
                return 'top-quote'
            return 'bottom-quote'
        elif char == '?':
            if i == 0 or text[i-1] == ' ':
                return 'top-question'
            return 'bottom-question'
        elif char == '.':
            return 'period'
        elif char == ',':
            return 'comma'
        else:
            return char.lower()

    def execute(self, context):
        cursor = context.scene.cursor.location
        original_cursor_location = cursor.copy()

        for i, c in enumerate(self.input_text):
            object_name = self.get_object_name(self.input_text, i)
            if object_name in bpy.data.objects:
                obj = bpy.data.objects[object_name]
                new_obj = obj.copy()
                new_obj.data = obj.data  # Link object data
                new_obj.location = cursor.copy()
                context.collection.objects.link(new_obj)
            cursor.y -= 1

        context.scene.cursor.location = original_cursor_location
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)

    def draw(self, context):
        self.layout.prop(self, 'input_text', text='Input Text')

def menu_func(self, context):
    self.layout.operator(WillowscriptWriter.bl_idname)

def register():
    bpy.utils.register_class(WillowscriptWriter)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(WillowscriptWriter)

if __name__ == "__main__":
    register()
