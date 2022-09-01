# https://www.quickprogrammingtips.com/python/how-to-search-in-xml-file-using-python-and-lxml-library.html

from lxml import etree

with open("../L2_eA20_MCOP_00_Ed2122_AUxx_APS_V10.cdfx", 'rb') as f:
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
    names = SW_INSTANCE.xpath('SHORT-NAME/text()')  # Extrahiere Signalnamen. Mit /text() wird Liste zurückgegeben
    #print(names)
    value = SW_INSTANCE.xpath('SW-VALUE-CONT/SW-VALUES-PHYS/V/text()')  # Extrahiere den Signalwert
    #print(value)
    unit = SW_INSTANCE.xpath('SW-VALUE-CONT/UNIT-DISPLAY-NAME/text()')  # Extrahiere Einheit
    print(unit)

    liste = list(zip(names, value, unit))

    for i in liste:
        if 'GbTrqRatio_L2ocIUW' in i[0] and '20.46875' in i[1] and 'NoUnit' in i[2]:

            print('String Found In CDFX')
            print(rf"Found signal {i[0]} with expected value {i[1]} {i[2]}")


'''
        flag = 1
        break

# checking condition for string found or not
if flag == 0:
    print('String Not Found')
else:
    print('String Found In CDFX')
'''

search_dict = {'GbTrqRatio_L2ocIUW': ['20.469999999999998863', 'NoUnit'],
               'tmpTcu_L2isISW': ['0.', '°C'],
               'dummyIDATA_L2cc': '1',
               'dummyIDATA_L2cg': '1',
               'dummyIDATA_L2ml': '1',
               'dummyIDATA_L2mp': '1',
               'dummyIDATA_L2mw': '1'}
