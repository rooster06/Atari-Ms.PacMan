# Deep Learning for Computer Graphics
## Final Project (Deep Reinforcement Learning: Playing Ms. Pac-Man)
### Prabhat Rayapati (pr2sn), Zack Verham (zdv8rb)


This repository contains our final project for CS6501 (Deep Learning for Computer Graphics). For our project, we implemented the deep learning pipeline proposed in [Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf) (Mnih et. al., 2013), and built a learner which takes as input the pixel-array output of an Atari Emulator (we are grateful for the Atari interface offered by the [Open AI Gym](https://gym.openai.com/) project), and learns to play Ms. Pac-Man better than an agent which takes naive random actions.


### Required Packages
- OpenAI Gym (plus atari module)
- numpy
- skimage
- Keras (we utilized the Tensorflow interface)
- matplotlib

### To Run:
After installing the required packages and setting the relevant hyperparameters in ```test.py```, simply run:

```python test.py```

to begin the learning process. The script will also periodically output videos of particular episodes (the paths to which are specified by the I/O hyperaparmeters in ```test.py```.


### Other repository elements:
- ```agent.py```: encapsulates the learning/decision-making code
- ```plot_output.py```: used to plot various logged values collected during the training process
- ```qval_plotting.py```: used to plot q_value data as live videos given the logged q-values from a given training run
- ```docs/```: contains both the final writeup pdf and the latex files used to generate our final report
- ```visualizations```: contains examples of qval_plotting.py output (videos representing network output over time as the game is played)
