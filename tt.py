from mpl_toolkits.basemap import Basemap  # 导入Basemap
import matplotlib.pyplot as plt  # 导入 matplotlib.pyplot
import numpy as np
from matplotlib.patches import Polygon
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(16, 9))
ax = plt.gca()
m = Basemap(projection='cyl',resolution='c',llcrnrlon=121.30, llcrnrlat=29.32, urcrnrlon=123.25, urcrnrlat=31.04)


shp_info=m.readshapefile('chnadm/gadm36_CHN_3',name='citys',drawbounds=True)
for info, shp in zip(m.citys_info, m.citys):

    proid = info['NAME_2']  # NAME_2 代表各市的拼音
    # proid = Converter('zh-hans').convert(info['NL_NAME_2'])  # 汉语
    #     print(proid)
    if proid=="Zhoushan":
        poly = Polygon(shp,facecolor='r', alpha=0.3,lw=3)
        ax.add_patch(poly)











# parallels = np.arange(30, 31., 0.1)  # 这两行画纬度，范围为[-90,90]间隔为10
# m.drawparallels(parallels, labels=[False, True, True, False])
# meridians = np.arange(122., 123., 0.1)  # 这两行画经度，范围为[-180,180]间隔为10
# m.drawmeridians(meridians, labels=[True, False, False, True])
# lon, lat = m(120, 30)  # lon, lat为给定的经纬度，可以使单个的，也可以是列表
m.drawcoastlines()  # 画海岸线
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral', lake_color='aqua')
m.drawcountries()
lons = [122.7368, 122.7790, 122.8240]
lats = [30.7276, 30.7810, 30.7100]
x, y = m(lons, lats)
m.plot(x, y, 'bo', markersize=10)
labels = ['1', '2', '3']
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt, ypt, label)
plt.savefig('fig_city.png', dpi=100, bbox_inches='tight')
plt.show()
