from boofuzz import *
import time

def main():
    session = Session(
        target=Target(connection=TCPSocketConnection("127.0.0.1", 5000))
    )

    s_initialize("PaymentRequest")
    with s_block("Request"):
        s_static("POST /pay HTTP/1.1\r\n")
        s_static("Host: localhost:5000\r\n")
        s_static("Content-Type: application/json\r\n")
        s_static("Content-Length: ")
        s_size("Body", output_format="ascii", fuzzable=False)
        s_static("\r\n\r\n")
        s_string('{"account":"user123","amount":100}', name="Body")

    session.connect(s_get("PaymentRequest"))
    session.fuzz()

if __name__ == "__main__":
    main()
