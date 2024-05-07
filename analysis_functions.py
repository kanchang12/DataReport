import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_mean(data, column):
    """
    Calculate the mean of a numerical column in the data.
    """
    return data[column].mean()

def calculate_median(data, column):
    """
    Calculate the median of a numerical column in the data.
    """
    return data[column].median()

def calculate_mode(data, column):
    """
    Calculate the mode(s) of a categorical or numerical column in the data.
    """
    return data[column].mode()

def calculate_variance(data, column):
    """
    Calculate the variance of a numerical column in the data.
    """
    return data[column].var()

def calculate_standard_deviation(data, column):
    """
    Calculate the standard deviation of a numerical column in the data.
    """
    return data[column].std()

def calculate_skewness(data, column):
    """
    Calculate the skewness of a numerical column in the data.
    """
    return stats.skew(data[column])

def calculate_kurtosis(data, column):
    """
    Calculate the kurtosis of a numerical column in the data.
    """
    return stats.kurtosis(data[column])

def perform_t_test(data1, data2):
    """
    Perform a t-test to compare the means of two datasets.
    """
    t_statistic, p_value = stats.ttest_ind(data1, data2)
    return t_statistic, p_value

def perform_chi_square_test(data, column1, column2):
    """
    Perform a chi-square test of independence between two categorical variables.
    """
    contingency_table = pd.crosstab(data[column1], data[column2])
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    return chi2, p_value

def perform_one_way_anova(data, groups_column, values_column):
    """
    Perform one-way ANOVA to compare means across multiple groups.
    """
    groups = [group for group, df in data.groupby(groups_column)]
    values = [df[values_column] for group, df in data.groupby(groups_column)]
    f_statistic, p_value = stats.f_oneway(*values)
    return f_statistic, p_value

def perform_linear_regression(data, x_column, y_column):
    """
    Perform linear regression between two numerical columns.
    """
    X = sm.add_constant(data[x_column])
    model = sm.OLS(data[y_column], X)
    results = model.fit()
    return results.summary()

def generate_histogram(data, column):
    """
    Generate a histogram for a numerical column in the data.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def generate_boxplot(data, column):
    """
    Generate a boxplot for a numerical column in the data.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data[column])
    plt.title(f"Boxplot of {column}")
    plt.xlabel(column)
    plt.show()

def perform_correlation(data, column1, column2):
    """
    Perform Pearson correlation analysis between two numerical columns.
    """
    correlation_coefficient, p_value = stats.pearsonr(data[column1], data[column2])
    return correlation_coefficient, p_value

def calculate_z_score(data, column):
    """
    Calculate the Z-score for a numerical column in the data.
    """
    z_scores = (data[column] - data[column].mean()) / data[column].std()
    return z_scores

def calculate_percentile(data, column, percentile):
    """
    Calculate the specified percentile of a numerical column in the data.
    """
    return np.percentile(data[column], percentile)

def calculate_entropy(data, column):
    """
    Calculate the entropy of a categorical column in the data.
    """
    value_counts = data[column].value_counts(normalize=True, dropna=False)
    entropy = -np.sum(value_counts * np.log2(value_counts))
    return entropy

def calculate_cumulative_sum(data, column):
    """
    Calculate the cumulative sum of a numerical column in the data.
    """
    return data[column].cumsum()

def calculate_exponential_moving_average(data, column, span=30):
    """
    Calculate the exponential moving average of a numerical column in the data.
    """
    return data[column].ewm(span=span, adjust=False).mean()

def calculate_rolling_mean(data, column, window=30):
    """
    Calculate the rolling mean of a numerical column in the data.
    """
    return data[column].rolling(window=window).mean()

def calculate_autocorrelation(data, column, lag=1):
    """
    Calculate the autocorrelation of a numerical column in the data.
    """
    return data[column].autocorr(lag=lag)

def calculate_cdf(data, column, value):
    """
    Calculate the cumulative distribution function (CDF) of a numerical column in the data.
    """
    return stats.percentileofscore(data[column], value) / 100

def perform_logistic_regression(data, x_columns, y_column):
    """
    Perform logistic regression using specified predictor columns and target column.
    """
    X = sm.add_constant(data[x_columns])
    y = data[y_column]
    model = sm.Logit(y, X)
    results = model.fit()
    return results.summary()

def perform_pca(data, columns, n_components=2):
    """
    Perform Principal Component Analysis (PCA) on specified columns with the given number of components.
    """
    X = data[columns]
    pca = PCA(n_components=n_components)
    pca.fit(X)
    return pca.transform(X)

def calculate_mann_whitney_u(data1, data2):
    """
    Calculate the Mann-Whitney U statistic to compare two independent samples.
    """
    return stats.mannwhitneyu(data1, data2)

def calculate_bayesian_inference(data, column):
    """
    Perform Bayesian inference on a numerical column in the data.
    """
    return sm.BayesGaussianMixture(data[column])

def calculate_seasonal_decomposition(data, column, model='additive'):
    """
    Perform seasonal decomposition on a time series column in the data.
    """
    decomposition = sm.tsa.seasonal_decompose(data[column], model=model)
    return decomposition.plot()

def calculate_log_return(data, column):
    """
    Calculate the log return of a numerical column representing stock prices.
    """
    return np.log(data[column] / data[column].shift(1))

def calculate_poisson_distribution(data, column):
    """
    Fit a Poisson distribution to count data in a numerical column.
    """
    return stats.poisson.fit(data[column])

def calculate_empirical_cdf(data, column):
    """
    Calculate the empirical cumulative distribution function (ECDF) of a numerical column in the data.
    """
    return sm.distributions.ECDF(data[column])

def calculate_power_transform(data, column, method='yeo-johnson'):
    """
    Apply power transform to a numerical column in the data.
    """
    pt = preprocessing.PowerTransformer(method=method)
    transformed_data = pt.fit_transform(data[column].values.reshape(-1, 1))
    return transformed_data

def calculate_grouped_summary_statistics(data, group_column, value_column, statistic='mean'):
    """
    Calculate summary statistics (e.g., mean, median, etc.) for groups in the data.
    """
    return data.groupby(group_column)[value_column].agg(statistic)

def detect_outliers_z_score(data, column, threshold=3):
    """
    Detect outliers using Z-score method for a numerical column in the data.
    """
    z_scores = np.abs(stats.zscore(data[column]))
    return np.where(z_scores > threshold)[0]

def detect_outliers_iqr(data, column):
    """
    Detect outliers using IQR method for a numerical column in the data.
    """
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    return data[(data[column] < Q1 - 1.5 * IQR) | (data[column] > Q3 + 1.5 * IQR)]

def calculate_cumulative_distribution(data, column):
    """
    Calculate the cumulative distribution of a numerical column in the data.
    """
    return data[column].value_counts(normalize=True).cumsum()

def calculate_hypothesis_test(data, column, test='normaltest'):
    """
    Perform a hypothesis test to check for normality of a numerical column in the data.
    """
    if test == 'normaltest':
        return stats.normaltest(data[column])
    elif test == 'shapiro':
        return stats.shapiro(data[column])
    elif test == 'anderson':
        return stats.anderson(data[column])

# Additional functions can be added based on specific requirements
