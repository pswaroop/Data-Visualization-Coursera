# -*- coding: utf-8 -*-
# Header files
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Reading CSV dataset using pandas
df = pd.read_csv('dataset\gistemp.csv')

# Defining custom fonts
font1 = {'family':'serif','color':'blue','size':40}
font2 = {'family':'serif','color':'darkred','size':25}

# Customizing figure size
f = plt.figure(figsize=(20,10))

plt.title('NASA GIS Temperatures',fontdict=font1)
plt.grid()
plt.xticks(np.arange(1800,2020,10),fontsize=20)
plt.yticks(np.arange(-40,90,10),fontsize=20)

# Changing face colour of visualization
ax=plt.gca()
ax.set_facecolor('#ccccb3')

# code for plotting 3 line-charts
plt.plot(df.Year,df.Glob,'s-r',label='Globe',linewidth=3,mec='black')
plt.plot(df.Year,df.NHem,'*-g',label='North Hemisphere',linewidth=3,mec='black')
plt.plot(df.Year,df.SHem,'o-b',label='South Hemisphere',linewidth=3,mec='black')

# displaying legends at upper center
plt.legend(loc='upper center',markerscale=3,prop={'size': 30})

plt.xlabel('Years in Decades',fontdict=font2)
plt.ylabel('Deviation in Temperatures',fontdict=font2)
plt.show()

# Saving figure
f.savefig("GISTEMP Data-Visualization.jpeg", bbox_inches='tight', dpi=200)