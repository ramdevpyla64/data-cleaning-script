# 🧹 Data Cleaning Script

A simple Python script that cleans user and page data from a JSON file by removing invalid entries, duplicate friends, and duplicate pages.

---

## 📄 Overview

This project processes a JSON dataset containing users and pages.
It performs the following cleaning steps:

* Removes users with empty names.
* Removes duplicate friend IDs for each user.
* Removes users who have neither friends nor liked pages.
* Removes duplicate pages based on their `id`.
* Saves the cleaned data into a new JSON file.

---

## 🧠 Example Input (`data.json`)

```json
{
    "users": [
        {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
        {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [101]},
        {"id": 3, "name": "", "friends": [1], "liked_pages": [101, 103]},
        {"id": 4, "name": "Sara", "friends": [2, 2], "liked_pages": [104]},
        {"id": 5, "name": "Amit", "friends": [], "liked_pages": []}
    ],
    "pages": [
        {"id": 101, "name": "Python developers"},
        {"id": 102, "name": "Data science Enthusiasts"},
        {"id": 103, "name": "AI & ML community"},
        {"id": 104, "name": "Web Dev Hub"},
        {"id": 104, "name": "Web development"}
    ]
}
```

---

## ⚙️ How It Works

```python
import json

def clean_data(data):
    data["users"] = [user for user in data["users"] if user["name"].strip()]
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))
    data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]
    unique = {}
    for page in data["pages"]:
        unique[page["id"]] = page
    data["pages"] = list(unique.values())
    return data

data = json.load(open("data.json"))
data = clean_data(data)
json.dump(data, open("cleaned_data1.json", "w"), indent=4)
print("Data cleaned successfully!")
```

---

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.

2. Save your input data as `data.json` in the same folder as the script.

3. Run the script:

   ```bash
   python clean_data.py
   ```

4. A new file named `cleaned_data1.json` will be created with the cleaned output.

---

## 🧾 Output Example

```json
{
    "users": [
        {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
        {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [101]},
        {"id": 4, "name": "Sara", "friends": [2], "liked_pages": [104]}
    ],
    "pages": [
        {"id": 101, "name": "Python developers"},
        {"id": 102, "name": "Data science Enthusiasts"},
        {"id": 103, "name": "AI & ML community"},
        {"id": 104, "name": "Web Dev Hub"}
    ]
}
```

---

## 💡 Author

**Ramdev Pyla**
📍 Visakhapatnam, Andhra Pradesh
🔗 [GitHub Profile](https://github.com/ramdevpyla64)
