import numpy as np

#Working with Mathematical Formulas
    #One of the things that makes numpy so special is it makes using mathematical formulas on arrays a piece of cake.

#useful image of Mean Square Formula: https://numpy.org/doc/stable/_images/np_MSE_formula.png
    #what makes this formula so viable is that predictions/labels can contain one or a thousand values
        #useful image: https://numpy.org/doc/stable/_images/np_mse_viz1.png
            #in this predictions and labels contain 3 vectors, meaning n has a value of three                                                   #pred = 1/1/1 
                                                #labels=1/2/3
#useful image: https://numpy.org/doc/stable/_images/np_mse_viz2.png
#useful image: https://numpy.org/doc/stable/_images/np_mse_viz2.png
#useful image: https://numpy.org/doc/stable/_images/np_MSE_explanation2.png



# error = (1/n) * np.sum(np.square(predictions - labels)))
# error = (1/3) * np.sum(np.square(predictions-labels)))
# error = (1/3) * np.sum(np.square(0/-1/-2))
# error = (1/3) * np.sum(0/1/4)
# error = (1/3) * 5
