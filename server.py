"""HTTP server for my app."""

from config import get_config

def start_server():
    config = get_config()
    print(f"Starting server on {config['host']}:{config['port']}")

if __name__ == "__main__":
    start_server()

ROUTES = {
    "/": "home",
    "/health": "health_check",
}

def handle_request(path):
    return ROUTES.get(path, "not_found")
