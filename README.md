## InfoDESReg


### Installation 

```bash
pip install infodesreg
```


### Example 

Loading necessary libraries and dataset:  

```python
import pandas as pd 

# models 
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression 

# metrics 
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import LabelEncoder
from ucimlrepo import fetch_ucirepo

# dataset
from ucimlrepo import fetch_ucirepo   

# InfoDESReg 
from infodesreg import DES
```

Loading data: 

```python
abalone = fetch_ucirepo(id=1) 
X = abalone.data.features 
y = abalone.data.targets  

le = LabelEncoder() 
X['Sex'] = le.fit_transform(X['Sex'])  

```

Split the dataset into training, validation for DES (DSEL) and testing.  
```python
TEST_SIZE = 0.2 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=42) 
X_train, X_dsel, y_train, y_dsel = train_test_split(X_train, y_train, test_size=0.2, random_state=42)   
```

1. Models pool generation 

```python
pool_models = [
    XGBRegressor(random_state=42), 
    RandomForestRegressor(random_state=42), 
    LinearRegression(), 
    KNeighborsRegressor(), 
]
```

2. Train the models (pool): 

```python 
for model in pool_models: 
    model.fit(X_train, y_train)  
```

3. Usage of our library: 

```python
des = DES(pool_regressors=pool_models, 
          k=6, 
          knn_metric='minkowski', 
          metrics='mape', 
          threshold=0.1)

des.fit(X_dsel, y_dsel) 
``` 

4. Testing 

```python 
des.score(X_test, y_test) # based on MSE 
```

5. Explainability 

```python 
index = 47
X_test.iloc[index]

prediction, contribution_df, neighbors_df = des.predict_xai(X_test.iloc[[index]])

print(prediction) 
```
