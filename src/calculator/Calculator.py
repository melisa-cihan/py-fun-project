
import math
class Calculator:
    def add(self, a, b):
        return a + b

    # --- Translation Data (Single-Digit 0-9, and Latin up to X) ---
    _TRANSLATIONS = {
        'english': {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9},
        'german': {'null': 0, 'eins': 1, 'zwei': 2, 'drei': 3, 'vier': 4, 'fünf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9},
        'spanish': {'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9},
        # Russian (Cyrillic)
        'russian': {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9},
        # Chinese (Simplified)
        'chinese': {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9},
        # Latin Roman Numerals (0-10) - stored in lowercase for case-insensitivity
        'latin': {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7, 'viii': 8, 'ix': 9, 'x': 10} 
    }
    
    # Flatten the map for fast, case-insensitive lookup
    _FLAT_MAP = {k: v for lang_map in _TRANSLATIONS.values() for k, v in lang_map.items()}

    def __init__(self):
        """Initializes a new Calculator instance."""
        pass

    def _parse_number(self, n):
        """Converts input n (int, float, or supported number-string) into a float."""
        
        # 1. Handle native numeric types (int, float)
        if isinstance(n, (int, float)):
            return float(n)
        
        # 2. Handle strings
        if isinstance(n, str):
            # Strip whitespace and convert to lowercase for case-insensitive and spacing-tolerant checks
            s = n.strip().lower() 
            
            # Check if it's a translated name (e.g., "three", "ocho", "v")
            if s in self._FLAT_MAP:
                return float(self._FLAT_MAP[s])
            
            # Check if it's a standard number string (e.g., "1", "1.600")
            try:
                # Handle standard float parsing
                return float(s)
            except ValueError:
                # If parsing fails (e.g., input is "X" but only up to "ix" was expected), 
                # we let it fall through or raise an error for strictness.
                pass 
        
        # For unsupported types or failed string conversions, return the original input
        return n

    # --- Arithmetic Methods ---

    def _perform_operation(self, a, b, operation):
        """Helper to parse and perform a binary arithmetic operation."""
        a_val = self._parse_number(a)
        b_val = self._parse_number(b)
        
        if isinstance(a_val, (int, float)) and isinstance(b_val, (int, float)):
            return operation(a_val, b_val)
        
        # Return string concatenation for add if parsing fails (as suggested by prompt example)
        if operation == (lambda x, y: x + y):
            return a + b
            
        raise TypeError(f"Operation failed: Cannot perform arithmetic on unparsed values: {a}, {b}")


    def add(self, a, b):
        """Adds two numbers, supporting string translations."""
        return self._perform_operation(a, b, lambda x, y: x + y)

    def sub(self, a, b):
        """Subtracts b from a, supporting string translations."""
        return self._perform_operation(a, b, lambda x, y: x - y)

    def mul(self, a, b):
        """Multiplies two numbers, supporting string translations."""
        return self._perform_operation(a, b, lambda x, y: x * y)

    def div(self, a, b):
        """Divides a by b, supporting string translations."""
        def safe_div(x, y):
            if y == 0:
                raise ZeroDivisionError("Division by zero.")
            return x / y
        return self._perform_operation(a, b, safe_div)


    # --- Factorize Method ---

    def factorize(self, n):
        """Returns the prime factors of a parsed integer n."""
        # Parse the number, forcing it to be an integer
        n_val = self._parse_number(n)
        
        if not isinstance(n_val, (int, float)):
             raise ValueError("Factorization requires a numeric value.")
        
        # Ensure it's a positive integer
        if n_val <= 0 or not math.isclose(n_val, round(n_val)):
            raise ValueError("Factorization requires a positive integer.")
            
        n_val = int(round(n_val))

        factors = []
        temp = n_val
        d = 2
        
        # Trial division algorithm
        while d * d <= temp:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1
        
        if temp > 1:
            factors.append(temp)
            
        return factors