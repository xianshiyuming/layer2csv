# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name                 : layer2csv Tools
Description          : easy to convert point data into csv with column
Date                 : Dec 16, 2013 
copyright            : (C) 2013 by Hiroaki Sengoku (microbase.LLC)
email                : hsengoku@live.jp

 ***************************************************************************/

/****************************************************************************
 *                                                                          *
 * This is commission program by microbase llc.								*
 *                                                                          *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import resources_rc
import csv
import os

### language

def setencoding():
  if os.name == "nt":
      encoding_lng = "cp932"
  elif os.name == "posix":
      encoding_lng = "utf-8"
  else:
      encoding_lng = "utf-8"
  
  return encoding_lng
    
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


### Initialize

class pluginSetting:

  def __init__(self, iface):
    self.iface = iface
    self.qgsVersion = unicode(QGis.QGIS_VERSION_INT)
    userPluginPath = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/layer2csv"
    systemPluginPath = QgsApplication.prefixPath() + "/python/plugins/layer2csv"
  
  def initGui(self):
    self.action = QAction(QIcon(":/icon/crs_icon.png"), "layer2csv", self.iface.mainWindow())
    self.action.setWhatsThis(QCoreApplication.translate("Layer2csv", "convert shapefile into csv"))
    self.action.setStatusTip(QCoreApplication.translate("Layer2csv", "convert shapefile into csv"))
    #self.action.triggered.connect(self.run)
    QObject.connect(self.action, SIGNAL("triggered()"), self.run)
    
    self.iface.addPluginToVectorMenu(QCoreApplication.translate("Layer2csv", "Layer2csv"), self.action)
    self.iface.addVectorToolBarIcon(self.action)
    #self.iface.addToolBarIcon(self.action)
    #self.iface.addPluginToMenu("layer2csv", self.action)
    #QObject.connect(self.iface.mapCanvas(), SIGNAL("renderComplete(QPainter *)"), self.renderTest)

  def unload(self):
    #self.iface.removePluginMenu("layer2csv", self.action)
    #self.iface.removeToolBarIcon(self.action)
    self.iface.removePluginVectorMenu(QCoreApplication.translate("Layer2csv", "Layer2csv"), self.action)
    self.iface.removeVectorToolBarIcon(self.action)
    #QObject.disconnect(self.iface.mapCanvas(), SIGNAL("renderComplete(QPainter *)"), self.renderTest)

  def run(self):
    dlg = Ui_Dialog(self.iface)
    #dlg.textEdit.setText(str(self.iface.mapCanvas().layerCount()))
    dlg.show()
    dlg.exec_()

  def tr(self, text):
    return QApplication.translate(plugin_classname, text, None, QApplication.UnicodeUTF8)


#### GUI
    
class Ui_Dialog(QDialog):

  def __init__(self, iface):
    QDialog.__init__(self)
    self.iface = iface
    self.caption = self.tr("Dialog")
    self.setupUi()
    #s = QSettings()
      
  def setupUi(self):
    Dialog = self
    Dialog.setObjectName("Dialog")
    Dialog.resize(472, 427)
    
    #label
    self.label = QtGui.QLabel(Dialog)
    self.label.setGeometry(QtCore.QRect(50, 80, 371, 41))
    self.label.setObjectName("label")
    self.label_2 = QtGui.QLabel(Dialog)
    self.label_2.setGeometry(QtCore.QRect(50, 120, 271, 41))
    self.label_2.setObjectName("label_2")
    self.label_3 = QtGui.QLabel(Dialog)
    self.label_3.setGeometry(QtCore.QRect(50, 20, 261, 41))
    self.label_3.setObjectName("label_3")
    self.label_4 = QtGui.QLabel(Dialog)
    self.label_4.setGeometry(QtCore.QRect(50, 300, 271, 41))
    self.label_4.setObjectName("label_4")
    self.label_5 = QtGui.QLabel(Dialog)
    self.label_5.setGeometry(QtCore.QRect(50, 180, 271, 41))
    self.label_5.setObjectName("label_5")
    self.label_6 = QtGui.QLabel(Dialog)
    self.label_6.setGeometry(QtCore.QRect(50, 240, 271, 41))
    self.label_6.setObjectName("label_6")

    #comboBox
    self.comboBox = QtGui.QComboBox(Dialog)
    self.comboBox.setGeometry(QtCore.QRect(50, 270, 311, 26))
    self.comboBox.setObjectName("comboBox")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    
    #
    self.inputDir = QLineEdit(Dialog)
    self.inputDir.setObjectName("inputDir")
    self.inputDir.setGeometry(QtCore.QRect(50, 50, 311, 21))
    self.outDir = QLineEdit(Dialog)
    self.outDir.setObjectName("outDir")
    self.outDir.setGeometry(QtCore.QRect(50, 330, 311, 21))
    self.columDir = QLineEdit(Dialog)
    self.columDir.setObjectName("columDir")
    self.columDir.setGeometry(QtCore.QRect(300, 90, 61, 21))
    self.sourceDir = QLineEdit(Dialog)
    self.sourceDir.setObjectName("sourceDir")
    self.sourceDir.setGeometry(QtCore.QRect(50, 150, 311, 21))
    self.dayDir = QLineEdit(Dialog)
    self.dayDir.setObjectName("dayDir")
    self.dayDir.setGeometry(QtCore.QRect(50, 210, 311, 21))
    
    #pushButton
    self.pushButton = QtGui.QPushButton(Dialog)
    self.pushButton.setGeometry(QtCore.QRect(380, 50, 61, 21))
    font = QtGui.QFont()
    font.setFamily("MS UI Gothic")
    font.setPointSize(12)
    font.setBold(False)
    font.setWeight(50)
    self.pushButton.setFont(font)
    self.pushButton.setObjectName("pushButton")
    
    #pushButton_2
    self.pushButton_2 = QtGui.QPushButton(Dialog)
    self.pushButton_2.setGeometry(QtCore.QRect(380, 330, 71, 21))
    font = QtGui.QFont()
    font.setFamily("MS UI Gothic")
    font.setPointSize(12)
    font.setBold(False)
    font.setWeight(50)
    self.pushButton_2.setFont(font)
    self.pushButton_2.setObjectName("pushButton_2")
    
    #buttonBox
    self.buttonBox = QtGui.QDialogButtonBox(Dialog)
    self.buttonBox.setGeometry(QtCore.QRect(290, 370, 156, 23))
    self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
    self.buttonBox.setObjectName("buttonBox")
    
    #set menu title
    self.retranslateUi(Dialog)
    
    #################
    #Event -> Action
    #load method
    #################
    QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"), self.convert)
    QObject.connect(self.buttonBox, SIGNAL("rejected()"), self.close)
    QObject.connect(self.pushButton, SIGNAL("clicked()"), self.directorydialog1)
    QObject.connect(self.pushButton_2, SIGNAL("clicked()"), self.directorydialog2)
    
    QMetaObject.connectSlotsByName(Dialog)


  def retranslateUi(self, Dialog):
    Dialog.setWindowTitle(_translate("Dialog", "layer2csv", None))
    self.label.setText(_translate("Dialog", "建物名称の列番号を追加してください", None))
    self.label_2.setText(_translate("Dialog", "提供元の情報を入力してください", None))
    self.label_3.setText(_translate("Dialog", "入力ファイルを選択してください", None))
    self.label_4.setText(_translate("Dialog", "出力するファイルパスを選択してください", None))
    self.label_5.setText(_translate("Dialog", "提供日の情報を入力してください", None))
    self.label_6.setText(_translate("Dialog", "ライセンスを選択してください", None))
    self.comboBox.setItemText(0, _translate("Dialog", "CC BY", None))
    self.comboBox.setItemText(1, _translate("Dialog", "CC BY-SA", None))
    self.comboBox.setItemText(2, _translate("Dialog", "CC BY-ND", None))
    self.comboBox.setItemText(3, _translate("Dialog", "CC BY-NC", None))
    self.comboBox.setItemText(4, _translate("Dialog", "CC BY-NC-SA", None))
    self.comboBox.setItemText(5, _translate("Dialog", "CC BY-NC-ND", None))
    self.comboBox.setItemText(6, _translate("Dialog", "CC0", None))
    self.pushButton_2.setText(_translate("Dialog", "参照", None))
    self.pushButton.setText(_translate("Dialog", "参照", None))


  ########## Dialog #########
  
  
  def convert(self):
    #pdir = os.path.dirname(__file__)
    encoding = setencoding()
    input_file = str(self.inputDir.text().encode(encoding))#.toLocal8Bit()
    out_file = str(self.outDir.text().encode(encoding))
    
    bname_column = str(self.columDir.text())
    if bname_column is None:
        QMessageBox.warning(self, self.caption, self.tr("Error: 列番号を入力してください"))
        return
    
    #text = self.sourceDir.text()
    #source = text.encode('utf-8')
    
    #source = str(unicode(text, 'utf-8'))
    source = str(self.sourceDir.text().encode(encoding))
    if source is None:
        QMessageBox.warning(self, self.caption, self.tr("Error: 提供元の情報を入力してください"))
        return
        
    date = str(self.dayDir.text().encode(encoding))
    if date is None:
        QMessageBox.warning(self, self.caption, self.tr("Error: 提供日の情報を入力してください"))
        return
    
    license = str(self.comboBox.currentText())
    
    table = self.layer2table(input_file,source,date,license,bname_column)
    self.exportcsv(table, out_file)
    QMessageBox.information(self.iface.mainWindow(), "Success", "Successfully saved as CSV")
  
  def directorydialog1(self):
    file = QFileDialog.getOpenFileName(self, self.tr("Select inputput directory"))
    if file != "":
      self.inputDir.setText(file)

  def directorydialog2(self):
    file = QFileDialog.getSaveFileName(self, self.tr("Select output directory"))
    if file != "":
      self.outDir.setText(file)
      
  def close(self):
    QDialog.close(self)



########## function ##########

	
  def exportcsv(self,table, output_file):
    # Export as CSV
    
    if not output_file.endswith('.csv'):
        output_file = output_file + '.csv'
    
    i = 0
    try:
        f = open(output_file,"w")
    except:
        QMessageBox.warning(self, self.caption, self.tr("Error: 出力パスが正しくありません"))
    
    writer = csv.writer(f)
    
    while i < len(table):
    	value = table[i]
    	writer.writerow(value)
    	#time.sleep(1)
    	i += 1
    	#size = int(i.size)
    
    f.close()
    
  def layer2table(self,inputfile,source,date,license,columnnum):
    
    try:
        vlayer = QgsVectorLayer(inputfile, "point", "ogr")
    except:
        QMessageBox.warning(self, self.caption, self.tr("Error: 入力パスが正しくありません"))
    
    encoding = setencoding()
    #vlayer = qgis.utils.iface.mapCanvas().currentLayer()
    #provider = vlayer.dataProvider()
    #feat = QgsFeature()
    #allAttrs = provider.attributeIndexes()
    #provider.select(allAttrs)

    jj = int(columnnum) - 1
    csvtable = []
        
    iter = vlayer.getFeatures()
    for feat in iter:
    #while provider.nextFeature(feat):
    	
        #1) geometry
        
        geom = feat.geometry()
        #if geom.vectorType() == QGis.Point:
        if vlayer.geometryType() == QGis.Point:
            pointxy = geom.exportToWkt()#.asPoint()
            #pointxy = geom.asPoint()
            xy = str(pointxy).lstrip('POINT(').rstrip(')')
            xy = xy.split(' ')
            x = str(xy[0])
            y = str(xy[1])
            #print x
        else:
            #print ""
            QMessageBox.warning(self, self.caption, self.tr("Please set point data."))
        
        #2) attribute
        attrs = feat.attributes()
        attr_text = ""
        text = attrs[jj].encode(encoding)
        #unitext = unicode(text, encoding)
        #print unicode(s, t)
        #attr_text = str(unitext)
        attr_text = text
        
        value = [attr_text,x,y,source,date,license]
        csvtable.append(value)
    
    header = ['name','lon','lat','source','date','license']
    
    csvtable.insert(0, header)
    #print csvtable
    return csvtable
	