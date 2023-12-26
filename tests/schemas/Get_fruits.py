valid_schema = {
    "type": "array",
    "properties": {
        "name": {"type": "string"},
        "id": {"type": "number"},
        "family": {"type": "string"},
        "order": {"type": "string"},
        "genus": {"type": "string"},
        "nutritions": {
            "type": "object",
            "properties": {
                "calories": {"type": "number"},
                "fat": {"type": "number"},
                "sugar": {"type": "number"},
                "carbohydrates": {"type": "number"},
                "protein": {"type": "number"}
            }
        }
    }
}

valid_schema_404 = {
    "error": {"type": "string"}
}
