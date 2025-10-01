# Copilot Instructions for TDI Rust Python Tools

## Project Overview
This is a **PyO3-based hybrid Rust/Python library** that provides high-performance data processing utilities for Python. The project compiles Rust code into a Python extension module (`.so`/`.pyd`) using **Maturin** as the build backend.

## Architecture

### Core Structure
- **`src/lib.rs`**: Single-file Rust library containing all functions and classes
  - Text processing utilities (regex-based transformations)
  - CSV/Excel conversion (`convert_to_xlsx`)
  - High-performance `DictWriter` class (drop-in replacement for `csv.DictWriter`)
- **`tdi_rust_python_tools.pyi`**: Python type stubs for IDE support
- **`shared/`**: Pure Python utilities (e.g., `timeit` decorator)

### Build System
- **Maturin** manages the Rust→Python compilation pipeline and PyPI publishing
  - Handles cross-compilation for multiple platforms (see `.github/workflows/CI.yml`)
  - Automatically generates Python wheels and source distributions
  - Publishes to PyPI on tagged releases via GitHub Actions
- **uv** manages Python dependencies and virtual environments
  - Project-based dependency management via `uv.lock`
  - Fast resolver and installer replacing pip/pip-tools
  - Virtual environment at `.venv/` (auto-created by uv)
- Uses **PyO3 0.25.1** for Python bindings
- Builds to `cdylib` (C dynamic library) for Python import
- Edition 2024 Rust features enabled

## Development Workflows

### Building & Testing
```bash
# Setup Python environment (uv handles venv creation)
uv sync

# Development build (fast, debug symbols) - installs into current Python env
maturin develop

# Release build (optimized, slower compilation)
maturin develop --release

# Build wheels for distribution (creates .whl files in target/wheels/)
maturin build --release

# Install Python dependencies (managed by uv, not pip)
uv add <package-name>

# Run Python tests (pytest configured in .vscode/settings.json)
pytest tests/

# Publish to PyPI (done automatically via CI on tags)
maturin publish
```

### Key Build Artifacts
- `target/debug/libtdi_rust_python_tools.so` - Debug build
- `target/release/libtdi_rust_python_tools.so` - Release build
- `target/wheels/*.whl` - Distributable wheel files

### Environment Setup
- Python 3.13+ required (`pyproject.toml`)
- Uses **uv** for dependency management (`uv.lock` present)
  - Project follows uv's [project structure](https://docs.astral.sh/uv/concepts/projects/init/)
  - Dependencies defined in `pyproject.toml` `[dependency-groups]`
  - Lock file ensures reproducible builds across environments
- Virtual environment at `.venv/` (auto-created by `uv sync`)

## Code Conventions

### Rust Patterns
1. **PyO3 function decoration**: All exported functions use `#[pyfunction]` or `#[pyclass]`
2. **Lazy regex compilation**: Use `lazy_static!` for regex patterns (see `LT_GT_PATTERN`, `TEMPERATURE_PATTERN`)
   ```rust
   lazy_static! {
       static ref PATTERN_NAME: Regex = Regex::new(r"...").unwrap();
   }
   ```
3. **Error handling**: Convert Rust errors to Python exceptions
   - File operations → `PyFileNotFoundError`, `PyValueError`
   - CSV errors → `PyValueError` via `csv_error_to_py_err` helper
4. **Performance optimizations**:
   - Reuse buffers in `DictWriter` (`string_buffer`, internal `buffer`)
   - Batch operations in `writerows()` to minimize Python interop
   - Use `Vec::with_capacity()` for pre-allocation

### Python Integration
- **Type stubs** must be updated when adding/modifying Rust functions
- Use Protocol types (e.g., `_SupportsWrite`) for file-like objects
- Python module name: `tdi_rust_python_tools` (defined in `#[pymodule]`)

### Linting & Formatting
- **Ruff** configured for Python (see `ruff.toml`)
  - Target: Python 3.13
  - Line length: 120
  - All rules enabled except docstrings, copyright, print statements
  - Google-style docstrings when used
- **Rust**: Standard `cargo fmt` and `cargo clippy`

## Critical Implementation Details

### DictWriter Optimization Strategy
The `DictWriter` class is **performance-critical** - it's designed to be faster than Python's stdlib `csv.DictWriter`:
- Maintains internal byte buffer to avoid repeated Python `write()` calls
- Reuses `string_buffer: Vec<String>` across rows to reduce allocations
- `writerows()` batches all rows before flushing (single Python interop)
- Custom delimiter support via `csv::WriterBuilder`

### Module Registration Pattern
New functions/classes must be registered in the `#[pymodule]` function:
```rust
#[pymodule(name = "tdi_rust_python_tools")]
fn string_sum(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(your_function, m)?)?;
    m.add_class::<YourClass>()?;
    Ok(())
}
```

### Regex-Based Text Processing
Most utility functions follow this pattern:
1. Define regex in `lazy_static!` block
2. Export simple `#[pyfunction]` wrapper
3. Return `PyResult<String>` for Python compatibility

## CI/CD
- **GitHub Actions** workflow at `.github/workflows/CI.yml` (auto-generated by Maturin)
- Builds wheels for Linux (x86_64, x86, aarch64, armv7, s390x, ppc64le), Windows (x64, x86), macOS (x86_64, aarch64)
- Auto-publishes to PyPI on tagged releases via [Maturin's publishing workflow](https://www.maturin.rs/tutorial.html)
- Uses `sccache` for Rust build caching
- Release process: Create git tag → CI builds wheels → Auto-publish to PyPI

## Adding New Functionality

### New Rust Function
1. Add function in `src/lib.rs` with `#[pyfunction]`
2. Register in `#[pymodule]` block
3. Add type signature to `tdi_rust_python_tools.pyi`
4. Rebuild with `maturin develop`
5. Write tests in `tests/` (pytest)

### New Rust Class
1. Define `#[pyclass]` struct and `#[pymethods]` impl in `src/lib.rs`
2. Register with `m.add_class::<YourClass>()?` in module
3. Add class definition to `.pyi` file
4. Follow buffer reuse patterns if performance-critical

## Version Management
- Version defined in both `Cargo.toml` and `pyproject.toml` (keep in sync!)
- `pyproject.toml` uses `dynamic = ["version"]` - Maturin reads from `Cargo.toml`
- Current version: 0.8.2
