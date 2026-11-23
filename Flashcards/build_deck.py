#!/usr/bin/env python3
"""Build an Anki .apkg from the YAML card sources in cards/.

Usage:  python build_deck.py [output.apkg]

Card source format (cards/*.yaml):

    deck: Quarkus                        # sub-deck name, under DECK_ROOT
    source: Java, Jakarta EE, Microprofile/Quarkus and MicroProfile.md
    tag: quarkus                         # tag prefix
    defaults: { reverse: false }         # optional defaults for all cards
    auto_prompt: true                    # optional: when q and a both start with **Label:**, add
                                         #   "Equivalent in <a label>?" (and the reverse) as the task line
    sections:
      - section: Configuration           # shown on the card, becomes tag quarkus::configuration
        source: ...                      # optional: overrides the file-level source
        cards:
          - id: q-config-ordinals        # STABLE, UNIQUE: identifies the note in Anki (keeps review history)
            q: |-                        # basic card: q + a (Markdown)
              ...
            a: |-
              ...
            extra: |-                    # optional, shown on the back
            reverse: true                # optional: also generate the reverse card (a -> q)
            prompt: |-                   # optional task line above the front (default: see auto_prompt)
            reverse_prompt: |-           # optional task line above the reverse front
          - id: q-bulkhead-queue
            prompt: |-                   # REQUIRED for cloze: the task, shown above the text
            cloze: |-                    # cloze card: {{c1::...}} markers (Markdown)
              ...

Never change an `id` once the deck has been imported -- edit the content instead.
"""
import hashlib
import re
import sys
from pathlib import Path

import genanki
import markdown
import yaml

ROOT = Path(__file__).resolve().parent
DECK_ROOT = "Java & Spring"

# Fixed IDs: changing them makes Anki treat the note types as new ones.
BASIC_MODEL_ID = 1730117201
CLOZE_MODEL_ID = 1730117202

CSS = """
.card {
  font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
  font-size: 18px; line-height: 1.45;
  text-align: left; max-width: 46em; margin: 0 auto; padding: 0 0.5em;
  color: #1d1d1f; background: #fff;
}
code, pre { font-family: "JetBrains Mono", Menlo, Consolas, monospace; font-size: 0.82em; }
code { background: #f0f0f3; padding: 0.05em 0.3em; border-radius: 4px; }
pre { background: #f6f6f8; padding: 0.7em 0.8em; border-radius: 6px;
      white-space: pre-wrap; word-break: break-word; overflow-x: auto; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 0.5em 0; }
td, th { border: 1px solid #ccc; padding: 0.2em 0.5em; }
.cloze { font-weight: bold; color: #0a58ca; }
.extra { margin-top: 1em; padding-top: 0.6em; border-top: 1px dashed #bbb; color: #444; font-size: 0.92em; }
.prompt { font-size: 0.8em; color: #666; margin-bottom: 0.6em; }
.source { margin-top: 1.2em; font-size: 0.72em; color: #888; }
hr#answer { border: none; border-top: 1px solid #ccc; }
.nightMode .card, .night_mode .card, .card.nightMode { color: #e6e6e6; background: #1e1e1e; }
.nightMode code, .night_mode code { background: #2c2c2e; }
.nightMode pre, .night_mode pre { background: #2a2a2c; }
.nightMode .cloze, .night_mode .cloze { color: #6ea8fe; }
.nightMode .prompt, .night_mode .prompt { color: #aaa; }
.nightMode .extra, .night_mode .extra { color: #bbb; border-color: #555; }
"""

SOURCE_HTML = '<div class="source">{{Source}}</div>'
PROMPT_HTML = '{{{{#{f}}}}}<div class="prompt">{{{{{f}}}}}</div>{{{{/{f}}}}}'
EXTRA_HTML = '{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'

BASIC_MODEL = genanki.Model(
    BASIC_MODEL_ID,
    "Notes card (optional reverse)",
    fields=[{"name": n} for n in ("Front", "Back", "Extra", "Source", "Reverse", "Prompt", "ReversePrompt")],
    templates=[
        {
            "name": "Forward",
            "qfmt": PROMPT_HTML.format(f="Prompt") + "{{Front}}",
            "afmt": '{{Front}}<hr id="answer">{{Back}}' + EXTRA_HTML + SOURCE_HTML,
        },
        {
            "name": "Reverse",
            "qfmt": "{{#Reverse}}" + PROMPT_HTML.format(f="ReversePrompt") + "{{Back}}{{/Reverse}}",
            "afmt": '{{Back}}<hr id="answer">{{Front}}' + EXTRA_HTML + SOURCE_HTML,
        },
    ],
    css=CSS,
)

CLOZE_MODEL = genanki.Model(
    CLOZE_MODEL_ID,
    "Notes cloze",
    fields=[{"name": n} for n in ("Text", "Extra", "Source", "Prompt")],
    templates=[
        {
            "name": "Cloze",
            "qfmt": PROMPT_HTML.format(f="Prompt") + "{{cloze:Text}}",
            "afmt": PROMPT_HTML.format(f="Prompt") + "{{cloze:Text}}" + EXTRA_HTML + SOURCE_HTML,
        }
    ],
    css=CSS,
    model_type=genanki.Model.CLOZE,
)


def md(text):
    if not text:
        return ""
    # Python-Markdown needs a blank line before an opening fence
    lines, in_code = [], False
    for line in text.strip().splitlines():
        if line.lstrip().startswith("```"):
            if not in_code and lines and lines[-1].strip():
                lines.append("")
            in_code = not in_code
        lines.append(line)
    return markdown.markdown("\n".join(lines), extensions=["fenced_code", "tables"])


LABEL_RE = re.compile(r"^\*\*([^*]+?):\*\*")


def auto_prompt(target_text):
    m = LABEL_RE.match(target_text.strip())
    return f"Equivalent in <b>{m.group(1)}</b>?" if m else ""


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def stable_int(s):
    return int(hashlib.sha1(s.encode()).hexdigest()[:9], 16)


class CardNote(genanki.Note):
    @property
    def guid(self):
        return genanki.guid_for(self._card_id)


def build(out_path):
    seen = {}
    decks = []
    errors = []
    for yaml_file in sorted((ROOT / "cards").glob("*.yaml")):
        data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
        deck_name = f"{DECK_ROOT}::{data['deck']}"
        deck = genanki.Deck(stable_int(deck_name), deck_name)
        defaults = data.get("defaults", {})
        for section in data["sections"]:
            src_file = section.get("source", data["source"])
            source = f"{Path(src_file).name} › {section['section']}"
            tags = [f"{data['tag']}::{slug(section['section'])}"]
            for card in section["cards"]:
                cid = card.get("id")
                where = f"{yaml_file.name}: {cid or '<no id>'}"
                if not cid:
                    errors.append(f"{where}: missing id")
                    continue
                if cid in seen:
                    errors.append(f"{where}: duplicate id (also in {seen[cid]})")
                    continue
                seen[cid] = yaml_file.name
                extra = md(card.get("extra"))
                tags_all = tags + card.get("tags", [])
                if "cloze" in card:
                    if not re.search(r"\{\{c\d+::", card["cloze"]):
                        errors.append(f"{where}: cloze card without {{{{c1::...}}}}")
                        continue
                    if not card.get("prompt"):
                        errors.append(f"{where}: cloze card needs a `prompt` (the task)")
                        continue
                    note = CardNote(model=CLOZE_MODEL, fields=[md(card["cloze"]), extra, source, md(card["prompt"])],
                                    tags=tags_all)
                elif "q" in card and "a" in card:
                    reverse = card.get("reverse", defaults.get("reverse", False))
                    prompt, rprompt = card.get("prompt", ""), card.get("reverse_prompt", "")
                    if data.get("auto_prompt") and LABEL_RE.match(card["q"].strip()):
                        prompt = prompt or auto_prompt(card["a"])
                        rprompt = rprompt or auto_prompt(card["q"])
                    if not prompt and "?" not in card["q"]:
                        errors.append(f"{where}: front is not a question; add `prompt` (the task)")
                        continue
                    if reverse and not rprompt:
                        errors.append(f"{where}: reverse card needs a `reverse_prompt` (or auto_prompt labels)")
                        continue
                    prompt, rprompt = md(prompt), md(rprompt)
                    note = CardNote(
                        model=BASIC_MODEL,
                        fields=[md(card["q"]), md(card["a"]), extra, source, "y" if reverse else "", prompt, rprompt],
                        tags=tags_all,
                    )
                else:
                    errors.append(f"{where}: needs either q+a or cloze")
                    continue
                note._card_id = cid
                deck.add_note(note)
        decks.append(deck)
        print(f"{deck_name}: {len(deck.notes)} notes")

    if errors:
        print("\n".join(["ERRORS:"] + errors), file=sys.stderr)
        sys.exit(1)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package(decks).write_to_file(str(out_path))
    print(f"Total: {len(seen)} notes -> {out_path}")


if __name__ == "__main__":
    build(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "build" / "java-spring.apkg")
