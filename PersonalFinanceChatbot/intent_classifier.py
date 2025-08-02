def classify_intent(query):
    query = query.lower()
    if any(keyword in query for keyword in ["save", "savings", "how to save"]):
        return "General Advice"
    elif any(keyword in query for keyword in ["invest", "investment", "portfolio"]):
        return "Investment Advice"
    elif any(keyword in query for keyword in ["budget", "track expenses", "spending"]):
        return "Budgeting Advice"
    else:
        return "General Advice"
