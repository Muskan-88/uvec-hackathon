# EmojiScript — A Programming Language Using Only Emojis! 🚀

This repository contains an **EmojiScript interpreter** implemented in Python - a fully functional programming language that uses ONLY EMOJIS!

## 📚 [**Complete Documentation →**](DOCUMENTATION.md)

For comprehensive language reference, syntax guide, examples, and tutorials, see the **[DOCUMENTATION.md](DOCUMENTATION.md)** file.

## What is EmojiScript?

- 🎨 A complete interpreter that uses only emojis as source-language tokens
- 🎮 Includes a fully-featured **Number Guessing Game** demo
- 💻 Supports variables, loops, conditionals, functions, and more
- ✅ Built-in error handling and input validation
- 🌍 Program source is emoji-only; runtime output is in English for usability

## Features

- ✅ **Variables & Assignment**: `📦 x ➡️ 5️⃣`
- ✅ **Control Flow**: If/else (`❓`/`❔`), While loops (`🔁`), Repeat (`🔂`)
- ✅ **Functions**: Define with `🎯`, return with `⬅️`
- ✅ **Input/Output**: Print (`🖨️`), Input (`📝`)
- ✅ **Operators**: Math (`➕➖✖️➗`), Comparison (`🟰⬆️⬇️`), Logic (`🤝🎭🚫`)
- ✅ **Built-ins**: Random numbers (`🎲`), Timer (`⏱️`)
- ✅ **Error Handling**: Type checking, input validation
- ✅ **Comments**: Using `💭`

## Quick Start

### Run the demo
1. Start the interpreter interactively:

```bash
python3 emoji.py
```

2. The Number Guessing Game will start. Type numeric guesses and press Enter.

### Example Code

```
💭 Hello World
🖨️ "👋🌍"

💭 Variables and Math
📦 🔵 ➡️ 1️⃣0️⃣
📦 🟢 ➡️ 5️⃣
🖨️ 🔵 ➕ 🟢    💭 Prints: 15

💭 Conditionals
❓ 🔵 ⬆️ 🟢 👉
    🖨️ "Blue is greater!"
🔚

💭 Loops
🔁 🔵 ⬆️ 0️⃣ 👉
    🖨️ 🔵
    🔵 ➡️ 🔵 ➖ 1️⃣
🔚
```

## 📖 Learning Resources

- **[Full Documentation](DOCUMENTATION.md)** - Complete language reference with examples
- **Demo Program** - See the commented number-guessing game in `emoji.py`
- **Quick Reference** - Emoji-to-keyword mappings in the docs

## Language Overview

### Core Syntax

| Emoji | Meaning | Example |
|-------|---------|---------|
| 📦 | Declare variable | `📦 x ➡️ 5️⃣` |
| ➡️ | Assign value | `x ➡️ 1️⃣0️⃣` |
| 🖨️ | Print | `🖨️ "Hello"` |
| 📝 | Input | `📦 x ➡️ 📝 "prompt"` |
| ❓ | If | `❓ condition 👉` |
| ❔ | Else | `❔ 👉` |
| 🔁 | While | `🔁 condition 👉` |
| 🔂 | Repeat | `🔂 5️⃣ 👉` |
| 🔚 | End block | `🔚` |
| 💭 | Comment | `💭 comment text` |

### Numbers
- Emoji digits: `0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟`
- Concatenate for larger numbers: `1️⃣0️⃣0️⃣` = 100

### Operators
- Math: `➕ ➖ ✖️ ➗`
- Comparison: `🟰 ❌🟰 ⬆️ ⬇️`
- Logic: `🤝 🎭 🚫`
- Booleans: `✅ ❌`

## Error Handling

The interpreter includes error handling:
- ⚠️ Input validation (detects non-numeric input)
- ❌ Variable redeclaration prevention
- ❌ Undefined variable detection
- ❌ Invalid assignment target checking
- 🛡️ Type-safe comparisons

## Notes

- **Program Source**: Write programs using only emojis
- **User Input**: Type standard text/numbers when prompted
- **Runtime Output**: English messages for usability (can be changed to emoji-only)
- **Comments**: Use `💭` to document your emoji code

## Contributing

Feel free to contribute by:
- Adding new emoji features
- Creating example programs
- Improving documentation
- Fixing bugs

## Repository

GitHub: https://github.com/Muskan-88/uvec-hackathon

---

*Created for the UVEC Hackathon*
