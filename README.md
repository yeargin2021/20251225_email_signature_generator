# Email Signature Generator

A simple Python utility that generates custom email signatures with different formatting styles based on the first letter of a person's name.

## Description

This tool creates email signatures with one of three different prefixes depending on the alphabetical range of the first letter of the person's name:

- **Names A-I**: Signature prefixed with `>>`
- **Names J-R**: Signature prefixed with `--`
- **Names S-Z**: Signature prefixed with `::`

## Features

- Automatic prefix selection based on first letter of name
- Clean signature format: `[prefix][Name], [Title] at [Company]`
- Simple function-based implementation
- Prints and returns the generated signature

## Usage

### Basic Usage

```python
from Mod01 import generate_signature

# Generate a signature
signature = generate_signature("John Doe", "Software Engineer", "Tech Solutions Inc.")
# Output: --John Doe, Software Engineer at Tech Solutions Inc.

signature = generate_signature("Alice Johnson", "Data Scientist", "Analytics Corp.")
# Output: >>Alice Johnson, Data Scientist at Analytics Corp.

signature = generate_signature("Sarah Wilson", "Project Manager", "Digital Ventures")
# Output: ::Sarah Wilson, Project Manager at Digital Ventures
```

### Function Parameters

- `name` (str): Full name of the person
- `title` (str): Job title or position
- `company` (str): Company or organization name

### Return Value

Returns a formatted string containing the complete email signature.

## Examples

```python
# Example 1: Name starting with A-I
generate_signature("Emma Thompson", "UX Designer", "Creative Studio")
# Returns: ">>Emma Thompson, UX Designer at Creative Studio"

# Example 2: Name starting with J-R
generate_signature("Michael Brown", "Marketing Director", "Global Marketing Ltd.")
# Returns: "--Michael Brown, Marketing Director at Global Marketing Ltd."

# Example 3: Name starting with S-Z
generate_signature("Zoe Davis", "Financial Analyst", "Investment Partners")
# Returns: "::Zoe Davis, Financial Analyst at Investment Partners"
```

## Prefix Rules

| First Letter Range | Prefix | Example Names |
|-------------------|--------|---------------|
| A-I | `>>` | Alice, Bob, Catherine, David, Emma, Frank, Grace, Henry, Isabella |
| J-R | `--` | Jack, Karen, Lisa, Michael, Nancy, Oliver, Patricia, Quinn, Rachel |
| S-Z | `::` | Sarah, Thomas, Ursula, Victoria, William, Xavier, Yvonne, Zachary |

## Installation

1. Clone this repository or download the `Mod01.py` file
2. Ensure you have Python installed (Python 3.x recommended)
3. Import the function in your Python script or run directly

## Requirements

- Python 3.x
- No external dependencies required

## File Structure

```
email_signature_generator/
├── Mod01.py          # Main module with signature generation function
└── README.md         # This documentation file
```

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional formatting options
- Support for more complex signature templates
- Configuration file support
- Email integration features

## License

This project is open source and available under the MIT License.