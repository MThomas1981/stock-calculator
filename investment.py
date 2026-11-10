# Stock Investment Calculator

# Version 1 - Calculate Investment Cost
stock_name = "Apple"
number_of_shares = 10
share_price = 150

investment_cost = number_of_shares * share_price

print("Stock:", stock_name)
print("Number of shares:", number_of_shares)
print("Purchase price per share: $", share_price)
print("Total investment cost: $", investment_cost)

# Version 2 - Calculate Investment Profit and Return
new_share_price = 175

current_value = new_share_price * number_of_shares
profit_or_loss = current_value - investment_cost
percentage_return = (profit_or_loss / investment_cost) * 100

print("New price per share: $", new_share_price)
print("Current investment value: $", current_value)
print("Profit or loss: $", profit_or_loss)
print("Percentage return:", round(percentage_return, 2), "%")
