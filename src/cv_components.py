import os
import yaml


def make_header(DATAPATH):
    header = """#import "../templates/preamble.typ": *

#show: resume.with(
  author-position: left,
  personal-info-position: left,
  accent-color: "#26428b",
"""

    with open(os.path.join(DATAPATH, "headers_en.yaml"), "r") as f:
        for k,v in yaml.safe_load(f).items():
            header += f"  {k}: \"{v}\",\n"

    header += ")\n"
    return header


class Section:

    def __init__(self, title, entrytype="generic-one-by-two", preferred_pos=0, entries=[]):
        self.title = title
        self.entrytype = entrytype
        self.entries = entries
        self.preferred_pos = preferred_pos
        self.mask = [True] * len(self.entries)

    def __str__(self):
        """Format yaml to typst."""
        if sum(self.mask) == 0:
            return ""

        outstr = f"== {self.title}\n"
        for (entry, included) in zip(self.entries, self.mask):
            if not included:
                continue

            outstr += f"#{self.entrytype}(\n"
            for k,v in entry.items():
                # skip content, dealt with outside of block
                if k == "content":
                    continue
                
                # top left explicitly emphasized
                if k == "top-left":
                    outstr += f"  {k}: strong(\"{v}\"),\n"
                else:
                    outstr += f"  {k}: \"{v}\",\n"
            outstr += ")\n"

            if "content" in entry:
                outstr += entry["content"]
            outstr += "\n"
        return outstr + "\n"

