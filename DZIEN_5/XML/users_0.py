import pandas as pd
from xml.etree.ElementTree import ElementTree

tree = ElementTree()
tree.parse("users.xml")
root = tree.getroot()

rows = []
for user in root.findall("user"):
    rows.append({
        "id": user.get("id"),
        "name": user.findtext("name"),
        "email": user.findtext("email"),
        "city": user.findtext("city"),
        "role": user.findtext("role"),
        "age": int(user.findtext("age")) if user.find("age") is not None else None,
    })

df = pd.DataFrame(rows)
print(df.head())
