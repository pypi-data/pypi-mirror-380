# DataValues
[![Pypi](https://img.shields.io/pypi/v/datavalues)](https://pypi.org/project/datavalues)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/bnassif/datavalues/main/LICENSE)
![GitHub Release Date](https://img.shields.io/github/release-date/bnassif/datavalues)

DataValues is a Python package for handling data sizes (bits/bytes) with full support for both SI (decimal) and IEC (binary) prefixes.

Many systems disagree on how to report storage or memory sizes:

- Proxmox VE reports in GiB (binary).
- NetBox reports in GB (decimal).
- Vendors often switch between bits vs bytes.

This package smooths out those inconsistencies by providing an object-oriented interface for conversion, arithmetic, and comparison across all supported units.

## Features

- Supports bits and bytes.
- Full range of SI (kilo, mega, giga, …) and IEC (kibi, mebi, gibi, …) units.
- Accurate conversions between decimal/binary forms.
- Intuitive comparisons (>, <, ==, >=, <=).
- Safe arithmetic with unit awareness (+, -, *, /, +=, etc.).
- Simple API that feels natural in Python.

## Installation

```bash
# PyPi Installation
pip install datavalues
# GitHub Installation
pip install git+'https://github.com/bnassif/datavalues.git' 
```

## Getting Started

### Coversion
```python
from datavalues import *

# 1 MB (decimal) to bytes
print(MegaByte(1).convert(Byte))   # 1000000

# 1 MiB (binary) to bytes
print(MebiByte(1).convert(Byte))   # 1048576

# 1 GiB (binary) to MB (decimal)
print(GibiByte(1).convert(MegaByte))  # 1073.741824
```

### Comparisons
```python
from datavalues import *

assert GigaByte(1) > MegaByte(500)
assert KibiByte(1024) == MebiByte(1)
```

### Arithmetic
```python
from datavalues import *

assert GigaByte(1) > MegaByte(500)
assert KibiByte(1024) == MebiByte(1)
```

## Why?
Different systems report the *same* underlying data sizes differently:
- **Proxmox VE**: `16 GiB RAM`
- **NetBox**: `16 GB RAM`

Both refer to the same ~17.18 billion bytes, but expressed in different units.  
**DataValues** eliminiates the guesswork by normalizing all operations through a consistent baseline (bits).

## License
MIT - Feel free to use, extend, and contribute.


## Supported Units

### Core Units

| Unit       | Symbol | Bytes equivalent | Class         |
| ---------- | ------ | ---------------- | ------------- |
| Bit        | b      | 1/8 byte         | `Bit`         |
| Byte       | B      | 1 byte           | `Byte`        |

### SI (Decimal, base 1000)

| Unit       | Symbol | Bytes equivalent | Class         |
| ---------- | ------ | ---------------- | ------------- |
| Kilobit    | kb     | 10³ bits         | `KiloBit`     |
| Kilobyte   | kB     | 10³ bytes        | `KiloByte`    |
| Megabit    | Mb     | 10⁶ bits         | `MegaBit`     |
| Megabyte   | MB     | 10⁶ bytes        | `MegaByte`    |
| Gigabit    | Gb     | 10⁹ bits         | `GigaBit`     |
| Gigabyte   | GB     | 10⁹ bytes        | `GigaByte`    |
| Terabit    | Tb     | 10¹² bits        | `TeraBit`     |
| Terabyte   | TB     | 10¹² bytes       | `TeraByte`    |
| Petabit    | Pb     | 10¹⁵ bits        | `PetaBit`     |
| Petabyte   | PB     | 10¹⁵ bytes       | `PetaByte`    |
| Exabit     | Eb     | 10¹⁸ bits        | `ExaBit`      |
| Exabyte    | EB     | 10¹⁸ bytes       | `ExaByte`     |
| Zettabit   | Zb     | 10²¹ bits        | `ZettaBit`    |
| Zettabyte  | ZB     | 10²¹ bytes       | `ZettaByte`   |
| Yottabit   | Yb     | 10²⁴ bits        | `YottaBit`    |
| Yottabyte  | YB     | 10²⁴ bytes       | `YottaByte`   |
| Ronnabit   | Rb     | 10²⁷ bits        | `RonnaBit`    |
| Ronnabyte  | RB     | 10²⁷ bytes       | `RonnaByte`   |
| Quettabit  | Qb     | 10³⁰ bits        | `QuettaBit`   |
| Quettabyte | QB     | 10³⁰ bytes       | `QuettaByte`  |

### IEC (Binary, base 1024)

| Unit      | Symbol | Bytes equivalent | Class         |
| --------- | ------ | ---------------- | ------------- |
| Kibibit   | Kib    | 2¹⁰ bits         | `KibiBit`     |
| Kibibyte  | KiB    | 2¹⁰ bytes        | `KibiByte`    |
| Mebibit   | Mib    | 2²⁰ bits         | `MebiBit`     |
| Mebibyte  | MiB    | 2²⁰ bytes        | `MebiByte`    |
| Gibibit   | Gib    | 2³⁰ bits         | `GibiBit`     |
| Gibibyte  | GiB    | 2³⁰ bytes        | `GibiByte`    |
| Tebibit   | Tib    | 2⁴⁰ bits         | `TebiBit`     |
| Tebibyte  | TiB    | 2⁴⁰ bytes        | `TebiByte`    |
| Pebibit   | Pib    | 2⁵⁰ bits         | `PebiBit`     |
| Pebibyte  | PiB    | 2⁵⁰ bytes        | `PebiByte`    |
| Exbibit   | Eib    | 2⁶⁰ bits         | `ExbiBit`     |
| Exbibyte  | EiB    | 2⁶⁰ bytes        | `ExbiByte`    |
| Zebibit   | Zib    | 2⁷⁰ bits         | `ZebiBit`     |
| Zebibyte  | ZiB    | 2⁷⁰ bytes        | `ZebiByte`    |
| Yobibit   | Yib    | 2⁸⁰ bits         | `YobiBit`     |
| Yobibyte  | YiB    | 2⁸⁰ bytes        | `YobiByte`    |
| Robibit   | Rib    | 2⁹⁰ bits         | `RobiBit`     |
| Robibyte  | RiB    | 2⁹⁰ bytes        | `RobiByte`    |
| Quebibit  | Qib    | 2¹⁰⁰ bits        | `QuebiBit`    |
| Quebibyte | QiB    | 2¹⁰⁰ bytes       | `QuebiByte`   |

## License
MIT - Feel free to use, extend, and contribute.