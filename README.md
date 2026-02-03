## CV Compositor

Simplified CV creation with toggleable entries.

### Getting Started

#### Requirements
Install project through nix or poetry:\
`>> nix develop .`\
or \
`>> poetry install # does not install typst`


#### Usage
- Fill yaml files in `data/` with content
- Start streamlit server\
   `>> [poetry run] streamlit run src/app.py`
- Open UI in browser: `http://localhost:xxxx` (default port is 8501)
- Select desired entries and compile
- Output written to `out/cv.pdf`
   




