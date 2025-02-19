# <pep8-80 compliant>

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Nutti <nutti.metro@gmail.com>"
__status__ = "production"
__version__ = "6.5"
__date__ = "6 Mar 2021"

import bpy

from ..op.copy_paste_uv_uvedit import (
    MUV_OT_CopyPasteUVUVEdit_CopyUV,
    MUV_OT_CopyPasteUVUVEdit_PasteUV,
    MUV_OT_CopyPasteUVUVEdit_CopyUVIsland,
    MUV_OT_CopyPasteUVUVEdit_PasteUVIsland,
)
from ..utils.bl_class_registry import BlClassRegistry
from ..utils import compatibility as compat


@BlClassRegistry()
@compat.ChangeRegionType(region_type='TOOLS')
class MUV_PT_UVEdit_CopyPasteUV(bpy.types.Panel):
    """
    Panel class: Copy/Paste UV on Property Panel on UV/ImageEditor
    """

    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_label = "Copy/Paste UV"
    bl_category = "Magic UV"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, _):
        layout = self.layout
        layout.label(text="", icon=compat.icon('IMAGE'))

    def draw(self, context):
        layout = self.layout
        sc = context.scene

        layout.label(text="Face:")
        row = layout.row(align=True)
        row.operator(MUV_OT_CopyPasteUVUVEdit_CopyUV.bl_idname, text="Copy")
        row.operator(MUV_OT_CopyPasteUVUVEdit_PasteUV.bl_idname, text="Paste")

        layout.separator()

        layout.label(text="Island:")
        row = layout.row(align=True)
        row.operator(MUV_OT_CopyPasteUVUVEdit_CopyUVIsland.bl_idname,
                     text="Copy")
        ops = row.operator(MUV_OT_CopyPasteUVUVEdit_PasteUVIsland.bl_idname,
                           text="Paste")
        ops.unique_target = sc.muv_copy_paste_uv_uvedit_unique_target
        layout.prop(sc, "muv_copy_paste_uv_uvedit_unique_target")
