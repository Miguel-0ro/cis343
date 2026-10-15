from expr_ast import Expr

class AstPrinter:
    def print(self, expr: Expr) -> str:
        return expr.accept(self)

    def visit_binary_expr(self, expr):
        return self._parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr):
        return self._parenthesize("group", expr.expression)

    def visit_literal_expr(self, expr):
        if expr.value is None:
            return "nil"
        # --- start AI code ---
        if isinstance(expr.value, bool):
            return "true" if expr.value else "false"
        # --- end AI code ---
        return str(expr.value)

    def visit_unary_expr(self, expr):
        return self._parenthesize(expr.operator.lexeme, expr.right)

    def _parenthesize(self, name, *exprs):
        parts = [name]
        for expr in exprs:
            parts.append(" " + expr.accept(self))
        return f"({ ''.join(parts) })"