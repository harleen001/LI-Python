import plotly.express as px

labels = [
    "Company",
    "Electronics", "Clothing",
    "Mobile", "Laptop", "Men", "Women"
]

parents = [
    "",                 # Company is root
    "Company", "Company",
    "Electronics", "Electronics",
    "Clothing", "Clothing"
]

values = [
    100,   # Company total
    60, 40,
    35, 25,
    20, 20
]

fig = px.sunburst(
    names=labels,
    parents=parents,
    values=values,
    title="Company Sales Breakdown"
)

fig.show()