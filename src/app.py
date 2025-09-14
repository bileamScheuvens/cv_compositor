import streamlit as st
import yaml
import os
import random
import base64
from typing import List

from cv_components import Section
from utils import write_and_compile_document, read_persistent_state, DATAPATH, OUTPATH

locale = "en"
st.set_page_config(page_title="CV Compositor",layout="wide")

def read_section_from_yaml(filename):
    with open(os.path.join(DATAPATH, filename), "r") as f:
        return yaml.safe_load(f)

def displayPDF(filename):
    # Opening file from file path
    with open(os.path.join(OUTPATH, f"{filename}.pdf"), "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="800" type="application/pdf"></iframe>'

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
            # TODO update toggles when state is loaded 
            button_states.append(st.toggle(displayed_text, value=section.mask[i]))
        section.mask = button_states
    # return button_states

sections = list(map(lambda st: Section(**read_section_from_yaml(st)), section_titles))
# sort sections with eps to randomly resolve conflicts
sections = sorted(sections, key=lambda s: s.preferred_pos + random.uniform(0,0.05))



input_col, preview_col = st.columns([2.5, 2], gap="medium")
with input_col:
    for s in sections:
        create_section_expander(s)

def filename_changed():
    read_persistent_state(sections, filename)

with preview_col:
    filename_col, compile_col = st.columns([4,1], vertical_alignment="bottom")

    # TODO record history
    with filename_col:
        filename = st.text_input("filename", value="cv", on_change=filename_changed)
    with compile_col:
        st.button("compile", icon="🔄", on_click=lambda: write_and_compile_document(sections, filename=filename))
    displayPDF(filename=filename)




