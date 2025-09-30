def hello_world(name: str = "world") -> str:
    """返回一个问候字符串。"""
    return f"Hello, {name}!"


def tour_plan(place: str = "BEIJING") -> dict:
    if place.upper() == "BEIJING":
        return {place: "这是中国的首都！"}
    return {place: "这 不 是中国的首都！"}
