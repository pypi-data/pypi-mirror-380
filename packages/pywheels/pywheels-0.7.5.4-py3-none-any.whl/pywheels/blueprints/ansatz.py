from __future__ import annotations
from ..i18n import translate
from ..typing import *
from ..external import *


__all__ = [
    "Ansatz",
    "ansatz_docstring",
]


ansatz_docstring = (
    "通过提供 expression、variables、functions 和 constant_whitelist，可以初始化一个 Ansatz 实例，用于表达一类待优化的数学结构。\n"
    "参数说明如下：\n"
    "- expression：一个字符串形式的数学表达式，表示一个带参函数。\n"
    "- variables：允许在 expression 中出现的变量名列表，每个变量名必须以字母或下划线开头，且仅包含字母、数字或下划线。\n"
    "- functions：允许调用的函数名列表，函数名必须是裸名称（例如 'sin' 而非 'math.sin'），并满足合法标识符规则。\n"
    "- constant_whitelist：允许使用的常量列表，可包含标识符型常量（如 'pi'）和数字型常量（如 '0.5'）。\n\n"

    "expression 中可以包含：\n"
    "- 上述 variables 中的变量；\n"
    "- 上述 functions 中的函数调用；\n"
    "- 参数 param1, param2, ..., paramN（编号必须从1开始，连续编号，不允许跳号）；\n"
    "- 支持的运算符，包括：+、-、*、/、**（即加减乘除和乘方）；\n"
    "- 括号，用于表达优先级；\n"
    "- constant_whitelist 中列出的常量。\n\n"

    "禁止事项：\n"
    "- 不允许在表达式中使用未在 variables、functions 或 constant_whitelist 中声明的标识符；\n"
    "- 不允许使用任何未在 constant_whitelist 中显式列出的数字常量；\n"
    "- 不允许使用不支持的语法结构，如列表、字典、条件表达式等；\n"
    "- 不允许使用不支持的函数调用形式，例如带模块前缀的函数。\n\n"

    "合法示例：\n"
    "若 variables = ['x', 'y']、functions = ['sin', 'exp']、constant_whitelist = ['pi', '0.5', '1']，那么以下表达式是合法的：\n"
    "- 'param1 * sin(param2 * x + pi)'\n"
    "- '(param1 * exp(param2 * x) + 0.5 * y) * param4 + 1'\n\n"

    "非法示例包括：\n"
    "- 使用未声明变量，如 'z + param1'\n"
    "- 使用未注册函数，如 'cos(param1 * x)' 若 'cos' 不在 functions 中\n"
    "- 使用未在白名单中的常量，如 '(x + param1) * 0.3' 若 '0.3' 不在 constant_whitelist 中\n"
    "- 参数编号不连续，如 'param1 + param3'\n\n"

    "通过合法的 ansatz 表达式，可以自动将参数替换为具体数值，用于函数评估或数值最优化等任务。"
)


class Ansatz:
    
    # ----------------------------- Ansatz 初始化 ----------------------------- 
    
    def __init__(
        self,
        expression: str,
        variables: List[str],
        functions: List[str],
        constant_whitelist: List[str] = [],
        seed: int  = 42,
    )-> None:
        
        self._random_generator = random.Random(seed)
        self._check_ansatz_format_error_info = ""
        self._check_ansatz_format_error_info_lock = Lock() 
        
        self._set_value(
            expression = expression,
            variables = variables,
            functions = functions,
            constant_whitelist = constant_whitelist,
        )
        
        self._standardize()
        
    # ----------------------------- 外部动作 -----------------------------   
        
    def get_param_num(
        self,
    )-> int:
        
        return self._param_num
    
    
    def to_expression(
        self,
    )-> str:
        
        return self._to_expression()
    
    
    def reduce_to_numeric_ansatz(
        self,
        params: List[float],
        stringify_format: str = ".8g",
    )-> str:
    
        return self._reduce_to_numeric_ansatz(
            params = params,
            stringify_format = stringify_format,
        )
    
    
    def apply_to(
        self,
        numeric_ansatz_user: Callable[[str], float],
        param_ranges: List[Tuple[float, float]],
        trial_num: int,
        method: Literal["random", "L-BFGS-B", "differential-evolution"] = "L-BFGS-B",
        do_minimize: bool = True,
    )-> Tuple[List[float], float]:

        if method == "random":
            
            return self._apply_to_mode_random(
                numeric_ansatz_user,
                param_ranges,
                trial_num,
                do_minimize,
            )

        else:

            return self._apply_to_mode_optimize(
                numeric_ansatz_user,
                param_ranges,
                trial_num,
                do_minimize,
                method,
            )
            
            
    def mutate(
        self,
    )-> None:
        
        tree = ast.parse(
            source = self._expression,
            mode = "eval",
        )

        class FuncMutator(ast.NodeTransformer):
            def __init__(self, functions, rand_gen):
                self.functions = functions
                self.rand_gen = rand_gen

            def visit_Call(self, node):
                if isinstance(node.func, ast.Name) and node.func.id in self.functions:
                    candidates = [f for f in self.functions if f != node.func.id]
                    if candidates:
                        new_func_name = self.rand_gen.choice(candidates)
                        node.func = ast.copy_location(ast.Name(id = new_func_name, ctx = ast.Load()), node.func)
                self.generic_visit(node)
                return node

        transformer = FuncMutator(
            functions = self._functions,
            rand_gen = self._random_generator,
        )

        mutated_tree = transformer.visit(tree)
        ast.fix_missing_locations(mutated_tree)
        mutated_expression = astor.to_source(mutated_tree).strip()

        self._set_value(
            expression = mutated_expression,
            variables = self._variables,
            functions = self._functions,
            constant_whitelist = self._constant_whitelist,
        )
        
        self._standardize()
            
    # ----------------------------- 重载运算符 ----------------------------- 
    
    def __add__(
        self, 
        other: Ansatz,
    )-> Ansatz:
        
        if not isinstance(other, Ansatz):
            
            raise NotImplementedError(
                translate(
                    "无法将 Ansatz 与 %s 类型的对象相加！"
                ) % (other.__class__.__name__)
            )
            
        if self._variables != other._variables:
            
            raise RuntimeError(
                translate("两个 Ansatz 变量列表相同方可相加！")
            )   

        left_expression = _linear_enhance(self._expression, self._param_num)
        right_expression = _linear_enhance(other._expression, other._param_num)
        
        right_expression = _get_standard_order_expression(
            expression = right_expression,
            start_no = Ansatz(
                expression = left_expression,
                variables = self._variables,
                functions = self._functions,
            ).get_param_num() + 1,
        )

        return Ansatz(
            expression = f"{left_expression} + {right_expression}",
            variables = self._variables,
            functions = list(set(self._functions) | set(other._functions)),
        )
        
        
    def __mul__(
        self, 
        other: Ansatz,
    )-> Ansatz:
        
        if not isinstance(other, Ansatz):
            
            raise NotImplementedError(
                translate(
                    "无法将 Ansatz 与 %s 类型的对象相乘！"
                ) % (other.__class__.__name__)
            )
            
        if self._variables != other._variables:
            
            raise RuntimeError(
                translate("两个 Ansatz 变量列表相同方可相乘！")
            )   

        left_expression = _linear_enhance(self._expression, self._param_num)
        right_expression = _linear_enhance(other._expression, other._param_num)
        
        right_expression = _get_standard_order_expression(
            expression = right_expression,
            start_no = Ansatz(
                expression = left_expression,
                variables = self._variables,
                functions = self._functions,
            ).get_param_num() + 1,
        )

        return Ansatz(
            expression = f"({left_expression}) * ({right_expression})",
            variables = self._variables,
            functions = list(set(self._functions) | set(other._functions)),
        )
        
        
    def __truediv__(
        self, 
        other: Ansatz,
    )-> Ansatz:
        
        if not isinstance(other, Ansatz):
            
            raise NotImplementedError(
                translate(
                    "无法将 Ansatz 与 %s 类型的对象相除！"
                ) % (other.__class__.__name__)
            )
            
        if self._variables != other._variables:
            
            raise RuntimeError(
                translate("两个 Ansatz 变量列表相同方可相除！")
            )   

        left_expression = _linear_enhance(self._expression, self._param_num)
        right_expression = _linear_enhance(other._expression, other._param_num)
        
        right_expression = _get_standard_order_expression(
            expression = right_expression,
            start_no = Ansatz(
                expression = left_expression,
                variables = self._variables,
                functions = self._functions,
            ).get_param_num() + 1,
        )

        return Ansatz(
            expression = f"({left_expression}) / ({right_expression})",
            variables = self._variables,
            functions = list(set(self._functions) | set(other._functions)),
        )

    # ----------------------------- 内部动作 ----------------------------- 
    
    def _set_value(
        self,
        expression: str,
        variables: List[str],
        functions: List[str],
        constant_whitelist: List[str],
    )-> None:
    
        self._expression = expression
        self._variables = variables
        self._functions = functions
        self._constant_whitelist = constant_whitelist

        self._check_format()
    
    
    def _check_format(
        self,
    )-> None:
        
        ansatz_param_num = self._check_ansatz_format(
            expression = self._expression,
            variables = self._variables,
            functions = self._functions,
            constant_whitelist = self._constant_whitelist,
        )
        
        if ansatz_param_num < 0:
            
            raise RuntimeError(
                translate("拟设格式有误：%s") % (self._check_ansatz_format_error_info)
            )
            
        self._param_num = ansatz_param_num
        
        
    def _standardize(
        self,
    )-> None:
        
        standard_expression = _get_standard_order_expression(
            expression = self._expression,
            start_no = 1,
        )
        
        while _is_top_level_bracketed(standard_expression):
            standard_expression = standard_expression[1:-1]
        
        self._set_value(
            expression = standard_expression,
            variables = self._variables,
            functions = self._functions,
            constant_whitelist = self._constant_whitelist,
        )
    
        
    def _to_expression(
        self,
    )-> str:
        
        return self._expression
        
        
    def _reduce_to_numeric_ansatz(
        self,
        params: List[float],
        stringify_format: str = ".8g",
    )-> str:
        
        if len(params) != self._param_num:
            
            raise ValueError(
                translate("提供的参数数量与拟设中所需参数数量不符。")
            )

        param_dict = {
            f"param{i + 1}": float(format(value, stringify_format)) 
            for i, value in enumerate(params)
        }

        tree = ast.parse(
            source = self._expression, 
            mode = "eval",
        )

        class ParamReplacer(ast.NodeTransformer):
            def visit_Name(self, node):
                if node.id in param_dict:
                    return ast.Constant(param_dict[node.id])
                return node

        transformer = ParamReplacer()
        modified_tree = transformer.visit(tree)
        ast.fix_missing_locations(modified_tree)

        return astor.to_source(modified_tree).strip()
    
    
    def _generate_random_params(
        self,
        param_ranges
    )-> List[float]:
        
        return [
            self._random_generator.uniform(param_ranges[i][0], param_ranges[i][1])
            for i in range(self._param_num)
        ]
        
        
    def _apply_to_mode_random(
        self,
        numeric_ansatz_user: Callable[[str], float],
        param_ranges: List[Tuple[float, float]],
        trial_num: int,
        do_minimize: bool,
    )-> Tuple[List[float], float]:
        
        best_params = []
        best_output = float('inf') if do_minimize else float('-inf')
        
        for _ in range(trial_num):
            
            params = self._generate_random_params(param_ranges)
            
            output = numeric_ansatz_user(
                self._reduce_to_numeric_ansatz(params)
            )
            
            if (output < best_output) == do_minimize:
                
                best_output = output
                best_params = params
            
        return best_params, best_output
    
    
    def _apply_to_mode_optimize(
        self,
        numeric_ansatz_user: Callable[[str], float],
        param_ranges: List[Tuple[float, float]],
        trial_num: int,
        do_minimize: bool,
        method: Literal["L-BFGS-B", "differential-evolution"],
    )-> Tuple[List[float], float]:

        def objective(
            params: List[float]
        ) -> float:
            
            expr = self._reduce_to_numeric_ansatz(params)
            value = numeric_ansatz_user(expr)
            return value if do_minimize else -value

        best_params = None
        best_output = float('inf') if do_minimize else float('-inf')

        for _ in range(trial_num):
            
            init_params = self._generate_random_params(param_ranges)

            if method == "L-BFGS-B":

                res = minimize(
                    fun = objective,
                    x0 = init_params,
                    bounds = param_ranges,
                    method = "L-BFGS-B",
                )
                
            elif method == "differential-evolution":
                
                res = differential_evolution(
                    func = objective,
                    bounds = param_ranges,
                    popsize = 15,
                    mutation = 0.8,
                    recombination = 0.7,
                    maxiter = 666,
                    strategy = "best1bin",
                    polish = True,
                    disp = False,
                    seed = 42,
                )
                
            else: raise NotImplementedError

            if not res.success: continue

            score = res.fun if do_minimize else -res.fun

            if (score < best_output) if do_minimize else (score > best_output):
                
                best_output = score; best_params = res.x.tolist()

        if best_params is None:
            
            raise RuntimeError(
                translate("优化器在所有初始点上均未成功收敛。")
            )

        return best_params, best_output


    def _check_ansatz_format(
        self,
        expression: str,
        variables: List[str],
        functions: List[str],
        constant_whitelist: List[str],
    )-> int:
        
        """
        检查输入的表达式是否符合预定义的拟设（ansatz）格式要求。

        本函数会：
        - 校验表达式中使用的运算符、变量、函数是否符合预定义要求；
        - 确保变量名、函数名、参数名称等符号合法，并且符合语法要求；
        - 校验表达式中的参数是否按规定编号且连续，不允许存在常数。

        参数：
            expression (str): 被检查的数学表达式字符串。
            variables (list[str]): 允许使用的变量名列表，表达式中的变量必须严格来自该列表。
            functions (list[str]): 允许使用的函数名列表，函数名必须为裸函数名，不带模块前缀。

        返回值：
            int: 
                - 如果表达式合法，返回最大参数编号（即 'paramN' 的 N 值）。
                - 如果表达式不合法，返回 0。

        注意：
            本函数会首先对 `variables` 和 `functions` 中的内容进行合法性校验，若包含非法名称（如带模块前缀的函数名），
            将设置错误信息并返回0。
        """
        
        identifier_pattern = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
        number_pattern = re.compile(r"^[+-]?("
            r"(0|[1-9][0-9]*)|"
            r"([0-9]*\.[0-9]+|[0-9]+\.?)([eE][+-]?[0-9]+)?|"
            r"0[xX][0-9a-fA-F]+|"
            r"0[oO][0-7]+|"
            r"0[bB][01]+"
            r")$"
        )

        for name in variables + functions:
            if not identifier_pattern.fullmatch(name):
                with self._check_ansatz_format_error_info_lock:
                    self._check_ansatz_format_error_info = \
                        translate(
                            "非法标识符名：'%s'，应仅由字母、数字、下划线组成，"
                            "不能包含点号等其它字符，且应以字母或下划线开头"
                        ) % (name)
                return -1
            
        constant_number_whitelist = []
        constant_identifier_whitelist = []
        for name in constant_whitelist:
            if identifier_pattern.fullmatch(name):
                constant_identifier_whitelist.append(name)
            elif number_pattern.fullmatch(name):
                constant_number_whitelist.append(name)
            else:
                with self._check_ansatz_format_error_info_lock:
                    self._check_ansatz_format_error_info = \
                        translate(
                            "非法常量名：'%s'，常量应为标识符或数字。"
                        ) % (name)
                return -1

        if re.search(r"[^\w\s+\-*/(),.]", expression):
            with self._check_ansatz_format_error_info_lock:
                self._check_ansatz_format_error_info = \
                    translate(
                        "表达式中含有非法字符"
                    )
            return -1

        try:
            tree = ast.parse(
                source = expression, 
                mode = "eval",
            )
        except Exception:
            with self._check_ansatz_format_error_info_lock: 
                self._check_ansatz_format_error_info = \
                    translate(
                        "表达式未成功解析"
                    )
            return -1

        used_names = set()
        used_funcs = set()

        param_indices = set()

        def visit(node):
            
            if isinstance(node, ast.BinOp) or isinstance(node, ast.UnaryOp):
                
                allowed_binops = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)
                allowed_unops = (ast.UAdd, ast.USub)
                
                if isinstance(node, ast.BinOp):
                    if not isinstance(node.op, allowed_binops):
                        raise ValueError(translate("不支持的二元运算符"))
                    
                if isinstance(node, ast.UnaryOp):
                    if not isinstance(node.op, allowed_unops):
                        raise ValueError(translate("不支持的一元运算符"))
                    
                visit(node.operand if isinstance(node, ast.UnaryOp) else node.left)
                
                if isinstance(node, ast.BinOp):
                    visit(node.right)
                    
            elif isinstance(node, ast.Call):
                
                if not isinstance(node.func, ast.Name):
                    raise ValueError(translate("函数调用形式非法"))
                
                func_name = node.func.id
                if func_name not in functions:
                    raise ValueError(translate("调用了未注册的函数 '%s'")%(func_name))
                
                used_funcs.add(func_name)
                
                for arg in node.args:
                    visit(arg)
                    
            elif isinstance(node, ast.Name):
                
                name = node.id
                used_names.add(name)
                
                if name.startswith("param"):
                    match = re.fullmatch(r"param([1-9][0-9]*)", name)
                    
                    if not match:
                        raise ValueError(translate("非法参数名称 '%s'")%(name))
                    param_indices.add(int(match.group(1)))
                    
                elif name not in variables + functions + constant_identifier_whitelist:
                    raise ValueError(translate("使用了非法常量、变量或未注册函数 '%s'")%(name))
                
            elif isinstance(node, ast.Constant):
                node_string = expression[node.col_offset:node.end_col_offset].strip()
                if node_string not in constant_number_whitelist:
                    raise ValueError(translate("表达式中不允许使用任何白名单外常数"))
            
            elif isinstance(node, ast.Expr):
                visit(node.value)
                
            else:
                
                raise ValueError(
                    translate("表达式中包含不支持的语法节点类型：%s")
                    %(type(node).__name__)
                )

        try:
            visit(tree.body)
            
        except Exception as error:
            
            with self._check_ansatz_format_error_info_lock:
                self._check_ansatz_format_error_info = error
                
            return -1

        if param_indices:
            max_index = max(param_indices)
            if sorted(param_indices) != list(range(1, max_index + 1)):
                with self._check_ansatz_format_error_info_lock:
                    self._check_ansatz_format_error_info = translate(
                        "参数编号跳号！"
                    )  
                return -1
            return max_index
        else:
            return 0
    
    
def _get_standard_order_expression(
    expression: str,
    start_no: int,
)-> str:
    
    pattern = re.compile(r'\bparam(\d+)\b')
        
    param_map = {}
    current_no = start_no - 1

    def replace(match):
        
        nonlocal current_no
        
        old_index = int(match.group(1))
        
        if old_index not in param_map:
            current_no += 1
            param_map[old_index] = current_no
            
        return f"param{param_map[old_index]}"
    
    return pattern.sub(replace, expression)


def _linear_enhance(
    expression: str,
    param_num: int,
)-> str:
    
    def is_single_param(node):
        return isinstance(node, ast.Name) and node.id.startswith('param')
    
    def is_param_multiplied(node):

        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            
            left = node.left
            right = node.right

            left_is_param = isinstance(left, ast.Name) and left.id.startswith('param')
            right_is_param = isinstance(right, ast.Name) and right.id.startswith('param')
            
            return left_is_param or right_is_param
        
        return False
    
    def is_param_divided(node):

        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            
            right = node.right
            left = node.left
            
            return (isinstance(right, ast.Name) and right.id.startswith('param')) \
                or (isinstance(left, ast.Name) and left.id.startswith('param'))
        
        return False
    
    def remove_uadd(node):
        
        while isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd):
            node = node.operand
            
        return node
    
    def add_level_flatten(node):
        
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return add_level_flatten(node.left) + add_level_flatten(node.right)
        
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
            neg_right = ast.UnaryOp(op = ast.USub(), operand = node.right)
            return add_level_flatten(node.left) + [neg_right]
        
        else:
            return [node]
    
    tree = ast.parse(
        source = expression, 
        mode = "eval",
    )
    
    add_level_terms = add_level_flatten(tree.body)
    
    new_add_level_terms = []
    additional_param_no = param_num + 1
    
    for node in add_level_terms:
        
        node = remove_uadd(node)
        
        source = astor.to_source(node).strip()

        if _is_top_level_bracketed(source):
            source = source[1:-1]

        if is_single_param(node) or is_param_multiplied(node) or is_param_divided(node):
            new_add_level_terms.append(source)
            
        else:
            
            new_add_level_terms.append(
                f"param{additional_param_no} * {source}"
            )
            
            additional_param_no += 1
        
    linear_enhanced_expression = ""
    
    for index, enhanced_term in enumerate(new_add_level_terms):
        
        if index: linear_enhanced_expression += " + "
        
        linear_enhanced_expression += enhanced_term

    return linear_enhanced_expression


def _is_top_level_bracketed(
    legal_expression: str,
)-> bool:
    
    if not legal_expression: return False
    
    if legal_expression[0] != "(": return False
    
    stack = 0
    
    for char in legal_expression[:-1]:
        
        if char == "(": stack += 1
        if char == ")": stack -= 1
        
        if not stack: return False
        
    return True


