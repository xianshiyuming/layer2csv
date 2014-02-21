# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name                 : layer2csv Tools
Description          : easy to convert point data into csv with column
Date                 : Dec 16, 2013 
copyright            : (C) 2013 by Hiroaki Sengoku (microbase.LLC)
email                : hsengoku@microgeodata.com

 ***************************************************************************/

/****************************************************************************
 *                                                                          *
 * This is commission program by microbase llc. 							*
 *                                                                          *
 ***************************************************************************/
"""


def classFactory(iface): 
    from setting import pluginSetting
    return pluginSetting(iface)