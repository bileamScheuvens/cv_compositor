import streamlit as st
import yaml
import os
from compose import write_document, compile_document, DATAPATH, OUTPATH, Section

def read_section_from_yaml(name):
    with open(os.path.join(DATAPATH, f"{name}_en.yaml"), "r") as f:
        return yaml.safe_load(f)

components = ["education", "experience", "skills", "projects", "awards", "publications"]

edu = Section(**read_section_from_yaml("education"))
button_states = []
with st.expander(edu.title):
    for (i, entry) in enumerate(edu.entries):

        displayed_text ="\n\r".join((entry.values()))

        button_states.append(st.toggle(displayed_text, value=True))
    edu.mask = button_states
    st.write(str(edu))



