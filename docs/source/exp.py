#import modules
import pandas  as pd
import matplotlib.pyplot as plt
from epidpy.data_utils import get_country_data
from epidpy.growth_models import EpiGrowthModel

#Feed data to epidpy
dF=pd.read_csv("../data/covid-19-global.csv")
df=get_country_data(dF,'India')
df['removed'] = df['deaths'] + df['recovered']
df['infected'] = df['confirmed'] - df['removed']
data = df[['infected','removed']].copy()
data = data [data['infected'] > 25]
#
days_to_predict = 10
y_train, y_test = data[:-days_to_predict], data[-days_to_predict:]

# instantiate a model
model = EpiGrowthModel('logistic', normalize=True, calc_ci=True)

# train a model
model.fit(y_train)

# obtain fitted values
x_fitted, y_fitted = model.get_fitted

# obtain predictions
x_predicted, y_predicted = model.predict(days_to_predict)

# visualize
fig, ax = plt.subplots()
ax.plot(x_fitted, y_train, 'b.', label='[train] confirmed cases')
ax.plot(x_predicted, y_test, 'r.', label='[test] confirmed cases')
ax.plot(x_fitted, y_fitted[1], 'b-', label='fitted')
ax.fill_between(x_fitted, y_fitted[0], y_fitted[2], color='b', alpha=0.2, label='$95\%$ CI')
ax.plot(x_predicted, y_predicted[1], 'r-', label='predicted')
ax.fill_between(x_predicted, y_predicted[0], y_predicted[2], color='r', alpha=0.2)

ax.set_xlabel('$\Delta t$ days from Feb, $25^{th}$')
ax.set_ylabel('$N$')
ax.legend()
ax.grid()
plt.show()


