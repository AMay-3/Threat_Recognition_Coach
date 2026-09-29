# Threat Recognition Coach

An in-progress Python command-line learning project by **Aaron May** that uses a fictional phishing scenario to practice input validation, branching, loops, and collections.

The scenario asks the user to respond to a message threatening account suspension. Choosing to contact IT through a known, trusted method produces an explanation of why independent verification is safer. Choosing to open the supplied link produces an explanation of the risk.

## Current version

This repository preserves the original `Python_Day_05.py` learning snapshot. It includes:

- A two-option training menu with feedback for either accepted choice.
- A `while` loop that rejects invalid menu entries and asks again.
- A counter that reports how many invalid entries occurred before an accepted choice.
- A list/set warm-up that adds a username and compares total entries with unique usernames. This separate exercise runs before the training scenario and remains in the file as part of the learning snapshot.

An accepted choice means the menu entry is valid; it does **not** mean the selected action is safe. The invalid-attempt count measures menu-entry errors, not security knowledge.

## Run locally

Install Python 3, open a terminal in the project folder, and run:

```bash
python Python_Day_05.py
```

If your installation uses a different command, use `python3 Python_Day_05.py` or, on Windows, `py Python_Day_05.py`.

No external packages are required. All interaction happens in the terminal. The program does not send email, open links, or connect to an external service.

## Example walkthrough

Enter the following values when prompted:

| Prompt | Input |
|---|---|
| Username to add | `alex` |
| Email address | `sam.tcr@tcr.com` |
| First menu entry | `9` |
| Second menu entry | `7` |
| Third menu entry | `2` |

The warm-up reports four total entries and three unique usernames. The displayed order of the set may vary. The menu rejects `9` and `7`, accepts `2`, explains the safer response, and ends with:

```text
Accepted choice: 2
Invalid attempts: 2
```

Entering `1` or `2` on the first menu attempt skips the retry loop and reports `Invalid attempts: 0`.

## Current limitations

- The scenario appears only for an exact match in the hard-coded sample email list. An unrecognized email skips the scenario text, but the menu still appears.
- Matching a typed email to that list does not authenticate anyone.
- This is one fictional training scenario, without saved results, scoring, or a web interface.
- Some earlier practice variables are unused. The scenario text also retains spacing and spelling issues from the original learning file.

Possible next steps are to handle unrecognized emails explicitly, clean up the displayed text, separate the collections warm-up, and add more scenarios. These improvements are not implemented in this version.

## Learning and assistance

The project demonstrates `input()`, `print()`, list `append()`, set conversion, `len()`, membership checks, `if`/`elif`/`else`, a `while` loop, and a counter.

I developed this project with VS Code suggestions and ChatGPT explanations and debugging guidance. I am using it to practice Python fundamentals and improve the program step by step.
