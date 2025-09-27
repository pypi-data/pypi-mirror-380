import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
import os
import glob
import hashlib
import subprocess
import shutil
from pathlib import Path
from typing import Union, Tuple, List, Optional
import tempfile


class Device:
    """Device class - Distinguishes between CPU and GPU"""

    def __init__(self, device_type: str, device_id: int = 0):
        if device_type not in ["cpu", "gpu"]:
            raise ValueError("Device type must be 'cpu' or 'gpu'")
        self.type = device_type
        self.id = device_id

    def __str__(self):
        return f"{self.type}:{self.id}" if self.type == "gpu" else "cpu"

    def __repr__(self):
        return self.__str__()


def device(device_type: str, device_id: int = 0) -> Device:
    """Device creation function"""
    return Device(device_type, device_id)


class KernelCache:
    """Kernel cache management for compiled PTX files"""

    def __init__(self, cache_dir: Optional[str] = None):
        if cache_dir is None:
            # Use user's home directory for cache
            home_dir = Path.home()
            self.cache_dir = home_dir / ".oven" / "kernels"
        else:
            self.cache_dir = Path(cache_dir)

        # Create cache directory if it doesn't exist
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_file_hash(self, file_path: str) -> str:
        """Calculate hash of Python kernel file"""
        with open(file_path, "rb") as f:
            content = f.read()
        return hashlib.sha256(content).hexdigest()[:16]

    def _get_cache_path(self, kernel_name: str, file_hash: str) -> Path:
        """Get path for cached PTX file"""
        return self.cache_dir / f"{kernel_name}_{file_hash}.ptx"

    def is_cached(self, kernel_path: str) -> bool:
        """Check if kernel is already compiled and cached"""
        kernel_name = Path(kernel_path).stem
        file_hash = self._get_file_hash(kernel_path)
        cache_path = self._get_cache_path(kernel_name, file_hash)
        return cache_path.exists()

    def get_cached_ptx(self, kernel_path: str) -> Optional[str]:
        """Get cached PTX file path if exists"""
        kernel_name = Path(kernel_path).stem
        file_hash = self._get_file_hash(kernel_path)
        cache_path = self._get_cache_path(kernel_name, file_hash)

        if cache_path.exists():
            return str(cache_path)
        return None

    def compile_and_cache(self, kernel_path: str) -> str:
        """Compile Python kernel to PTX and cache it"""
        kernel_name = Path(kernel_path).stem
        file_hash = self._get_file_hash(kernel_path)
        cache_path = self._get_cache_path(kernel_name, file_hash)

        # If already cached, return cached path
        if cache_path.exists():
            return str(cache_path)

        try:
            # Compile using oven-compiler
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_ptx = Path(temp_dir) / f"{kernel_name}.ptx"

                # Run oven-compiler
                cmd = ["oven-compiler", "--python", kernel_path, "-o", str(temp_ptx)]

                result = subprocess.run(cmd, capture_output=True, text=True, check=True)

                if temp_ptx.exists():
                    # Copy to cache
                    shutil.copy2(temp_ptx, cache_path)
                    print(f"Compiled and cached kernel: {kernel_name}")
                    return str(cache_path)
                else:
                    raise RuntimeError(f"PTX file not generated: {temp_ptx}")

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to compile kernel {kernel_path}: {e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("oven-compiler not found. Please install oven-compiler.")

    def clear_cache(self):
        """Clear all cached PTX files"""
        for ptx_file in self.cache_dir.glob("*.ptx"):
            ptx_file.unlink()
        print(f"Cleared kernel cache: {self.cache_dir}")


class KernelManager:
    """PTX kernel management class with automatic compilation and caching"""

    def __init__(
        self, kernels_path: Optional[str] = None, cache_dir: Optional[str] = None
    ):
        if kernels_path is None:
            # Use package's built-in kernels
            package_dir = Path(__file__).parent
            self.kernels_path = package_dir / "kernels"
        else:
            self.kernels_path = Path(kernels_path)

        self.cache = KernelCache(cache_dir)
        self.modules = {}
        self.functions = {}
        self._load_kernels()

    def _load_kernels(self):
        """Load all Python kernels, compile to PTX and cache"""
        # Look for Python kernel files
        python_kernels = list(self.kernels_path.glob("*.py"))

        if not python_kernels:
            print(f"Warning: No Python kernel files found in {self.kernels_path}")
            return

        for py_file in python_kernels:
            if py_file.name.startswith("__"):  # Skip __init__.py etc
                continue

            module_name = py_file.stem
            try:
                # Check if cached, otherwise compile
                ptx_file = self.cache.get_cached_ptx(str(py_file))
                if ptx_file is None:
                    print(f"Compiling kernel: {py_file.name}")
                    ptx_file = self.cache.compile_and_cache(str(py_file))
                else:
                    print(f"Using cached kernel: {module_name}")

                # Load PTX module
                with open(ptx_file, "r") as f:
                    ptx_code = f.read()

                module = cuda.module_from_buffer(ptx_code.encode("utf-8"))
                self.modules[module_name] = module

                # Extract available functions from each module
                self._extract_functions(module_name, module)

            except Exception as e:
                print(f"Warning: Failed to load kernel {py_file}: {e}")

    def _extract_functions(self, module_name: str, module):
        """Extract functions from module"""
        # Try common function names to find existing functions
        common_functions = [
            # unary operations
            "sigmoid",
            "exp",
            "sqrt",
            "abs",
            "ceil",
            "floor",
            "rsqrt",
            "sin",
            "cos",
            "tan",
            "log",
            "log10",
            "tanh",
            # binary operations
            "add",
            "mul",
            "sub",
            "div",
            "pow",
            "mod",
            "vadd",
            "vsub",
            "vmul",
            "vdiv",
            # matrix operations
            "matmul",
        ]

        for func_name in common_functions:
            try:
                func = module.get_function(func_name)
                self.functions[func_name] = (module_name, func)
            except cuda.LogicError:
                # Ignore if function doesn't exist
                pass

    def get_function(self, func_name: str):
        """Return CUDA function object by function name"""
        if func_name not in self.functions:
            return None
        return self.functions[func_name][1]

    def has_function(self, func_name: str) -> bool:
        """Check if function exists"""
        return func_name in self.functions

    def reload_kernels(self):
        """Reload all kernels (useful for development)"""
        self.modules.clear()
        self.functions.clear()
        self._load_kernels()

    def clear_cache(self):
        """Clear kernel cache"""
        self.cache.clear_cache()

    def execute_kernel(
        self, kernel_name: str, *tensors, grid=None, block=None, **kwargs
    ):
        """
        Execute a custom kernel with tensor arguments

        Args:
            kernel_name (str): Name of the kernel function
            *tensors: Tensor objects to pass as arguments
            grid: CUDA grid dimensions (tuple)
            block: CUDA block dimensions (tuple)
            **kwargs: Additional kernel parameters (scalars)

        Returns:
            None (modifies tensors in-place or creates new results)
        """
        if kernel_name not in self.functions:
            raise RuntimeError(
                f"Kernel '{kernel_name}' not found. Available: {list(self.functions.keys())}"
            )

        # Get kernel function
        func = self.functions[kernel_name][1]

        # Extract GPU pointers from tensors
        gpu_args = []
        for tensor in tensors:
            if tensor.device.type != "gpu":
                raise RuntimeError(f"All tensors must be on GPU for kernel execution")
            gpu_args.append(tensor._gpu_ptr)

        # Add scalar arguments
        for key, value in kwargs.items():
            if isinstance(value, int):
                gpu_args.append(np.int32(value))
            elif isinstance(value, float):
                gpu_args.append(np.float32(value))
            else:
                gpu_args.append(value)

        # Set default grid/block if not provided
        if grid is None or block is None:
            # Use first tensor to determine size
            if tensors:
                first_tensor = tensors[0]
                if block is None:
                    block = (128, 1, 1)
                if grid is None:
                    grid_size = (first_tensor.size + block[0] - 1) // block[0]
                    grid = (grid_size, 1, 1)
            else:
                if block is None:
                    block = (128, 1, 1)
                if grid is None:
                    grid = (1, 1, 1)

        # Execute kernel
        func(*gpu_args, block=block, grid=grid)

    def register_kernel_from_file(
        self, kernel_file_path: str, function_names: List[str] = None
    ):
        """
        Register a new kernel from a Python file

        Args:
            kernel_file_path (str): Path to the Python kernel file
            function_names (List[str], optional): List of function names to register.
                                                If None, tries to extract all functions.

        Returns:
            List[str]: Names of successfully registered functions
        """
        kernel_file_path = Path(kernel_file_path)
        if not kernel_file_path.exists():
            raise FileNotFoundError(f"Kernel file not found: {kernel_file_path}")

        try:
            # Compile the kernel file
            ptx_file = self.cache.compile_and_cache(str(kernel_file_path))

            # Load PTX module
            with open(ptx_file, "r") as f:
                ptx_code = f.read()

            module = cuda.module_from_buffer(ptx_code.encode("utf-8"))
            module_name = kernel_file_path.stem
            self.modules[module_name] = module

            # Register functions
            registered_functions = []
            if function_names is None:
                # Try to extract functions automatically
                function_names = self._extract_function_names_from_file(
                    str(kernel_file_path)
                )

            for func_name in function_names:
                try:
                    func = module.get_function(func_name)
                    self.functions[func_name] = (module_name, func)
                    registered_functions.append(func_name)
                    print(f"Registered function: {func_name}")
                except cuda.LogicError:
                    print(
                        f"Warning: Function '{func_name}' not found in compiled module"
                    )

            return registered_functions

        except Exception as e:
            raise RuntimeError(
                f"Failed to register kernel from {kernel_file_path}: {e}"
            )

    def register_kernel_from_code(
        self, kernel_code: str, module_name: str, function_names: List[str]
    ):
        """
        Register a new kernel from Python code string

        Args:
            kernel_code (str): Python kernel code as string
            module_name (str): Name for the module
            function_names (List[str]): List of function names to register

        Returns:
            List[str]: Names of successfully registered functions
        """
        # Create temporary file with the kernel code
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False
        ) as tmp_file:
            tmp_file.write(kernel_code)
            tmp_file_path = tmp_file.name

        try:
            # Compile the temporary file
            ptx_file = self.cache.compile_and_cache(tmp_file_path)

            # Load PTX module
            with open(ptx_file, "r") as f:
                ptx_code = f.read()

            module = cuda.module_from_buffer(ptx_code.encode("utf-8"))
            self.modules[module_name] = module

            # Register functions
            registered_functions = []
            for func_name in function_names:
                try:
                    func = module.get_function(func_name)
                    self.functions[func_name] = (module_name, func)
                    registered_functions.append(func_name)
                    print(f"Registered function: {func_name}")
                except cuda.LogicError:
                    print(
                        f"Warning: Function '{func_name}' not found in compiled module"
                    )

            return registered_functions

        except Exception as e:
            raise RuntimeError(f"Failed to register kernel from code: {e}")
        finally:
            # Clean up temporary file
            try:
                os.unlink(tmp_file_path)
            except:
                pass

    def _extract_function_names_from_file(self, file_path: str) -> List[str]:
        """
        Extract function names from a Python file

        Args:
            file_path (str): Path to Python file

        Returns:
            List[str]: List of function names found in the file
        """
        function_names = []
        try:
            with open(file_path, "r") as f:
                content = f.read()

            # Simple regex to find function definitions
            import re

            matches = re.findall(r"^def\s+(\w+)\s*\(", content, re.MULTILINE)
            function_names = [match for match in matches if not match.startswith("_")]

        except Exception as e:
            print(f"Warning: Could not extract function names from {file_path}: {e}")

        return function_names

    def unregister_kernel(self, function_name: str):
        """
        Unregister a kernel function

        Args:
            function_name (str): Name of the function to unregister
        """
        if function_name in self.functions:
            del self.functions[function_name]
            print(f"Unregistered function: {function_name}")
        else:
            print(f"Warning: Function '{function_name}' was not registered")


# Global kernel manager instance
_kernel_manager = None


def get_kernel_manager():
    """Get global kernel manager instance"""
    global _kernel_manager
    if _kernel_manager is None:
        _kernel_manager = KernelManager()
    return _kernel_manager


class Tensor:
    """PyTorch-style Tensor class"""

    def __init__(
        self,
        data: Union[np.ndarray, List, float, int],
        device: Device = device("cpu"),
        dtype=np.float32,
    ):
        self.device = device
        self.dtype = dtype

        # Convert data to numpy array
        if isinstance(data, (int, float)):
            self._data = np.array([data], dtype=dtype)
        elif isinstance(data, list):
            self._data = np.array(data, dtype=dtype)
        elif isinstance(data, np.ndarray):
            self._data = data.astype(dtype)
        else:
            raise ValueError(f"Unsupported data type: {type(data)}")

        self.shape = self._data.shape
        self.size = self._data.size
        self.nbytes = self._data.nbytes

        # GPU memory pointer (used only for GPU device)
        self._gpu_ptr = None

        if self.device.type == "gpu":
            self._allocate_gpu_memory()
            self._copy_to_gpu()

    def _allocate_gpu_memory(self):
        """Allocate GPU memory"""
        if self._gpu_ptr is not None:
            cuda.mem_free(self._gpu_ptr)
        self._gpu_ptr = cuda.mem_alloc(self.nbytes)

    def _copy_to_gpu(self):
        """Copy data from CPU to GPU"""
        if self._gpu_ptr is not None:
            cuda.memcpy_htod(self._gpu_ptr, self._data)

    def _copy_to_cpu(self):
        """Copy data from GPU to CPU"""
        if self._gpu_ptr is not None:
            cuda.memcpy_dtoh(self._data, self._gpu_ptr)

    def to(self, device: Device) -> "Tensor":
        """Move to device"""
        if device.type == self.device.type:
            return self

        new_tensor = Tensor(self.cpu().numpy(), device, self.dtype)
        return new_tensor

    def cpu(self) -> "Tensor":
        """Move to CPU"""
        if self.device.type == "cpu":
            return self

        # Copy data from GPU to CPU
        self._copy_to_cpu()
        return Tensor(self._data.copy(), device("cpu"), self.dtype)

    def gpu(self, device_id: int = 0) -> "Tensor":
        """Move to GPU"""
        return self.to(device("gpu", device_id))

    def numpy(self) -> np.ndarray:
        """Convert to numpy array (only available on CPU)"""
        if self.device.type == "gpu":
            self._copy_to_cpu()
        return self._data.copy()

    def _get_launch_config(self):
        """Grid/block configuration for CUDA kernel execution"""
        block_size = 128
        grid_size = (self.size + block_size - 1) // block_size
        return (grid_size, 1, 1), (block_size, 1, 1)

    def _execute_unary_op(self, op_name: str) -> "Tensor":
        """Execute unary operation"""
        if self.device.type == "cpu":
            # NumPy operations on CPU
            if op_name == "sigmoid":
                result_data = 1.0 / (1.0 + np.exp(-self._data))
            elif op_name == "exp":
                result_data = np.exp(self._data)
            elif op_name == "sqrt":
                result_data = np.sqrt(self._data)
            elif op_name == "abs":
                result_data = np.abs(self._data)
            elif op_name == "ceil":
                result_data = np.ceil(self._data)
            elif op_name == "floor":
                result_data = np.floor(self._data)
            elif op_name == "rsqrt":
                result_data = 1.0 / np.sqrt(self._data)
            elif op_name == "sin":
                result_data = np.sin(self._data)
            elif op_name == "cos":
                result_data = np.cos(self._data)
            elif op_name == "tan":
                result_data = np.tan(self._data)
            elif op_name == "log":
                result_data = np.log(self._data)
            elif op_name == "log10":
                result_data = np.log10(self._data)
            elif op_name == "tanh":
                result_data = np.tanh(self._data)
            else:
                raise NotImplementedError(f"CPU operation '{op_name}' not implemented")

            return Tensor(result_data, self.device, self.dtype)

        else:  # GPU
            kernel_manager = get_kernel_manager()
            func = kernel_manager.get_function(op_name)
            if func is None:
                raise RuntimeError(
                    f"GPU kernel '{op_name}' not found. Available functions: {list(kernel_manager.functions.keys())}"
                )

            # Create result tensor
            result = Tensor(np.zeros_like(self._data), self.device, self.dtype)

            # Execute kernel
            grid, block = self._get_launch_config()
            func(self._gpu_ptr, result._gpu_ptr, block=block, grid=grid)

            return result

    def _execute_binary_op(self, other: "Tensor", op_name: str) -> "Tensor":
        """Execute binary operation"""
        # Check device match
        if self.device.type != other.device.type:
            raise RuntimeError(
                "Tensors must be on the same device for binary operations"
            )

        # Check shape match (broadcasting not supported)
        if self.shape != other.shape:
            raise RuntimeError(f"Shape mismatch: {self.shape} vs {other.shape}")

        if self.device.type == "cpu":
            # NumPy operations on CPU
            if op_name == "add":
                result_data = self._data + other._data
            elif op_name == "mul":
                result_data = self._data * other._data
            elif op_name == "sub":
                result_data = self._data - other._data
            elif op_name == "div":
                result_data = self._data / other._data
            elif op_name == "pow":
                result_data = np.power(self._data, other._data)
            elif op_name == "mod":
                result_data = np.mod(self._data, other._data)
            else:
                raise NotImplementedError(f"CPU operation '{op_name}' not implemented")

            return Tensor(result_data, self.device, self.dtype)

        else:  # GPU
            kernel_manager = get_kernel_manager()
            func = kernel_manager.get_function(op_name)
            if func is None:
                raise RuntimeError(
                    f"GPU kernel '{op_name}' not found. Available functions: {list(kernel_manager.functions.keys())}"
                )

            # Create result tensor
            result = Tensor(np.zeros_like(self._data), self.device, self.dtype)

            # Execute kernel
            grid, block = self._get_launch_config()
            func(self._gpu_ptr, other._gpu_ptr, result._gpu_ptr, block=block, grid=grid)

            return result

    def _execute_matmul_op(self, other: "Tensor") -> "Tensor":
        """Execute matrix multiplication operation"""
        # Check device match
        if self.device.type != other.device.type:
            raise RuntimeError(
                "Tensors must be on the same device for matmul operations"
            )

        # Check 2D matrices
        if len(self.shape) != 2 or len(other.shape) != 2:
            raise RuntimeError("matmul requires 2D tensors (matrices)")

        m, k1 = self.shape
        k2, n = other.shape

        if k1 != k2:
            raise RuntimeError(
                f"Matrix dimensions incompatible: {self.shape} @ {other.shape}"
            )

        if self.device.type == "cpu":
            # NumPy matrix multiplication on CPU
            result_data = np.dot(self._data, other._data)
            return Tensor(result_data, self.device, self.dtype)

        else:  # GPU
            kernel_manager = get_kernel_manager()
            func = kernel_manager.get_function("matmul")
            if func is None:
                raise RuntimeError(
                    f"GPU kernel 'matmul' not found. Available functions: {list(kernel_manager.functions.keys())}"
                )

            # Create result tensor
            result_shape = (m, n)
            result = Tensor(
                np.zeros(result_shape, dtype=self.dtype), self.device, self.dtype
            )

            # Configure 2D grid for matrix multiplication
            block_size = 16  # 16x16 thread blocks
            grid_x = (n + block_size - 1) // block_size
            grid_y = (m + block_size - 1) // block_size

            grid = (grid_x, grid_y, 1)
            block = (block_size, block_size, 1)

            # Execute kernel with m, n, k parameters
            func(
                self._gpu_ptr,
                other._gpu_ptr,
                result._gpu_ptr,
                np.int32(m),
                np.int32(n),
                np.int32(k1),
                block=block,
                grid=grid,
            )

            return result

    # Unary operation methods
    def sigmoid(self) -> "Tensor":
        return self._execute_unary_op("sigmoid")

    def exp(self) -> "Tensor":
        return self._execute_unary_op("exp")

    def sqrt(self) -> "Tensor":
        return self._execute_unary_op("sqrt")

    def abs(self) -> "Tensor":
        return self._execute_unary_op("abs")

    def ceil(self) -> "Tensor":
        return self._execute_unary_op("ceil")

    def floor(self) -> "Tensor":
        return self._execute_unary_op("floor")

    def rsqrt(self) -> "Tensor":
        return self._execute_unary_op("rsqrt")

    def sin(self) -> "Tensor":
        return self._execute_unary_op("sin")

    def cos(self) -> "Tensor":
        return self._execute_unary_op("cos")

    def tan(self) -> "Tensor":
        return self._execute_unary_op("tan")

    def log(self) -> "Tensor":
        return self._execute_unary_op("log")

    def log10(self) -> "Tensor":
        return self._execute_unary_op("log10")

    def tanh(self) -> "Tensor":
        return self._execute_unary_op("tanh")

    # Binary operation methods
    def add(self, other: "Tensor") -> "Tensor":
        return self._execute_binary_op(other, "add")

    def mul(self, other: "Tensor") -> "Tensor":
        return self._execute_binary_op(other, "mul")

    def sub(self, other: "Tensor") -> "Tensor":
        return self._execute_binary_op(other, "sub")

    def div(self, other: "Tensor") -> "Tensor":
        return self._execute_binary_op(other, "div")

    def pow(self, other: "Tensor") -> "Tensor":
        return self._execute_binary_op(other, "pow")

    def mod(self, other: "Tensor") -> "Tensor":
        return self._execute_binary_op(other, "mod")

    # Matrix operation methods
    def matmul(self, other: "Tensor") -> "Tensor":
        """Matrix multiplication: self @ other"""
        return self._execute_matmul_op(other)

    # Custom kernel execution
    @staticmethod
    def execute_kernel(kernel_name: str, *tensors, grid=None, block=None, **kwargs):
        """
        Execute a custom kernel with tensor arguments

        Args:
            kernel_name (str): Name of the kernel function
            *tensors: Tensor objects to pass as arguments
            grid: CUDA grid dimensions (tuple)
            block: CUDA block dimensions (tuple)
            **kwargs: Additional kernel parameters (scalars)

        Example:
            # Execute custom kernel
            a = ot.tensor([1, 2, 3, 4]).gpu()
            b = ot.tensor([0, 0, 0, 0]).gpu()
            ot.Tensor.execute_kernel("my_kernel", a, b, block=(128, 1, 1))
        """
        kernel_manager = get_kernel_manager()
        return kernel_manager.execute_kernel(
            kernel_name, *tensors, grid=grid, block=block, **kwargs
        )

    # Python operator overloading
    def __add__(self, other: "Tensor") -> "Tensor":
        return self.add(other)

    def __mul__(self, other: "Tensor") -> "Tensor":
        return self.mul(other)

    def __sub__(self, other: "Tensor") -> "Tensor":
        return self.sub(other)

    def __truediv__(self, other: "Tensor") -> "Tensor":
        return self.div(other)

    def __pow__(self, other: "Tensor") -> "Tensor":
        return self.pow(other)

    def __mod__(self, other: "Tensor") -> "Tensor":
        return self.mod(other)

    def __matmul__(self, other: "Tensor") -> "Tensor":
        return self.matmul(other)

    def __str__(self) -> str:
        if self.device.type == "gpu":
            self._copy_to_cpu()
        return f"Tensor({self._data}, device={self.device})"

    def __repr__(self) -> str:
        return self.__str__()

    def __del__(self):
        """Destructor - Free GPU memory"""
        if hasattr(self, "_gpu_ptr") and self._gpu_ptr is not None:
            try:
                cuda.mem_free(self._gpu_ptr)
            except:
                pass


# Convenience functions
def tensor(data, device=device("cpu"), dtype=np.float32) -> Tensor:
    """Tensor creation function"""
    return Tensor(data, device, dtype)


def zeros(shape: Tuple, device=device("cpu"), dtype=np.float32) -> Tensor:
    """Create zero matrix"""
    data = np.zeros(shape, dtype=dtype)
    return Tensor(data, device, dtype)


def ones(shape: Tuple, device=device("cpu"), dtype=np.float32) -> Tensor:
    """Create ones matrix"""
    data = np.ones(shape, dtype=dtype)
    return Tensor(data, device, dtype)


def randn(shape: Tuple, device=device("cpu"), dtype=np.float32) -> Tensor:
    """Create random tensor with normal distribution"""
    data = np.random.randn(*shape).astype(dtype)
    return Tensor(data, device, dtype)


def linspace(
    start: float, stop: float, num: int = 50, device=device("cpu"), dtype=np.float32
) -> Tensor:
    """
    Create a tensor with evenly spaced values over a specified interval

    Args:
        start (float): The starting value of the sequence
        stop (float): The end value of the sequence
        num (int): Number of samples to generate. Default is 50.
        device: Device to place the tensor on ('cpu' or 'gpu')
        dtype: Data type of the tensor elements

    Returns:
        Tensor: 1-D tensor of evenly spaced values

    Example:
        >>> ot.linspace(0, 10, 5)
        Tensor([0.0, 2.5, 5.0, 7.5, 10.0], device=cpu)
    """
    data = np.linspace(start, stop, num, dtype=dtype)
    return Tensor(data, device, dtype)


def matmul(a: Tensor, b: Tensor) -> Tensor:
    """Matrix multiplication: a @ b"""
    return a.matmul(b)


# Package management functions
def clear_kernel_cache():
    """Clear all cached kernels"""
    kernel_manager = get_kernel_manager()
    kernel_manager.clear_cache()


def reload_kernels():
    """Reload all kernels (useful for development)"""
    kernel_manager = get_kernel_manager()
    kernel_manager.reload_kernels()


def list_available_functions():
    """List all available GPU functions"""
    kernel_manager = get_kernel_manager()
    return list(kernel_manager.functions.keys())


def execute_kernel(kernel_name: str, *tensors, grid=None, block=None, **kwargs):
    """
    Execute a custom kernel with tensor arguments

    Args:
        kernel_name (str): Name of the kernel function
        *tensors: Tensor objects to pass as arguments
        grid: CUDA grid dimensions (tuple)
        block: CUDA block dimensions (tuple)
        **kwargs: Additional kernel parameters (scalars)

    Example:
        import oven_tensor as ot

        # Create tensors on GPU
        a = ot.tensor([1, 2, 3, 4]).gpu()
        result = ot.zeros((4,)).gpu()

        # Execute custom kernel
        ot.execute_kernel("my_custom_kernel", a, result,
                         grid=(1, 1, 1), block=(128, 1, 1))
    """
    kernel_manager = get_kernel_manager()
    return kernel_manager.execute_kernel(
        kernel_name, *tensors, grid=grid, block=block, **kwargs
    )


def register_kernel_from_file(kernel_file_path: str, function_names: List[str] = None):
    """
    Register a new kernel from a Python file

    Args:
        kernel_file_path (str): Path to the Python kernel file
        function_names (List[str], optional): List of function names to register.
                                            If None, tries to extract all functions.

    Returns:
        List[str]: Names of successfully registered functions

    Example:
        import oven_tensor as ot

        # Register all functions from a file
        functions = ot.register_kernel_from_file("my_kernels.py")

        # Register specific functions only
        functions = ot.register_kernel_from_file("my_kernels.py", ["my_kernel1", "my_kernel2"])
    """
    kernel_manager = get_kernel_manager()
    return kernel_manager.register_kernel_from_file(kernel_file_path, function_names)


def register_kernel_from_code(
    kernel_code: str, module_name: str, function_names: List[str]
):
    """
        Register a new kernel from Python code string

        Args:
            kernel_code (str): Python kernel code as string
            module_name (str): Name for the module
            function_names (List[str]): List of function names to register

        Returns:
            List[str]: Names of successfully registered functions

        Example:
            import oven_tensor as ot

            kernel_code = '''
    import oven.language as ol

    def my_custom_kernel(x_ptr: ol.ptr, y_ptr: ol.ptr, scale: float):
        idx = ol.get_global_id()
        x_val = ol.load(x_ptr, idx)
        y_val = x_val * scale
        ol.store(y_val, y_ptr, idx)
    '''

            functions = ot.register_kernel_from_code(kernel_code, "my_module", ["my_custom_kernel"])
    """
    kernel_manager = get_kernel_manager()
    return kernel_manager.register_kernel_from_code(
        kernel_code, module_name, function_names
    )


def unregister_kernel(function_name: str):
    """
    Unregister a kernel function

    Args:
        function_name (str): Name of the function to unregister

    Example:
        import oven_tensor as ot

        ot.unregister_kernel("my_custom_kernel")
    """
    kernel_manager = get_kernel_manager()
    return kernel_manager.unregister_kernel(function_name)
