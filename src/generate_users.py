import pandas as pd
import random
from datetime import datetime, timedelta

# 🌍 20 REALISTIC FREELANCER NAMES
users = [
    ("Aarav Sharma", "Freelancer"),
    ("Sophia Brown", "Freelancer"),
    ("Liam Johnson", "Freelancer"),
    ("Emma Wilson", "Freelancer"),
    ("Noah Davis", "Freelancer"),
    ("Olivia Martinez", "Freelancer"),
    ("Ethan Taylor", "Freelancer"),
    ("Isabella Anderson", "Freelancer"),
    ("James Thomas", "Freelancer"),
    ("Mia White", "Freelancer"),
    ("Alexander Lee", "Freelancer"),
    ("Charlotte Harris", "Freelancer"),
    ("Benjamin Clark", "Freelancer"),
    ("Amelia Lewis", "Freelancer"),
    ("Daniel Walker", "Freelancer"),
    ("Harper Hall", "Freelancer"),
    ("Matthew Allen", "Freelancer"),
    ("Evelyn Young", "Freelancer"),
    ("Henry King", "Freelancer"),
    ("Grace Scott", "Freelancer")
]

categories = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Income"]

data = []

for _ in range(1500):
    user_id, user_type = random.choice(users)

    date = datetime.now() - timedelta(days=random.randint(0, 120))
    category = random.choice(categories)

    amount = round(random.uniform(200, 8000), 2)

    if category == "Income":
        amount = abs(amount)
    else:
        amount = -abs(amount)

    payment = random.choice(["UPI", "Card", "Cash"])

    data.append([user_id, user_type, date, category, amount, payment])

df = pd.DataFrame(data, columns=[
    "user_id", "user_type", "date", "category", "amount", "payment"
])

df.to_csv("data/multi_user_expenses.csv", index=False)

print("✅ Dataset created with realistic freelancer names!")