#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xml.etree.ElementTree as ET
import csv

#parse XML
xml = ET.parse('input_data.xml')
root = xml.getroot( )

#creat csv file
csvfile = open("data.csv","w",encoding = "utf-8")
csvfile_writer = csv.writer(csvfile)

#ADD the header to csv file
csvfile_writer.writerow(["FinInstrmGnlAttrbts.Id",
                         "FinInstrmGnlAttrbts.FullNm",
                         "FinInstrmGnlAttrbts.ClssfctnTp",
                         "FinInstrmGnlAttrbts.CmmdtyDerivInd",
                         "FinInstrmGnlAttrbts.NtnlCcy",
                         "Issr"])

for i in xml.findall("BizData"):
    if(BizData):
        FinInstrmGnlAttrbts_Id = i.find("Id")
        FinInstrmGnlAttrbts_FullNm = i.find("FullNm")
        FinInstrmGnlAttrbts_ClssfctnTp = i.find("ClssfctnTp")
        FinInstrmGnlAttrbts_CmmdtyDerivInd = i.find("CmmdtyDerivInd")
        FinInstrmGnlAttrbts_NtnlCcy = i.find("NtnlCcy ")
        Issr = i.find("Issr")
        
        csvline = [FinInstrmGnlAttrbts_Id.text,
                         FinInstrmGnlAttrbts_FullNm.text, 
                         FinInstrmGnlAttrbts_ClssfctnTp.text,
                         FinInstrmGnlAttrbts_CmmdtyDerivInd.text,
                         FinInstrmGnlAttrbts_NtnlCcy.text,   
                         Issr.text]
        csvfile_writer.writerow(csvline)
csvfile.close( )

