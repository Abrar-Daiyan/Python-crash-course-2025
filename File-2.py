#Topics :
# Formatted strings
# Lists
# Adding elements
# Deleting element
# Organizing lists
# Length meter function


# Formatted strings

x = "Daiyan"
print(x.title())
print(x.upper())
print(x.lower())
print(f"Hello {x}")

# Lists

xc = [1,2,3,4,5,6,7,8,9]
print(xc[0])

#* Adding elements

xc = [1,2,3,4,5,6,7,8,9]
xc.append(10)
print(xc)

#! Position setup :

xc = [1,2,3,4,5,6,7,8,9]
xc.insert(10,10)
print(xc)

#* Deleting element :

#Method 1
xc = [1,2,3,4,5,6,7,8,9]
del xc[2]
print(xc)

#Method 2 

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_cheap = 'ducati'
motorcycles.remove(too_cheap)
print(motorcycles)
print("\nA " + too_cheap.title() + " is too cheap for me.")


# Organizing lists : 

xc = ["Ibrahim","Nubaha","Lazina","Daiyan","Alim","Araf","Abdullah","Safira"]
xc.sort()
print(xc)

#Length meter function :  
xc = "Hello"
print(len(xc))

xc = [1,2,3,4,5,6,7,8,9]
print(len(xc))