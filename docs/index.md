=======================================
InfoDESLib 
=======================================

**Dynamic Ensemble Selection library for regression tasks.**

InfoDESReg is open source library focusing the implementation of the state-of-the-art techniques for dynamic regressor and ensemble selection.
This project is under active development. Contributions are welcomed through its GitHub page: https://github.com/adv-panda/infodesreg   


**Example** 

.. code-block:: python  

  from infodeslreg.des import DES  
  
  pool_regressors = [regressor1, ..., regressorN]
  
  # Initialize the DS model
  des = DES(pool_regressors)
  
  # Fit the dynamic selection model
  des.fit(X_dsel, y_dsel) 
  
  # Predict new examples
  des.predict(X_test)
  
  # Check performance (based on MSE)
  des.score(X_test, y_test) 
