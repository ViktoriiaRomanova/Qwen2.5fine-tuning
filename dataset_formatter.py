from json_repair import repair_json


SYSTEM_MESSAGE = """You are a Vision Language Model specialized in interpreting visual data from images.
Your task is to analyze the provided image and respond to queries with concise answers, usually a single word, number, or short phrase.
Focus on delivering accurate, succinct answers based on the visual information. Avoid additional explanation unless absolutely necessary."""


def format_data(sample):
    return {
        "images": [sample["images"][0]],
        "messages": [
            {
                "role": "system",
                "content": [{"type": "text", "text": SYSTEM_MESSAGE}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": sample["images"][0],
                    },
                    {
                        "type": "text",
                        "text": '1. How many watermarks on the picture? Short answer.\n 2. Extract all visible text content from this image. 3. Who or what on this picture? Short answer.\n 4. What artistic style is the whole picture?. Short answer.\n Return json style format: {{"watermarks": int, "text": str, "main object": str, "style": str}}',
                    },
                ],
            },
            {
                "role": "assistant",
                "content": [{"type": "text", "text": repair_json(sample["texts"][0]["assistant"])}],
            },
        ],
    }
