# --- imports (top of file) ---


# --- variables (grouped and clear) ---
base_numbers = [5, 10, 15, 20]
scale_factor = 2
extra_values = [3, 6]


# --- reusable functions ---

def multiply_by_factor(values, factor):
    return [value * factor for value in values]


def add_offset(values, offset):
    return [value + offset for value in values]


def describe_list(values):
    return {
        'count': len(values),
        'minimum': min(values) if values else None,
        'maximum': max(values) if values else None,
        'sum': sum(values)
    }


def print_summary(header, values):
    information = describe_list(values)
    print(f"{header}")
    print(f"  numbers: {values}")
    print(f"  count: {information['count']}")
    print(f"  min: {information['minimum']}")
    print(f"  max: {information['maximum']}")
    print(f"  sum: {information['sum']}")
    print("")


# --- main execution ---

def main():
    initial = base_numbers
    print_summary("Initial numbers:", initial)

    scaled = multiply_by_factor(initial, scale_factor)
    print_summary("Scaled numbers:", scaled)

    offset = 5
    adjusted = add_offset(scaled, offset)
    print_summary("Scaled + offset numbers:", adjusted)

    combined = adjusted + extra_values
    print_summary("Final combined numbers:", combined)

    scaled_again = multiply_by_factor(combined, 3)
    print_summary("Reused function (scaled again):", scaled_again)


if __name__ == "__main__":
    main()


# --- explanation section ---

# Why code structure matters:
# Organizing imports, variables, functions, and execution in order helps others follow logic quickly.
# It allows easy updates and makes debugging simpler.

# How functions improve reuse:
# Small functions with one responsibility can be called in multiple places, reducing duplication.
# This keeps the program consistent and easier to extend.

# How separating logic from execution improves readability:
# Defining functions first and using a lean main() block means the script reads like a narrative.
# The core logic is reusable and tests can target functions directly.

# Script usage:
# Run in terminal with: python clean_code_demo.py
