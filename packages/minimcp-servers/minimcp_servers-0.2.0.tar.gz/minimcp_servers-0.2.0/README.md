# ✨ MiniMCP Servers

![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
[![PyPI version](https://img.shields.io/pypi/v/minimcp-servers.svg)](https://pypi.org/project/minimcp-servers/)

A collection of MCP servers built with MiniMCP that expose Python's standard library functionality through clean, focused interfaces.

## 🚀 Installation

```bash
pip install minimcp-servers
# or
uvx --from minimcp-servers <server-name>
```

## ⚙️ Claude Desktop Configuration

Add any server to your Claude Desktop configuration:

```json
{
    "mcpServers": {
        "math-utils": {
            "command": "uvx",
            "args": ["--from", "minimcp-servers", "math-utils"]
        },
        "text-utils": {
            "command": "uvx",
            "args": ["--from", "minimcp-servers", "text-utils"]
        },
        "datetime-utils": {
            "command": "uvx",
            "args": ["--from", "minimcp-servers", "datetime-utils"]
        }
    }
}
```

## 📦 Available Servers

### 1. `math-utils`

**Comprehensive mathematical toolkit combining all tools from arithmetic, continuous, discrete and statistics math servers.**

Perfect for scientific computing, engineering calculations, data analysis, financial modeling, and educational applications requiring diverse mathematical operations.

### 2. `arithmetic-math-utils`

**Fundamental mathematical operations for basic calculations and numerical processing.**

Ideal for applications requiring core arithmetic operations, rounding, array operations, and floating-point manipulations.

| Category | Tool Name |
|----------|-----------|
| **Basic Operations** | `add`, `subtract`, `multiply`, `divide`, `modulo`, `floor_divide`, `pow` |
| **Array Operations** | `minimum`, `maximum` |
| **Rounding** | `round_to`, `ceil`, `floor`, `trunc` |
| **Utility Functions** | `absolute`, `sqrt`, `sign`, `clamp` |
| **Float Operations** | `copysign`, `frexp`, `ldexp`, `modf` |

### 3. `continuous-math-utils`

**Advanced continuous mathematics for scientific computing and engineering applications.**

Essential for physics simulations, signal processing, calculus operations, and applications requiring trigonometric and logarithmic functions.

| Category | Tool Name |
|----------|-----------|
| **Trigonometric** | `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2` |
| **Hyperbolic** | `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh` |
| **Exponential** | `exp`, `expm1` |
| **Logarithmic** | `log`, `log10`, `log2`, `log1p` |
| **Angle Conversion** | `degrees`, `radians` |
| **Distance & Geometry** | `hypot`, `multidimensional_hypot`, `dist` |
| **Special Functions** | `gamma`, `lgamma`, `erf`, `erfc` |

### 4. `discrete-math-utils`

**Integer mathematics and combinatorics for exact discrete computations.**

Perfect for combinatorial analysis, number theory, cryptographic applications, and algorithm design requiring precise integer operations.

| Category | Tool Name |
|----------|-----------|
| **Integer Operations** | `isqrt`, `factorial` |
| **Number Theory** | `gcd`, `lcm` |
| **Combinatorics** | `combination`, `permutation` |

### 5. `statistics-math-utils`

**Comprehensive statistical analysis tools for data science and research applications.**

Essential for exploratory data analysis, quality control, research, business analytics, and machine learning preprocessing.

| Category | Tool Name |
|----------|-----------|
| **Central Tendency** | `mean`, `geometric_mean`, `harmonic_mean`, `median`, `median_low`, `median_high`, `median_grouped`, `mode`, `multimode` |
| **Dispersion** | `variance`, `pvariance`, `stdev`, `pstdev` |
| **Distribution** | `quantiles` |
| **Bivariate Analysis** | `covariance`, `correlation`, `linear_regression` |

### 6. `text-utils`

**Comprehensive text processing toolkit for analysis, manipulation, and secure encoding.**

Perfect for document analysis, content management, data validation, security applications, and text mining operations.

| Category | Tool Name |
|----------|-----------|
| **Analysis** | `length`, `count_substr`, `most_common_words`, `first_index_of_substr`, `last_index_of_substr` |
| **Manipulation** | `normalize_text`, `slice_text`, `replace_substr` |
| **Hashing** | `md5`, `sha1`, `sha256`, `sha512` |
| **Encoding** | `base64_encode`, `base64_decode`, `base64_urlsafe_encode`, `base64_urlsafe_decode`, `hex_encode`, `hex_decode` |

### 7. `datetime-utils`

**Date, time, and duration utilities for temporal data processing.**

Essential for timestamp generation, time format conversions, scheduling systems, and applications requiring precise time calculations.

| Category | Tool Name |
|----------|-----------|
| **Current Time** | `epoch_seconds_now`, `iso_utc_now` |
| **Format Conversion** | `epoch_to_iso_utc`, `iso_utc_to_epoch`, `is_valid_iso_format` |
| **Duration** | `duration_seconds`, `format_duration` |
| **Calendar** | `isleap`, `days_in_month` |

### 8. `random-generator`

**Cryptographically secure random data generation for security applications.**

Perfect for authentication tokens, session IDs, password generation, unique identifiers, and any application requiring secure randomness.

| Category | Tool Name |
|----------|-----------|
| **Secure Generation** | `generate_uuid`, `generate_random_number`, `generate_random_text` |

## Note

Generated using Claude 4 Sonnet!
