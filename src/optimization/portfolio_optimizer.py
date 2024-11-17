from pypfopt import EfficientFrontier, risk_models, expected_returns

def optimize_portfolio(prices):
    # Calculate expected returns and covariance matrix
    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)

    # Create EfficientFrontier object
    ef = EfficientFrontier(mu, S)

    try:
        # Optimize for maximum Sharpe ratio
        ef.max_sharpe(risk_free_rate=0.001)  # Try lowering risk-free rate
    except ValueError as e:
        print(f"Error during optimization: {e}")
        return None, None  # Return None in case of error

    # Get cleaned weights
    cleaned_weights = ef.clean_weights()

    # Get portfolio performance
    performance = ef.portfolio_performance(verbose=True)

    return cleaned_weights, performance

# No need for an example usage in this file, since it's being used in the app
