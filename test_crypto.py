import pytest
from encrypt_logic import core_encrypt_logic
from decrypt_logic import core_decrypt_logic

# Test Encryption Function
def test_encryption_generates_valid_output():
    message = "Hello World"
    key, ciphertext = core_encrypt_logic(message)
    
    # Assert that key and ciphertext are bytes (standard Fernet output)
    assert isinstance(key, bytes)
    assert isinstance(ciphertext, bytes)
    # Assert the message is not empty
    assert len(ciphertext) > 0

# 2. Test Decryption Function (The Happy Path)
def test_decryption_successful():
    message = "Secret Data"
    # Valid encrypted data to test decryption
    key, ciphertext = core_encrypt_logic(message)
    
    # Convert to string because our GUI passes strings
    key_str = key.decode()
    cipher_str = ciphertext.decode()
    
    # Run the core decryption logic
    success, result = core_decrypt_logic(key_str, cipher_str)
    
    # Assertions
    assert success is True
    assert result == "Secret Data"

# Test Regex and Error Handling ,The Fail Path
def test_decryption_validation_and_errors():
    # Case A: Invalid Key Format (Regex should catch this)
    bad_key = "This is not a key!!!" 
    cipher = "SomeData"
    
    success, error_msg = core_decrypt_logic(bad_key, cipher)
    assert success is False
    assert "Key format is invalid" in error_msg

    # Generate a random key that is valid format, but wrong for the data
    valid_format_key_wrong, _ = core_encrypt_logic("Dummy")
    valid_key_str = valid_format_key_wrong.decode()
    
    # Generate a ciphertext with a DIFFERENT key
    _, real_cipher = core_encrypt_logic("Real Message")
    real_cipher_str = real_cipher.decode()
    
    success_2, error_msg_2 = core_decrypt_logic(valid_key_str, real_cipher_str)
    
    # This should fail with Invalid Token (caught by try...except)
    assert success_2 is False
    assert "Invalid Token" in error_msg_2