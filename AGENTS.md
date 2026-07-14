# AI Coding Agent Instructions

## Project Context

**IT Starter Pack #32 / Basic Programming Workshop 2** — A beginner Python workshop with two tasks:

- **Task A**: Profit calculation system (quantity, cost, selling price inputs)
- **Task B**: Recruitment screening system (name, age, height, strength, money inputs)

This is educational material designed to teach fundamental Python: input, arithmetic, conditionals, and string formatting.

## Code Style & Conventions

### Input/Output Pattern
- Use `input()` with Thai language prompts and clear labels
- Use `int()` or appropriate type conversion immediately when reading inputs
- Store inputs in descriptive variable names (e.g., `quantity`, `cost_price`, `sell_price`)
- Format output with f-strings and Thai labels for clarity

**Example from existing code:**
```python
quantity = int(input("จำนวนปืนที่รับมาขาย"))
cost = int(input("ต้นทุนปืนที่รับมา"))
print(f"ต้นทุน{total}")
```

### Common Patterns to Use
- **Arithmetic calculations**: Sequence operations clearly (totals → profit → deductions → per-person splits)
- **Conditionals**: Use `if` statements for screening logic and position assignment
- **String formatting**: Use f-strings with meaningful labels and units

## Inline Suggestion Guidelines

### When Suggesting Improvements

**1. Type Safety & Input Validation**
- Suggest converting inputs immediately to appropriate types (int, float)
- Highlight incomplete type conversions (e.g., `money = ("เงิน")` should be `money = int(input("เงิน"))`)
- Recommend input validation for edge cases (negative values, age bounds)

**2. Variable Naming**
- Suggest descriptive names over abbreviations for learner clarity
- Flag typos like `strangth` → `strength`, `teammembers` → `team_members`

**3. Calculation Clarity**
- Suggest breaking complex calculations into intermediate variables
- Recommend comments explaining business logic (e.g., `# Boss takes 20% of profit`)

**4. Output Formatting**
- Suggest adding units and context in print statements
- Recommend consistent formatting (f-strings) for all output

**5. Conditional Logic**
- Suggest using clear `if`/`elif`/`else` patterns
- Recommend defining screening criteria before implementation

### What NOT to Suggest
- Advanced patterns (list comprehensions, decorators, async)
- Complex libraries beyond standard library basics
- Refactoring into functions/classes (unless explicitly requested)
- Non-educational optimizations

### Tone for Suggestions
- Use friendly, educational language
- Explain *why* a suggestion improves the code
- Reference the existing code patterns as examples
- Keep suggestions focused on one improvement at a time

## Common Beginner Mistakes to Watch For

| Issue | Pattern | Suggestion |
|-------|---------|-----------|
| Incomplete input conversion | `money = ("เงิน")` | Wrap with `int(input(...))` |
| Inconsistent variable names | `cost`, `Cost`, or abbreviations | Use snake_case consistently |
| Missing calculation steps | Combining operations inline | Break into named intermediate variables |
| Unclear output | Raw print of numbers | Use f-strings with labels and context |
| Incomplete conditionals | `if age` without comparison | Complete the condition (e.g., `if age >= 18`) |

## Task-Specific Notes

### Task A: Profit Calculation
- Expected workflow: Total Cost → Total Revenue → Net Profit → Boss Share → Per-Member Share
- Common issue: Forgetting to subtract boss share before dividing among team members
- Validation needed: Ensure team_members > 0 for division

### Task B: Recruitment Screening
- Screening criteria are flexible and learner-defined
- Expected pattern: Input → Evaluate conditions → Assign position or reject
- Common issue: Multiple nested conditions can become unclear
- Suggestion: Define criteria clearly with comments before building the if/elif chain

---

**For AI Agents**: Focus inline suggestions on clarity, correctness, and beginner-appropriate improvements. Link to the [README.md](README.md) for full task requirements.
