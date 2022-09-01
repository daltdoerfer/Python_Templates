# https://www.python-forum.de/viewtopic.php?t=39447
# https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python UTF8 Problem vermeiden
import os
from glob import glob
import io

# Nimmt alle CDFX Files im entsprechenden Ordner
filenames = glob(r"C:\03_Programming\Python_Templates\02_Testprojekte\Search_Change_Text\*.cdfx")

# Abschnitte nach denen Gesucht werden soll
search_dict = {'GbTrqRatio_L2ocIUW': '''<SHORT-NAME>L2oc_IDATA.GbTrqRatio_L2ocIUW</SHORT-NAME>
<LONG-NAME>Wheel Torque ratio</LONG-NAME>
<DISPLAY-NAME>L2oc_IDATA.GbTrqRatio_L2ocIUW</DISPLAY-NAME>
<CATEGORY>VALUE</CATEGORY>

<SW-FEATURE-REF>L2oc_calibration_parameters</SW-FEATURE-REF><SW-VALUE-CONT>
<UNIT-DISPLAY-NAME xml:space="preserve">NoUnit</UNIT-DISPLAY-NAME>
<SW-VALUES-PHYS>
<V>20.469999999999998863</V>
</SW-VALUES-PHYS>''',

               'GbTrqRatioL2InvL2_L2oiIUW': '''<SHORT-NAME>L2oi_IDATA.GbTrqRatioL2InvL2_L2oiIUW</SHORT-NAME>
<LONG-NAME>Crankshaft to Wheel Ratio from L2 TCU to L2 Inv</LONG-NAME>
<DISPLAY-NAME>L2oi_IDATA.GbTrqRatioL2InvL2_L2oiIUW</DISPLAY-NAME>
<CATEGORY>VALUE</CATEGORY>

<SW-FEATURE-REF>L2oi_calibration_parameters</SW-FEATURE-REF><SW-VALUE-CONT>
<UNIT-DISPLAY-NAME xml:space="preserve">NoUnit</UNIT-DISPLAY-NAME>
<SW-VALUES-PHYS>
<V>20.469999999999998863</V>
</SW-VALUES-PHYS>''',

               'tmpTcu_L2isISW': '''<SHORT-NAME>L2is_IDATA.tmpTcu_L2isISW</SHORT-NAME>
<LONG-NAME>Temperaturwert Steuergerätesensor (default sensor)</LONG-NAME>
<DISPLAY-NAME>L2is_IDATA.tmpTcu_L2isISW</DISPLAY-NAME>
<CATEGORY>VALUE</CATEGORY>

<SW-FEATURE-REF>L2is_calibration_parameters</SW-FEATURE-REF><SW-VALUE-CONT>
<UNIT-DISPLAY-NAME xml:space="preserve">°C</UNIT-DISPLAY-NAME>
<SW-VALUES-PHYS>
<V>0.</V>
</SW-VALUES-PHYS>''',

               'dummyIDATA_L2cc': '''<SHORT-NAME>L2cc_IDATA.dummyIDATA_L2cc</SHORT-NAME>''',
               'dummyIDATA_L2cg': '''<SHORT-NAME>L2cg_IDATA.dummyIDATA_L2cg</SHORT-NAME>''',
               'dummyIDATA_L2ml': '''<SHORT-NAME>L2ml_IDATA.dummyIDATA_L2ml</SHORT-NAME>'''
}

# ----------------------------------------------------
# Folgender CODE prüft ob Textabschnitte vorhanden (ÄÖÜ usw wird durch UTF 8 Berücksichtigt)
#-----------------------------------------------------
def contains(k, textfile):
    return k in textfile.read()

# Durch Files Iterieren
for filename in filenames:

    # Durch Search Dictionary Iterieren
    for (key, search_text) in search_dict.items():

        # opening a text file
        with io.open(filename, mode="r", encoding="utf-8") as textfile:

            print(rf"OK: {key} exakt enthalten in:" if contains(search_text, textfile) else rf"FAILED: {key} nicht gefunden", textfile.name)

        #print('key: ', key)
        #print('value: ', search_text)
