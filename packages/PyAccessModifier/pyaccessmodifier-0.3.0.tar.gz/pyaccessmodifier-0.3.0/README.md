# Python Access Modifiers Library

This library provides **access control mechanisms** for Python classes, including `Private`, `Protected`, `Internal`, and `Public` variables and methods. Python does not enforce strict access modifiers like Java or C++, but this library uses **descriptors and decorators** to simulate them.

---

## Variable Descriptors

### 1. `Private`
- **Purpose:** Restrict access to the variable only within the defining class.
- **Example:**
```python
class MyClass:
    my_private = Private(42)
```
- **Behavior:** 
  - Reading or writing from outside the class raises `PermissionError`.
  - Only instances of the defining class can access the value.

---

### 2. `Protected`
- **Purpose:** Allow access only from the defining class and its subclasses.
- **Example:**
```python
class MyClass:
    my_protected = Protected(10)

class Child(MyClass):
    def access_protected(self):
        print(self.my_protected)
```
- **Behavior:** 
  - Reading or writing from unrelated classes raises `PermissionError`.
  - Subclasses can access and modify the value.

---

### 3. `Internal`
- **Purpose:** Restrict access to code within the same folder/module.
- **Example:**
```python
class MyClass:
    my_internal = Internal(99)
```
- **Behavior:** 
  - Access from files outside the same folder raises `PermissionError`.
  - Useful for module-level encapsulation.

---

### 4. `Public`
- **Purpose:** Standard public variable, no access restriction.
- **Example:**
```python
class MyClass:
    my_public = Public(123)
```
- **Behavior:** 
  - Can be accessed and modified freely from anywhere.

---

## Function Decorators

### 1. `@private`
- **Purpose:** Restrict method access to the defining class only.
- **Example:**
```python
class MyClass:
    @private
    def secret_method(self):
        print("Private Method")
```
- **Behavior:** 
  - Calling from outside the class raises `PermissionError`.

---

### 2. `@protected`
- **Purpose:** Allow method access from the defining class and subclasses.
- **Example:**
```python
class MyClass:
    @protected
    def prot_method(self):
        print("Protected Method")
```
- **Behavior:** 
  - Calling from unrelated classes raises `PermissionError`.

---

### 3. `@internal`
- **Purpose:** Restrict method access to the same folder/module.
- **Example:**
```python
class MyClass:
    @internal
    def internal_method(self):
        print("Internal Method")
```
- **Behavior:** 
  - Calling from files in different folders raises `PermissionError`.

---

### 4. `@public`
- **Purpose:** Standard public method, no restriction.
- **Example:**
```python
class MyClass:
    @public
    def pub_method(self):
        print("Public Method")
```
- **Behavior:** 
  - Can be called from anywhere.

---

## Example Usage
```python
class MyClass:
    my_private = Private(42)
    my_protected = Protected(10)
    my_internal = Internal(99)
    my_public = Public(123)

    @private
    def secret_method(self):
        print(self.my_private)

    @protected
    def prot_method(self):
        print(self.my_protected)

    @internal
    def internal_method(self):
        print(self.my_internal)

    @public
    def pub_method(self):
        print(self.my_public)


class Child(MyClass):
    def access_protected(self):
        print(self.my_protected)
        self.prot_method()
```

**Notes:**
- Python does not natively support strict access control.
- This library leverages **descriptors** for variables and **decorators** for methods.
- Use with caution, as it relies on **call stack inspection** (`inspect`) and may not cover all edge cases.
