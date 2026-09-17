def format_status(status):
    status = status.lower()

    if status == "active":
        return "🟢 Active"

    if status == "banned":
        return "🔴 Banned"

    
