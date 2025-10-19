"""
EmojiScript Interpreter
A programming language that uses ONLY EMOJIS! 🚀

Language Syntax (Emoji-only examples):
- Variables: 📦 🔵 ➡️ 5️⃣  (store 5 in variable 🔵)
- Output: 📢 🔵  (print variable 🔵)
- Output: 📢 "🎉"  (print emoji string)
- Math: ➕ ➖ ✖️ ➗ (add, subtract, multiply, divide)
- Comparisons: 🟰 (equals), ❌🟰 (not equals), ⬆️ (greater), ⬇️ (less)
- Boolean: ✅ (true), ❌ (false)
- Logic: 🤝 (and), 🎭 (or), � (not)
- Comments: � This is a comment

Examples:
  Print statement:
    � "✅🎉"
  If statement:
    ❓ 🔵 🟰 5️⃣ �👉
        📢 "✅"
    🔄 👉
        📢 "❌"
    🔚
  While loop:
    📦 🟢 ➡️ 0️⃣
    🔁 � ⬇️ 🔟 👉
        📢 🟢
        🟢 ➡️ 🟢 ➕ 1️⃣
    🔚
  Repeat loop: 🔂 5️⃣ 👉 📢 "🎉" 🔚
  Functions: 🎯 🌟 📥 🔵 🟢 👉 ... ⬅️ result 🔚
  Range: 🔢 0️⃣ 🔟 (numbers from 0 to 10)
  Input: � "🔢➡️" (prompt for input)
  Random: 🎲 1️⃣ � (random number 1-10)
"""

import re
import random
from typing import Any, Dict, List, Optional, Tuple

class Token:
    def __init__(self, type: str, value: Any, line: int = 0):
        self.type = type
        self.value = value
        self.line = line
    
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.line = 1
        self.tokens = []
        
        # Emoji keyword mappings
        self.emoji_keywords = {
            '📦': 'STORE',      # Variable declaration/assignment
            '➡️': 'ASSIGN',     # Assignment operator
            '📢': 'PRINT',      # Print/output
            '❓': 'IF',         # If statement
            '🔄': 'ELSE',       # Else statement
            '🔁': 'WHILE',      # While loop
            '🔂': 'REPEAT',     # Repeat n times
            '🎯': 'DEFINE',     # Function definition
            '📥': 'PARAMS',     # Function parameters
            '⬅️': 'RETURN',     # Return statement
            '👉': 'THEN',       # Then (body start)
            '🔚': 'END',        # End block
            '✅': 'TRUE',       # Boolean true
            '❌': 'FALSE',      # Boolean false
            '➕': 'PLUS',       # Addition
            '➖': 'MINUS',      # Subtraction
            '✖️': 'MULT',       # Multiplication
            '➗': 'DIV',        # Division
            '🟰': 'EQ',         # Equals
            '❌🟰': 'NEQ',      # Not equals
            '⬆️': 'GT',         # Greater than
            '⬇️': 'LT',         # Less than
            '🤝': 'AND',        # Logical and
            '🎭': 'OR',         # Logical or
            '🚫': 'NOT',        # Logical not
            '🔢': 'RANGE',      # Range
            '💭': 'COMMENT',    # Comment
            '📝': 'INPUT',       # Input from user (prompt)
            '🎲': 'RANDOM',      # Random number generator
            '(': 'LPAREN',
            ')': 'RPAREN',
        }
        # Emoji numerals mapping (single emoji -> digit string)
        self.emoji_digits = {
            '0️⃣': '0', '1️⃣': '1', '2️⃣': '2', '3️⃣': '3', '4️⃣': '4',
            '5️⃣': '5', '6️⃣': '6', '7️⃣': '7', '8️⃣': '8', '9️⃣': '9',
            '🔟': '10'
        }
    
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.code):
            char = self.peek()
            
            # Skip whitespace
            if char in ' \t\r':
                self.pos += 1
                continue
            
            if char == '\n':
                self.line += 1
                self.pos += 1
                continue
            
            # Check for comment
            if char == '💭':
                while self.pos < len(self.code) and self.peek() != '\n':
                    self.pos += 1
                continue
            
            # Check for emoji keywords using longest-first matching to support
            # multi-codepoint emojis (e.g., ➡️, ❌🟰).
            matched = False
            for key in sorted(self.emoji_keywords.keys(), key=len, reverse=True):
                if self.code.startswith(key, self.pos):
                    token_type = self.emoji_keywords[key]
                    self.tokens.append(Token(token_type, key, self.line))
                    self.pos += len(key)
                    matched = True
                    break
            if matched:
                continue

            # Emoji numerals: read sequences like 1️⃣0️⃣0️⃣ -> NUM(100)
            digit_found = False
            for dkey in sorted(self.emoji_digits.keys(), key=len, reverse=True):
                if self.code.startswith(dkey, self.pos):
                    digit_found = True
                    break
            if digit_found:
                num_str = ''
                while True:
                    matched_digit = False
                    for dkey in sorted(self.emoji_digits.keys(), key=len, reverse=True):
                        if self.code.startswith(dkey, self.pos):
                            num_str += self.emoji_digits[dkey]
                            self.pos += len(dkey)
                            matched_digit = True
                            break
                    if not matched_digit:
                        break
                # Convert concatenated digit string to integer
                try:
                    value = int(num_str)
                except Exception:
                    value = 0
                self.tokens.append(Token('NUM', value, self.line))
                continue

            # If the character is a non-ASCII emoji and not a keyword, treat it as an identifier (single emoji id)
            if ord(char) > 127:
                self.tokens.append(Token('ID', char, self.line))
                self.pos += 1
                continue
            
            # Numbers
            if char.isdigit():
                self.tokens.append(self.read_number())
                continue
            
            # Strings (quoted text)
            if char in '"\'':
                self.tokens.append(self.read_string())
                continue
            
            # Identifiers (variable/function names)
            if char.isalpha() or char == '_':
                self.tokens.append(self.read_identifier())
                continue
            
            # Parentheses
            if char in '()':
                token_type = 'LPAREN' if char == '(' else 'RPAREN'
                self.tokens.append(Token(token_type, char, self.line))
                self.pos += 1
                continue
            
            # Skip unknown characters
            self.pos += 1
        
        self.tokens.append(Token('EOF', None, self.line))
        return self.tokens
    
    def peek(self, n=1) -> str:
        if self.pos + n > len(self.code):
            return ''
        return self.code[self.pos:self.pos+n] if n > 1 else self.code[self.pos]
    
    def read_number(self) -> Token:
        start = self.pos
        has_dot = False
        while self.pos < len(self.code) and (self.code[self.pos].isdigit() or self.code[self.pos] == '.'):
            if self.code[self.pos] == '.':
                has_dot = True
            self.pos += 1
        num_str = self.code[start:self.pos]
        value = float(num_str) if has_dot else int(num_str)
        return Token('NUM', value, self.line)
    
    def read_string(self) -> Token:
        quote = self.peek()
        self.pos += 1
        value = ""
        while self.pos < len(self.code) and self.peek() != quote:
            if self.peek() == '\\':
                self.pos += 1
                if self.pos < len(self.code):
                    value += self.peek()
                    self.pos += 1
            else:
                value += self.peek()
                self.pos += 1
        self.pos += 1  # Skip closing quote
        return Token('STR', value, self.line)
    
    def read_identifier(self) -> Token:
        start = self.pos
        while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == '_'):
            self.pos += 1
        name = self.code[start:self.pos]
        return Token('ID', name, self.line)

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self) -> List[Any]:
        statements = []
        while not self.match('EOF'):
            statements.append(self.statement())
        return statements
    
    def statement(self):
        if self.match('STORE'):
            return self.assignment()
        # Allow shorthand assignment: ID ASSIGN expr
        if self.match('ID') and self.peek_type(1) == 'ASSIGN':
            return self.assignment_short()
        elif self.match('PRINT'):
            return self.print_statement()
        elif self.match('IF'):
            return self.if_statement()
        elif self.match('WHILE'):
            return self.while_statement()
        elif self.match('REPEAT'):
            return self.repeat_statement()
        elif self.match('DEFINE'):
            return self.function_def()
        elif self.match('RETURN'):
            return self.return_statement()
        else:
            return self.expression()
    
    def assignment(self):
        self.consume('STORE')
        var_name = self.consume('ID').value
        self.consume('ASSIGN')
        value = self.expression()
        return ('assign', var_name, value)

    def assignment_short(self):
        var_name = self.consume('ID').value
        self.consume('ASSIGN')
        value = self.expression()
        return ('assign', var_name, value)

    def peek_type(self, offset: int) -> Optional[str]:
        idx = self.pos + offset
        if idx < len(self.tokens):
            return self.tokens[idx].type
        return None
    
    def print_statement(self):
        self.consume('PRINT')
        value = self.expression()
        return ('print', value)
    
    def if_statement(self):
        self.consume('IF')
        condition = self.expression()
        self.consume('THEN')
        
        then_body = []
        while not self.match('ELSE') and not self.match('END'):
            then_body.append(self.statement())
        
        else_body = None
        if self.match('ELSE'):
            self.consume('ELSE')
            self.consume('THEN')
            else_body = []
            while not self.match('END'):
                else_body.append(self.statement())
        
        self.consume('END')
        return ('if', condition, then_body, else_body)
    
    def while_statement(self):
        self.consume('WHILE')
        condition = self.expression()
        self.consume('THEN')
        
        body = []
        while not self.match('END'):
            body.append(self.statement())
        
        self.consume('END')
        return ('while', condition, body)
    
    def repeat_statement(self):
        self.consume('REPEAT')
        count = self.expression()
        self.consume('THEN')
        
        body = []
        while not self.match('END'):
            body.append(self.statement())
        
        self.consume('END')
        return ('repeat', count, body)
    
    def function_def(self):
        self.consume('DEFINE')
        name = self.consume('ID').value
        
        params = []
        if self.match('PARAMS'):
            self.consume('PARAMS')
            while not self.match('THEN'):
                params.append(self.consume('ID').value)
        
        self.consume('THEN')
        
        body = []
        while not self.match('END'):
            body.append(self.statement())
        
        self.consume('END')
        return ('def', name, params, body)
    
    def return_statement(self):
        self.consume('RETURN')
        value = self.expression()
        return ('return', value)
    
    def expression(self):
        return self.logic_or()
    
    def logic_or(self):
        left = self.logic_and()
        while self.match('OR'):
            self.consume('OR')
            right = self.logic_and()
            left = ('or', left, right)
        return left
    
    def logic_and(self):
        left = self.logic_not()
        while self.match('AND'):
            self.consume('AND')
            right = self.logic_not()
            left = ('and', left, right)
        return left
    
    def logic_not(self):
        if self.match('NOT'):
            self.consume('NOT')
            expr = self.logic_not()
            return ('not', expr)
        return self.comparison()
    
    def comparison(self):
        left = self.term()
        
        if self.match('EQ'):
            self.consume('EQ')
            right = self.term()
            return ('binop', '==', left, right)
        elif self.match('NEQ'):
            self.consume('NEQ')
            right = self.term()
            return ('binop', '!=', left, right)
        elif self.match('GT'):
            self.consume('GT')
            right = self.term()
            return ('binop', '>', left, right)
        elif self.match('LT'):
            self.consume('LT')
            right = self.term()
            return ('binop', '<', left, right)
        
        return left
    
    def term(self):
        left = self.factor()
        
        while self.match('PLUS') or self.match('MINUS'):
            if self.match('PLUS'):
                self.consume('PLUS')
                right = self.factor()
                left = ('binop', '+', left, right)
            elif self.match('MINUS'):
                self.consume('MINUS')
                right = self.factor()
                left = ('binop', '-', left, right)
        
        return left
    
    def factor(self):
        left = self.unary()
        
        while self.match('MULT') or self.match('DIV'):
            if self.match('MULT'):
                self.consume('MULT')
                right = self.unary()
                left = ('binop', '*', left, right)
            elif self.match('DIV'):
                self.consume('DIV')
                right = self.unary()
                left = ('binop', '/', left, right)
        
        return left
    
    def unary(self):
        if self.match('MINUS'):
            self.consume('MINUS')
            expr = self.unary()
            return ('unop', '-', expr)
        return self.call()
    
    def call(self):
        expr = self.primary()
        
        while self.match('LPAREN'):
            self.consume('LPAREN')
            args = []
            while not self.match('RPAREN'):
                args.append(self.expression())
            self.consume('RPAREN')
            expr = ('call', expr, args)
        
        return expr
    
    def primary(self):
        if self.match('NUM'):
            value = self.current().value
            self.advance()
            return ('num', value)
        elif self.match('STR'):
            value = self.current().value
            self.advance()
            return ('str', value)
        elif self.match('TRUE'):
            self.advance()
            return ('bool', True)
        elif self.match('FALSE'):
            self.advance()
            return ('bool', False)
        elif self.match('RANGE'):
            self.consume('RANGE')
            start = self.expression()
            end = self.expression()
            return ('range', start, end)
        elif self.match('INPUT'):
            self.consume('INPUT')
            # optional string prompt
            if self.match('STR'):
                prompt = ('str', self.current().value)
                self.advance()
                return ('input', prompt)
            return ('input', None)
        elif self.match('RANDOM'):
            self.consume('RANDOM')
            min_expr = self.expression()
            max_expr = self.expression()
            return ('random', min_expr, max_expr)
        elif self.match('ID'):
            name = self.current().value
            self.advance()
            return ('var', name)
        elif self.match('LPAREN'):
            self.consume('LPAREN')
            expr = self.expression()
            self.consume('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Unexpected token: {self.current()}")
    
    def current(self) -> Token:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else Token('EOF', None)
    
    def advance(self):
        self.pos += 1
    
    def match(self, type: str) -> bool:
        return self.current().type == type
    
    def consume(self, type: str) -> Token:
        token = self.current()
        if not self.match(type):
            raise SyntaxError(f"Expected {type}, got {token}")
        self.advance()
        return token

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.globals = {}
        self.scopes = [self.globals]
        # Mapping from emoji-only program strings to English output
        self.output_translations = {
            "🔢❓": "Guess the number:",
            "➡️": "to",
                "🔢➡️": "Enter your guess:\n",
            "✅🎉": "Correct! You guessed it.",
            "📈❌": "Too high!",
            "📉❌": "Too low!",
        }
        # Emoji numerals map for translating emoji numerals inside strings
        self.emoji_digits = {
            '0️⃣': '0', '1️⃣': '1', '2️⃣': '2', '3️⃣': '3', '4️⃣': '4',
            '5️⃣': '5', '6️⃣': '6', '7️⃣': '7', '8️⃣': '8', '9️⃣': '9',
            '🔟': '10'
        }

    def translate_output(self, s: str) -> str:
        # Replace known emoji tokens with English words
        out = s
        for k, v in self.output_translations.items():
            out = out.replace(k, v)
        # Replace emoji numerals inside string with digits
        for k, v in self.emoji_digits.items():
            out = out.replace(k, v)
        return out
    
    def execute(self, ast: List[Any]):
        result = None
        for statement in ast:
            result = self.eval(statement)
        return result
    
    def eval(self, node):
        if node is None:
            return None
        
        if node[0] == 'num':
            return node[1]
        elif node[0] == 'str':
            return node[1]
        elif node[0] == 'bool':
            return node[1]
        elif node[0] == 'var':
            return self.get_var(node[1])
        elif node[0] == 'assign':
            value = self.eval(node[2])
            self.set_var(node[1], value)
            return value
        elif node[0] == 'binop':
            return self.eval_binop(node[1], node[2], node[3])
        elif node[0] == 'unop':
            return self.eval_unop(node[1], node[2])
        elif node[0] == 'and':
            left = self.eval(node[1])
            if not left:
                return False
            return self.eval(node[2])
        elif node[0] == 'or':
            left = self.eval(node[1])
            if left:
                return True
            return self.eval(node[2])
        elif node[0] == 'not':
            return not self.eval(node[1])
        elif node[0] == 'if':
            condition = self.eval(node[1])
            if condition:
                return self.eval_block(node[2])
            elif node[3]:
                return self.eval_block(node[3])
        elif node[0] == 'while':
            result = None
            while self.eval(node[1]):
                result = self.eval_block(node[2])
            return result
        elif node[0] == 'repeat':
            count = self.eval(node[1])
            result = None
            for _ in range(count):
                result = self.eval_block(node[2])
            return result
        elif node[0] == 'range':
            start = self.eval(node[1])
            end = self.eval(node[2])
            return list(range(start, end + 1))
        elif node[0] == 'input':
            # ('input', prompt?) where prompt is ('str', text) or None
            prompt_node = node[1]
            prompt = ''
            if prompt_node:
                prompt = self.eval(prompt_node)
                # If prompt is a string, translate emoji prompt to English for display
                if isinstance(prompt, str):
                    prompt = self.output_translations.get(prompt, prompt)
            # Use Python input() to get a line, try to convert to int if possible
            raw = input(prompt if prompt is not None else '')
            raw = raw.strip()
            # Return number if numeric, else string
            if raw.isdigit() or (raw.startswith('-') and raw[1:].isdigit()):
                try:
                    return int(raw)
                except Exception:
                    pass
            try:
                return float(raw)
            except Exception:
                return raw
        elif node[0] == 'random':
            lo = self.eval(node[1])
            hi = self.eval(node[2])
            # Ensure ints
            try:
                lo_i = int(lo)
                hi_i = int(hi)
            except Exception:
                raise RuntimeError("RANDOM bounds must be numeric")
            return random.randint(lo_i, hi_i)
        elif node[0] == 'def':
            self.globals[node[1]] = ('function', node[2], node[3])
            return None
        elif node[0] == 'call':
            func = self.eval(node[1])
            args = [self.eval(arg) for arg in node[2]]
            return self.call_function(func, args)
        elif node[0] == 'print':
            value = self.eval(node[1])
            # If the program prints a string, translate embedded emoji tokens to English
            if isinstance(value, str):
                out = self.translate_output(value)
                print(out)
            else:
                print(value)
            return None
        elif node[0] == 'return':
            value = self.eval(node[1])
            raise ReturnException(value)
        else:
            return None
    
    def eval_block(self, statements):
        result = None
        for stmt in statements:
            result = self.eval(stmt)
        return result
    
    def eval_binop(self, op, left, right):
        left_val = self.eval(left)
        right_val = self.eval(right)
        
        if op == '+': return left_val + right_val
        elif op == '-': return left_val - right_val
        elif op == '*': return left_val * right_val
        elif op == '/': return left_val / right_val
        elif op == '==': return left_val == right_val
        elif op == '!=': return left_val != right_val
        elif op == '<': return left_val < right_val
        elif op == '>': return left_val > right_val
        else:
            raise RuntimeError(f"Unknown operator: {op}")
    
    def eval_unop(self, op, expr):
        val = self.eval(expr)
        if op == '-': return -val
        else:
            raise RuntimeError(f"Unknown operator: {op}")
    
    def get_var(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(f"Undefined variable: {name}")
    
    def set_var(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name] = value
                return
        self.scopes[-1][name] = value
    
    def call_function(self, func, args):
        if func[0] != 'function':
            raise RuntimeError("Not a function")
        
        params, body = func[1], func[2]
        if len(args) != len(params):
            raise RuntimeError(f"Expected {len(params)} arguments, got {len(args)}")
        
        new_scope = dict(zip(params, args))
        self.scopes.append(new_scope)
        
        try:
            self.eval_block(body)
            result = None
        except ReturnException as e:
            result = e.value
        finally:
            self.scopes.pop()
        
        return result

demo_program = """
�set_min_range_to_1
📦 � ➡️ 1️⃣
�set_max_range_to_10
📦 � ➡️ �
�generate_random_secret_number_between_min_and_max
� � ➡️ 🎲 � 🔵

💭print_guess_the_number_1_to_10
� "🔢❓ 1️⃣ ➡️ 🔟"

💭set_game_running_flag_to_true
� 🏃 ➡️ ✅
💭while_game_is_running
🔁 🏃 �
    �get_user_guess_from_input
    📦 🟣 ➡️ � "�➡️"
    💭if_guess_equals_secret
    ❓ 🟣 🟰 🔒 �
        💭print_correct_you_win
        � "✅�"
        💭set_running_to_false_to_end_game
        � 🏃 ➡️ ❌
    💭else
    🔄 👉
        �if_guess_is_greater_than_secret
        ❓ 🟣 ⬆️ � �
            💭print_too_high
            � "�❌"
        💭else
        🔄 👉
            💭print_too_low
            📢 "�❌"
        💭end_inner_if
        🔚
    💭end_outer_if
    🔚
💭end_while_loop
🔚
"""

# Emoji language reference
emoji_reference = """
╔══════════════════════════════════════════════════════════════╗
║           🎨 EMOJISCRIPT LANGUAGE REFERENCE 🎨              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📦 VARIABLES & ASSIGNMENT                                   ║
║  ───────────────────────────────────────────────────────────║
║  📦 x ➡️ 5          Store value in variable                 ║
║  📦 name ➡️ "Hi"    Store string in variable                ║
║                                                              ║
║  📢 OUTPUT                                                   ║
║  ───────────────────────────────────────────────────────────║
║  📢 x               Print value                              ║
║  📢 "Hello"         Print string                             ║
║                                                              ║
║  ➕ MATH OPERATORS                                           ║
║  ───────────────────────────────────────────────────────────║
║  ➕                  Addition                                ║
║  ➖                  Subtraction                             ║
║  ✖️                  Multiplication                          ║
║  ➗                  Division                                ║
║                                                              ║
║  🔍 COMPARISONS                                              ║
║  ───────────────────────────────────────────────────────────║
║  🟰                  Equals                                  ║
║  ❌🟰                Not equals                              ║
║  ⬆️                  Greater than                            ║
║  ⬇️                  Less than                               ║
║                                                              ║
║  🤔 LOGIC                                                    ║
║  ───────────────────────────────────────────────────────────║
║  🤝                  AND                                     ║
║  🎭                  OR                                      ║
║  🚫                  NOT                                     ║
║  ✅                  True                                    ║
║  ❌                  False                                   ║
║                                                              ║
║  ❓ CONDITIONALS                                             ║
║  ───────────────────────────────────────────────────────────║
║  ❓ condition 👉     If statement                            ║
║      ...                                                     ║
║  🔄 👉               Else                                    ║
║      ...                                                     ║
║  🔚                  End block                               ║
║                                                              ║
║  🔁 LOOPS                                                    ║
║  ───────────────────────────────────────────────────────────║
║  🔁 condition 👉    While loop                              ║
║      ...                                                     ║
║  🔚                                                          ║
║                                                              ║
║  🔂 n 👉            Repeat n times                          ║
║      ...                                                     ║
║  🔚                                                          ║
║                                                              ║
║  🎯 FUNCTIONS                                                ║
║  ───────────────────────────────────────────────────────────║
║  🎯 name 📥 a b 👉  Define function                         ║
║      ...                                                     ║
║      ⬅️ result      Return value                            ║
║  🔚                                                          ║
║                                                              ║
║  name(x)            Call function                            ║
║                                                              ║
║  🔢 RANGES                                                   ║
║  ───────────────────────────────────────────────────────────║
║  🔢 0 10            Numbers from 0 to 10                    ║
║                                                              ║
║  💭 COMMENTS                                                 ║
║  ───────────────────────────────────────────────────────────║
║  💭 This is a comment                                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

if __name__ == "__main__":
    print("🎉 EmojiScript Interpreter 🎉")
    print("=" * 60)
    print("A programming language using ONLY EMOJIS!\n")
    print(emoji_reference)
    print("\n" + "=" * 60)
    print("\n📝 Program Code:\n")
    print(demo_program)
    print("\n" + "=" * 60)
    print("\n🚀 Program Output:\n")
    
    try:
        lexer = Lexer(demo_program)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter()
        result = interpreter.execute(ast)
        
        print("\n" + "=" * 60)
        print("\n✅ Program completed successfully!")
    except EOFError:
        # Clean exit when stdin reaches EOF (useful for piped tests)
        print("\n⚠️ Input ended (EOF). Exiting.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()