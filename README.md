# OptionsPredictor
This uses machine learning to predict if a particular option will expire in the money or not. 

OptionsParser.py parses a given set of JSON's into 3 csv's: calls, puts, and main. These CSV's contain data on: optionsExpire,inTheMoney,optionType,strikePrice,volume,delta,gamma,iv,rho,theta,vega


For the K-nearest-neighbor predictions, the following features are selected for prediciton: optionsExpire, strikePrice, volume, delta, gamma, iv, rho, theta, vega
  to increase accuracy, select only the greeks and optionsExpire: optionsExpire, delta, gamma, iv, rho, theta, vega
