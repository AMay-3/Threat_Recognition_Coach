# Threat Recognition Coach

An in-progress Python command-line learning project by **Aaron May**. It uses a fictional phishing scenario to practice input validation, branching, loops, functions, dictionaries, and lists.

The scenario presents a message threatening account suspension. The user chooses whether to open its link or contact IT through a known, trusted method. The program explains the risk or safer response and displays a training summary.

## Current version

The current learning snapshot is `Python_Day_14.py`. The original `Python_Day_05.py` is retained as an earlier snapshot.

Day 14 includes:

- An email prompt that retries until the entry exactly matches the sample training roster.
- A two-option menu with feedback for both accepted choices.
- A retry loop and counter for invalid menu entries.
- A summary dictionary containing the email, accepted choice, outcome, invalid-attempt count, scenario ID, and completion status.
- A list that stores one completed summary during the run.
- Reusable functions and a guarded starting point.

The earlier username/list-set warm-up is not part of the Day 14 workflow.

An accepted menu choice means the entry is valid; it does **not** mean the chosen action is safe. Both outcomes receive a completion status of `Complete`. The invalid-attempt counter measures menu-entry errors, not security knowledge or rejected emails.

## Run locally

Install Python 3, open a terminal in the project folder, and run:

```bash
python Python_Day_14.py
```

Depending on your installation, use `python3 Python_Day_14.py` or, on Windows, `py Python_Day_14.py`.

No external packages are required. All interaction happens in the terminal. The program does not send email, open links, or connect to an external service.

## Example walkthrough

Enter these values when prompted:

| Prompt | Input |
| --- | --- |
| Email address | `sam.tcr@tcr.com` |
| First menu entry | `9` |
| Retry menu entry | `2` |

The program rejects `9`, accepts `2`, explains the safer response, and displays:

```text
Training session summary:
Email: sam.tcr@tcr.com
Choice: 2
Outcome: Safe Response
Invalid attempts: 1
Scenario ID: account_expiration_001
Completion Status: Complete
Completed Records: 1
```

Choosing `1` on the first menu attempt produces `Risky Response`, `Invalid attempts: 0`, and `Complete`. An unlisted email triggers another email prompt before the scenario begins.

## Program organization

| Function | Role |
| --- | --- |
| `get_outcome(selected_choice)` | Returns the matching safe or risky outcome label. |
| `show_summary(record)` | Prints the fields from a supplied summary dictionary. |
| `main()` | Coordinates one training run and returns its records list. |

The `if __name__ == "__main__":` guard starts training when the file runs directly. It captures the list returned by `main()` in `completed_records` and prints its length. Importing the file does not start the training prompts.

## Current limitations

- This version contains one fictional scenario and two response choices.
- Email matching uses a hard-coded sample roster and is exact, including capitalization and whitespace. It does not authenticate the user.
- Records exist only in memory. Each fresh run starts with an empty list; results are not saved to a file or database.
- There is no security-knowledge score, web interface, or real phishing detection.
- Some earlier practice variables remain unused.

Possible future improvements include additional scenarios, saved results, and scoring. These features are not implemented in this version.

## Learning and assistance

The project practices input/output, membership checks, conditionals, validation loops, counters, dictionary keys, list `append()`, indexing, `len()`, function parameters and arguments, returned values, local scope, and a guarded program entry point.

I developed the code using VS Code suggestions and ChatGPT explanations, code-review and debugging guidance, and README editing assistance. I am using the project to build my understanding of Python fundamentals and improve the program step by step.
