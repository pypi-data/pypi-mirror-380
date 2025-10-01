# Multi-Stock Regime Analysis Report
*Comprehensive Cross-Asset Regime Detection and Correlation Study*

## Executive Summary

This report presents a comprehensive regime analysis across **10 stocks** using Hidden Markov Model detection. The analysis identifies current market regimes, cross-asset correlations, and sector-based patterns to provide institutional-grade market intelligence.

### Key Findings

- **Market Consensus**: Sideways regime dominance (80.0% of stocks)
- **Average Cross-Correlation**: 0.077
- **Analysis Period**: 252 trading days
- **Regime Detection Method**: 3-state Hidden Markov Model

## Market Overview

### Current Regime Distribution

- **Sideways Regime**: 8 stocks (80.0%)
- **Bull Regime**: 1 stocks (10.0%)
- **Bear Regime**: 1 stocks (10.0%)


### Cross-Asset Correlation Analysis

The average regime correlation across all stock pairs is **0.077**, indicating weak regime synchronization across the market.

**Top Correlated Pairs**:
- SPY-QQQ: 0.608
- MSFT-BAC: -0.515
- MSFT-NFLX: 0.496
- BAC-NFLX: -0.392
- TSLA-QQQ: 0.391


## Sector Analysis

### Tech Giants

| Stock | Current Regime | Mean Return | Volatility | Frequency |
|-------|----------------|-------------|------------|-----------|
| AAPL | Sideways | 0.0025 | 0.0064 | 0.639 |
| MSFT | Bull | 0.0024 | 0.0061 | 0.649 |

**Sector Consensus**: Sideways (50.0%)

### Finance

| Stock | Current Regime | Mean Return | Volatility | Frequency |
|-------|----------------|-------------|------------|-----------|
| JPM | Sideways | 0.0016 | 0.0049 | 0.502 |
| BAC | Sideways | 0.0013 | 0.0097 | 0.829 |

**Sector Consensus**: Sideways (100.0%)

### Healthcare

| Stock | Current Regime | Mean Return | Volatility | Frequency |
|-------|----------------|-------------|------------|-----------|
| JNJ | Sideways | 0.0010 | 0.0068 | 0.854 |
| PFE | Sideways | -0.0045 | 0.0066 | 0.629 |

**Sector Consensus**: Sideways (100.0%)

### Consumer

| Stock | Current Regime | Mean Return | Volatility | Frequency |
|-------|----------------|-------------|------------|-----------|
| TSLA | Sideways | 0.0024 | 0.0184 | 0.551 |
| NFLX | Bear | -0.0048 | 0.0090 | 0.537 |

**Sector Consensus**: Bear (50.0%)

### Index ETFs

| Stock | Current Regime | Mean Return | Volatility | Frequency |
|-------|----------------|-------------|------------|-----------|
| SPY | Sideways | 0.0015 | 0.0048 | 0.790 |
| QQQ | Sideways | 0.0025 | 0.0051 | 0.590 |

**Sector Consensus**: Sideways (100.0%)



## Individual Stock Analysis

### Detailed Stock Performance

| Stock | Current Regime | Mean Return | Volatility | Duration | Data Points |
|-------|----------------|-------------|------------|----------|-------------|
| AAPL | Sideways | 0.0025 | 0.0064 | 8.7 | 205 |
| BAC | Sideways | 0.0013 | 0.0097 | 42.5 | 205 |
| JNJ | Sideways | 0.0010 | 0.0068 | 29.2 | 205 |
| JPM | Sideways | 0.0016 | 0.0049 | 10.3 | 205 |
| MSFT | Bull | 0.0024 | 0.0061 | 16.6 | 205 |
| NFLX | Bear | -0.0048 | 0.0090 | 7.9 | 205 |
| PFE | Sideways | -0.0045 | 0.0066 | 5.9 | 205 |
| QQQ | Sideways | 0.0025 | 0.0051 | 13.4 | 205 |
| SPY | Sideways | 0.0015 | 0.0048 | 12.5 | 205 |
| TSLA | Sideways | 0.0024 | 0.0184 | 8.7 | 205 |


## Methodology

### Regime Detection Framework

- **Model**: 3-state Hidden Markov Model with Gaussian emissions
- **States**: Bear, Sideways, Bull (classified by mean return)
- **Training**: Maximum Likelihood Estimation via Baum-Welch algorithm
- **Validation**: Out-of-sample state prediction and likelihood scoring

### Classification Criteria

- **Bear Regime**: Negative mean returns, typically high volatility
- **Bull Regime**: Positive mean returns, moderate to high volatility  
- **Sideways Regime**: Near-zero mean returns, typically lower volatility

### Correlation Analysis

Cross-asset regime correlations are calculated using Pearson correlation between regime state sequences, providing insights into market-wide regime synchronization.

## Investment Implications

### Portfolio Management

1. **Regime Diversification**: Current 80.0% consensus suggests limited diversification benefits across assets

2. **Sector Rotation**: Strong sector differentiation provides rotation opportunities

3. **Risk Management**: Moderate correlation allows for some risk diversification

### Trading Strategies

- **Consensus Plays**: 80.0% of stocks in Sideways regime suggests directional opportunities
- **Contrarian Opportunities**: Stocks in minority regimes may offer contrarian value
- **Regime Momentum**: High correlation (0.077) suggests regime changes may cascade across assets

## Risk Considerations

- **Model Risk**: HMM assumptions may not capture all market dynamics
- **Parameter Stability**: Regime parameters may shift during market stress
- **Look-ahead Bias**: Real-time implementation may differ from historical analysis
- **Transaction Costs**: Regime switching strategies require active management

## Conclusion

The multi-stock regime analysis reveals **Sideways regime dominance** across 80.0% of analyzed stocks, with 0.077 average cross-correlation indicating partially synchronized market behavior.

This analysis provides a quantitative foundation for:
- Strategic asset allocation decisions
- Risk management framework development
- Systematic trading strategy implementation
- Market timing and regime transition identification

---

*This analysis is for educational and research purposes only. Past performance does not guarantee future results. Please consult with qualified financial advisors before making investment decisions.*

*Generated using Hidden Regime framework - [hiddenregime.com](https://hiddenregime.com)*
