"""
IntelSeed: Python module for Intel RDSEED hardware random number generation.

This module provides access to Intel's RDSEED instruction for generating
cryptographically secure random numbers using hardware entropy.
"""

import ctypes
import os
import math
import platform


class RDSEEDError(Exception):
    """Exception raised when RDSEED operations fail."""
    pass


class IntelSeed:
    """Intel RDSEED hardware random number generator."""
    
    def __init__(self, library_path: str = None):
        """
        Initialize the RDSEED generator.
        
        Args:
            library_path: Path to the librdseed library file. If None, detects OS and looks for it
                          in the same directory as this module (librdseed.so on Linux/macOS, librdseed.dll on Windows).
        
        Raises:
            RDSEEDError: If the library cannot be loaded or RDSEED is not supported.
        """
        if library_path is None:
            # Look for the library in the same directory as this module
            module_dir = os.path.dirname(os.path.abspath(__file__))
            if platform.system() == "Windows":
                lib_name = "librdseed.dll"
            else:
                lib_name = "librdseed.so"
            library_path = os.path.join(module_dir, lib_name)
        
        if not os.path.exists(library_path):
            raise RDSEEDError(f"RDSEED library not found at {library_path}")
        
        try:
            self.lib = ctypes.CDLL(library_path)
        except OSError as e:
            raise RDSEEDError(f"Failed to load RDSEED library: {e}")
        
        # Define function signatures
        self.lib.rdseed_bytes.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t]
        self.lib.rdseed_bytes.restype = ctypes.c_size_t
        
        # Test if RDSEED is available
        try:
            _test_data = self.get_bytes(1)
        except Exception as e:
            raise RDSEEDError(f"RDSEED instruction not available on this CPU: {e}")
    
    def get_bytes(self, n_bytes: int) -> bytes:
        """
        Generate n_bytes of raw entropy from RDSEED.
        
        Args:
            n_bytes: Number of bytes to generate (must be positive).
        
        Returns:
            bytes: Raw entropy data.
        
        Raises:
            RDSEEDError: If the requested number of bytes cannot be generated.
            ValueError: If n_bytes is not positive.
        """
        if n_bytes <= 0:
            raise ValueError("n_bytes must be positive")
        
        buf = (ctypes.c_uint8 * n_bytes)()
        written = self.lib.rdseed_bytes(buf, n_bytes)
        
        if written != n_bytes:
            raise RDSEEDError(f"RDSEED failed: wrote {written}/{n_bytes} bytes")
        
        return bytes(buf)
    
    def get_bits(self, n_bits: int) -> bytes:
        """
        Generate n_bits of raw entropy from RDSEED.
        
        Args:
            n_bits: Number of bits to generate (must be positive).
        
        Returns:
            bytes: Raw entropy data. The number of bytes returned is
                   ceil(n_bits / 8), so there may be extra bits at the end.
        
        Raises:
            RDSEEDError: If the requested number of bits cannot be generated.
            ValueError: If n_bits is not positive.
        """
        if n_bits <= 0:
            raise ValueError("n_bits must be positive")
        
        n_bytes = math.ceil(n_bits / 8)
        return self.get_bytes(n_bytes)
    
    def get_exact_bits(self, n_bits: int) -> bytes:
        """
        Generate exactly n_bits of raw entropy from RDSEED.
        
        This function generates the minimum number of bytes needed and
        truncates any extra bits to return exactly the requested number of bits.
        
        Args:
            n_bits: Number of bits to generate (must be positive).
        
        Returns:
            bytes: Raw entropy data with exactly n_bits.
        
        Raises:
            RDSEEDError: If the requested number of bits cannot be generated.
            ValueError: If n_bits is not positive.
        """
        if n_bits <= 0:
            raise ValueError("n_bits must be positive")
        
        n_bytes = math.ceil(n_bits / 8)
        data = self.get_bytes(n_bytes)
        
        # Truncate to exact number of bits
        if n_bits % 8 != 0:
            # Mask off the extra bits in the last byte
            last_byte = data[-1]
            mask = (1 << (n_bits % 8)) - 1
            last_byte &= mask
            data = data[:-1] + bytes([last_byte])
        
        return data

    def random_int(self, low: int = 0, high: int = 1) -> int:
        """
        Generate a cryptographically secure random integer in the range [low, high].

        Uses RDSEED hardware entropy with rejection sampling to ensure uniform distribution
        without bias. This is suitable for cryptographic or security-sensitive applications.

        Args:
            low: The lower bound of the range (inclusive). Default: 0.
            high: The upper bound of the range (inclusive). Default: 1.

        Returns:
            int: A random integer N where low <= N <= high.

        Raises:
            ValueError: If high < low.
            RDSEEDError: If RDSEED fails to generate sufficient entropy.
        """
        if high < low:
            raise ValueError("high must be >= low")
        if low == high:
            return low
        
        range_size = high - low + 1
        bits_needed = (range_size - 1).bit_length()
        
        while True:
            data = self.get_exact_bits(bits_needed)
            value = int.from_bytes(data, 'big')
            if value < range_size:
                return low + value


def is_rdseed_available(library_path: str | None = None) -> bool:
    """
    Safely check if RDSEED is available on this CPU and the library can load.

    This attempts to instantiate IntelSeed, which tests the RDSEED instruction.
    It returns False for CPU unsupport but re-raises other errors (e.g., missing library).

    Args:
        library_path: Optional path to the librdseed library. Defaults to auto-detection
                      (same as IntelSeed constructor).

    Returns:
        bool: True if RDSEED is supported and the library loads successfully.

    Raises:
        RDSEEDError: For non-CPU issues like missing library (so the caller can handle them).
        OSError: If library loading fails in a way not caught by RDSEEDError.
    """
    try:
        IntelSeed(library_path=library_path)
        return True
    except RDSEEDError as e:
        error_msg = str(e).lower()
        if "not available on this cpu" in error_msg:
            # Optional: Log for debugging (remove if not needed)
            print(f"RDSEED not supported on this CPU: {e}")
            return False
        else:
            # Re-raise other RDSEEDError cases (e.g., library not found)
            raise
    except Exception as e:
        # Catch unexpected issues but treat as unavailable
        print(f"Unexpected error checking RDSEED: {e}")
        return False


# Global instance for convenience
_rdseed = None

def get_rdseed() -> IntelSeed:
    """Get the global RDSEED instance."""
    global _rdseed
    if _rdseed is None:
        _rdseed = IntelSeed()
    return _rdseed


def get_bytes(n_bytes: int) -> bytes:
    """
    Generate n_bytes of raw entropy from RDSEED.
    
    Convenience function using the global RDSEED instance.
    """
    return get_rdseed().get_bytes(n_bytes)


def get_bits(n_bits: int) -> bytes:
    """
    Generate n_bits of raw entropy from RDSEED.
    
    Convenience function using the global RDSEED instance.
    """
    return get_rdseed().get_bits(n_bits)


def get_exact_bits(n_bits: int) -> bytes:
    """
    Generate exactly n_bits of raw entropy from RDSEED.
    
    Convenience function using the global RDSEED instance.
    """
    return get_rdseed().get_exact_bits(n_bits)


def random_int(low: int = 0, high: int = 1) -> int:
    """
    Generate a cryptographically secure random integer in the range [low, high].

    Convenience function using the global RDSEED instance. See IntelSeed.random_int for details.
    """
    return get_rdseed().random_int(low, high)


# Example usage
if __name__ == "__main__":
    try:
        # Test basic functionality
        print("Testing IntelSeed module...")
        
        # Test byte generation
        data_32 = get_bytes(32)
        print(f"32 bytes: {data_32.hex()}")
        
        # Test bit generation
        data_256_bits = get_bits(256)
        print(f"256 bits (32 bytes): {data_256_bits.hex()}")
        
        # Test exact bit generation
        data_200_bits = get_exact_bits(200)
        print(f"200 bits (25 bytes): {data_200_bits.hex()}")
        print(f"200 bits length: {len(data_200_bits)} bytes = {len(data_200_bits) * 8} bits")
        
        # Test various bit sizes
        for bits in [1, 7, 8, 15, 16, 31, 32, 63, 64, 127, 128]:
            data = get_exact_bits(bits)
            actual_bits = len(data) * 8
            print(f"{bits:3d} bits -> {len(data):2d} bytes ({actual_bits:3d} bits): {data.hex()}")
        
    except RDSEEDError as e:
        print(f"RDSEED Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
