import ast
import inspect
import textwrap

def backwardable(func):
    src = inspect.getsource(func)
    src = textwrap.dedent(src)

    tree = ast.parse(src)
    func_def = tree.body[0]
    assert isinstance(func_def, ast.FunctionDef)

    # Reverse top-level statements
    reversed_func_def = ast.FunctionDef(
        name=func_def.name,
        args=func_def.args,
        body=list(reversed(func_def.body)),
        decorator_list=[],
        returns=func_def.returns
    )

    # Build two versions: original and reversed
    normal_tree = ast.Module(body=[func_def], type_ignores=[])
    reversed_tree = ast.Module(body=[reversed_func_def], type_ignores=[])

    normal_ns, reversed_ns = {}, {}
    exec(compile(normal_tree, filename="<ast>", mode="exec"), func.__globals__, normal_ns)
    exec(compile(reversed_tree, filename="<ast>", mode="exec"), func.__globals__, reversed_ns)

    normal_func = normal_ns[func.__name__]
    reversed_func = reversed_ns[func.__name__]

    @functools.wraps(func)
    def wrapper(*args, backward=False, **kwargs):
        if backward:
            return reversed_func(*args, **kwargs)
        else:
            return normal_func(*args, **kwargs)

    return wrapper