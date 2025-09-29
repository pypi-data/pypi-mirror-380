from graphql import (
    GraphQLField,
    GraphQLObjectType,
    GraphQLSchema,
    GraphQLString,
    graphql_sync,
)

user = GraphQLObjectType(
    name="User",
    fields={
        "id": GraphQLField(GraphQLString),
        "name": GraphQLField(GraphQLString),
    },
)


def resolve_user(_obj, _info):
    return {
        "id": "1",
        "name": "Sarah",
    }


schema = GraphQLSchema(
    query=GraphQLObjectType(
        name="Query",
        fields={
            "user": GraphQLField(
                user,
                resolve=resolve_user,
            )
        },
    )
)


def test_execute_basic_sync(benchmark):
    result = benchmark(lambda: graphql_sync(schema, "query { user { id, name }}"))
    assert not result.errors
    assert result.data == {
        "user": {
            "id": "1",
            "name": "Sarah",
        },
    }
