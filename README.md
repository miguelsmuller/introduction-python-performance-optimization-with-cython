# Introduction to Performance Optimization in Python with Cython

This is a demonstration project that illustrates how Cython can be used to optimize the performance of Python code. In this project, two code versions that perform intensive mathematical calculations are presented and compared in terms of execution time.

## Version 1

The file `version_1.py` contains the first version of the code. In this version, optimization was not applied, and the code uses standard Python functions to perform the calculation.

- [version_1.py](./src/version_1.py)
- [module_1.py](./src/module_1.py): Used in version 1, it contains the non-optimized code.

## Version 2

The file `version_2.py` contains the second version of the code. In this version, Cython was used to optimize the code's performance. The code was rewritten in Cython, and variable typing was added to improve performance.

- [version_2.py](./src/version_2.py)
- [module_2.pyx](./src/module_2.pyx): Used in version 2, it contains the code optimized in Cython.

## How to Run

To execute each version of the code, simply run the respective `version_1.py` or `version_2.py` files. The execution time will be displayed in the console.

To compile the Cython module (`module_2.pyx`), you can use the following command:

`python src/setup.py build_ext --inplace --build-lib ./src/`

After compiling the module, you can use the optimized version in `version_2.py`.

## Results

The optimized version of the code (version 2) demonstrates significantly better performance compared to the non-optimized version (version 1). The same calculation that took 20 seconds in version 1 now takes less than 1 second in version 2.

## Conclusion

This project highlights the power of Cython for optimizing the performance of Python code, especially in cases where intensive processing is required. If you're facing performance challenges in your Python projects, consider Cython as a valuable tool to accelerate your critical operations.

Feel free to explore the source code and experiment with different versions to gain a deeper understanding of how Cython can be applied to improve performance in your own projects.
