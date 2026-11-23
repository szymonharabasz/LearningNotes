Anki flashcards generated from the notes in `Java, Jakarta EE, Microprofile/` and `Spring and Spring Boot/`.

## Decks
All decks are under **Java & Spring**:

| Subdeck | Source file | Contents |
|---|---|---|
| `Quarkus` | `cards/quarkus.yaml` | Quarkus and MicroProfile |
| `Spring Cloud` | `cards/spring-cloud.yaml` | Config Server, Eureka/Feign, Gateway, Resilience4j, Cloud Stream |
| `Comparisons` | `cards/comparisons.yaml` | Spring ↔ Jakarta EE / MicroProfile / Quarkus, mostly generated in **both directions** |

Every card shows its source note and section at the bottom. Tags such as `quarkus::fault-tolerance` let you study one topic at a time: in Anki, use Browse → tag, or a filtered deck.

## Building
```shell
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python build_deck.py          # writes build/java-spring.apkg
```
The script refuses to build if an id is duplicated or a card is malformed.

## Getting it onto a phone
**Easiest: through AnkiWeb (free).**
1. Install Anki on the desktop (https://apps.ankiweb.net).
2. File → Import → `build/java-spring.apkg`.
3. Sync with a free AnkiWeb account.
4. On the phone, install the app and sync with the same account. **Android:** AnkiDroid (free). **iOS:** AnkiMobile (paid; the official app that funds Anki development).

You can also open the `.apkg` directly on the phone. Without a sync account, though, your progress lives only on that device.

## Updating the cards later
- Edit the YAML, rebuild, and import again. Notes are matched by their **`id`**, so edited cards are updated **in place**, and your review history is kept.
- **Never change or reuse an `id`.** A changed id becomes a new card, and the old one stays in Anki until you delete it there.
- Deleting a card from the YAML does not delete it from Anki. Remove it in Anki too.

## Card format
```yaml
- id: q-bulkhead-queue          # stable and unique
  q: |-                         # basic card (Markdown); or `cloze:` with {{c1::...}}
    ...
  a: |-
    ...
  extra: |-                     # optional, shown on the back
    ...
  reverse: true                 # optional, also creates the reverse card
  prompt: |-                    # task line above the front (reverse_prompt: for the reverse)
    ...
```
**Every card must state its task**, or the build fails. A cloze card needs a `prompt`. A basic card needs either a `prompt` or a front that is a question (contains `?`). A reversed card needs a `reverse_prompt`, unless `auto_prompt` provides one.
In `comparisons.yaml`, `auto_prompt: true` builds the task line from the labels: a card `**Spring:** … → **Quarkus:** …` asks "Equivalent in **Quarkus**?" and, reversed, "Equivalent in **Spring**?". So always start both sides with a `**Label:**`.
A cloze ending right before `}}` needs a space, `{{c1::${x} }}`, otherwise Anki sees `}}}`.
