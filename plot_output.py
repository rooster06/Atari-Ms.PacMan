"""
Utility script for plotting logs from training process

Prabhat Rayapati (pr2sn)
Zack Verham (zdv8rb)
Deep Learning for Computer Graphics (Fall 2016)
Final Project
"""


import sys
import matplotlib.pyplot as plt
import numpy as np

def main(args):
    print "running %s" % args[0]
    print "input path: %s" % args[1]

    #parse logfile
    with open(args[1], "r") as f:
        lines = f.readlines()

        X = range(len(lines))

        time_y = []
        reward_y = []

        for line in lines:

            #Expected data format:
            #<episode,timesteps survived,reward collected>

            data_row = line.strip().split(",")
            episode = int(data_row[0])
            time = float(data_row[1])
            reward = float(data_row[2])

            time_y.append(time)
            reward_y.append(reward)

        #plot logged data
        plt.plot(X, time_y, 'r')
        plt.plot(X, np.poly1d(np.polyfit(X, time_y, 1))(X), 'b')

        # plt.plot(X, reward_y, 'r')
        # plt.plot(X, np.poly1d(np.polyfit(X, reward_y, 1))(X), 'b')

        plt.xlabel("Episode")
        plt.ylabel("Timesteps")
        plt.title("Timesteps per Episode")

        plt.show()


if __name__ == "__main__":
    main(sys.argv)
