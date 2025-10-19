from emoji import Lexer, Parser, Interpreter

print("=" * 60)
print("Testing Error Handling")
print("=" * 60)

# Test 1: Redeclaring a variable
print("\n1. Test redeclaring a variable:")
test1 = """
📦 🔵 ➡️ 5️⃣
📦 🔵 ➡️ 1️⃣0️⃣
"""
try:
    lexer = Lexer(test1)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast)
    print("❌ Should have raised an error!")
except RuntimeError as e:
    print(f"✅ Caught error: {e}")

# Test 2: Assigning to a non-existent variable (using shorthand)
print("\n2. Test assigning to undeclared variable (shorthand):")
test2 = """
🔴 ➡️ 1️⃣0️⃣
"""
try:
    lexer = Lexer(test2)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast)
    print("✅ Shorthand assignment creates variable (allowed)")
except Exception as e:
    print(f"Error: {e}")

# Test 3: Using undefined variable
print("\n3. Test using undefined variable:")
test3 = """
🖨️ 🔴
"""
try:
    lexer = Lexer(test3)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast)
    print("❌ Should have raised an error!")
except NameError as e:
    print(f"✅ Caught error: {e}")

# Test 4: Valid redeclaration in different scopes (should work)
print("\n4. Test valid code (no errors):")
test4 = """
📦 🔵 ➡️ 5️⃣
🔵 ➡️ 1️⃣0️⃣
��️ 🔵
"""
try:
    lexer = Lexer(test4)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.execute(ast)
    print("✅ Code executed successfully")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n" + "=" * 60)
print("Error Handling Tests Complete")
print("=" * 60)
