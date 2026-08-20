# 🏦 Abstraction in Python: Banking Software

### This repository explores **Abstraction** and **Abstract Base Classes (ABC)** in Python, demonstrating how to enforce design standards across different application interfaces (such as Mobile and Web apps).

### Abstraction ensures that foundational security protocols and essential interfaces are **mandated** across all subclass implementations.

---

## 🛠️ Tools & Environment

* **Language:** Python 🐍
* **Environment:** Jupyter Notebook / VS Code
* **Concepts Used:**
* Abstract Base Classes (`ABC`)
* Abstract Decorators (`@abstractmethod`)
* Method Overriding & Implementation
* Interface Enforcement



---

## 🔒 1. Abstract Base Class (`BankApp`)

### 📌 Concept

An **Abstract Base Class** serves as a blueprint or contract. It defines concrete methods shared by all apps alongside abstract methods that **must** be implemented by any child class before an object can be instantiated.

### 🧾 Code

```python
from abc import ABC, abstractmethod

# Abstract Base Class defining the blueprint
class BankApp(ABC):
    
    # Concrete Method: Shared by all inheriting classes
    def database(self):
        return "Database Connected Successfully!"

    # Abstract Method: Enforces child classes to define security logic
    @abstractmethod
    def security(self):
        pass 

    # Abstract Method: Enforces child classes to define display logic
    @abstractmethod
    def display(self):
        return "This is the display!"

```

### 📘 Explanation

* **`ABC`**: Inheriting from `ABC` prevents `BankApp` from being instantiated directly (e.g., `app = BankApp()` raises an error).
* **`@abstractmethod`**: Decorator indicating that child classes must override and provide their own custom implementation for these specific methods.

---

## 📱 2. Concrete Implementation (`MobileApp`)

### 📌 Concept

A **Concrete Class** inherits from the abstract parent class and implements all defined abstract methods, allowing objects of this class to be instantiated.

### 🧾 Code

```python
# Child Class implementing the abstract blueprint
class MobileApp(BankApp):

    # Specialized Method unique to MobileApp
    def mobile_login(self):
        return "Login to mobile!"

    # Implementing mandatory abstract method
    def security(self):
        return "Mobile app is secured" 

    # Implementing mandatory abstract method
    def display(self):
        return "This is the mobile display!"


# Object Creation and Execution
myapp = MobileApp()  

print(myapp.database())     # Output: Database Connected Successfully! (Inherited)
print(myapp.mobile_login()) # Output: Login to mobile!
print(myapp.security())     # Output: Mobile app is secured
print(myapp.display())      # Output: This is the mobile display!

```

### 🎯 Use Case

✔ **Standardized Frameworks:** Guarantees that every platform (Mobile, Web, ATM) includes critical mechanisms like `security()` and `display()` before deployment.
✔ **Preventing Incomplete Code:** If a child class fails to implement *any* `@abstractmethod`, Python throws a `TypeError` at runtime during object creation.

---

## 🧠 Concepts Practiced

* **Data Abstraction:** Hiding complex execution details and exposing only essential interface definitions.
* **Enforced Consistency:** Utilizing `@abstractmethod` to enforce strict coding standards across distinct module teams.
* **Contract-Driven Design:** Designing reliable enterprise systems by specifying clear subclass contracts.

---
