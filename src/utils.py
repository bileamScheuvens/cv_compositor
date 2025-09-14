import os
import yaml
import subprocess
from cv_components import make_header

BASEPATH = os.path.join(os.path.dirname(__file__), "..")
DATAPATH = os.path.join(BASEPATH, "data")
OUTPATH = os.path.join(BASEPATH, "out")


def compose_document(sections):
    """Combine header with sections."""
    res = make_header(DATAPATH)
    for sec in sections:
        res += str(sec)
    return res

def stringify_entry(entry):
    return "|".join(entry.values())

def write_persistent_state(sections, filename):
    """Persist state (order and included elements)."""
    session_state = {}
    for sec in sections:
        section_state = {}
        for (entry, state) in zip(sec.entries, sec.mask):
            section_state[stringify_entry(entry)] = state
        session_state[sec.title] = section_state
    with open(os.path.join(OUTPATH, f"{filename}.yaml"), "w") as f:
        yaml.dump(session_state, f)

def read_persistent_state(sections, filename):
    """Restore persistent state."""
    session_state = {}
    full_path = os.path.join(OUTPATH, f"{filename}.yaml")
    if not os.path.exists(full_path):
        return

    with open(full_path, "r") as f:
        session_state = yaml.safe_load(f)

    # TODO: restore order
    for sec in sections:
        for (i, entry) in enumerate(sec.entries):
            if stringify_entry(entry) in session_state[sec.title]:
                sec.mask[i] = session_state[sec.title][stringify_entry(entry)]



def write_and_compile_document(sections, filename="out", verbose=False, write_state=True):
    """Compose document, then compile."""
    with open(os.path.join(OUTPATH, f"{filename}.typ"), "w") as f:
        f.write(compose_document(sections))

    if write_state:
        write_persistent_state(sections, filename=filename)

    compilation_result = subprocess.run(f"typst compile --root .. {OUTPATH}/{filename}.typ ", shell=True, capture_output=True, text=True)

    if verbose:
        print(compilation_result.stdout)
        print(compilation_result.stderr)





