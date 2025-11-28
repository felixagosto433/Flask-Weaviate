from flask import Blueprint, jsonify, request
import os

bp = Blueprint("api", __name__)

@bp.get("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200

@bp.post("/chat")
def chat():
    """Simple echo endpoint that mimics chatbot behavior."""
    data = request.get_json(force=True, silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"error": "message is required"}), 400

    return jsonify({
        "answer": f"(stub) you said: {message}",
        "sources": [],
        "env": {"ENV": os.getenv("FLASK_ENV", "development")}
    }), 200