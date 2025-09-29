# Example with `Joining` Multiple Sources.

In this example, we show the how EQL can perform complex queries that require joining of multiple sources 
(equivalent to tables in a structured database) without ever mentioning join or how to join, instead it is implicit
in the conditions of the query.

This allows for a minimal query description that only contains the high level logic.

## Example Usage

```python
from dataclasses import dataclass, field

from typing_extensions import List

from entity_query_language import an, set_of, From, symbol, HasType, symbolic_mode


@symbol
@dataclass
class Body:
    name: str


@dataclass
class Container(Body):
    ...


@dataclass
class Handle(Body):
    ...


@symbol
@dataclass
class Connection:
    parent: Body
    child: Body


@dataclass
class PrismaticConnection(Connection):
    ...


@dataclass
class FixedConnection(Connection):
    ...


@symbol
@dataclass
class World:
    id_: int
    bodies: List[Body]
    connections: List[Connection] = field(default_factory=list)


# Create the world with its bodies and connections
world = World(1, [Container("Container1"), Container("Container2"), Handle("Handle1"), Handle("Handle2")])
c1_c2 = PrismaticConnection(world.bodies[0], world.bodies[1])
c2_h2 = FixedConnection(world.bodies[1], world.bodies[3])
world.connections = [c1_c2, c2_h2]

# Query for the kinematic tree of the drawer which has more than one component.
with symbolic_mode():
    # Declare the variables
    prismatic_connection = PrismaticConnection(From(world.connections))
    fixed_connection = FixedConnection(From(world.connections))
    parent_container = prismatic_connection.parent
    drawer_body = fixed_connection.parent
    handle = fixed_connection.child

    # Declare the selected variables that will be outputted by the query
    drawer_kinematic_tree = (parent_container, prismatic_connection, drawer_body,
                             fixed_connection, handle)

    # Write the query body
    query = an(set_of(drawer_kinematic_tree,
                      HasType(prismatic_connection.parent, Container),
                      HasType(fixed_connection.child, Handle),
                      prismatic_connection.child == fixed_connection.parent)
               )
results = list(query.evaluate())
assert len(results) == 1
assert results[0][parent_container].name == "Container1"
assert results[0][drawer_body].name == "Container2"
assert results[0][handle].name == "Handle2"
```

In the above example we want to find all drawers and their components by describing their kinematic tree using a
conjunction (AND operation) of conditions that show how the components are connected to each other to form the kinematic
tree.
