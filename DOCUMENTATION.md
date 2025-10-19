# 📚 EmojiScript Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Language Syntax](#language-syntax)
4. [Data Types](#data-types)
5. [Variables](#variables)
6. [Operators](#operators)
7. [Control Flow](#control-flow)
8. [Input/Output](#inputoutput)
9. [Functions](#functions)
10. [Comments](#comments)
11. [Built-in Features](#built-in-features)
12. [Error Handling](#error-handling)
13. [Example Programs](#example-programs)
14. [Complete Emoji Reference](#complete-emoji-reference)

---

## Introduction

**EmojiScript** is a programming language that uses ONLY EMOJIS! 🚀 It's a fully functional interpreter that allows you to write programs using emoji symbols instead of traditional text-based keywords.

### Why EmojiScript?
- 🎨 **Visual Programming**: Code becomes more expressive and fun
- 🌍 **Universal**: Emojis transcend language barriers
- 🎓 **Educational**: Learn programming concepts in a unique way
- 🎮 **Interactive**: Perfect for games and creative projects

### Features
- ✅ Variables and assignments
- ✅ Arithmetic and logical operations
- ✅ Conditional statements (if/else)
- ✅ Loops (while, repeat)
- ✅ Functions with parameters and return values
- ✅ User input and random number generation
- ✅ Comprehensive error handling
- ✅ Type validation

---

## Getting Started

### Installation
No installation required! Just have Python 3 installed on your system.

### Running Your First Program

1. Create a file with your EmojiScript code
2. Run it with Python:
   ```bash
   python3 emoji.py
   ```

### Hello World Example
```
🖨️ "👋🌍"
```
**Output:** `Hello World` (translated from emoji to English)

---

## Language Syntax

### Basic Program Structure
```
💭 This is a comment
📦 variable ➡️ value
🖨️ variable
```

### Key Principles
1. **One statement per line** (or use 👉 for block starts)
2. **Indentation matters** for nested blocks
3. **Blocks end with** 🔚
4. **Comments start with** 💭

---

## Data Types

### Numbers
EmojiScript supports integers and floating-point numbers.

#### Emoji Numerals
```
0️⃣ = 0    1️⃣ = 1    2️⃣ = 2    3️⃣ = 3    4️⃣ = 4
5️⃣ = 5    6️⃣ = 6    7️⃣ = 7    8️⃣ = 8    9️⃣ = 9
🔟 = 10
```

#### Numbers can be concatenated:
```
1️⃣0️⃣0️⃣ = 100
2️⃣5️⃣ = 25
```

#### ASCII Numbers (also supported):
```
📦 x ➡️ 42
📦 y ➡️ 3.14
```

### Strings
Text enclosed in quotes:
```
📦 name ➡️ "EmojiScript"
📦 greeting ➡️ "👋🎉"
```

### Booleans
```
✅ = true
❌ = false
```

### Example:
```
📦 🔵 ➡️ 1️⃣0️⃣      💭 Store 10 in variable
📦 🟢 ➡️ "Hello"   💭 Store string
📦 🔴 ➡️ ✅         💭 Store true
```

---

## Variables

### Declaration and Assignment

#### Method 1: Using STORE (📦)
Declares a **new variable** for the first time:
```
📦 variableName ➡️ value
```

**Examples:**
```
📦 🔵 ➡️ 5️⃣                💭 Declare and initialize to 5
📦 name ➡️ "Alice"        💭 Declare string variable
📦 isRunning ➡️ ✅        💭 Declare boolean variable
```

#### Method 2: Shorthand Reassignment
Reassign to an **existing variable** (without 📦):
```
variableName ➡️ newValue
```

**Examples:**
```
📦 🔵 ➡️ 5️⃣                💭 First declaration
🔵 ➡️ 1️⃣0️⃣               💭 Reassignment (no 📦)
🔵 ➡️ 🔵 ➕ 1️⃣           💭 Increment by 1
```

### Variable Naming Rules
1. Can use any emoji as variable name: 🔵 🟢 🔴 🟡 🟣 🟠
2. Can use ASCII identifiers: `x`, `count`, `total`
3. Can use regional indicator emojis: 🇦 🇧 🇨 ... 🇿
4. Cannot use reserved keywords
5. Cannot redeclare the same variable in the same scope

### Variable Scope
- **Global scope**: Variables declared at the top level
- **Function scope**: Variables declared inside functions
- **Block scope**: Variables declared inside loops/conditionals

---

## Operators

### Arithmetic Operators

| Emoji | Operation | Example | Result |
|-------|-----------|---------|--------|
| ➕ | Addition | `5️⃣ ➕ 3️⃣` | 8 |
| ➖ | Subtraction | `1️⃣0️⃣ ➖ 4️⃣` | 6 |
| ✖️ | Multiplication | `3️⃣ ✖️ 4️⃣` | 12 |
| ➗ | Division | `1️⃣0️⃣ ➗ 2️⃣` | 5 |

**Example:**
```
📦 🔵 ➡️ 1️⃣0️⃣
📦 🟢 ➡️ 5️⃣
📦 result ➡️ 🔵 ➕ 🟢 ✖️ 2️⃣   💭 Result = 20
🖨️ result
```

### Comparison Operators

| Emoji | Operation | Example | Result |
|-------|-----------|---------|--------|
| 🟰 | Equal to | `5️⃣ 🟰 5️⃣` | ✅ (true) |
| ❌🟰 | Not equal to | `5️⃣ ❌🟰 3️⃣` | ✅ (true) |
| ⬆️ | Greater than | `1️⃣0️⃣ ⬆️ 5️⃣` | ✅ (true) |
| ⬇️ | Less than | `3️⃣ ⬇️ 7️⃣` | ✅ (true) |

**Example:**
```
📦 age ➡️ 1️⃣8️⃣
❓ age ⬆️ 1️⃣7️⃣ 👉
    🖨️ "Adult"
🔚
```

### Logical Operators

| Emoji | Operation | Example | Result |
|-------|-----------|---------|--------|
| 🤝 | AND | `✅ 🤝 ✅` | ✅ (true) |
| 🎭 | OR | `✅ 🎭 ❌` | ✅ (true) |
| 🚫 | NOT | `🚫 ❌` | ✅ (true) |

**Example:**
```
📦 hasTicket ➡️ ✅
📦 isAdult ➡️ ✅
❓ hasTicket 🤝 isAdult 👉
    🖨️ "Can enter"
🔚
```

---

## Control Flow

### If Statement

**Syntax:**
```
❓ condition 👉
    💭 code block
🔚
```

**Example:**
```
📦 🔵 ➡️ 1️⃣0️⃣
❓ 🔵 ⬆️ 5️⃣ 👉
    🖨️ "Greater than 5"
🔚
```

### If-Else Statement

**Syntax:**
```
❓ condition 👉
    💭 if block
❔ 👉
    💭 else block
🔚
```

**Example:**
```
📦 score ➡️ 8️⃣5️⃣
❓ score ⬆️ 7️⃣5️⃣ 👉
    🖨️ "Pass"
❔ 👉
    🖨️ "Fail"
🔚
```

### Nested If-Else

**Example:**
```
📦 grade ➡️ 8️⃣5️⃣
❓ grade ⬆️ 9️⃣0️⃣ 👉
    🖨️ "A"
❔ 👉
    ❓ grade ⬆️ 8️⃣0️⃣ 👉
        🖨️ "B"
    ❔ 👉
        🖨️ "C"
    🔚
🔚
```

### While Loop

**Syntax:**
```
🔁 condition 👉
    💭 loop body
🔚
```

**Example:**
```
📦 count ➡️ 0️⃣
🔁 count ⬇️ 5️⃣ 👉
    🖨️ count
    count ➡️ count ➕ 1️⃣
🔚
```
**Output:** `0 1 2 3 4`

### Repeat Loop

**Syntax:**
```
🔂 numberOfTimes 👉
    💭 loop body
🔚
```

**Example:**
```
🔂 5️⃣ 👉
    🖨️ "🎉"
🔚
```
**Output:** `🎉 🎉 🎉 🎉 🎉`

---

## Input/Output

### Print Statement

**Syntax:**
```
🖨️ value
```

**Examples:**
```
🖨️ "Hello!"           💭 Print string
🖨️ 4️⃣2️⃣              💭 Print number
📦 🔵 ➡️ 1️⃣0️⃣
🖨️ 🔵                 💭 Print variable
```

### Input Statement

**Syntax:**
```
📦 variable ➡️ 📝 "prompt"
```

**Examples:**
```
📦 name ➡️ 📝 "Enter name:"
🖨️ name

📦 age ➡️ 📝 "Enter age:"
🖨️ age
```

**Input Behavior:**
- Automatically converts numeric input to numbers
- Non-numeric input is stored as strings
- Empty input returns empty string

---

## Functions

### Function Definition

**Syntax:**
```
🎯 functionName 📥 param1 param2 👉
    💭 function body
    ⬅️ returnValue
🔚
```

**Example:**
```
🎯 add 📥 a b 👉
    📦 result ➡️ a ➕ b
    ⬅️ result
🔚
```

### Function Call

**Syntax:**
```
functionName(arg1, arg2)
```

**Example:**
```
📦 sum ➡️ add(5️⃣, 3️⃣)
🖨️ sum    💭 Output: 8
```

### Complete Function Example
```
💭 Define function to calculate square
🎯 square 📥 num 👉
    ⬅️ num ✖️ num
🔚

💭 Use the function
📦 result ➡️ square(5️⃣)
🖨️ result    💭 Output: 25
```

---

## Comments

### Single-Line Comments

**Syntax:**
```
💭 This is a comment
```

**Examples:**
```
💭 Initialize counter
📦 count ➡️ 0️⃣

📦 🔵 ➡️ 1️⃣0️⃣    💭 Inline comment
```

### Best Practices
- Use comments to explain complex logic
- Document variable purposes
- Add section headers for organization
- Use inline comments sparingly

---

## Built-in Features

### Random Numbers

**Syntax:**
```
🎲 min max
```

**Example:**
```
📦 dice ➡️ 🎲 1️⃣ 6️⃣        💭 Random number from 1 to 6
🖨️ dice

📦 secret ➡️ 🎲 1️⃣ 🔟     💭 Random number from 1 to 10
```

### Range

**Syntax:**
```
🔢 start end
```

**Example:**
```
📦 numbers ➡️ 🔢 0️⃣ 5️⃣    💭 Creates [0, 1, 2, 3, 4, 5]
```

### Timer

**Syntax:**
```
⏱️    💭 Start/end timer
```

**Example:**
```
⏱️    💭 Start timer
💭 Your code here
📦 🔵 ➡️ 1️⃣0️⃣0️⃣0️⃣0️⃣
⏱️    💭 End timer and display elapsed time
```
**Output:** `⏱️ Runtime: 0.0012 seconds`

---

## Error Handling

### Input Validation

EmojiScript includes built-in error handling for common issues:

#### 1. **Invalid Input Type**
When user enters non-numeric input where a number is expected:
```
📦 guess ➡️ 📝 "Enter number:"
❓ guess ⬆️ 0️⃣ 👉
    🖨️ "Valid number"
❔ 👉
    🖨️ "Invalid input"
🔚
```

#### 2. **Variable Redeclaration**
Cannot declare the same variable twice in the same scope:
```
📦 🔵 ➡️ 5️⃣
📦 🔵 ➡️ 1️⃣0️⃣    💭 ERROR! Already declared
```
**Error:** `❌ Error: Variable '🔵' is already declared in this scope. Use ➡️ (without 📦) to reassign.`

**Correct way:**
```
📦 🔵 ➡️ 5️⃣        💭 First declaration
🔵 ➡️ 1️⃣0️⃣         💭 Reassignment (correct)
```

#### 3. **Undefined Variable**
Cannot use a variable before declaring it:
```
🖨️ 🔴              💭 ERROR! Not declared
```
**Error:** `❌ Error: Variable '🔴' is not defined. Did you forget to declare it with 📦?`

#### 4. **Invalid Assignment Target**
Cannot assign to literals or expressions:
```
📦 5️⃣ ➡️ 1️⃣0️⃣       💭 ERROR! Cannot assign to number
```
**Error:** `❌ Error: Cannot assign to NUM. Expected a variable name after 📦 (STORE).`

### Type Comparison Safety

When comparing incompatible types (e.g., string vs number):
- Comparison operators return `false` instead of crashing
- Equality checks handle type mismatches gracefully

**Example:**
```
📦 text ➡️ 📝 "Enter something:"
❓ text ⬆️ 5️⃣ 👉                    💭 Safely returns false if text is not a number
    🖨️ "Valid number"
❔ 👉
    🖨️ "Not a number or too small"
🔚
```

---

## Example Programs

### 1. Hello World
```
🖨️ "👋🌍 Hello World!"
```

### 2. Simple Calculator
```
💭 Simple Calculator
📦 🅰️ ➡️ 📝 "Enter first number:"
📦 🅱️ ➡️ 📝 "Enter second number:"

🖨️ "Sum:"
🖨️ 🅰️ ➕ 🅱️

🖨️ "Product:"
🖨️ 🅰️ ✖️ 🅱️
```

### 3. Countdown Timer
```
💭 Countdown from 10 to 1
📦 count ➡️ 🔟

🔁 count ⬆️ 0️⃣ 👉
    🖨️ count
    count ➡️ count ➖ 1️⃣
🔚

🖨️ "🚀 Blast off!"
```

### 4. Even or Odd Checker
```
💭 Check if number is even or odd
📦 num ➡️ 📝 "Enter a number:"

💭 Note: This is a simplified check
❓ num 🟰 2️⃣ 👉
    🖨️ "Even"
❔ 👉
    ❓ num 🟰 1️⃣ 👉
        🖨️ "Odd"
    ❔ 👉
        🖨️ "Other"
    🔚
🔚
```

### 5. Number Guessing Game (Complete)
```
💭 Number Guessing Game
⏱️

📦 🟢 ➡️ 1️⃣                  💭 Minimum value
📦 🔵 ➡️ 🔟                  💭 Maximum value
📦 🔒 ➡️ 🎲 🟢 🔵            💭 Random secret number

🖨️ "🔢❓ Guess 1️⃣ to 🔟"

📦 🏃 ➡️ ✅                  💭 Running flag
📦 🟣 ➡️ 0️⃣                  💭 User guess
📦 🆚 ➡️ ❌                  💭 Validation flag

🔁 🏃 👉
    🟣 ➡️ 📝 "Enter guess:"
    
    💭 Validate input
    🆚 ➡️ ❌
    ❓ 🟣 ⬆️ 0️⃣ 👉
        🆚 ➡️ ✅
    ❔ 👉
        ❓ 🟣 ⬇️ 0️⃣ 👉
            🆚 ➡️ ✅
        ❔ 👉
            ❓ 🟣 🟰 0️⃣ 👉
                🆚 ➡️ ✅
            🔚
        🔚
    🔚
    
    ❓ 🆚 🟰 ❌ 👉
        🖨️ "⚠️ Invalid input!"
    ❔ 👉
        ❓ 🟣 ⬇️ 🟢 👉
            🖨️ "⚠️ Too low! Min is 1️⃣"
        ❔ 👉
            ❓ 🟣 ⬆️ 🔵 👉
                🖨️ "⚠️ Too high! Max is 🔟"
            ❔ 👉
                ❓ 🟣 🟰 🔒 👉
                    🖨️ "✅🎉 Correct!"
                    🏃 ➡️ ❌
                ❔ 👉
                    ❓ 🟣 ⬆️ 🔒 👉
                        🖨️ "📈 Too high!"
                    ❔ 👉
                        🖨️ "📉 Too low!"
                    🔚
                🔚
            🔚
        🔚
    🔚
🔚

⏱️
```

---

## Complete Emoji Reference

### Keywords & Control Structures

| Emoji | Keyword | Usage | Description |
|-------|---------|-------|-------------|
| 📦 | STORE | `📦 var ➡️ value` | Declare new variable |
| ➡️ | ASSIGN | `var ➡️ value` | Assign/reassign value |
| 🖨️ | PRINT | `🖨️ value` | Output to console |
| ❓ | IF | `❓ condition 👉` | If statement |
| ❔ | ELSE | `❔ 👉` | Else statement |
| 🔁 | WHILE | `🔁 condition 👉` | While loop |
| 🔂 | REPEAT | `🔂 n 👉` | Repeat n times |
| 🎯 | DEFINE | `🎯 name 📥 params 👉` | Define function |
| 📥 | PARAMS | `📥 a b c` | Function parameters |
| ⬅️ | RETURN | `⬅️ value` | Return from function |
| 👉 | THEN | `👉` | Start code block |
| 🔚 | END | `🔚` | End code block |
| 💭 | COMMENT | `💭 text` | Comment line |

### Data Types & Values

| Emoji | Type | Value | Description |
|-------|------|-------|-------------|
| ✅ | TRUE | true | Boolean true |
| ❌ | FALSE | false | Boolean false |
| 0️⃣ | NUM | 0 | Digit zero |
| 1️⃣ | NUM | 1 | Digit one |
| 2️⃣ | NUM | 2 | Digit two |
| 3️⃣ | NUM | 3 | Digit three |
| 4️⃣ | NUM | 4 | Digit four |
| 5️⃣ | NUM | 5 | Digit five |
| 6️⃣ | NUM | 6 | Digit six |
| 7️⃣ | NUM | 7 | Digit seven |
| 8️⃣ | NUM | 8 | Digit eight |
| 9️⃣ | NUM | 9 | Digit nine |
| 🔟 | NUM | 10 | Number ten |

### Arithmetic Operators

| Emoji | Operator | Example | Result |
|-------|----------|---------|--------|
| ➕ | PLUS | `5️⃣ ➕ 3️⃣` | 8 |
| ➖ | MINUS | `8️⃣ ➖ 3️⃣` | 5 |
| ✖️ | MULT | `4️⃣ ✖️ 3️⃣` | 12 |
| ➗ | DIV | `1️⃣2️⃣ ➗ 3️⃣` | 4 |

### Comparison Operators

| Emoji | Operator | Example | Result |
|-------|----------|---------|--------|
| 🟰 | EQ | `5️⃣ 🟰 5️⃣` | ✅ |
| ❌🟰 | NEQ | `5️⃣ ❌🟰 3️⃣` | ✅ |
| ⬆️ | GT | `5️⃣ ⬆️ 3️⃣` | ✅ |
| ⬇️ | LT | `3️⃣ ⬇️ 5️⃣` | ✅ |

### Logical Operators

| Emoji | Operator | Example | Result |
|-------|----------|---------|--------|
| 🤝 | AND | `✅ 🤝 ✅` | ✅ |
| 🎭 | OR | `✅ 🎭 ❌` | ✅ |
| 🚫 | NOT | `🚫 ❌` | ✅ |

### Built-in Functions

| Emoji | Function | Usage | Description |
|-------|----------|-------|-------------|
| 📝 | INPUT | `📝 "prompt"` | Get user input |
| 🎲 | RANDOM | `🎲 min max` | Random number |
| 🔢 | RANGE | `🔢 start end` | Number range |
| ⏱️ | TIMER | `⏱️` | Start/end timer |

### Alphabet Emojis (Variable Names)

| Emoji | Letter | Emoji | Letter | Emoji | Letter |
|-------|--------|-------|--------|-------|--------|
| 🇦 | A | 🇧 | B | 🇨 | C |
| 🇩 | D | 🇪 | E | 🇫 | F |
| 🇬 | G | 🇭 | H | 🇮 | I |
| 🇯 | J | 🇰 | K | 🇱 | L |
| 🇲 | M | 🇳 | N | 🇴 | O |
| 🇵 | P | 🇶 | Q | 🇷 | R |
| 🇸 | S | 🇹 | T | 🇺 | U |
| 🇻 | V | 🇼 | W | 🇽 | X |
| 🇾 | Y | 🇿 | Z | | |

### Special Squared Letters

| Emoji | Value |
|-------|-------|
| 🅰️ | a |
| 🅱️ | b |
| 🅾️ | o |
| 🅿️ | p |

---

## Quick Reference Card

### Essential Patterns

```
💭 Variables
📦 name ➡️ value        💭 Declare
name ➡️ newValue       💭 Reassign

💭 Output
🖨️ value               💭 Print

💭 Input
📦 x ➡️ 📝 "prompt"     💭 Get input

💭 If-Else
❓ condition 👉
    💭 if block
❔ 👉
    💭 else block
🔚

💭 While Loop
🔁 condition 👉
    💭 loop body
🔚

💭 Function
🎯 funcName 📥 params 👉
    ⬅️ returnValue
🔚
```

---

## Tips and Best Practices

### 1. **Use Descriptive Emoji Variables**
```
📦 🔵 ➡️ 1️⃣0️⃣    💭 Good: Blue for maximum
📦 🟢 ➡️ 1️⃣     💭 Good: Green for minimum
📦 🔒 ➡️ 🎲 1️⃣ 🔟  💭 Good: Lock for secret
```

### 2. **Comment Your Code**
```
💭 ====================================
💭 Section: Input Validation
💭 ====================================
📦 🆚 ➡️ ❌         💭 Validation flag
```

### 3. **Use Proper Indentation**
Indent nested blocks for readability:
```
🔁 condition 👉
    ❓ innerCondition 👉
        🖨️ "Nested"
    🔚
🔚
```

### 4. **Validate User Input**
Always check if input is valid before using it:
```
📦 num ➡️ 📝 "Enter number:"
❓ num ⬆️ 0️⃣ 👉
    💭 Valid number
    🖨️ num
❔ 👉
    🖨️ "Invalid input"
🔚
```

### 5. **Use Meaningful Variable Names**
Either emojis or ASCII, but be consistent:
```
💭 Good
📦 🔵 ➡️ 1️⃣0️⃣     💭 Emoji variable
📦 count ➡️ 0️⃣    💭 ASCII variable

💭 Bad (mixed without reason)
📦 🔵count ➡️ 1️⃣0️⃣  💭 Don't mix arbitrarily
```

---

## Troubleshooting

### Common Errors

#### 1. **Variable Already Declared**
```
❌ Error: Variable 'x' is already declared in this scope.
```
**Solution:** Use reassignment without 📦:
```
📦 x ➡️ 5️⃣     💭 First time
x ➡️ 1️⃣0️⃣      💭 Reassignment (no 📦)
```

#### 2. **Undefined Variable**
```
❌ Error: Variable 'y' is not defined.
```
**Solution:** Declare before use:
```
📦 y ➡️ 5️⃣     💭 Declare first
🖨️ y          💭 Then use
```

#### 3. **Invalid Assignment Target**
```
❌ Error: Cannot assign to NUM.
```
**Solution:** Assign to variable, not literal:
```
📦 x ➡️ 5️⃣     💭 Correct
📦 5️⃣ ➡️ x      💭 Wrong!
```

#### 4. **Missing THEN (👉)**
```
❌ Error: Expected THEN, got ...
```
**Solution:** Add 👉 after condition:
```
❓ x ⬆️ 5️⃣ 👉    💭 Needs 👉
    🖨️ x
🔚
```

---

## Additional Resources

### File Structure
```
uvec-hackathon/
├── emoji.py           # Main interpreter
├── README.md          # Project overview
├── DOCUMENTATION.md   # This file
└── Evaluator.py      # Legacy code
```

### Running Custom Programs

1. Edit the `demo_program` variable in `emoji.py`
2. Or create a new Python file:
```python
from emoji import Lexer, Parser, Interpreter

my_program = """
🖨️ "Hello!"
"""

lexer = Lexer(my_program)
tokens = lexer.tokenize()
parser = Parser(tokens)
ast = parser.parse()
interpreter = Interpreter()
interpreter.execute(ast)
```

---

## Conclusion

**EmojiScript** provides a unique and fun way to learn programming concepts while using expressive emoji symbols. Whether you're building games, teaching programming, or just experimenting, EmojiScript offers a complete programming environment with:

✅ Variables and data types  
✅ Control flow (if/else, loops)  
✅ Functions with parameters  
✅ User input and output  
✅ Error handling and validation  
✅ Built-in utilities (random, timer)  

**Happy Emoji Coding! 🎉🚀💻**

---

*Last Updated: October 19, 2025*  
*Version: 1.0*  
*Repository: https://github.com/Muskan-88/uvec-hackathon*
