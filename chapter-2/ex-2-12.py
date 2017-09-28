#Exercise 2-12

#Joe's stock
#Purchased 2000 shares
#Paid 40 per share
#3% commission

#Sold 2000 shares
#Sold for 42.75 per share
#3% commission

#Display amount paid
#Commision paid when he bought the stock
#Amount he sold the stock for
#Commission paid when he sold the stock
#Display the total money he has left over

shares_bought = 2000
buy_price_per_share = 40
buy_commission_rate = .03
shares_sold = 2000
sell_price_per_share = 42.75
sell_commission_rate = .03

amount_buy = shares_bought * buy_price_per_share
buy_commission = amount_buy * buy_commission_rate
total_paid = amount_buy + buy_commission
amount_sell = shares_sold * sell_price_per_share
sell_commission = amount_sell * sell_commission_rate
total_made = amount_sell - sell_commission
money_left = total_made - total_paid

print("Joe paid", format(amount_buy, '.2f'), "for his stocks and", format(buy_commission, '.2f'), "as commission. In total he paid", format(total_paid, '.2f'), "for his stocks.")
print("Joe made", format(amount_sell, '.2f'), "from his stocks, but he paid", format(sell_commission, '.2f'), "as commission. He made", format(total_made, '.2f'), "selling his stocks.")
print("Joe actually made", format(money_left, '.2f'), "in total.")
