import numpy as np


def empirical_risk(theta: float, b: float, data: np.ndarray) -> float:
    """
    Compute the empirical risk of a set of parameters
    for a linear prediction, in 1 dimension.
    """
    X = data[:, 0]
    y = data[:, 1]
    predictions = X * theta + b
    errors = predictions - y
    empirical_risk = np.linalg.norm(errors) ** 2
    return empirical_risk


def optimal_params(data: np.ndarray) -> tuple[float, float]:
    """
    Compute the optimal theta and b, obtained by
    gradient cancellation
    """
    X = data[:, 0]
    y = data[:, 1]

    n_samples = X.shape[0]

    # intermediate quantities
    sum_xy = np.sum(X * y)
    sum_xx = np.sum(X * X)
    sum_x_2 = np.sum(X)**2
    sum_y = np.sum(y)
    sum_x = np.sum(X)

    # apply formulas for gradient cancellation
    theta_star = (sum_xy - sum_x*sum_y/n_samples)/(sum_xx - sum_x_2/n_samples)
    b_star = (sum_y-theta_star*sum_x)/n_samples

    return theta_star, b_star
