# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.
/ consider storing the list in **init**
implement an \_add method that adds tasks to the todo list.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

implement a \_remove method which takes in item to remove and removes from list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Todos:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   none
        # stores the list in which the todos are assigned and removed
        self._todos = []


    def add(self, item):
        # Parameters:
        #   item: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the todo to the self._todos list
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def remove(self, item_to_delete):
        # Returns:
        #    "This todo item is not in your list" if item_to_delete not in list
        # Side-effects:
            #removes item_to_delete from self._todos []
            #throws an exception if item_to_delete is not stored in self._todos
        pass # No code here yet

    def display_todos(self):
        # Returns:
            #a list of all todos
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python
# EXAMPLE

"""
Given a todo item
#my_todos.add(item) stores the todo

"""
my_todos = Todos()
my_todos.add("first todo item")

tick

"""
Given a todo item
#my_todos.add(item) stores the todo
#my_todos.remove(item_to_delete) removes given todo from list
#my_todos.display_todos() returns a list of all current todos.

"""
my_todos = Todos()
my_todos.add("do the laundry", "walk the dog")
my_todos.remove("do the laundry")

my_todos.display_todos() => ["walk the dog"]


"""
Given no todo
#my_todo.add() raises an exception
"""
my_todos = Todos()
my_todos.add() => exception "no todo was set"

"""
Given a todo that isn't stored in the todo list
#my_todos.remove("not in list") raises an exception
"""
my_todos = Todos()
my_todos.add("walk the dog")
my_todos.remove("do the laundry") => exception "this item is not in your todo list"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
