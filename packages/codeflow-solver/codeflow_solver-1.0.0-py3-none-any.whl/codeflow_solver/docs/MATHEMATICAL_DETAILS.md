# SAST Set Cover Solver: Optimized Vulnerability Remediation

## The Challenge

When Static Application Security Testing (SAST) tools scan large codebases, they often identify thousands of vulnerabilities. A typical enterprise scan might reveal thousands of vulnerabilities across hundreds of files. The traditional approach of addressing each vulnerability individually is inefficient and time-consuming.

**Traditional approach:** Fix each vulnerability individually

**Optimized approach:** Strategic fixing using mathematical optimization


---

## Part 1: Why SAST Problems Are Set Cover Problems

### The Core Insight

SAST (Static Application Security Testing) tools don't just find individual vulnerabilities—they discover relationships between them. When a security scanner analyzes your code, it uses [taint analysis](https://www.sonarsource.com/blog/what-is-taint-analysis/) to track how untrusted data flows through your application. This analysis reveals a crucial pattern: many vulnerabilities share common root causes.

### How Taint Analysis Works

**Taint analysis** follows untrusted data through three stages:

1. **Sources:** Where dangerous data enters (user input, file reads, network data)
2. **Flows:** How data moves through your code (string operations, function calls, assignments)  
3. **Sinks:** Where vulnerabilities manifest (database queries, HTML output, file operations)

Multiple vulnerabilities often trace back to the same data sources and flow through shared code paths.

### Why This Creates Optimization Opportunities

When SAST tools map these data flows, they reveal that fixing at **upstream locations** can eliminate **multiple downstream vulnerabilities** simultaneously. Instead of patching each vulnerability individually, you can implement strategic fixes that address root causes.

### From Security Problem to Mathematical Optimization

This problem can be mapped into a well-known mathematical optimization problem: the **Set Cover Problem**.

- **Universe:** The set of all vulnerabilities that need to be eliminated
- **Sets:** Each potential fix location and the vulnerabilities it covers
- **Objective:** Find the minimum number of fix locations that cover all vulnerabilities


---

## Part 2: SAST Set Cover Problem Formulation

### How SAST scans Data Maps to Set Cover

When our solver analyzes SAST scan results, it extracts two key mathematical structures:

**1. Vulnerability Universe (V)**
- Each vulnerability `vⱼ` found by the SAST tool becomes an element in our universe
- Example: `v₁₂₃` = XSS vulnerability at `login.jsp:45`
- The universe V contains all vulnerabilities that must be eliminated for each vulnerability type

**2. Fix Location Coverage Sets (N and Sᵥ)**
- Each potential fix location `nᵢ` is extracted from SARIF code flows
- Each fix location has a coverage set `Sᵥ(nᵢ)` = vulnerabilities eliminated by fixing at that location
- Example: Fix at `InputValidator.java:23` might eliminate vulnerabilities {v₁₂₃, v₄₅₆, v₇₈₉}

### Mathematical Formulation for SAST

**Universe:** `V = {v₁, v₂, ..., vₘ}` (all vulnerabilities from SARIF)

**Fix Locations:** `N = {n₁, n₂, ..., nₖ}` (potential fix points from code flows)

**Coverage Function:** `Sᵥ(nᵢ) ⊆ V` (vulnerabilities covered by fixing at location nᵢ)

### Integer Linear Programming Translation

**Decision Variables:**
- `xᵢ ∈ {0,1}` for each fix location nᵢ
- `xᵢ = 1` means "implement fix at location nᵢ"
- `xᵢ = 0` means "skip this fix location"

**Objective Function:**
- `Minimize Σ xᵢ` (minimize total number of code changes)

**Coverage Constraints:**
- For each vulnerability `vⱼ ∈ V`: `Σ(xᵢ : vⱼ ∈ Sᵥ(nᵢ)) ≥ 1`
- Translation: "Every vulnerability must be covered by at least one selected fix"

### SAST Example

Consider a scan that finds 5 XSS vulnerabilities:

```
Vulnerabilities (V):
v₁ = XSS at login.jsp:23
v₂ = XSS at search.jsp:45  
v₃ = XSS at profile.jsp:67
v₄ = XSS at admin.jsp:89
v₅ = XSS at dashboard.jsp:12

Fix Locations (N) with Coverage Sets Sᵥ(nᵢ):
n₁: InputValidator.java:15    → Sᵥ(n₁) = {v₁, v₂, v₃}
n₂: DatabaseUtil.java:42      → Sᵥ(n₂) = {v₁, v₄}
n₃: SessionHandler.java:78    → Sᵥ(n₃) = {v₃, v₅}
n₄: OutputEncoder.java:23     → Sᵥ(n₄) = {v₂, v₄, v₅}
```

**ILP Constraints:**
- v₁ coverage: x₁ + x₂ ≥ 1 (must fix at n₁ or n₂)
- v₂ coverage: x₁ + x₄ ≥ 1 (must fix at n₁ or n₄)  
- v₃ coverage: x₁ + x₃ ≥ 1 (must fix at n₁ or n₃)
- v₄ coverage: x₂ + x₄ ≥ 1 (must fix at n₂ or n₄)
- v₅ coverage: x₃ + x₄ ≥ 1 (must fix at n₃ or n₄)

**Optimal Solution:** x₁ = 1, x₄ = 1 (fix at n₁ and n₄)
- **Result:** 2 code changes eliminate all 5 vulnerabilities
- **Verification:** Sᵥ(n₁) ∪ Sᵥ(n₄) = {v₁,v₂,v₃} ∪ {v₂,v₄,v₅} = {v₁,v₂,v₃,v₄,v₅} ✓

### Why Integer Linear Programming?

The set cover problem is **NP-hard**, meaning there's no known algorithm that can solve it efficiently for large instances using brute force. With thousands of vulnerabilities and fix locations, checking all possible combinations would take longer than the age of the universe.

**Why we chose OR-Tools instead of coding our own algorithm:**
- Implementing set cover algorithms from scratch would require a lot of time
- We'd need to code complex algorithms like branch-and-bound, cutting planes, and heuristics
- OR-Tools provides battle-tested, industrial-grade solvers

**Integer Linear Programming (ILP) with OR-Tools SCIP solver:**
- OR-Tools offers the [SCIP solver](https://developers.google.com/optimization/cp/cp_solver) for integer programming problems
- SCIP uses state-of-the-art algorithms (branch-and-bound, cutting planes, presolving)
- It can find optimal solutions for problems with thousands of variables in seconds
- **Requirement:** Problems must be formulated as ILP with integer variables and linear constraints


---

## Part 3: Implementation Using OR-Tools

*Our implementation follows the excellent tutorial by Matt Chapman: [Solving the Set Cover Problem with Python and OR-Tools](https://insidedatascience.com/blog/set-cover-problem), we just adapted it specifically for SAST vulnerability remediation.*


### OR-Tools Overview

OR-Tools is Google's open-source optimization suite that provides industrial-strength solvers for linear programming, integer programming, constraint programming, and other optimization problems. For the Set Cover Problem, we leverage its Integer Linear Programming (ILP) capabilities.

**Core functionality:** OR-Tools implements state-of-the-art algorithms (branch-and-bound, cutting planes, heuristics) to find provably optimal solutions to combinatorial optimization problems.

### Implementation Strategy

#### Step 1: Extract Problem Structure from SARIF Data

```python
# Parse SARIF file to extract vulnerability universe and coverage sets
vulnerabilities = ['v1', 'v2', 'v3', 'v4', 'v5']  # Universe U: all vulnerabilities to eliminate

# Coverage mapping: fix location → set of vulnerabilities eliminated
fix_locations = {
    'UserInputValidator.java:45': ['v1', 'v2', 'v3'],  # Set A
    'DatabaseQuery.java:12': ['v1', 'v4'],             # Set B  
    'SessionManager.java:78': ['v3', 'v5'],            # Set C
    'OutputEncoder.java:23': ['v2', 'v4', 'v5']        # Set D
}
```

#### Step 2: Initialize Integer Programming Solver

```python
from ortools.linear_solver import pywraplp

# Create SCIP solver for integer linear programming
solver = pywraplp.Solver.CreateSolver('SCIP')

# Define binary decision variables xᵢ ∈ {0,1} for each fix location
fix_vars = {}
for location in fix_locations:
    fix_vars[location] = solver.IntVar(0, 1, location)
```

#### Step 3: Define Coverage Constraints

```python
# Constraint: Each vulnerability must be covered by at least one selected fix
for vuln in vulnerabilities:
    constraint = solver.Constraint(1, solver.infinity())  # Σ xᵢ ≥ 1
    for location, covered_vulns in fix_locations.items():
        if vuln in covered_vulns:
            constraint.SetCoefficient(fix_vars[location], 1)
```

#### Step 4: Set Optimization Objective

```python
# Objective: Minimize Σ xᵢ (total number of selected fix locations)
objective = solver.Objective()
for location in fix_locations:
    objective.SetCoefficient(fix_vars[location], 1)
objective.SetMinimization()
```

#### Step 5: Solve and Extract Solution

```python
# Execute optimization
status = solver.Solve()

# Extract optimal fix locations
if status == pywraplp.Solver.OPTIMAL:
    selected_fixes = []
    for location in fix_locations:
        if fix_vars[location].solution_value() > 0.5:  # xᵢ = 1
            selected_fixes.append(location)
    
    print(f"Optimal solution requires {len(selected_fixes)} fixes")
    for fix in selected_fixes:
        print(f"Fix location: {fix}")
```