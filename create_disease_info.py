import pandas as pd

# Define the disease information based on your data
disease_data = [
    {
        "Disease": "Fungal infection",
        "Description": "Fungal infection is a common skin condition caused by fungi.",
        "Precautions": "bath twice, use detol or neem in bathing water, keep infected area dry, use clean cloths",
        "Medications": "Antifungal Cream, Fluconazole, Terbinafine, Clotrimazole, Ketoconazole",
        "Workouts": "Avoid sugary foods, Consume probiotics, Increase intake of garlic, Include yogurt in diet, Limit processed foods, Stay hydrated, Consume green tea, Eat foods rich in zinc, Include turmeric in diet, Eat fruits and vegetables",
        "Diet": "Antifungal Diet, Probiotics, Garlic, Coconut oil, Turmeric"
    },
    {
        "Disease": "Allergy",
        "Description": "Allergy is an immune system reaction to a substance in the environment.",
        "Precautions": "apply calamine, cover area with bandage, use ice to compress itching",
        "Medications": "Antihistamines, Decongestants, Epinephrine, Corticosteroids, Immunotherapy",
        "Workouts": "Avoid allergenic foods, Consume anti-inflammatory foods, Include omega-3 fatty acids, Stay hydrated, Eat foods rich in vitamin C, Include quercetin-rich foods, Consume local honey, Limit processed foods, Include ginger in diet, Avoid artificial additives",
        "Diet": "Elimination Diet, Omega-3-rich foods, Vitamin C-rich foods, Quercetin-rich foods, Probiotics"
    },
    {
        "Disease": "GERD",
        "Description": "GERD (Gastroesophageal Reflux Disease) is a digestive disorder that affects the lower esophageal sphincter.",
        "Precautions": "avoid fatty spicy food, avoid lying down after eating, maintain healthy weight, exercise",
        "Medications": "Proton Pump Inhibitors (PPIs), H2 Blockers, Antacids, Prokinetics, Antibiotics",
        "Workouts": "Consume smaller meals, Avoid trigger foods (spicy, fatty), Eat high-fiber foods, Limit caffeine and alcohol, Chew food thoroughly, Avoid late-night eating, Consume non-citrus fruits, Include lean proteins, Stay hydrated, Avoid carbonated beverages",
        "Diet": "Low-Acid Diet, Fiber-rich foods, Ginger, Licorice, Aloe vera juice"
    },
    # Add more diseases as needed from your dataset...
]

# Create DataFrame
df = pd.DataFrame(disease_data)

# Save to CSV
df.to_csv("disease_info.csv", index=False)
print("disease_info.csv created successfully!")