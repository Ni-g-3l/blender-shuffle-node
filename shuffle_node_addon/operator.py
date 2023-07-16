import bpy
import random


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
            node.location = [
                random.uniform((width * -1), width),
                random.uniform((height * -1), height),
            ]

        return {"FINISHED"}

    @staticmethod
    def get_node_editor_area(context):
        for area in context.screen.areas:
            if area.type == "NODE_EDITOR":
                return area.width, area.height
