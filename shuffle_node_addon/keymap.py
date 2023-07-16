import bpy

from shuffle_node_addon.operator import ShuffleNodeOperator

addon_keymaps = []


def register():
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

    # Remove the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()
