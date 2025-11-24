import numpy as np

#Do this last
#stateParams are the old coords, nextStateParams are the new coords

def RL_update_QMatrix(QMatrix, stateParams, nextStateParams, rewardParams, action):
    #VARIABLES
    alpha = 1 #LEARNING RATE
    gamma = 0.9 #DISCOUNT FACTOR
    numStateParams = len(stateParams)

    if numStateParams > 5:
        print('A MAXIMUM OF FIVE REWARD PARAMETERS ARE ALLOWED!')
        return None
    
    #CALCULATE THE REWARD
    reward = np.sum(rewardParams) #!!!AMEND FORMULA BASED ON NEEDS!!!

    #EXTRACT THE REWARD VALUES ASSOCIATED WITH EACH RESPECTIVE ACTION
    if numStateParams == 1:
        nextQs = QMatrix[nextStateParams[0], :]
    elif numStateParams == 2:
        nextQs = QMatrix[nextStateParams[0], nextStateParams[1], :]
    elif numStateParams == 3:
        nextQs = QMatrix[nextStateParams[0], nextStateParams[1], nextStateParams[2], :]
    elif numStateParams == 4:
        nextQs = QMatrix[nextStateParams[0], nextStateParams[1], nextStateParams[2], nextStateParams[3], :]
    elif numStateParams == 5:
        nextQs = QMatrix[nextStateParams[0], nextStateParams[1], nextStateParams[2], nextStateParams[3], nextStateParams[4], :]
    
    #GET THE ACTION WITH THE HIGHEST REWARD
    maxQVal = max(nextQs)
    newQMatrix = QMatrix

    #UPDATE THE QMATRIX FOR OUTPUT
    V = [QMatrix, maxQVal, action, alpha, gamma, reward, stateParams]
    
    if numStateParams == 1:
        newQMatrix[stateParams[0], action] = calcQ(V)
    elif numStateParams == 2:
        newQMatrix[stateParams[0], stateParams[1], action] = calcQ(V)
    elif numStateParams == 3:
        newQMatrix[stateParams[0], stateParams[1], stateParams[2], action] = calcQ(V)
    elif numStateParams == 4:
        newQMatrix[stateParams[0], stateParams[1], stateParams[2], stateParams[3], action] = calcQ(V)
    elif numStateParams == 5:
        newQMatrix[stateParams[0], stateParams[1], stateParams[2], stateParams[3], stateParams[4], action] = calcQ(V)

    return newQMatrix    
    
def calcQ(V):
    QMatrix, maxQVal, action, alpha, gamma, reward, stateParams = V
    numStateParams = len(stateParams)
    
    if alpha == 1:
        newQ = reward + gamma * maxQVal 
    else:
        if numStateParams == 1:
            newQ = (1 - alpha) * QMatrix[stateParams[0], action] + alpha * (reward + gamma * maxQVal)
        elif numStateParams == 2:
            newQ = (1 - alpha) * QMatrix[stateParams[0], stateParams[1], action] + alpha * (reward + gamma * maxQVal)                
        elif numStateParams == 3:
            newQ = (1 - alpha) * QMatrix[stateParams[0], stateParams[1], stateParams[2], action] + alpha * (reward + gamma * maxQVal)                
        elif numStateParams == 4:
            newQ = (1 - alpha) * QMatrix[stateParams[0], stateParams[1], stateParams[2], stateParams[3], action] + alpha * (reward + gamma * maxQVal)                
        elif numStateParams == 5:
            newQ = (1 - alpha) * QMatrix[stateParams[0], stateParams[1], stateParams[2], stateParams[3], stateParams[4], action] + alpha * (reward + gamma * maxQVal)                

    return newQ
