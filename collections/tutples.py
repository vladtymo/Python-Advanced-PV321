# ----- tuple - fixed-size imutable collection

coord = (12, -4, 0)

print(f"Coord: {coord[0]} : {coord[1]}")

# coord[1] = 0 # - error

location = (1.45634634, 12.855834, "Rivne", "Ukraine")

print(f"Country: {location[3]}")

# ---- destructuring
lon, lat, city, country = location

print(f"City: {city}")