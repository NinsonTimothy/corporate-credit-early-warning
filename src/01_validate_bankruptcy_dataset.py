from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff("C:/Users/timot/Documents/ML_Career_Portfolio/01_corporate_credit_early_warning/data/raw/5year.arff")
df = pd.DataFrame(data)

# df.to_csv("C:/Users/timot/Documents/ML_Career_Portfolio/01_corporate_credit_early_warning/data/processed/5year.csv", index=False)


working_data = pd.read_csv("C:/Users/timot/Documents/ML_Career_Portfolio/01_corporate_credit_early_warning/data/processed/5year.csv")
print("The shape of the dataset is", working_data.shape, end = "\n\n")
print("The dataset has", working_data.shape[1], " features", end = "\n\n")
print("The dataset has", working_data.shape[0], " observations", end = "\n\n")

print("The target columnn or feature of this dataset is the class", end = "\n\n")
print(working_data["class"].head(20), end = "\n\n")

print("The total number of missing values in the dataset are :", working_data.isnull().sum(), end = "\n\n")

print("The number of duplicates in the dataset",working_data.duplicated().sum(), end = "\n\n")

print("The data types of each column can be found below")
print(working_data.dtypes, end = "\n\n")
bankrupt_companies =working_data[working_data["class"] == "b'1'"]
Bankrupt_prevalence =(len(bankrupt_companies)/ len(working_data)) * 100

print("The bankrupt prevalence is ", Bankrupt_prevalence, end = "\n\n")

print(working_data.info())


feature_names = [
    "net_profit_to_total_assets",
    "total_liabilities_to_total_assets",
    "working_capital_to_total_assets",
    "current_assets_to_short_term_liabilities",
    "liquid_assets_net_st_liabilities_days",
    "retained_earnings_to_total_assets",
    "ebit_to_total_assets",
    "book_equity_to_total_liabilities",
    "sales_to_total_assets",
    "equity_to_total_assets",
    "gross_profit_extraordinary_finexp_to_total_assets",
    "gross_profit_to_short_term_liabilities",
    "gross_profit_plus_depreciation_to_sales",
    "gross_profit_plus_interest_to_total_assets",
    "liabilities_days_to_gross_profit_plus_depreciation",
    "gross_profit_plus_depreciation_to_total_liabilities",
    "total_assets_to_total_liabilities",
    "gross_profit_to_total_assets",
    "gross_profit_to_sales",
    "inventory_days_to_sales",
    "sales_growth_ratio",
    "operating_profit_to_total_assets",
    "net_profit_to_sales",
    "three_year_gross_profit_to_total_assets",
    "equity_minus_share_capital_to_total_assets",
    "net_profit_plus_depreciation_to_total_liabilities",
    "operating_profit_to_financial_expenses",
    "working_capital_to_fixed_assets",
    "log_total_assets",
    "liabilities_minus_cash_to_sales",
    "gross_profit_plus_interest_to_sales",
    "current_liabilities_days_to_cogs",
    "operating_expenses_to_short_term_liabilities",
    "operating_expenses_to_total_liabilities",
    "profit_on_sales_to_total_assets",
    "total_sales_to_total_assets",
    "current_assets_minus_inventory_to_long_term_liabilities",
    "constant_capital_to_total_assets",
    "profit_on_sales_to_sales",
    "current_assets_minus_inventory_receivables_to_st_liabilities",
    "liabilities_to_annualized_operating_cash_proxy",
    "operating_profit_to_sales",
    "receivables_plus_inventory_turnover_days",
    "receivables_days",
    "net_profit_to_inventory",
    "current_assets_minus_inventory_to_st_liabilities",
    "inventory_days_to_cogs",
    "documented_ebitda_to_total_assets",
    "documented_ebitda_to_sales",
    "current_assets_to_total_liabilities",
    "short_term_liabilities_to_total_assets",
    "short_term_liabilities_days_to_cogs",
    "equity_to_fixed_assets",
    "constant_capital_to_fixed_assets",
    "working_capital",
    "sales_minus_cogs_to_sales",
    "liquidity_balance_to_cost_base",
    "total_costs_to_total_sales",
    "long_term_liabilities_to_equity",
    "sales_to_inventory",
    "sales_to_receivables",
    "short_term_liabilities_days_to_sales",
    "sales_to_short_term_liabilities",
    "sales_to_fixed_assets"
]

rename_map = {
    f"Attr{i + 1}": name
    for i, name in enumerate(feature_names)
}

rename_map["class"] = "bankrupt_within_1y"

named_data = working_data.rename(columns=rename_map)

named_data.to_csv(
    "C:/Users/timot/Documents/ML_Career_Portfolio/01_corporate_credit_early_warning/data/processed/5year_named.csv",
    index=False
)

named_df = pd.read_csv("C:/Users/timot/Documents/ML_Career_Portfolio/01_corporate_credit_early_warning/data/processed/5year_named.csv")
print(named_df.info())