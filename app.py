# Main entrypoint for local development.
from app import app

if __name__ == "__main__":
    print("🚀 Starting Flask dev server on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)