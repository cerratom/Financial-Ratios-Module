# This is a module of Financial Ratio

# Liquidity Ratio

# Defining the function to calculate the current ratio

def get_current_ratio(current_assets, current_liabilities):
    "Returns the current ratio. You will need to pass two values. The first value is for the parameter current assets and a second value for the parameter current liabilities"
    current_ratio = current_assets/current_liabilities
    return(current_ratio)

# Defining the function to calculate the quick or acid test ratio


def get_quick_ratio(current_assets, inventories, current_liabilities):
    "Returns the quick or acid test ratio. Your need to pass three values. The first value is for the parameter current assets, the second value for the parameter inventories, and a third value for the parameter current liabilities"
    quick_ratio = (current_assets - inventories)/current_liabilities
    return(quick_ratio)

# Defining the function to calculate the cash ratio


def get_cash_ratio(cash, current_liabilities, cash_equivalent=0):
    "Returns the cash ratio. Your need to pass atleast two values. The first value for the parameter cash account, the second value for parameter current liabilities, and an optional third value for the parameter cash equivalent assets."
    cash_ratio = (cash + cash_equivalent)/current_liabilities
    return(cash_ratio)

# Defining the function to calculate the Operating Cash Flow Ratio


def get_operating_cashflow_ratio(operating_cashflow, current_liabilities):
    "Returns the operating cashflow ratio. Your need to pass atleast two values. The first value for the parameter operating cashflow and the second value for parameter current liabilities."
    operating_cashflow_ratio = operating_cashflow / current_liabilities
    return(operating_cashflow_ratio)

# Leverage Ratio

# Defining the function to calculate the Debt to Equity Ratio


def get_debt_to_equity_ratio(total_liabilities, shareholders_equity):
    "Calculates the debt to equity ratio. You need to pass atleast two values. The first one is the value for total liabilities and the second value is shareholders equity."
    debt_to_equity_ratio = total_liabilities / shareholders_equity
    return(debt_to_equity_ratio)

# Defining the function to calculate the Debt to total assets ratio


def get_debt_to_total_assets_ratio(total_liabilities, total_assets):
    "Calculates the debt to total assets ratio. You need to pass two values. The first one is the value for total liabilities and the second value is for total assets."
    debt_to_total_assets_ratio = total_liabilities / total_assets
    return(debt_to_total_assets_ratio)

# Defining the function to calculate the interest coverage ratio


def get_interest_coverage_ratio(operating_income, interest_expenses):
    "Calculates the interest coverage ratio. You need to pass two values. The first one is the value for operating income and the second value is for interest expenses."
    interest_coverage_ratio = operating_income / interest_expenses
    return(interest_coverage_ratio)

# Defining the function to calculate the debt service coverage ratio


def get_debt_service_coverage_ratio(operating_income, total_debt_service):
    "Calculates the service coverage ratio. You need to pass two values. The first value is for operating income and the second value is for total_debt_service."
    debt_service_coverage_ratio = operating_income / total_debt_service
    return(debt_service_coverage_ratio)

# Efficiency Ratios

# Defining the function to calculate the Asset Turnover Ratio


def get_asset_turnonver_ratio(net_sales, total_assets):
    "Calculates the asset turnover ratio. You need to pass two values. The first one is the value for net sales and the second value is for total assets."
    asset_turnover_ratio = net_sales / total_assets
    return(asset_turnover_ratio)

# Defining the function to calculate the Inventory Turnover Ratio


def get_inventory_turnonver_ratio(cost_of_good_sold, average_inventory):
    "Calculates the inventory turnover ratio. You need to pass two values. The first one is the value for cost of goods sold and the average of inventory."
    inventory_turnover_ratio = cost_of_good_sold / average_inventory
    return(inventory_turnover_ratio)

# Defining the function to calculate the Receivable Turnover Ratio


def get_receivable_turnonver_ratio(net_credit_sales, average_account_receivables):
    "Calculates the receivable turnover ratio. You need to pass two values. The first one is the value for Net Credit Sales and the second value is for average account receivables."
    receivable_turnover_ratio = net_credit_sales / average_account_receivables
    return(receivable_turnover_ratio)

# Defining the function to calculate the day sale inventory Ratio


def get_day_sale_inventory_ratio(cost_of_good_sold, average_inventory):
    "Calculates the day sale inventory ratio. You need to pass two values. The first one is the value for cost of good sold and the second value is for average inventory."
    day_sale_inventory_ratio = 365 / \
        get_inventory_turnonver_ratio(cost_of_good_sold, average_inventory)
    return(day_sale_inventory_ratio)

# Profitability Ratios

# Defining the function to calculate the Gross Margin Ratio


def get_gross_margin_ratio(gross_profit, net_sales):
    "Calculates the gross margin ratio. You need to pass two values. The first one is the value for gross profit and the second value is for net sales."
    gross_margin_ratio = gross_profit / net_sales
    return(gross_margin_ratio)

# Defining the function to calculate the Operating Margin Ratio


def get_operating_margin_ratio(operating_income, net_sales):
    "Calculates the operating margin ratio. You need to pass two values. The first one is the value for operating income and the second value is for net sales."
    operating_margin_ratio = operating_income / net_sales
    return(operating_margin_ratio)

# Defining the function to calculate the Return on Asset Ratio


def get_return_on_asset_ratio(net_income, total_assets):
    "Calculates the return on asset ratio. You need to pass two values. The first one is the value for net income and the second value is for total assets."
    return_on_assets_ratio = net_income / total_assets
    return(return_on_assets_ratio)

# Defining the function to calculate the Return on Equity Ratio


def get_return_on_equity_ratio(net_income, shareholders_equity):
    "Calculates the return on equity ratio. You need to pass two values. The first one is the value for net income and the second value is for shareholders equity."
    return_on_equity_ratio = net_income / shareholders_equity
    return(return_on_equity_ratio)

# Market Value Ratios

# Defining the function to calculate the Book Value Per Share Ratio


def get_bookvalue__per_share_ratio(shareholders_equity, total_share_outstanding):
    "Calculates the Book Value per Share Ratio. You need to pass two values. The first one is the value for shareholders equity and the second value is for total shares outstanding."
    bookvalue_per_share_ratio = shareholders_equity / total_share_outstanding
    return(bookvalue_per_share_ratio)

# Defining the function to calculate the Divindend Yield Ratio


def get_dividend_yield_ratio(dividend_per_share, share_price):
    "Calculates the Dividend Yield Ratio. You need to pass two values. The first one is the value for dividend per share and the second value is for the share price."
    dividend_yield_ratio = dividend_per_share / share_price
    return(dividend_yield_ratio)

# Defining the function to calculate the Earning per Share Ratio


def get_earning_per_share_ratio(net_earning, total_share_outstanding):
    "Calculates the Earning per Share Ratio. You need to pass two values. The first one is the value for net earning and the second value is for the total sahres outstanding."
    earning_per_share_ratio = net_earning / total_share_outstanding
    return(earning_per_share_ratio)

# Defining the function to calculate the Price Earning Ratio


def get_price_earning_ratio(share_price, earning_per_share):
    "Calculates the Price Earning Ratio. You need to pass two values. The first one is the value for share price and the second value is for the earning per share."
    price_earning_ratio = share_price / earning_per_share
    return(price_earning_ratio)
