#include <stddef.h>
#include <stdio.h>

typedef enum { OTHER_NODE, ASSERT_NODE, TUPLE_NODE } NodeKind;

typedef struct Node {
    NodeKind kind;
    int line;
    const struct Node *children[3];
    size_t child_count;
} Node;

void check_ast(const Node *node)
{
    if (node->kind == ASSERT_NODE) {
        const Node *test = node->children[0];
        if (test->kind == TUPLE_NODE && test->child_count > 0) {
            printf("Line %d: F631 assert test is a non-empty tuple\n", node->line);
        }
    }
    for (size_t i = 0; i < node->child_count; i++) {
        check_ast(node->children[i]);
    }
}

int main(void)
{
    Node comparison = {OTHER_NODE, 2, {NULL}, 0};
    Node message = {OTHER_NODE, 2, {NULL}, 0};
    Node tuple = {TUPLE_NODE, 2, {&comparison, &message}, 2};
    Node bad_assert = {ASSERT_NODE, 2, {&tuple}, 1};
    Node fixed_assert = {ASSERT_NODE, 2, {&comparison, &message}, 2};

    puts("Before fix");
    check_ast(&bad_assert);
    puts("After fix");
    check_ast(&fixed_assert);
    return 0;
}
