#include <stddef.h>
#include <stdio.h>

typedef struct ExpressionNode {
    const char *label;
    struct ExpressionNode *left;
    struct ExpressionNode *right;
} ExpressionNode;

int main(void)
{
    ExpressionNode two = {"2", NULL, NULL};
    ExpressionNode three = {"3", NULL, NULL};
    ExpressionNode four = {"4", NULL, NULL};
    ExpressionNode multiply = {"*", &three, &four};
    ExpressionNode add = {"+", &two, &multiply};
    ExpressionNode *root = &add;

    printf("Root: %s\n", root->label);
    printf("Left child: %s\n", root->left->label);
    printf("Right child: %s\n", root->right->label);
    printf("Multiply operands: %s, %s\n",
           root->right->left->label, root->right->right->label);
    return 0;
}
