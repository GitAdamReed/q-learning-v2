import numpy as np

#Do this second
#stateParams are the x and y coordinates of the agent

def RL_select_action(QMatrix, stateParams, epsilon):
    #VARIABLES
    #epsilon = 0.01 #PROBABILITY OF RANDOM ACTION BEING CHOSEN
    numStateParams = len(stateParams)
    numActions = np.size(QMatrix, numStateParams)
    
    if numStateParams > 5:
        print('A MAXIMUM OF FIVE REWARD PARAMETERS ARE ALLOWED!')
        return None
    
    #EPSILON GREEDINESS
    if np.random.random() < epsilon:
        action = np.random.randint(0, numActions)
        
    else:
        params = stateParams
        #EXTRACT THE REWARD VALUES ASSOCIATED WITH EACH RESPECTIVE ACTION
        if numStateParams == 1:
            currQs = QMatrix[params[0], :]
        elif numStateParams == 2:
            currQs = QMatrix[params[0], params[1], :]
        elif numStateParams == 3:
            currQs = QMatrix[params[0], params[1], params[2], :]
        elif numStateParams == 4:
            currQs = QMatrix[params[0], params[1], params[2], params[3], :]
        elif numStateParams == 5:
            currQs = QMatrix[params[0], params[1], params[2], params[3], params[4], :]
        
        #SELECT ACTION WITH HIGHEST REWARD
        action = list(np.where(np.array(currQs)==max(currQs))[0])
        
        #IN THE CASE OF A TIE, SELECT A RANDOM ACTION IN THE TIE
        if len(action) > 1:
           temp = np.random.randint(0, len(action))
           action = action[temp]

    return action
