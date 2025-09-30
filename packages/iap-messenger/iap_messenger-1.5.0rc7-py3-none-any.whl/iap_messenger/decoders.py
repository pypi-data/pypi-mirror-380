"""
IA Parc Inference decoders
"""
import logging
from re import L
from typing import Any
from struct import unpack
from PIL.Image import Image
from io import BytesIO
import msgpack
import msgpack_numpy as m
import lz4.frame as lz4

from iap_messenger.config import LOGGER


Error = ValueError | None
LOGGER = logging.getLogger("Decoders")
LOGGER.propagate = True
## Data decoders


def decode(data: bytes, decoder: str) -> tuple[Any, Error]:
    """
    Decode data
    Arguments:
    data: bytes
    decoder: str
    """
    use_lz4 = False
    if "lz4(" in decoder:
        use_lz4 = True
        decoder = decoder.replace("lz4(", "").replace(")", "")
    if decoder == "float":
        return decode_float(data)
    if decoder == "int" or decoder == "integer":
        return decode_int(data)
    if decoder == "bool":
        return decode_bool(data)
    if decoder == "file":
        return decode_file(data, use_lz4)
    elif decoder == "image":
        return decode_image(data, use_lz4)
    elif decoder == "text" or decoder == "str" or decoder == "string":
        return decode_text(data, use_lz4)
    elif decoder == "json":
        return decode_json(data, use_lz4)
    elif decoder == "msgpack":
        return decode_msgpack(data, use_lz4)
    elif decoder == "numpy":
        return decode_numpy(data, use_lz4)
    elif decoder == "multipart":
        return decode_multipart(data, [], "", use_lz4)

    
    return None, ValueError(f"Decoder {decoder} is not supported")

def decode_float(data: bytes) -> tuple[float, Error]:
    """
    Read float - robust implementation that handles various formats
    Arguments:
    data: bytes
    """
    if data is None:
        return 0.0, ValueError("No data to read")
    if not isinstance(data, bytes):
        return 0.0, ValueError("Data is not bytes")
    if not data:
        return 0.0, ValueError("Empty data")
    
    try:
        # First try to parse as string representation (most flexible)
        try:
            # Try UTF-8 first, then latin-1 as fallback
            try:
                text = data.decode('utf-8').strip()
            except UnicodeDecodeError:
                text = data.decode('latin-1').strip()
            
            # Handle common string representations
            if text:
                # Support hex, binary, and octal formats by converting to int first, then float
                if text.startswith('0x') or text.startswith('0X'):
                    return float(int(text, 16)), None  # Hexadecimal
                elif text.startswith('0b') or text.startswith('0B'):
                    return float(int(text, 2)), None   # Binary
                elif text.startswith('0o') or text.startswith('0O'):
                    return float(int(text, 8)), None   # Octal
                else:
                    return float(text), None           # Decimal or scientific notation
        except (ValueError, UnicodeDecodeError):
            pass
        
        # Try to interpret as integer bytes first (more likely to be intended as numbers)
        if len(data) <= 8:
            try:
                int_val = int.from_bytes(data, byteorder='little', signed=True)
                # Check if this looks like a reasonable integer (not too large for float precision)
                if abs(int_val) < 2**53:  # 53 bits is float64 precision limit
                    return float(int_val), None
            except Exception:
                pass
            
            try:
                int_val = int.from_bytes(data, byteorder='big', signed=True)
                if abs(int_val) < 2**53:
                    return float(int_val), None
            except Exception:
                pass
        
        # Try struct unpack for binary float data (when int interpretation doesn't make sense)
        if len(data) == 4:
            try:
                value = unpack('f', data)[0]  # 32-bit float
                return value, None
            except Exception:
                try:
                    value = unpack('!f', data)[0]  # Big-endian 32-bit float
                    return value, None
                except Exception:
                    pass
        elif len(data) == 8:
            try:
                value = unpack('d', data)[0]  # 64-bit double
                return value, None
            except Exception:
                try:
                    value = unpack('!d', data)[0]  # Big-endian 64-bit double
                    return value, None
                except Exception:
                    pass
        
        # Final fallback for remaining cases
        if len(data) <= 8:
            try:
                int_val = int.from_bytes(data, byteorder='little', signed=False)
                return float(int_val), None
            except Exception:
                try:
                    int_val = int.from_bytes(data, byteorder='big', signed=False)
                    return float(int_val), None
                except Exception:
                    pass
        
    except Exception as e:
        return 0.0, ValueError(f"Error reading float: {e}")
    
    return 0.0, ValueError(f"Could not decode {len(data)} bytes as float")

def decode_int(data: bytes) -> tuple[int, Error]:
    """
    Read int - robust implementation using int.from_bytes and string parsing
    Arguments:
    data: bytes
    """
    if data is None:
        return 0, ValueError("No data to read")
    if not isinstance(data, bytes):
        return 0, ValueError("Data is not bytes")
    if not data:
        return 0, ValueError("Empty data")
    
    try:
        LOGGER.debug(f"Decoding int from {len(data)} bytes")
        
        # First try to parse as string representation (most flexible)
        try:
            # Try UTF-8 first, then latin-1 as fallback
            try:
                text = data.decode('utf-8').strip()
            except UnicodeDecodeError:
                text = data.decode('latin-1').strip()
            
            # Handle common string representations
            if text:
                # Support different bases (decimal, hex, binary)
                if text.startswith('0x') or text.startswith('0X'):
                    return int(text, 16), None  # Hexadecimal
                elif text.startswith('0b') or text.startswith('0B'):
                    return int(text, 2), None   # Binary
                elif text.startswith('0o') or text.startswith('0O'):
                    return int(text, 8), None   # Octal
                else:
                    return int(text), None      # Decimal
        except (ValueError, UnicodeDecodeError):
            pass
        
        # Use int.from_bytes for binary data (most robust for various byte lengths)
        if len(data) <= 8:  # Support up to 64-bit integers
            try:
                # Try little-endian first (most common)
                value = int.from_bytes(data, byteorder='little', signed=True)
                return value, None
            except Exception:
                try:
                    # Try big-endian
                    value = int.from_bytes(data, byteorder='big', signed=True)
                    return value, None
                except Exception:
                    try:
                        # Try unsigned little-endian
                        value = int.from_bytes(data, byteorder='little', signed=False)
                        return value, None
                    except Exception:
                        try:
                            # Try unsigned big-endian
                            value = int.from_bytes(data, byteorder='big', signed=False)
                            return value, None
                        except Exception:
                            pass
        
        # Fallback to struct unpack for compatibility with existing code
        if len(data) == 4:
            try:
                value = unpack('i', data)[0]  # 32-bit signed int
                return value, None
            except Exception:
                try:
                    value = unpack('!i', data)[0]  # Big-endian 32-bit signed int
                    return value, None
                except Exception:
                    pass
        elif len(data) == 8:
            try:
                value = unpack('q', data)[0]  # 64-bit signed int
                return value, None
            except Exception:
                try:
                    value = unpack('!q', data)[0]  # Big-endian 64-bit signed int
                    return value, None
                except Exception:
                    pass
        
    except Exception as e:
        return 0, ValueError(f"Error reading int: {e}")
    
    return 0, ValueError(f"Could not decode {len(data)} bytes as int")

def decode_bool(data: bytes) -> tuple[bool, Error]:
    """
    Read bool - robust implementation that handles various boolean representations
    Arguments:
    data: bytes
    """
    if data is None:
        return False, ValueError("No data to read")
    if not isinstance(data, bytes):
        return False, ValueError("Data is not bytes")
    if not data:
        return False, ValueError("Empty data")
    
    try:
        # First try to parse as string representation (most flexible)
        try:
            # Try UTF-8 first, then latin-1 as fallback
            try:
                text = data.decode('utf-8').strip().lower()
            except UnicodeDecodeError:
                text = data.decode('latin-1').strip().lower()
            
            # Handle common string representations
            if text in ('true', '1', 'yes', 'on', 't', 'y'):
                return True, None
            elif text in ('false', '0', 'no', 'off', 'f', 'n', ''):
                return False, None
            else:
                # Try to parse as number and check if non-zero
                try:
                    num_val = float(text)
                    return bool(num_val), None
                except ValueError:
                    pass
        except (ValueError, UnicodeDecodeError):
            pass
        
        # Try struct unpack for single byte boolean
        if len(data) == 1:
            try:
                value = unpack('?', data)[0]
                return value, None
            except Exception:
                # Interpret single byte as boolean (0 = False, non-zero = True)
                return bool(data[0]), None
        
        # For multi-byte data, use int.from_bytes and check if non-zero
        if len(data) <= 8:
            try:
                # Try little-endian
                int_val = int.from_bytes(data, byteorder='little', signed=False)
                return bool(int_val), None
            except Exception:
                try:
                    # Try big-endian
                    int_val = int.from_bytes(data, byteorder='big', signed=False)
                    return bool(int_val), None
                except Exception:
                    pass
        
        # Fallback: any non-empty, non-zero byte sequence is True
        return any(b != 0 for b in data), None
        
    except Exception as e:
        return False, ValueError(f"Error reading bool: {e}")
    
    return False, ValueError(f"Could not decode {len(data)} bytes as bool")

def decode_file(data: bytes, use_lz4: bool=False) -> tuple[BytesIO, Error]:
    """
    Read file
    Arguments:
    data: bytes
    """
    if not data:
        return BytesIO(), ValueError("No data to read")
    if not isinstance(data, bytes):
        return BytesIO(), ValueError("Data is not bytes")
    try:
        if use_lz4:
            data = lz4.decompress(data)
        file = BytesIO(data)
    except Exception as e:
        return BytesIO(), ValueError(f"Error reading file: {e}")
    return file, None

def decode_image(data: bytes, use_lz4: bool=False) -> tuple[Image|None, Error]:
    """
    Read image
    Arguments:
    data: bytes
    """
    if not data:
        return None, ValueError("No data to read")
    if not isinstance(data, bytes):
        return None, ValueError("Data is not bytes")
    try:
        from PIL import Image
        if use_lz4:
            data = lz4.decompress(data)
        image = Image.open(BytesIO(data))
    except Exception as e:
        return None, ValueError(f"Error reading image: {e}")
    return image, None

def decode_text(data: bytes, use_lz4: bool=False) -> tuple[str, Error]:
    """
    Read text
    Arguments:
    data: bytes
    """
    if not data:
        return "", ValueError("No data to read")
    if not isinstance(data, bytes):
        return "", ValueError("Data is not bytes")
    try:
        if use_lz4:
            data = lz4.decompress(data)
        
        # Try UTF-8 decoding first (most common case)
        try:
            text = data.decode("utf-8")
            return text, None
        except UnicodeDecodeError:
            # Fallback to latin-1 which can decode any byte sequence
            try:
                text = data.decode("latin-1")
                return text, None
            except UnicodeDecodeError:
                # Final fallback: decode only ASCII characters
                try:
                    text = data.decode("ascii", errors="ignore")
                    return text, None
                except Exception:
                    # If all decoding attempts fail, return error
                    pass
        
    except Exception as e:
        return "", ValueError(f"Error reading text: {e}")
    
    return "", ValueError("Could not decode text data with any supported encoding")

def decode_json(data: bytes, use_lz4: bool=False) -> tuple[dict, Error]:
    """
    Read json
    Arguments:
    data: bytes
    """
    if not data:
        return {}, ValueError("No data to read")
    if not isinstance(data, bytes):
        return {}, ValueError("Data is not bytes")
    try:
        from json_tricks import loads
        if use_lz4:
            data = lz4.decompress(data)
        json_data = loads(data.decode("utf-8"))
    except Exception as e:
        return {}, ValueError(f"Error reading json: {e}")
    return json_data, None

def decode_msgpack(data: bytes, use_lz4: bool=False) -> tuple[dict, Error]:
    """
    Read msgpack
    Arguments:
    data: bytes
    """
    if not data:
        return {}, ValueError("No data to read")
    if not isinstance(data, bytes):
        return {}, ValueError("Data is not bytes")
    try:
        if use_lz4:
            data = lz4.decompress(data)
        json_data = msgpack.unpackb(data, object_hook=m.decode)
    except Exception as e:
        return {}, ValueError(f"Error reading msgpack: {e}")
    return json_data, None

def decode_numpy(data: bytes, use_lz4: bool=False) -> tuple[dict, Error]:
    """
    Read numpy
    Arguments:
    data: bytes
    """
    return decode_msgpack(data, use_lz4)

def decode_multipart(data: bytes, items: list, content_type: str, use_lz4: bool=False) -> tuple[dict, Error]:
    """
    Read multi-part data
    Arguments:
    data: bytes
    """
    if not data:
        return {}, ValueError("No data to read")
    if not isinstance(data, bytes):
        return {}, ValueError("Data is not bytes")
    if not items:
        return {}, ValueError("No items to read")
    try:
        from streaming_form_data import StreamingFormDataParser
        from streaming_form_data.targets import BaseTarget
        if use_lz4:
            data = lz4.decompress(data)
        LOGGER.info(f"init decode_multipart with content_type: '{content_type}'")
        class BytesTarget(BaseTarget):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self._data = None
                
            def on_data_received(self, data: bytes):
                self.data = data

        res = {}
        results = {}
        if "boundary" not in content_type:
            boundary = _get_boundary(data)
            if boundary:
                content_type += f'; boundary={boundary}'
        
        headers = {'Content-Type': content_type}
        LOGGER.info(f"Headers for multipart parsing: {headers}")
        #headers = {'Content-Type': 'multipart/form-data; boundary=boundary'}
        parser = StreamingFormDataParser(headers=headers)
        for item in items:
            LOGGER.info(f"Registering item: {item['name']}")
            res[item["name"]] = BytesTarget()
            parser.register(item["name"], res[item["name"]])
        LOGGER.info("Starting data reception in parser")
        parser.data_received(data)
        
        for item in items:
            LOGGER.info(f"Extracting data for item: {item['name']}")
            if item["name"] in res and hasattr(res[item["name"]], 'data'):
                results[item["name"]] = res[item["name"]].data
            else:
                LOGGER.warning(f"No data found for item: {item['name']}")
        
        LOGGER.info(f"Finished decoding multipart data, results keys: {list(results.keys())}")
    except Exception as e:
        LOGGER.error(f"Exception in decode_multipart: {e}")
        return {}, ValueError(f"Error reading multi-part data: {e}")
    return results, None

def decode_audio(data: bytes):
    """
    Read audio
    Arguments:
    data: bytes
    """
    pass


def _get_boundary(data: bytes) -> str | None:
    """
    Get boundary from multipart data
    Arguments:
    data: bytes
    """
    splitted = data.split(b"\r\n")
    if len(splitted) < 2:
        return None
    boundary = splitted[0]
    if len(boundary) < 2:
        return None
    
    # Extract boundary after the '--' prefix
    boundary_bytes = boundary[2:]
    
    # RFC 2046 specifies boundaries should be ASCII, but we'll handle edge cases
    try:
        # First try UTF-8 decoding (most common case)
        return boundary_bytes.decode("utf-8")
    except UnicodeDecodeError:
        try:
            # Try latin-1 which can decode any byte sequence
            decoded = boundary_bytes.decode("latin-1")
            
            # For better safety, if the decoded boundary contains non-printable
            # or unusual characters, extract only printable ASCII part
            if any(ord(c) < 32 or ord(c) > 126 for c in decoded):
                # Extract only ASCII printable characters
                ascii_chars = ''.join(c for c in decoded if 32 <= ord(c) <= 126)
                if len(ascii_chars) >= 3:  # Minimum reasonable boundary length
                    return ascii_chars
                # If too short after filtering, return the original latin-1 decoded string
                # The multipart parser will handle validation
            return decoded
        except UnicodeDecodeError:
            # Should never happen with latin-1, but just in case
            # Extract only ASCII printable bytes
            ascii_bytes = bytes([b for b in boundary_bytes if 32 <= b <= 126])
            if len(ascii_bytes) >= 3:
                try:
                    return ascii_bytes.decode("ascii")
                except UnicodeDecodeError:
                    pass
            return None