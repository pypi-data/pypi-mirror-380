from __future__ import annotations

from graphql.pyutils import suggestion_list


def expect_suggestions(input_: str, options: list[str], expected: list[str]) -> None:
    assert suggestion_list(input_, options) == expected


def describe_suggestion_list():
    def returns_results_when_input_is_empty():
        expect_suggestions("", ["a"], ["a"])

    def returns_empty_array_when_there_are_no_options():
        expect_suggestions("input", [], [])

    def returns_options_with_small_lexical_distance():
        expect_suggestions("greenish", ["green"], ["green"])
        expect_suggestions("green", ["greenish"], ["greenish"])

    def rejects_options_with_distance_that_exceeds_threshold():
        expect_suggestions("aaaa", ["aaab"], ["aaab"])
        expect_suggestions("aaaa", ["aabb"], ["aabb"])
        expect_suggestions("aaaa", ["abbb"], [])

        expect_suggestions("ab", ["ca"], [])

    def returns_options_with_different_case():
        expect_suggestions("verylongstring", ["VERYLONGSTRING"], ["VERYLONGSTRING"])

        expect_suggestions("VERYLONGSTRING", ["verylongstring"], ["verylongstring"])

        expect_suggestions("VERYLONGSTRING", ["VeryLongString"], ["VeryLongString"])

    def returns_options_with_transpositions():
        expect_suggestions("agr", ["arg"], ["arg"])

        expect_suggestions("214365879", ["123456789"], ["123456789"])

    def returns_options_sorted_based_on_lexical_distance():
        expect_suggestions("abc", ["a", "ab", "abc"], ["abc", "ab", "a"])

        expect_suggestions(
            "GraphQl",
            ["graphics", "SQL", "GraphQL", "quarks", "mark"],
            ["GraphQL", "graphics"],
        )

    def returns_options_with_the_same_lexical_distance_sorted_naturally():
        expect_suggestions("a", ["az", "ax", "ay"], ["ax", "ay", "az"])

        expect_suggestions("boo", ["moo", "foo", "zoo"], ["foo", "moo", "zoo"])

        expect_suggestions("abc", ["a1", "a12", "a2"], ["a1", "a2", "a12"])

    def returns_options_sorted_first_by_lexical_distance_then_naturally():
        expect_suggestions(
            "csutomer",
            ["store", "customer", "stomer", "some", "more"],
            ["customer", "stomer", "some", "store"],
        )
