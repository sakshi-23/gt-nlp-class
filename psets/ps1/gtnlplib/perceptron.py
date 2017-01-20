from collections import defaultdict
from gtnlplib.clf_base import predict,make_feature_vector,argmax

def perceptron_update(x,y,weights,labels):
    """compute the perceptron update for a single instance

    :param x: instance, a counter of base features and weights
    :param y: label, a string
    :param weights: a weight vector, represented as a dict
    :param labels: set of possible labels
    :returns: updates to weights, which should be added to weights
    :rtype: defaultdict

    """
    # f(x,y) - f(x,y_hat)
    feature_vecs = {l:make_feature_vector(x,l) for l in labels}
    y_hat, scores = predict(x,weights,labels)
    if y_hat == y:
        return defaultdict(float)
    delta = defaultdict(float)
    for k in feature_vecs[y].keys():
        delta[k] += feature_vecs[y][k]
    for k in feature_vecs[y_hat].keys():
        delta[k] -= feature_vecs[y_hat][k]
    return delta


def estimate_perceptron(x,y,N_its):
    """estimate perceptron weights for N_its iterations over the dataset (x,y)

    :param x: list of instances, each a counter of base features and weights
    :param y: list of labels, each a string
    :param N_its: number of iterations over the entire dataset
    :returns: weight dictionary
    :returns: list of weights dictionaries at each iteration
    :rtype: defaultdict, list

    """
    labels = set(y)
    weights = defaultdict(float)
    weight_history = []
    for it in xrange(N_its):
        for x_i,y_i in zip(x,y):
            # YOUR CODE GOES HERE
            raise NotImplementedError
        weight_history.append(weights.copy())
    return weights, weight_history

def estimate_avg_perceptron(x,y,N_its):
    """estimate averaged perceptron classifier

    :param x: list of instances, each a counter of base features and weights
    :param y: list of labels, each a string
    :param N_its: number of iterations over the entire dataset
    :returns: weight dictionary
    :returns: list of weights dictionaries at each iteration
    :rtype: defaultdict, list

    """
    labels = set(y)
    w_sum = defaultdict(float) #hint
    weights = defaultdict(float)
    weight_history = []
    
    t=1.0 #hint
    for it in xrange(N_its):
        for x_i,y_i in zip(x,y):
            # YOUR CODE GOES HERE
            raise NotImplementedError
        weight_history.append(avg_weights.copy())
    return avg_weights, weight_history
