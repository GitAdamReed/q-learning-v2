import numpy as np

#Do this first
#stateSizes are the width and height of the environment
#numActions are how many possible actions can be taken by the agent
#numActions in this case are up, down, left, right

def RL_create_qmatrix(stateSizes, numActions):
    #VARIABLES
    numParams = len(stateSizes);
    
    #INITIALISE QMATRIX BASED ON GIVEN DIMENSION SIZES
    if numParams == 1:
        QMatrix = np.zeros((stateSizes[0], numActions));
    elif numParams == 2:
        QMatrix = np.zeros((stateSizes[0], stateSizes[1], numActions));
    elif numParams == 3:
        QMatrix = np.zeros((stateSizes[0], stateSizes[1], stateSizes[2], numActions));
    elif numParams == 4:
        QMatrix = np.zeros((stateSizes[0], stateSizes[1], stateSizes[2], stateSizes[3], numActions));
    elif numParams == 5:
        QMatrix = np.zeros((stateSizes[0], stateSizes[1], stateSizes[2], stateSizes[3], stateSizes[4], numActions));
    else:
        print("A MAXIMUM OF FIVE REWARD PARAMETERS ARE ALLOWED!")
    
    return QMatrix
