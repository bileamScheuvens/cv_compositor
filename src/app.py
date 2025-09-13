import streamlit as st
import yaml
import os
import random
import base64
from compose import write_document, compile_document, DATAPATH, OUTPATH, Section
from typing import List

locale = "en"
st.set_page_config(page_title="CV Compositor",layout="wide")

def read_section_from_yaml(filename):
    with open(os.path.join(DATAPATH, filename), "r") as f:
        return yaml.safe_load(f)

def displayPDF():
    # Opening file from file path
    with open(os.path.join(OUTPATH, "out.pdf"), "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="650" height="900" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

section_titles = [file for file in os.listdir(DATAPATH) if file.endswith(f"_{locale}.yaml")]
section_titles.remove(f"headers_{locale}.yaml")


def create_section_expander(section) -> List:
    """Creates collapsable element corresponding to CV section."""
    button_states = []
    # create expander
    with st.expander(section.title):
        # populate expander
        for (i, entry) in enumerate(section.entries):
            displayed_text ="\n\r".join((entry.values()))
            button_states.append(st.toggle(displayed_text, value=True))
        section.mask = button_states
    return button_states

sections = list(map(lambda st: Section(**read_section_from_yaml(st)), section_titles))
# sort sections with eps to randomly resolve conflicts
sections = sorted(sections, key=lambda s: s.preferred_pos + random.uniform(0,0.05))


input_col, compile_col, preview_col = st.columns([2.5,0.3, 2], gap="small")
with input_col:
    for s in sections:
        create_section_expander(s)

def write_and_compile():
    write_document(sections)
    compile_document(verbose=True)

with compile_col:
    st.button("compile", on_click=write_and_compile)

with preview_col:
    displayPDF()




