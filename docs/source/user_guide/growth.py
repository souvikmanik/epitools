#Select the specified column you want fit with EpiGrowthModel
cum_positive = df.Confirmed.values
#Split the data into train and test for validation of Exponentoal model
y_train, y_test = cum_positive[:90], cum_positive[90:105]
cum_positives1 = cum_positive[:190]
#If you want to fit using exponential growth model
model1 = EpiGrowthModel('exponential', normalize=True, calc_ci=True)
#If you want to fit using logistic growth model
model2 = EpiGrowthModel('logistic', normalize=True, calc_ci=True)
#fit model1 (exponential)
model1.fit(y_train)
x1, fitted1 = model1.get_fitted
#15 days prediction using model1
x_pred, y_pred = model1.predict(15)
#fit model2 (logistic)
model2.fit(cum_positives1)
x2, fitted2 = model2.get_fitted
#Now plot the data with best fitted result
plt.figure(figsize=(6,4))
plt.plot(x2, cum_positives1, '.', markersize=10, color='orange', label='confirmed positive cases')
plt.plot(x1, fitted1[1], '-.', color='green')
plt.plot(x_pred, y_pred[1], '-.', color='green', label='Exponential')
plt.plot(x2, fitted2[1], '-', color='red', label='Logistic')
plt.legend()
plt.xlabel('Days', fontsize=16)
plt.ylabel('Counts', fontsize=16)
