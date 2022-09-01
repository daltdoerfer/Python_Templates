# https://www.quickprogrammingtips.com/python/how-to-search-in-xml-file-using-python-and-lxml-library.html
from lxml import etree
from glob import glob
import io

# Nimmt alle CDFX Files im entsprechenden Ordner
#filenames = glob(r"C:\03_Programming\Python_Templates\02_Testprojekte\Search_Change_Text\*.cdfx")
filenames = glob(r"C:\Users\altdoerfer\Desktop\20220815_e1v1u22d2415tx\*.cdfx")


# Nach diesen Werten im Dict wird gesucht
search_dict = {'GbTrqRatio_L2ocIUW': ['20.46875', 'NoUnit'],
               'GbTrqRatioL2InvL2': ['20.46875', 'NoUnit'],
               'tmpTcu_L2isISW': ['0.', '°C'],
               'dummyIDATA_L2cg': ['1', 'NONE'],
               'dummyIDATA_L2ml': ['1', 'NONE']}


# Durch Files Iterieren
for filename in filenames:

    print(rf"--------------------------------------------------")
    print(rf"START CHECK: {filename} ---")
    print(rf"--------------------------------------------------")

    #"L2_eA20_MCOP_00_Ed2122_AUxx_APS_V10.cdfx"
    with open(filename, 'rb') as f:
        file_content = f.read()
        tree = etree.fromstring(file_content)

        # Example
        #customer_ids = tree.xpath('//customer/@id')
        #customers_in_la = tree.xpath('//customer[state/text()="LA"]/name/text()')
        #for id in customer_ids:
        #    print(id)



    ''' TAG Hierachie im CDFX-File
    MSRSW
        SW-SYSTEMS
            SW-SYSTEM
                SW-INSTANCE-SPEC
                    SW-INSTANCE-TREE
                        SW-INSTANCE
                            SHORT-NAME = L2oc_IDATA.GbTrqRatio_L2ocIUW
                            SW-VALUE-CONT
                                SW-VALUES-PHYS
                                    V= 20.46875
    '''
    SW_INSTANCES = tree.xpath('//MSRSW/SW-SYSTEMS/SW-SYSTEM/SW-INSTANCE-SPEC/SW-INSTANCE-TREE/SW-INSTANCE')


    cnt_find = 0
    print()

    for SW_INSTANCE in SW_INSTANCES:
        names = SW_INSTANCE.xpath('SHORT-NAME/text()')  # Extrahiere Signalnamende aus Hierarchie. Mit /text() wird Liste zurückgegeben
        value = SW_INSTANCE.xpath('SW-VALUE-CONT/SW-VALUES-PHYS/V/text()')  # Extrahiere den Signalwert  aus Hierarchie
        unit = SW_INSTANCE.xpath('SW-VALUE-CONT/UNIT-DISPLAY-NAME/text()')  # Extrahiere Einheit aus Hierarchie
        #print(names)
        #print(value)
        #print(unit)

        if not unit: # Wenn keine Unit im XML vohanden
            unit = ['NONE']

        liste = list(zip(names, value, unit))
        cnt_key = 0

        for (key, search_text) in search_dict.items():

            #print(key)
            #print(search_text)
            #print(len(search_text))
            cnt_key += 1

            for i in liste:

                if key in i[0] and search_text[0] in i[1] and search_text[1] in i[2] and len(search_text) == 2: # Sucht nur wenn 2 Einträge in serach_text vorhanden sind spricht -> Einheit auch vorhanden
                    print(rf"Found SIGNAL: {i[0]} with expected VALUE: {i[1]} with UNIT: {i[2]}")
                    cnt_find += 1

    #print(cnt_key)
    #print(cnt_find)
    if cnt_key == cnt_find:
        print(rf"--------------------------------------------------")
        print(rf"CHECK PASSED: {f.name}")
        print(rf"--------------------------------------------------")
    else:
        print(rf"--------------------------------------------------")
        print(rf"CHECK FAILED !")
        print(rf"{cnt_key-cnt_find} Signals Missing !")
        print(rf"Please check File {f.name} manually !")
        print(rf"--------------------------------------------------")
