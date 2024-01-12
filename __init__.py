# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LayerEditor
                                 A QGIS plugin
 TEST
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-12-28
        copyright            : (C) 2023 by Avanesyan and Kazmin
        email                : dul4ityx@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LayerEditor class from file LayerEditor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .layer_editor import LayerEditor
    return LayerEditor(iface)
