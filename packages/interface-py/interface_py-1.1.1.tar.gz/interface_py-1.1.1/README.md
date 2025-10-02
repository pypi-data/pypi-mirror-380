# interface-py

**interface-py** is a lightweight Python package for defining **interfaces** and **concrete implementations** with enforced contracts.  
It ensures that concrete classes implement all required methods, properties, and **fields**, including optional enforcement of getter/setter properties.

---

## Features

- Define **interfaces** using a decorator or base class.
- Enforce that concrete classes implement all interface methods, fields, and properties.
- Support for **fields** with three declaration styles:
  1. With annotation only → `x: int`
  2. With annotation + `...` → `y: float = ...`
  3. Without annotation + `...` → `z = ...`
- Enforce **getter** and **setter** implementation for properties.
- Supports **multi-level interface hierarchies**.
- Prevents runtime errors from missing implementations.
- Works alongside Python's built-in ABCs.

---

## Installation

```bash
pip install interface-py
```

---

## Usage

### Defining an Interface

```python
from interface_py import interface, InterfaceBase

@interface
class HumanInterface(InterfaceBase):
    # field definitions
    name: str
    age: int = ...
    nickname = ...
    
    def speak(self): ...
    
    @property
    def rank(self): ...
    
    @rank.setter
    def rank(self, value): ...
```

### Multi-level Interface Example

```python
from interface_py import interface, concrete

@interface
class MilitaryHumanInterface(HumanInterface):
    def march(self): ...

@concrete
class Soldier(MilitaryHumanInterface):
    name: str = "John"
    age: int = 25
    nickname = "Eagle"
    
    def speak(self):
        print("Reporting for duty!")

    def march(self):
        print("Marching!")

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, value):
        self._rank = value
```

---

## Field Enforcement Examples

```python
from interface_py import interface, concrete, InterfaceBase

@interface
class ExampleInterface(InterfaceBase):
    x: int              # only annotation
    y: float = ...      # annotation with ellipsis
    z = ...             # plain ellipsis


# ✅ Correct implementation
@concrete
class GoodImpl(ExampleInterface):
    x: int = 10
    y: float = 3.14
    z = "hello"


# ❌ Incorrect implementation
@concrete
class BadImpl(ExampleInterface):
    x: str = "oops"   # wrong type (expected int)
    # y missing → TypeError
    z = ...           # not allowed to keep ellipsis
```

---

## Validation

- Instantiating a concrete class that **does not implement all interface methods/fields/properties** raises a `TypeError`.
- Ensures consistent **interface contracts** across your project.

---

## Why Use interface-py?

- Provides **contract enforcement** in dynamically typed Python.
- Helps structure large codebases with clear **interface and implementation separation**.
- Avoids runtime errors from missing methods, fields, or properties.
- Enhances code **readability**, **maintainability**, and **Pythonic design**.

---

## License

MIT License
