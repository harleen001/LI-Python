from jinja2 import Template
import streamlit.components.v1 as components

def render_table(data):
    with open("table.html") as table_file:
        template = Template(table_file.read())
        return template.render(data=data)


data = [
    {"column1": "Row 1, Col 1", "column2": "Row 1, Col 2"},
    {"column1": "Row 2, Col 1", "column2": "Row 2, Col 2"}
]

# Now you can call the function because 'data' exists
table_html = render_table(data=data) 
components.html(table_html)