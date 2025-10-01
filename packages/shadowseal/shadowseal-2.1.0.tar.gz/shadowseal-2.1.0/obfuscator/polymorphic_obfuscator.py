"""
Advanced Polymorphic Obfuscation for ShadowSeal

This module provides polymorphic code transformation that changes the code's
appearance while maintaining its functionality. Each encryption produces
different output even for the same input.
"""

import ast
import random
import string
import hashlib
import secrets


class PolymorphicTransformer(ast.NodeTransformer):
    """
    Transforms Python code into semantically equivalent but structurally different code
    """
    
    def __init__(self, seed=None):
        self.seed = seed or secrets.token_hex(16)
        self.name_mapping = {}
        self.counter = 0
        random.seed(self.seed)
    
    def generate_random_name(self, prefix='_'):
        """Generate obfuscated variable names"""
        self.counter += 1
        # Mix of letters and underscores to make it look legitimate but confusing
        chars = ''.join(random.choices(string.ascii_letters + '_', k=random.randint(12, 24)))
        return f"{prefix}{chars}_{self.counter}"
    
    def visit_FunctionDef(self, node):
        """Transform function definitions"""
        # Skip magic methods
        if node.name.startswith('__') and node.name.endswith('__'):
            return self.generic_visit(node)
        
        # Generate new name
        if node.name not in self.name_mapping:
            self.name_mapping[node.name] = self.generate_random_name('func')
        node.name = self.name_mapping[node.name]
        
        # Transform arguments
        for arg in node.args.args:
            if arg.arg != 'self':
                old_name = arg.arg
                if old_name not in self.name_mapping:
                    self.name_mapping[old_name] = self.generate_random_name('arg')
                arg.arg = self.name_mapping[old_name]
        
        return self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        """Transform class definitions"""
        if node.name not in self.name_mapping:
            self.name_mapping[node.name] = self.generate_random_name('cls')
        node.name = self.name_mapping[node.name]
        return self.generic_visit(node)
    
    def visit_Name(self, node):
        """Transform variable names"""
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            if node.id not in self.name_mapping:
                self.name_mapping[node.id] = self.generate_random_name('var')
            node.id = self.name_mapping[node.id]
        elif isinstance(node.ctx, ast.Load):
            if node.id in self.name_mapping:
                node.id = self.name_mapping[node.id]
        return node


class DeadCodeInjector:
    """Injects dead code to confuse static analysis"""
    
    @staticmethod
    def generate_dead_code_block():
        """Generate random dead code that never executes"""
        dead_code_templates = [
            """
if False:
    _temp_var_{0} = {1}
    _temp_result_{0} = _temp_var_{0} * {2} + {3}
    _temp_list_{0} = [i for i in range({4}) if i % {5} == 0]
""",
            """
if 1 > 2:
    def _unused_func_{0}(x, y):
        return x ** y + {1}
    _result_{0} = _unused_func_{0}({2}, {3})
""",
            """
if None:
    class _UnusedClass_{0}:
        def __init__(self):
            self.value = {1}
        def method(self):
            return self.value * {2}
""",
        ]
        
        template = random.choice(dead_code_templates)
        rand_values = [random.randint(1, 1000) for _ in range(10)]
        return template.format(*rand_values)
    
    @staticmethod
    def inject_dead_code(source_code: str) -> str:
        """Inject dead code blocks into source"""
        tree = ast.parse(source_code)
        
        # Add dead code blocks at random positions
        num_blocks = random.randint(2, 5)
        for _ in range(num_blocks):
            dead_code = DeadCodeInjector.generate_dead_code_block()
            dead_tree = ast.parse(dead_code)
            
            if len(tree.body) > 0:
                insert_pos = random.randint(0, len(tree.body))
                tree.body[insert_pos:insert_pos] = dead_tree.body
        
        ast.fix_missing_locations(tree)
        return ast.unparse(tree)


class StringPolymorphism:
    """Polymorphic string encoding"""
    
    @staticmethod
    def encode_string(s: str) -> str:
        """Encode string using random method"""
        methods = [
            StringPolymorphism._base64_encode,
            StringPolymorphism._hex_encode,
            StringPolymorphism._xor_encode,
        ]
        method = random.choice(methods)
        return method(s)
    
    @staticmethod
    def _base64_encode(s: str) -> str:
        """Base64 encoding"""
        import base64
        encoded = base64.b64encode(s.encode()).decode()
        return f"__import__('base64').b64decode({repr(encoded)}).decode()"
    
    @staticmethod
    def _hex_encode(s: str) -> str:
        """Hex encoding"""
        hex_str = s.encode().hex()
        return f"bytes.fromhex({repr(hex_str)}).decode()"
    
    @staticmethod
    def _xor_encode(s: str) -> str:
        """XOR encoding"""
        key = random.randint(1, 255)
        encoded = bytes(c ^ key for c in s.encode())
        return f"bytes(c ^ {key} for c in {repr(encoded)}).decode()"


def apply_polymorphic_obfuscation(source_code: str) -> str:
    """
    Apply comprehensive polymorphic obfuscation
    
    This makes each encryption unique even for the same source code
    """
    # Parse the source
    tree = ast.parse(source_code)
    
    # Apply polymorphic transformation
    transformer = PolymorphicTransformer()
    tree = transformer.visit(tree)
    
    # Fix locations
    ast.fix_missing_locations(tree)
    
    # Convert back to source
    transformed = ast.unparse(tree)
    
    # Inject dead code
    obfuscated = DeadCodeInjector.inject_dead_code(transformed)
    
    return obfuscated


def create_code_virtualization_layer(source_code: str) -> str:
    """
    Create a virtualization layer that interprets bytecode
    
    This adds another layer of indirection, making static analysis harder
    """
    # Compile to bytecode
    import marshal
    import base64
    
    code_obj = compile(source_code, '<encrypted>', 'exec')
    bytecode = marshal.dumps(code_obj)
    encoded = base64.b64encode(bytecode).decode()
    
    # Create virtualization wrapper
    wrapper = f"""
import marshal
import base64
_bc = base64.b64decode({repr(encoded)})
_co = marshal.loads(_bc)
exec(_co)
"""
    
    return wrapper


if __name__ == "__main__":
    # Test the obfuscator
    sample_code = """
def hello(name):
    message = "Hello, " + name
    return message

result = hello("World")
print(result)
"""
    
    print("Original:")
    print(sample_code)
    print("\n" + "="*50 + "\n")
    
    print("Obfuscated:")
    obfuscated = apply_polymorphic_obfuscation(sample_code)
    print(obfuscated)

