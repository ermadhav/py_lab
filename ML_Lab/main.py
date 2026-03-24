import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
data = pd.read_csv("cleanned.csv")
data['sex'] = data['sex'].map({'Male':1, 'Female':0})
data['num'] = data['num'].apply(lambda x: 1 if x > 0 else 0)
data['age'] = pd.cut(data['age'], bins=[0,40,55,100], labels=[0,1,2])
data['trestbps'] = pd.cut(data['trestbps'], bins=[0,120,140,200], labels=[0,1,2])
data['chol'] = pd.cut(data['chol'], bins=[0,200,240,600], labels=[0,1,2])
data = data[['age','sex','cp','trestbps','chol','num']]
data = data.dropna()
model = DiscreteBayesianNetwork([('age','num'),('sex','num'),('cp','num'),('trestbps','num'),('chol','num')])
model.fit(data, estimator=MaximumLikelihoodEstimator)
infer = VariableElimination(model)
result = infer.query(variables=['num'],evidence={'age':1,'sex':1,'cp':'asymptomatic','trestbps':1,'chol':1})
print(result)