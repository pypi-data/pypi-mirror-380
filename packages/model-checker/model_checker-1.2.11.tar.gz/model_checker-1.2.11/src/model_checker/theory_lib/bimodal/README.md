# Bimodal Logic Implementation

## Table of Contents

- [Overview](#overview)
  - [Package Contents](#package-contents)
- [Basic Usage](#basic-usage)
  - [Settings](#settings)
  - [Example Structure](#example-structure)
  - [Running Examples](#running-examples)
    - [1. From the Command Line](#1-from-the-command-line)
    - [2. In VSCodium/VSCode](#2-in-vscodiumvscode)
    - [3. In Development Mode](#3-in-development-mode)
    - [4. Using the API](#4-using-the-api)
  - [Theory Configuration](#theory-configuration)
- [Key Classes](#key-classes)
  - [BimodalSemantics](#bimodalsemantics)
  - [BimodalProposition](#bimodalpropositon)
  - [BimodalStructure](#bimodalstructure)
- [Bimodal Language](#bimodal-language)
  - [Necessity Operator](#necessity-operator-box)
  - [Future Operator](#future-operator-future)
  - [Past Operator](#past-operator-past)
- [Important Theorems](#important-theorems)
- [Implementation Details](#implementation-details)
  - [World and Time Representation](#world-and-time-representation)
  - [Time-Shift Relations](#time-shift-relations)
  - [Model Extraction Process](#model-extraction-process)
- [Model Iteration](#model-iteration)
  - [Iterator Functionality](#iterator-functionality)
  - [Difference Detection](#difference-detection)
- [Frame Constraints](#frame-constraints)
- [Known Limitations](#known-limitations)
- [References](#references)

## Overview

The bimodal theory provides **15 operators** (9 primitive, 6 defined) across **3 categories** with **22 test examples**:

1. **Temporal operators** (4 operators): For reasoning about different times (past and future)
   - Future (`\Future`), Past (`\Past`), and their duals
2. **Modal operators** (2 operators): For reasoning about different world histories  
   - Necessity (`\Box`) and Possibility (`\Diamond`)
3. **Extensional operators** (9 operators): For classical reasoning
   - Negation, conjunction, disjunction, conditional, biconditional, top, bottom

This implementation provides a framework to study bimodal logics where:

- World histories are sequences of world states evolving over time
- Each world state is an instantaneous configuration of the system
- Sentence letters are assigned truth-values at world states alone (times are exogenous)
- World states are not inherently indexed to any time or times
- World histories follow lawful transitions between consecutive world states
- Times can be negative, zero, or positive integers
- Each world history has a temporal interval that includes 0 (the evaluation time)
- World histories may be temporally shifted by including the same sequence of world states
- Every world history that can be temporally shifted has a temporally shifted counterpart

The abundance of temporally shifted worlds ensures that world states are agnostic about the times at which they occur.
It follows that what is necessarily the case is always the case, and what is sometimes the case is possible.

### Package Contents

This package includes the following core modules:

- `semantic.py`: Defines the core semantics and model structure for bimodal logic
- `operators.py`: Implements all primitive and derived logical operators
- `examples.py`: Contains example formulas for testing and demonstration
- `__init__.py`: Exposes package definitions for external use

## Key Classes

### BimodalSemantics

The `BimodalSemantics` class defines the semantic models for the language, including:

- **Primitive relations**: Task transitions between world states
- **Frame constraints**: Rules that define valid model structures
- **Truth conditions**: How to evaluate atomic propositions at world states

The semantics is independent of the operators defined over the semantics.
This modular design makes it easy to compare semantic theories for the same operators as well as to compare operators for the same semantics.

### BimodalProposition

The `BimodalProposition` class handles the interpretation and representation of sentences over a model.
This includes:

- **Extension calculation**: Computing truth/falsity across worlds and times
- **Truth evaluation**: Checking truth values at specific world-time pairs
- **Proposition display**: Visualizing propositions in the model

Although sentence letters may be evaluated at world states on their own, tense and modal operators can only be interpreted at a world history and time.

### BimodalStructure

The `BimodalStructure` class manages the model structure extracted from a Z3 model:

- **Time intervals**: Valid intervals for each world history
- **World arrays**: Mappings from time points to world states
- **Time-shift relations**: Relationships between shifted world histories
- **Visualization**: Methods to display the resulting model structure

## Basic Usage

The bimodal theory provides a framework for working with temporal and modal operators in combination. This section explains how to use the theory's main components and run examples.

For comprehensive documentation of all available settings including theory-specific options like `M` (time points) and `align_vertically`, see **[docs/SETTINGS.md](docs/SETTINGS.md)**.

For general settings that apply across all theories, see the [main settings documentation](../../settings/README.md).

### Settings

The bimodal theory supports the following configurable settings:

```python
DEFAULT_EXAMPLE_SETTINGS = {
    # Number of world_states
    'N': 2,
    # Number of times - specific to bimodal's temporal dimension
    'M': 2,
    # Whether sentence_letters are assigned to contingent propositions
    'contingent': False,
    # Whether sentence_letters are assigned to distinct world_states
    'disjoint': False,
    # Maximum time Z3 is permitted to look for a model
    'max_time': 1,
    # Whether a model is expected or not (used for unit testing)
    'expectation': True,
}

# Bimodal-specific general settings that affect display format
DEFAULT_GENERAL_SETTINGS = {
    "print_impossible": False,
    "print_constraints": False,
    "print_z3": False, 
    "save_output": False,
    "maximize": False,
    "align_vertically": True,  # Bimodal-specific setting for timeline visualization
}
```

The bimodal theory defines two unique settings not found in other theories:

1. **M**: Controls the number of time points in the temporal dimension. Higher values allow for longer world histories but increase computational complexity.

2. **align_vertically**: When set to `True`, displays world histories with time flowing vertically (top to bottom) which is often easier to read for bimodal models. When set to `False`, displays world histories horizontally.

### Example Structure

Each example is structured as a list containing three elements:

```python
[premises, conclusions, settings]
```

Where:
- `premises`: List of formulas that must be true in the model
- `conclusions`: List of formulas to check (invalid if all premises are true and at least one conclusion is false)
- `settings`: Dictionary of settings for this example

Here's a complete example definition:

```python
# Countermodel showing that Future A does not imply Box A
BM_CM_1_premises = ['\\Future A']
BM_CM_1_conclusions = ['\\Box A']
BM_CM_1_settings = {
    'N': 1,
    'M': 2,
    'contingent': False,
    'disjoint': False,
    'max_time': 5,
    'expectation': True,  # Expects to find a countermodel
}
BM_CM_1_example = [
    BM_CM_1_premises,
    BM_CM_1_conclusions,
    BM_CM_1_settings,
]
```

### Running Examples

You can run examples in several ways:

#### 1. From the Command Line

```bash
# Run the default example from examples.py
model-checker path/to/examples.py

# Run with constraints printed 
model-checker -p path/to/examples.py

# Run with Z3 output
model-checker -z path/to/examples.py

# Force vertical alignment for display (bimodal-specific)
model-checker -a path/to/examples.py
```

#### 2. In VSCodium/VSCode

1. Open the `examples.py` file in VSCodium/VSCode
2. Use one of these methods:
   - Click the "Run Python File" play button in the top-right corner
   - Right-click in the editor and select "Run Python File in Terminal"
   - Use keyboard shortcut (Shift+Enter) to run selected lines

#### 3. In Development Mode

For development purposes, you can use the `dev_cli.py` script from the project root directory:

```bash
# Run the examples file
./dev_cli.py path/to/examples.py

# Run with constraints printed
./dev_cli.py -p path/to/examples.py

# Run with Z3 output and constraints printed (combined flags)
./dev_cli.py -z path/to/examples.py

# Run with vertical alignment (bimodal-specific)
./dev_cli.py -a path/to/examples.py
```

#### 4. Using the API

The bimodal theory exposes a clean API:

```python
from model_checker.theory_lib.bimodal import (
    BimodalSemantics, BimodalProposition, BimodalStructure, bimodal_operators
)
from model_checker import ModelConstraints
from model_checker.theory_lib import get_examples

# Get examples
examples = get_examples('bimodal')
example_data = examples['BM_CM_1']
premises, conclusions, settings = example_data

# Create semantic structure
semantics = BimodalSemantics(settings)
model_constraints = ModelConstraints(semantics, bimodal_operators)
model = BimodalStructure(model_constraints, settings)

# Check a formula
prop = BimodalProposition("\\Box A", model)
is_true = prop.truth_value_at(model.main_world, model.main_time)
```

### Theory Configuration

The bimodal theory is defined by combining several components:

```python
bimodal_theory = {
    "semantics": BimodalSemantics,
    "proposition": BimodalProposition,
    "model": BimodalStructure,
    "operators": bimodal_operators,
}

# Define which theories to use when running examples
semantic_theories = {
    "Brast-McKie" : bimodal_theory,
    # additional theories will require translation dictionaries
}
```

#### Countermodel Example

Examples that are expected to have countermodels may be presented as follows:

```python
# Countermodel showing that Future A does not imply Box A
BM_CM_1_premises = ['\\Future A']
BM_CM_1_conclusions = ['\\Box A']
BM_CM_1_settings = {
    'N': 1,
    'M': 2,
    'contingent': False,
    'disjoint': False,
    'max_time': 5,
    'expectation': True,  # Expects to find a countermodel
}
BM_CM_1_example = [
    BM_CM_1_premises,
    BM_CM_1_conclusions,
    BM_CM_1_settings,
]
```

**BM_CM_1:** Shows that "Future A → Box A" is not valid (has a countermodel).

#### Theorem Example

Examples that are not expected to have countermodels may be presented as follows:

```python
# Theorem showing that Box A implies Future A
BM_TH_1_premises = ['\\Box A']
BM_TH_1_conclusions = ['\\Future A']
BM_TH_1_settings = {
    'N': 1,
    'M': 2,
    'contingent': False,
    'disjoint': False,
    'max_time': 5,
    'expectation': False,  # Expects NOT to find a countermodel
}
BM_TH_1_example = [
    BM_TH_1_premises,
    BM_TH_1_conclusions,
    BM_TH_1_settings,
]
```

**BM_TH_1:** Shows that "Box A → Future A" is valid (no countermodel exists).

### Testing

The examples are then collected into dictionaries with `name_string : example` entries:

```python
example_range = {
    # Selected examples for current use
    "BM_CM_2": BM_CM_2_example,
    "BM_TH_1": BM_TH_1_example,
}
```

The `semantic_theories` are then used to evaluate the examples in the `example_range` given the `general_settings`.
It is typical to include many examples, most of which are commented out in order to focus on particular cases.

An optional `test_example_range` may be provided for automating testing when developing semantic theories:

```python
test_example_range = {
    # All examples for testing
    "BM_CM_1": BM_CM_1_example,
    "BM_TH_1": BM_TH_1_example,
    # ... more examples
}
```

See the [README.md](test/README.md) in the `test/` directory for further details on setting up unit testing.py` is run.

## Bimodal Language

> [NOTE] The code blocks included below are abridged for readability.
> Consult the `operators.py` for the complete implementation of the semantic clauses for the language.

Formal languages implemented in the `model-checker` must conform to the following specifications:

- Operators are designated with a double backslash as in `\\Box` and `\\Future`.
- Sentence letters are alpha-numeric strings as in `A`, `B_2`, `Mary_sings`, etc., using underscore `_` for spaces.
- Parentheses must be included around sentences whose main connective is a binary operator.
- Parentheses must NOT be included around sentences whose main connective is a unary operator.

### Necessity Operator (`\\Box`)

The necessity operator (`\\Box`) evaluates whether a formula holds across all possible worlds at a given time.

This operator implements 'It is necessarily the case that' which takes one sentence as an argument.
The operator evaluates whether its argument is true in every possible world at the evaluation time.

**Key Properties:**

- Evaluates truth across all possible worlds at a fixed evaluation time (purely modal)
- Returns true only if the argument is true in ALL possible worlds
- Returns false if there exists ANY possible world where the argument is false

#### Truth Condition

`\\Box A` is true in `eval_world` at `eval_time` if and only if `A` is true in all world histories at `eval_time`.

```python
def true_at(self, argument, eval_world, eval_time):
    return z3.ForAll(
        other_world,
        z3.Implies(
            semantics.is_world(other_world),
            semantics.true_at(argument, other_world, eval_time)
        )
    )
```

#### Falsity Condition

`\\Box A` is false in `eval_world` at `eval_time` if and only if `A` is false in some world history at `eval_time`.

```python
def false_at(self, argument, eval_world, eval_time):
    return z3.Exists(
        other_world,
        z3.And(
            semantics.is_world(other_world),
            semantics.false_at(argument, other_world, eval_time)
        )
    )
```

### Future Operator (`\\Future`)

The future operator (`\\Future`) evaluates whether a formula holds at all future times in a given world history.

This operator implements 'It will always be the case that' which takes one sentence as an argument.
The operator evaluates whether its argument is true at every future time point in the current world history.
Future times are understood to exclude the present time of evaluation.

**Key Properties:**

- Evaluates truth across all future times in the current world history (purely temporal)
- Returns true only if the argument is true at ALL future times
- Returns false if there exists ANY future time where the argument is false

#### Truth Condition

`\Future A` is true at world `w` at time `t` if and only if A is true at all future times in world `w`.

```python
def true_at(self, argument, eval_world, eval_time):
    return z3.ForAll(
        time,
        z3.Implies(
            z3.And(
                semantics.is_valid_time_for_world(eval_world, time),
                eval_time < time
            ),
            semantics.true_at(argument, eval_world, time)
        )
    )
```

#### Falsity Condition

`\Future A` is false at world `w` at time `t` if and only if A is false at at least one future time in world `w`.

### Past Operator (`\Past`)

The past operator `\Past A` has a purely temporal semantics:

#### Truth Condition

`\Past A` is true at world `w` at time `t` if and only if A is true at all past times in world `w`.

```python
def true_at(self, argument, eval_world, eval_time):
    return z3.ForAll(
        time,
        z3.Implies(
            z3.And(
                semantics.is_valid_time_for_world(eval_world, time),
                eval_time > time
            ),
            semantics.true_at(argument, eval_world, time)
        )
    )
```

#### Falsity Condition

`\Past A` is false at world `w` at time `t` if and only if A is false at at least one past time in world `w`.

## Important Theorems

The bimodal semantics validates several important theorems that demonstrate the interaction between modal and temporal operators:

1. **Box-Future Theorem**: `\Box A → \Future A`
   - If A is necessarily true, then it is always true in the future
2. **Box-Past Theorem**: `\Box A → \Past A`
   - If A is necessarily true, then it was always true in the past
3. **Possibility-Future Theorem**: `\future A → \Diamond A`
   - If A is possibly true in the future, then A is possible
4. **Possibility-Past Theorem**: `\past A → \Diamond A`
   - If A was possibly true in the past, then A is possible
   - This theorem connects past possibility to general possibility

## Implementation Details

### World and Time Representation

The bimodal implementation uses these key representations:

- **World states**: Represented as bitvectors (fusions of atomic states)
- **World IDs**: Integer identifiers for world histories (starting at 0)
- **Time points**: Integers allowing negative, zero, and positive values
- **World histories**: Arrays mapping time points to world states
- **Time intervals**: Each world history has a valid interval within which it's defined
- **Evaluation point**: Fixed at world ID 0, time 0

The semantic model defines several Z3 sorts used throughout the implementation:

```python
# Define the Z3 sorts used in the bimodal logic model
self.WorldStateSort = z3.BitVecSort(self.N)  # World states as bitvectors
self.TimeSort = z3.IntSort()                 # Time points as integers
self.WorldIdSort = z3.IntSort()              # World IDs as integers
```

### Time-Shift Relations

Each world has a valid time interval defined by two functions:

```python
# Define interval tracking functions
self.world_interval_start = z3.Function(
    'world_interval_start',
    self.WorldIdSort,  # World ID
    self.TimeSort      # Start time of interval
)

self.world_interval_end = z3.Function(
    'world_interval_end',
    self.WorldIdSort,  # World ID
    self.TimeSort      # End time of interval
)
```

Time intervals are required to be convex (no gaps) and are generated within the range [-M+1, M-1]:

```python
def generate_time_intervals(self, M):
    """Generate all valid time intervals of length M that include time 0."""
    intervals = []
    for start in range(-M+1, 1):  # Start points from -M+1 to 0
        end = start + M - 1       # Each interval has exactly M time points
        intervals.append((start, end))
    return intervals
```

### World Function and Task Relation

The core of the bimodal implementation includes:

1. The world function that maps world IDs to their history arrays:

```python
# Mapping from world IDs to world histories (arrays from time to state)
self.world_function = z3.Function(
    'world_function',
    self.WorldIdSort,                          # Input: world ID
    z3.ArraySort(self.TimeSort, self.WorldStateSort)  # Output: world history
)
```

2. The task relation specifying valid transitions between world states:

```python
# Define the task relation between world states
self.task = z3.Function(
    "Task",
    self.WorldStateSort,  # From state
    self.WorldStateSort,  # To state
    z3.BoolSort()         # Is valid transition?
)
```

The model extraction process follows these steps:

The Skolem abundance constraint ensures that time-shifted worlds exist where needed. This optimization uses Skolem functions to directly define the shifted worlds:

```python
# Define Skolem functions that directly compute the necessary worlds
forward_of = z3.Function('forward_of', self.WorldIdSort, self.WorldIdSort)
backward_of = z3.Function('backward_of', self.WorldIdSort, self.WorldIdSort)
```

For example, if world ID 0 can be shifted forward by 1, then the world `forward_of(0)` must exist and must be a properly time-shifted version of world 0.

This constraint is critical for correctly modeling the interaction between modal and temporal operators in bimodal logic.

### Model Extraction Process

The model extraction process follows these steps:

1. Extract valid world IDs (`_extract_valid_world_ids`)
2. Extract world arrays for each world ID (`_extract_world_arrays`)
3. Extract time intervals for each world (`_extract_time_intervals`)
4. Build time-state mappings for each world history (`_extract_world_histories`)
5. Determine time-shift relations between worlds (`_extract_time_shift_relations`)

This highly structured extraction process helps manage the complexity of bimodal models.

## Frame Constraints

The bimodal logic is defined by the following key frame constraints that determine the structure of models, as implemented in `build_frame_constraints()`:

### 1. Valid World Constraint

Every model must have at least one world history (designated as world 0) that is marked as valid.

```python
valid_main_world = self.is_world(self.main_world)
```

### 2. Valid Time Constraint

Every model must have a valid evaluation time (designated as time 0).

```python
valid_main_time = self.is_valid_time(self.main_time)
```

### 3. Classical Truth Constraint

Each atomic sentence must have a consistent classical truth value at each world state.

```python
classical_truth = z3.ForAll(
    [world_state, sentence_letter],
    z3.Or(
        # Either sentence_letter is true in the world_state
        self.truth_condition(world_state, sentence_letter),
        # Or not
        z3.Not(self.truth_condition(world_state, sentence_letter))
    )
)
```

### 4. World Enumeration Constraint

World histories must be enumerated in sequence starting from 0.

```python
enumeration_constraint = z3.ForAll(
    [enumerate_world],
    z3.Implies(
        # If enumerate_world is a world
        self.is_world(enumerate_world),
        # Then it's non-negative
        enumerate_world >= 0,
    )
)
```

### 5. Convex World Ordering Constraint

There can be no gaps in the enumeration of worlds, ensuring worlds are created in sequence.

```python
convex_world_ordering = z3.ForAll(
    [convex_world],
    z3.Implies(
        # If both:
        z3.And(
            # The convex_world is a world
            self.is_world(convex_world),
            # And greater than 0
            convex_world > 0,
        ),
        # Then world_id - 1 must be valid
        self.is_world(convex_world - 1)
    )
)
```

### 6. Lawful Transition Constraint

Each world history must follow lawful transitions between consecutive states.

```python
lawful = z3.ForAll(
    [lawful_world, lawful_time],
    # If for any lawful_world and lawful time
    z3.Implies(
        z3.And(
            # The lawful_world is a valid world
            self.is_world(lawful_world),
            # The lawful_time is in (-M - 1, M - 1), so has a successor
            self.is_valid_time(lawful_time, -1),
            # The lawful_time is in the lawful_world
            self.is_valid_time_for_world(lawful_world, lawful_time),
            # The successor of the lawful_time is in the lawful_world
            self.is_valid_time_for_world(lawful_world, lawful_time + 1),
        ),
        # Then there is a task
        self.task(
            # From the lawful_world at the lawful_time
            z3.Select(self.world_function(lawful_world), lawful_time),
            # To the lawful_world at the successor of the lawful_time
            z3.Select(self.world_function(lawful_world), lawful_time + 1)
        )
    )
)
```

### 8. Skolem Abundance Constraint

An optimized version of the abundance constraint using Skolem functions to eliminate nested quantifiers, improving Z3 performance.

```python
# Define Skolem functions that directly compute the necessary worlds
forward_of = z3.Function('forward_of', self.WorldIdSort, self.WorldIdSort)
backward_of = z3.Function('backward_of', self.WorldIdSort, self.WorldIdSort)

# Use Skolem functions instead of existential quantifiers
return z3.ForAll(
    [source_world],
    z3.Implies(
        # If the source_world is a valid world
        self.is_world(source_world),
        # Then both:
        z3.And(
            # Forwards condition - if source can shift forward
            z3.Implies(
                self.can_shift_forward(source_world),
                z3.And(
                    # The forward_of function must produce a valid world
                    self.is_world(forward_of(source_world)),
                    # The produced world must be properly shifted
                    self.is_shifted_by(source_world, 1, forward_of(source_world))
                )
            ),
            # Backwards condition - if source can shift backwards
            z3.Implies(
                self.can_shift_backward(source_world),
                z3.And(
                    # The backward_of function must produce a valid world
                    self.is_world(backward_of(source_world)),
                    # The produced world must be properly shifted
                    self.is_shifted_by(source_world, -1, backward_of(source_world))
                )
            )
        )
    )
)
```

### 8. World Uniqueness Constraint

No two worlds can have identical histories over their entire intervals.

```python
world_uniqueness = z3.ForAll(
    [world_one, world_two],
    z3.Implies(
        z3.And(
            self.is_world(world_one),
            self.is_world(world_two),
            world_one != world_two
        ),
        # Worlds must differ at some time point that is valid for both
        z3.Exists(
            [some_time],
            z3.And(
                self.is_valid_time(some_time),
                self.is_valid_time_for_world(world_one, some_time),
                self.is_valid_time_for_world(world_two, some_time),
                z3.Select(self.world_function(world_one), some_time) !=
                z3.Select(self.world_function(world_two), some_time)
            )
        )
    )
)
```

### 9. Time Interval Constraint

An optimized version of the world interval constraint that directly defines interval bounds for each world.

```python
# Generate valid time intervals
time_intervals = self.generate_time_intervals(self.M)

# Create direct mapping for interval bounds
interval_constraints = []

# For each valid world ID, create direct interval constraints
for world_id in range(self.max_world_id):
    # A world must have exactly one of the valid intervals if it exists
    world_constraint = z3.Implies(
        self.is_world(world_id),
        z3.Or(*world_interval_options)
    )

    interval_constraints.append(world_constraint)

# Combine all world constraints
return z3.And(*interval_constraints)
```

### Additional Optional Constraints

The semantic model also defines several optional constraints that can be enabled as needed:

#### Task Restriction Constraint

Ensures the task relation only holds between states in lawful world histories.

```python
task_restriction = z3.ForAll(
    [some_state, next_state],
    z3.Implies(
        # If there is a task from some_state to next_state
        self.task(some_state, next_state),
        # Then for some task_world at time_shifted:
        z3.Exists(
            [task_world, time_shifted],
            z3.And(
                # The task_world is a valid world
                self.is_world(task_world),
                # The successor or time_shifted is a valid time
                self.is_valid_time(time_shifted, -1),
                # Where time_shifted is a time in the task_world,
                self.is_valid_time_for_world(task_world, time_shifted),
                # The successor of time_shifted is a time in the task_world
                self.is_valid_time_for_world(task_world, time_shifted + 1),
                # The task_world is in some_state at time_shifted
                some_state == z3.Select(self.world_function(task_world), time_shifted),
                # And the task_world is in next_state at the successor of time_shifted
                next_state == z3.Select(self.world_function(task_world), time_shifted + 1)
            )
        )
    )
)
```

#### Task Minimization Constraint

Guides Z3 to prefer solutions where consecutive world states are identical when possible, reducing unnecessary state changes.

```python
task_minimization = z3.ForAll(
    [world_id, time_point],
    z3.Implies(
        z3.And(
            self.is_world(world_id),
            self.is_valid_time_for_world(world_id, time_point),
            self.is_valid_time_for_world(world_id, time_point + 1)
        ),
        # Encourage identical states if possible (soft constraint)
        z3.Select(self.world_function(world_id), time_point) ==
        z3.Select(self.world_function(world_id), time_point + 1)
    )
)
```

The frame constraints are applied in a specific order to guide Z3's model search efficiently.

## Model Iteration

The bimodal theory supports finding multiple distinct models through the `BimodalModelIterator` class, which extends the core iteration framework with bimodal-specific features.

### Iterator Functionality

The iterator can find multiple non-isomorphic models that satisfy the same logical constraints:

```python
from model_checker.theory_lib.bimodal import iterate_example

# Find up to 3 distinct models
models = iterate_example(example, max_iterations=3)

# Each model has different structural properties
for i, model in enumerate(models):
    print(f"Model {i+1}:")
    model.print_all()
```

### Difference Detection

The bimodal iterator tracks five categories of differences between consecutive models:

1. **World History Changes**: Modifications to time-state mappings
   - Added/removed worlds
   - Changed states at specific times
   - Modified time points within histories

2. **Truth Condition Changes**: How sentence letters are evaluated
   - Truth value changes at specific states
   - New/removed truth assignments

3. **Task Relation Changes**: Transitions between world states
   - Added/removed task transitions
   - Modified transition relationships

4. **Time Interval Changes**: Valid time ranges for worlds
   - Extended/shortened intervals
   - Shifted interval boundaries

5. **Time Shift Relations**: Relationships between temporally shifted worlds
   - New/removed shift relationships
   - Changed shift targets

Example output:
```
=== DIFFERENCES FROM PREVIOUS MODEL ===

World History Changes:
  World W_0 changed:
    Time -1: a -> b
  + World W_2 added
    History: (-1:a) -> (0:a) -> (1:b)

Truth Condition Changes:
  Letter A:
    State b: False -> True

Task Relation Changes:
  Task a->b: added

Time Interval Changes:
  World W_0 interval: (-1, 1) -> (-2, 2)

Time Shift Relation Changes:
  Time shifts for World W_0 changed:
    Shift -1: W_1 -> W_2
```

These comprehensive differences help understand how the iterator explores the model space and what structural variations exist between models.

## Known Limitations

- **Performance**: Models with many time points or complex formulas may run slowly
- **Z3 Timeouts**: Complex models may hit solver timeouts (adjust the `max_time` setting)
- **Abundance Impact**: The abundance constraint significantly increases computational load
- **Model Complexity**: The full bimodal semantics creates models that may challenge Z3's capabilities
- **Memory Usage**: Large models with many worlds and times can consume significant memory

## References

For more information on bimodal logics and related topics, see:

- The full ModelChecker documentation in `/home/benjamin/Documents/Philosophy/Projects/ModelChecker/Code/src/model_checker/README.md`
- The test suite in `/home/benjamin/Documents/Philosophy/Projects/ModelChecker/Code/src/model_checker/theory_lib/bimodal/test/`
