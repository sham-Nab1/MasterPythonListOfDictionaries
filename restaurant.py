# List of restaurant dictionaries
restaurants = [
    {"ID": 1, "Name": "Vikings Luxury Buffet", "Location": "Pasay City", "Cuisine Type": "Buffet", "Established Year": 2011, "Website": "www.vikings.ph"},
    {"ID": 2, "Name": "Antonio's Restaurant", "Location": "Tagaytay", "Cuisine Type": "Fine Dining", "Established Year": 2002, "Website": "www.antoniosrestaurant.ph"},
    {"ID": 3, "Name": "Mesa Filipino Moderne", "Location": "Makati City", "Cuisine Type": "Filipino", "Established Year": 2009, "Website": "www.mesa.ph"},
    {"ID": 4, "Name": "Manam Comfort Filipino", "Location": "Quezon City", "Cuisine Type": "Filipino", "Established Year": 2013, "Website": "www.manam.ph"},
    {"ID": 5, "Name": "Ramen Nagi", "Location": "Various Locations", "Cuisine Type": "Japanese", "Established Year": 2013, "Website": "www.ramennagi.com.ph"}
]

# Print restaurant data
for restaurant in restaurants:
    print(f"ID: {restaurant['ID']}, Name: {restaurant['Name']}, Location: {restaurant['Location']}, "
          f"Cuisine Type: {restaurant['Cuisine Type']}, Established Year: {restaurant['Established Year']}, "
          f"Website: {restaurant['Website']},")
