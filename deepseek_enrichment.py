import json
import os
import requests

def deepseek_analyze(dict_features: dict, chat_sample: str) -> dict:
    """Call DeepSeek and return JSON fields; return defaults on error."""
    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        return {
            "style_summary": None,
            "formality": None,
            "sentiment": None,
            "topics": None,
            "strengths": None,
            "suggestions": ["Missing DEEPSEEK_API_KEY"],
            "estimated_readability_grade": None,
        }

    url = os.environ.get(
        "DEEPSEEK_API_URL",
        "https://api.deepseek.com/v1/chat/completions",
    )
    headers = {"Authorization": f"Bearer {api_key}",
               "Content-Type": "application/json"}
    payload = {
        "model": os.environ.get("DEEPSEEK_MODEL", "deepseek-chat"),
        "messages": [
            {"role": "system",
             "content": ("Return compact JSON with keys: style_summary, "
                         "formality, sentiment, topics, strengths, "
                         "suggestions, estimated_readability_grade.")},
            {"role": "user",
             "content": (
                 f"CHAT (<=1200 chars): {(chat_sample or '')[:1200]}\n\n"
                 f"DICT FEATURES:\n{json.dumps(dict_features)}\n\n"
                 "Return ONLY JSON."
             )},
        ],
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
    }

    try:
        r = requests.post(url, json=payload, headers=headers, timeout=60)
        r.raise_for_status()
        content = r.json().get("choices", [{}])[0] \
                         .get("message", {}).get("content", "{}")
        parsed = json.loads(content)
        return {
            "style_summary": parsed.get("style_summary"),
            "formality": parsed.get("formality"),
            "sentiment": parsed.get("sentiment"),
            "topics": parsed.get("topics"),
            "strengths": parsed.get("strengths"),
            "suggestions": parsed.get("suggestions"),
            "estimated_readability_grade": parsed.get(
                "estimated_readability_grade"
            ),
        }
    except Exception as e:
        return {
            "style_summary": None,
            "formality": None,
            "sentiment": None,
            "topics": None,
            "strengths": None,
            "suggestions": [f"DeepSeek error: {str(e)[:160]}"],
            "estimated_readability_grade": None,
        }
