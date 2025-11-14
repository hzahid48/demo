# Demo Arithmetic

A simple Python package demonstrating modular GitHub Actions workflow with CI/CD pipeline.

## Features

- Basic arithmetic operations
- Automated testing with pytest
- CI/CD pipeline with GitHub Actions
- Windows-compatible workflow
- Code coverage reporting

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/demo.git
   cd demo
   ```

2. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Usage

```python
from src.arithmetic import add, subtract

result = add(5, 3)  # Returns 8
result = subtract(5, 3)  # Returns 2
```

## Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ --cov=src/
```

### Building the Package

```bash
# Install build tools
pip install build

# Build the package
python -m build
```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:

1. **Test**: Runs unit tests with coverage
2. **Build**: Builds the Python package
3. **Deploy**: Publishes to PyPI (on main branch)

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/yourusername/demo](https://github.com/yourusername/demo)
