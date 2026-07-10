import socket

import uvicorn

from backend.main import app


def _get_free_port(host: str = "127.0.0.1", start_port: int = 8000) -> int:
    port = start_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
                return port
            except OSError:
                port += 1


def main() -> None:
    port = _get_free_port()
    print(f"Starting Multi-Agent SOC on http://127.0.0.1:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port)


if __name__ == "__main__":
    main()
