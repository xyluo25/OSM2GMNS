'''
##############################################################
# Created Date: Wednesday, December 11th 2024
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################
'''


import osm2gmns as og

path = r"C:\Users\xyluo25\anaconda3_workspace\001_GitHub\OSM2GMNS\examples\Arizona State University, Tempe Campus\asu.osm"

net = og.getNetFromFile(path, strict_mode=False, start_node_id=1, start_link_id=1, default_lanes=True,)

og.consolidateComplexIntersections(net, auto_identify=True)
og.buildMultiResolutionNets(net)
og.outputNetToCSV(net)
