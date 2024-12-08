import qrcode

class QRCodeGenerator:
    def __init__(self, save_path="output.png"):
        self.save_path = save_path

    def generate(self, data):
        """
        Generates a QR Code from the given data and saves it to the specified path.
        """
        if not data:
            raise ValueError("Data cannot be empty.")

        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        img.save(self.save_path)
        return self.save_path

if __name__ == "__main__":
    qr_generator = QRCodeGenerator("images/output.png")
    qr_path = qr_generator.generate("Hello, World!")
    print(f"QR Code saved to: {qr_path}")
