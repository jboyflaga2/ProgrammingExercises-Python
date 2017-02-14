
# feb 8, 2016

"""
1. The volume of a sphere with radius r is <insert fomula here>. 
What is the volume of a sphere with radius 5?
"""
def sphere_volume(radius):
    pi = 3.1416
    volume = (4/3) * pi * radius * radius * radius
    return volume

sphere_volume(5)

"""
2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?
"""
discount = 24.95 * 0.4
price_per_book = 24.95 - discount
total_cost_of_books = price_per_book * 60
shippping_cost_of_first_book = 3
shipping_cost_of_next_books = 0.75
total_cost_of_shipping = shippping_cost_of_first_book + (59 * shipping_cost_of_next_books)
total_cost = total_cost_of_books + total_cost_of_shipping

print(total_cost)


"""
3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
"""
minutes_part = 8 + (7 * 3) + 8
seconds_part = 15 + (12 * 3) + 15

# answer -> 38 mins and 5 secs of running
# answer -> you will get home at 7:30 am

