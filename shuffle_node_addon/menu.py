import bpy

from shuffle_node_addon.operator import ShuffleNodeOperator


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
    bpy.types.NODE_MT_select.append(draw_select_menu)
    bpy.types.NODE_MT_context_menu.append(draw_contextual_menu)


def unregister():
    bpy.types.NODE_MT_select.remove(draw_select_menu)
    bpy.types.NODE_MT_context_menu.remove(draw_contextual_menu)
