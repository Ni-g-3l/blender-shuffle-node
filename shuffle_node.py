import bpy
import random

bl_info = {
    "name": "Shuffle Node",
    "author": "Nig3l",
    "version": (1, 0),
    "blender": (3, 5, 1),
    "location": "Node Editor > Select Menu & Node Editor > Contextual Menu",
    "description": "Shuffle selected nodes in the Node Editor",
    "warning": "",
    "doc_url": "https://github.com/Ni-g-3l/blender-node-shuffler",
    "category": "Node",
}

addon_keymaps = []


class ShuffleNodeOperator(bpy.types.Operator):
    """Shuffle selected nodes in the Node Editor"""

    bl_idname = "node.shuffle_node"
    bl_label = "Shuffle Node"

    @classmethod
    def poll(cls, context):
        return len(context.selected_nodes) > 0

    def execute(self, context):
        width, height = ShuffleNodeOperator.get_node_editor_area(context)
        for node in context.selected_nodes:
            node.location = [random.uniform(-width, width), random.uniform(-height, height)]

        return {"FINISHED"}

    @staticmethod
    def get_node_editor_area(context):
        for area in context.screen.areas:
            if area.type == "NODE_EDITOR":
                return area.width, area.height


def draw_select_menu(self, context):
    self.layout.operator(
        ShuffleNodeOperator.bl_idname, text=ShuffleNodeOperator.bl_label
    )


def draw_contextual_menu(self, context):
    self.layout.separator()
    self.layout.operator(
        ShuffleNodeOperator.bl_idname, text=ShuffleNodeOperator.bl_label
    )


def register():
    bpy.utils.register_class(ShuffleNodeOperator)
    bpy.types.NODE_MT_select.append(draw_select_menu)
    bpy.types.NODE_MT_context_menu.append(draw_contextual_menu)

    # Set up the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Node Editor", space_type="NODE_EDITOR")
    kmi = km.keymap_items.new(
        ShuffleNodeOperator.bl_idname,
        type="S",
        value="PRESS",
        ctrl=False,
        shift=True,
        alt=True,
    )
    addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_class(ShuffleNodeOperator)
    bpy.types.NODE_MT_select.remove(draw_select_menu)
    bpy.types.NODE_MT_context_menu.remove(draw_contextual_menu)

    # Remove the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()


if __name__ == "__main__":
    register()
