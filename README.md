EmojiScript — Emoji-only demo (with English runtime output)

This repository contains a tiny EmojiScript interpreter implemented in Python.

What it is
- A minimal interpreter that uses only emojis as the source-language tokens.
- The included demo is an emoji-only Number Guessing Game (program source contains only emojis and emoji-strings).
- Runtime output (prompts, hint messages) is displayed in English for clarity, while the program source remains emoji-only.

Run the demo
1. Start the interpreter interactively so you can type guesses:

```bash
python3 emoji.py
```

2. The program will print the range and prompt in English (for usability). Type a numeric guess and press Enter.

Notes
- Program source is emoji-only; however, keyboard input is standard text (type numbers as digits).
- If you want to edit or create emoji programs, put only emojis and emoji-strings in `demo_program`.

If you want the runtime output to also be emoji-only, I can flip the translations back to emojis; currently runtime is English to be easier to play and test.