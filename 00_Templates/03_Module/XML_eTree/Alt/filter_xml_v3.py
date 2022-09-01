# https://www.quickprogrammingtips.com/python/how-to-search-in-xml-file-using-python-and-lxml-library.html

from lxml import etree
#"L2_eA20_MCOP_00_Ed2122_AUxx_APS_V10.cdfx"
with open("../SONDERPARAMETER_V1.cdfx", 'rb') as f:
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


for SW_INSTANCE in SW_INSTANCES:
    names = SW_INSTANCE.xpath('SHORT-NAME/text()')  # Extrahiere Signalnamende aus Hierarchie. Mit /text() wird Liste zurückgegeben
    print(names)
    value = SW_INSTANCE.xpath('SW-VALUE-CONT/SW-VALUES-PHYS/V/text()')  # Extrahiere den Signalwert  aus Hierarchie
    print(value)


    unit = SW_INSTANCE.xpath('SW-VALUE-CONT/UNIT-DISPLAY-NAME/text()')  # Extrahiere Einheit aus Hierarchie
    print(unit)

    liste = list(zip(names, value, unit))

    search_dict = {'GbTrqRatio_L2ocIUW': ['20.46875', 'NoUnit'],
                   'GbTrqRatioL2InvL2': ['20.46875', 'NoUnit'],
                   'tmpTcu_L2isISW': ['0.', '°C'],
                   'dummyIDATA_L2cc': ['1'],
                   'dummyIDATA_L2cg': ['1'],
                   'dummyIDATA_L2ml': ['1'],
                   'dummyIDATA_L2mp': ['1'],
                   'dummyIDATA_L2mw': ['1']}

    keycounter = 0
    for (key, search_text) in search_dict.items():

        #print(key)
        #print(search_text)
        #print(len(search_text))
        keycounter += 1

        for i in liste:

            #print(i)
            #if 'GbTrqRatio_L2ocIUW' in i[0]:
                # print("NOW")

            if key in i[0] and search_text[0] in i[1] and search_text[1] in i[2] and len(search_text) == 2: # Sucht nur wenn 2 Einträge in serach_text vorhanden sind spricht -> Einheit auch vorhanden

                #print('String Found In CDFX')
                print(rf"Found signal {i[0]} with expected value {i[1]} {i[2]}")

            #if key in i[0] and search_text[0] in i[1] and len(search_text) == 1:
            if key in i[0] and len(search_text) == 1:
                print(rf"Found signal {i[0]} ")


'''
        flag = 1
        break

# checking condition for string found or not
if flag == 0:
    print('String Not Found')
else:
    print('String Found In CDFX')
'''


