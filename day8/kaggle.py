import pandas as pd

titanic = pd.read_csv('titanic.csv')

y = titanic['Survived']

features = ['Pclass', 'SibSp', 'Parch', 'Fare']

X = titanic[features].copy()

X['Sex'], genders = pd.factorize(titanic['Sex'])



##################################################
# 
# 1) Prepare the data
#
# Machine learning is regression with a sexier name.
#
# Fitting regression models requires clean numeric data.
# Typically we have an n x 1 vector response y and an n x p 
# predictor matrix X. 
#
# Much of the art is in preparing an appropriate X. 
# Tasks include:
#   - Separating validation data set
#   - Joins / calculated columns
#   - transform categorical data and text
#   - impute missing data
# 
##################################################


from sklearn.ensemble import RandomForestClassifier

rfmod = RandomForestClassifier()

rfmod.fit(X,y)



from sklearn.cross_validation import cross_val_score
scores = cross_val_score(rfmod,X,y,cv = 10)


##################################################
# 
# 2) Fit and evaluate models
# 
# Fitting models is easy in scikit learn.
#
# Some techniques:
#   - Cross validation
#   - Grid searches over model parameter spaces
#   - Various ways to score
# 
##################################################



##################################################
#
# 3) Predict
#
# Make predictions on new data using fitted model
#
##################################################
