import os
import pytest
from main import QRCodeGenerator
from qrcode import QRCode
from PIL import Image
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    """
    Reads the content of a QR Code from an image file.
    """
    decoded_data = decode(Image.open(image_path))
    if decoded_data:
        return decoded_data[0].data.decode("utf-8")
    raise ValueError("No QR Code found in the image.")

@pytest.fixture
def qr_generator():
    """Fixture to initialize QRCodeGenerator."""
    return QRCodeGenerator(save_path="images/test_qr_code.png")

def teardown_function():
    """Remove the QR Code file after each test."""
    if os.path.exists("test_qr_code.png"):
        os.remove("test_qr_code.png")
    if os.path.exists("custom_qr_code.png"):
        os.remove("custom_qr_code.png")

def test_generate_valid_data(qr_generator):
    # Test generating a QR Code with valid data
    result_path = qr_generator.generate("https://example.com")
    assert os.path.exists(result_path), "QR Code file was not created."

def test_generate_empty_data(qr_generator):
    # Test generating a QR Code with empty data
    with pytest.raises(ValueError, match="Data cannot be empty."):
        qr_generator.generate("")

def test_generate_custom_save_path():
    # Test saving the QR Code to a custom path
    custom_path = "custom_qr_code.png"
    generator = QRCodeGenerator(save_path=custom_path)
    result_path = generator.generate("Custom path test")
    assert os.path.exists(result_path)

def test_generated_qr_content(qr_generator):
    # Input data for the QR Code
    data = "https://example.com"

    # Generate QR Code
    result_path = qr_generator.generate(data)

    # Read the QR Code and verify its content
    read_data = read_qr_code(result_path)
    assert read_data == data, f"Expected QR content '{data}', got '{read_data}'"
