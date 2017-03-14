"""
Animation-Plotting DQN predicted max Q-value & Q-values for all actions 

Zack Verham (zdv8rb)
Prabhat Rayapati (pr2sn)
Deep Learning for Computer Graphics (Fall 2016)
Final Project 
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import os
from os import makedirs,path
import sys

################################
#-------------------------------
# INPUT & OUTPUT PARAMETERS 
#-------------------------------

csv_file='1999.csv'
max_qval_video_name='max_qval.mp4'
act_qval_video_name='act_qval.mp4'

#-------------------------------
################################



# enter the name of the csv file that contains the networks 
# predicted q_vals for each action 
tab=pd.read_csv(csv_file)


#--------------------------------
#
#	real time max q-val plotting 
#
#--------------------------------

# enter the name of the directory/folder you want the plots to be saved in 
mypath='episode_act_plots'

# make the directory 
makedirs(mypath)

# max of all q_vals
y = np.amax(tab.ix[:,0:9],axis=1)

# iterate through the csv to plot the bars for each action
for i in range(len(y)):

	plt.plot(np.arange(len(y[:i])),y[:i],linewidth=2.0)
	axes = plt.gca()
	axes.set_xlim([0,len(y)])
	axes.set_ylim([np.min(y),np.max(y)])
	plt.ylabel('Max Q_val')
	plt.xlabel('Time-steps')
	plt.title('Predicted max Q_vals')
	plt.savefig(os.path.join(mypath,str(i)))
	plt.clf()

# cd to the folder mypath and run the following command in the terminal 
os.chdir(mypath)

# use ffmpeg to stitch the plots created 
ffmpeg_cmd="ffmpeg -r 7.5 -f image2 -i %d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p "
ffmpeg_cmd=ffmpeg_cmd+max_qval_video_name
os.system(ffmpeg_cmd)

# mv the file to your folder 
move_cmd="mv "+max_qval_video_name+" "+ str(sys.path[0])
os.system(move_cmd)

os.chdir(str(sys.path[0]))

# lets delete the directory with the plots 
os.system("rm -r -f episode_act_plots")



#--------------------------------
#
#	real time max q-val plotting 
#
#--------------------------------

mypath='episode_plots'
makedirs(mypath)

# iterate through the csv to plot the bars for each action
for i in range(len(tab.ix[:,1])):

	objects = ('stay', 'U', 'R', 'L', 'D', 'UR','UL','DR','DL')
	y_pos = np.arange(len(objects))
	performance = [tab.ix[i,0],tab.ix[i,1],tab.ix[i,2],tab.ix[i,3],tab.ix[i,4],tab.ix[i,5],tab.ix[i,6],tab.ix[i,7],tab.ix[i,8]]
	plt.bar(y_pos, performance, align='center', alpha=0.5)
	axes = plt.gca()
#	axes.set_xlim([0,len(y)])
	axes.set_ylim([np.min(tab.min(axis=1)),np.max(tab.max(axis=1))])
	plt.xticks(y_pos, objects)
	plt.ylabel('action')
	plt.title('Predicted Q_vals for actions')
 
	plt.savefig(os.path.join(mypath,str(i)))
	plt.clf()


# cd to the folder mypath and run the following command in the terminal 
os.chdir(mypath)

# use ffmpeg to stitch the plots created 
ffmpeg_cmd="ffmpeg -r 7.5 -f image2 -i %d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p "
ffmpeg_cmd=ffmpeg_cmd+act_qval_video_name
os.system(ffmpeg_cmd)

# mv the file to your folder 
move_cmd="mv "+act_qval_video_name+" "+str(sys.path[0])
os.system(move_cmd)

os.chdir(str(sys.path[0]))

# lets delete the directory with the plots 
os.system("rm -r -f episode_plots")



