from jinja2 import Template
import streamlit.components.v1 as components

def render_table(data):
               with open("templates/table.html") as table:
                   template = Template(table.read())
                   return template.render(
                       data=data
               )


table = render_table(data=data) # type: ignore
components.html(table)
