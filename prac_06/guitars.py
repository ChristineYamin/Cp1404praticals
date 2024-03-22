"""
Word Occurrences
Estimate: 30 minutes
Actual:   35 minutes
"""

from prac_06.guitar import Guitar

guitars =[]
print("My guitars!!")
# guitar_name = input("Name :")
# guitar_year = input(" Year :")
# guitar_cost = input(" Cost :")
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
guitars.append(Guitar("Fender Stratocaster" ,2014 , 765.40 ))


print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}  {vintage_string}")
