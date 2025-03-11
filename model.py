# List of symptoms for the analyzer (defined at module level for import)
symptom_list = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 
    'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 
    'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain', 
    'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
    'headache', 'dizziness', 'cough', 'sore_throat', 'runny_nose', 'fever', 'body_aches', 
    'nausea', 'diarrhea', 'chest_pain', 'shortness_of_breath', 'swelling', 'bruising', 
    'bleeding_gums', 'vision_problems', 'hearing_loss', 'memory_loss', 'sleep_disturbances'
]

def predict_disease(symptoms):
    """
    Predict a disease and provide recommendations based on selected symptoms.
    This is a rule-based system; replace with ML model or more complex logic if needed.
    """
    symptom_set = set(symptoms)  # Convert to set for easier checking
    
    # Define symptom-to-disease mappings for all symptoms
    disease_mappings = {
        # Fungal Infection (itching, skin_rash, nodal_skin_eruptions)
        frozenset(['itching', 'skin_rash', 'nodal_skin_eruptions']): {
            'disease': 'Fungal Infection',
            'description': 'Fungal infection is a common skin condition caused by fungi, often appearing as itching, rashes, or eruptions.',
            'recommendations': {
                'General': ['Bath twice daily', 'Use detol or neem in bathing water', 'Keep infected area dry', 'Use clean, breathable cloths'],
                'Medications': ['Antifungal Cream (e.g., Clotrimazole)', 'Terbinafine', 'Ketoconazole', 'Miconazole'],
                'Workouts': ['Avoid sugary foods', 'Consume probiotic foods', 'Increase intake of green tea', 'Include yogurt in diet', 
                            'Limit processed foods', 'Stay hydrated', 'Eat foods rich in zinc', 'Include turmeric in diet', 'Eat fruits and vegetables']
            }
        },
        # Common Cold (continuous_sneezing, shivering, chills, runny_nose, cough, sore_throat)
        frozenset(['continuous_sneezing', 'shivering', 'chills', 'runny_nose', 'cough', 'sore_throat']): {
            'disease': 'Common Cold',
            'description': 'Common cold is a viral infection of the upper respiratory tract, causing sneezing, chills, and congestion.',
            'recommendations': {
                'General': ['Rest adequately', 'Stay hydrated with water and clear fluids', 'Use a humidifier', 'Avoid close contact with others'],
                'Medications': ['Over-the-counter cold medicine', 'Decongestants', 'Antihistamines', 'Cough suppressants'],
                'Workouts': ['Light exercise if feeling well', 'Avoid strenuous activity', 'Eat nutrient-rich foods like citrus fruits']
            }
        },
        # Arthritis (joint_pain, muscle_wasting, swelling)
        frozenset(['joint_pain', 'muscle_wasting', 'swelling']): {
            'disease': 'Arthritis',
            'description': 'Arthritis is inflammation of one or more joints, causing pain, stiffness, and swelling.',
            'recommendations': {
                'General': ['Apply warm compresses', 'Avoid overexertion', 'Maintain a healthy weight', 'Use supportive devices like braces'],
                'Medications': ['Nonsteroidal anti-inflammatory drugs (NSAIDs)', 'Acetaminophen', 'Corticosteroids', 'DMARDs'],
                'Workouts': ['Low-impact exercises like swimming', 'Physical therapy', 'Strength training for joints', 'Tai Chi']
            }
        },
        # Acid Reflux (acidity, stomach_pain, nausea)
        frozenset(['acidity', 'stomach_pain', 'nausea']): {
            'disease': 'Acid Reflux',
            'description': 'Acid reflux is a condition where stomach acid flows back into the esophagus, causing heartburn and nausea.',
            'recommendations': {
                'General': ['Eat smaller, more frequent meals', 'Avoid lying down after eating', 'Elevate the head of your bed', 'Avoid spicy or fatty foods'],
                'Medications': ['Antacids', 'H2 blockers (e.g., Ranitidine)', 'Proton pump inhibitors (e.g., Omeprazole)'],
                'Workouts': ['Light exercise after meals', 'Avoid heavy lifting', 'Maintain a healthy weight', 'Yoga for digestion']
            }
        },
        # Oral Ulcers (ulcers_on_tongue, stomach_pain, nausea)
        frozenset(['ulcers_on_tongue', 'stomach_pain', 'nausea']): {
            'disease': 'Oral Ulcers',
            'description': 'Oral ulcers are painful sores in the mouth, often caused by stress, dietary issues, or infections.',
            'recommendations': {
                'General': ['Maintain good oral hygiene', 'Avoid spicy or acidic foods', 'Stay hydrated', 'Use a soft toothbrush', 'Reduce stress'],
                'Medications': ['Topical anesthetics (e.g., Benzocaine)', 'Antiseptic mouthwashes', 'Corticosteroid gels', 'Vitamin B supplements'],
                'Workouts': ['Light exercise to reduce stress', 'Yoga or meditation', 'Balanced diet rich in vitamins']
            }
        },
        # Gastroenteritis (vomiting, stomach_pain, diarrhea, nausea)
        frozenset(['vomiting', 'stomach_pain', 'diarrhea', 'nausea']): {
            'disease': 'Gastroenteritis',
            'description': 'Gastroenteritis is inflammation of the stomach and intestines, often due to viral or bacterial infection, causing vomiting and diarrhea.',
            'recommendations': {
                'General': ['Stay hydrated with clear fluids', 'Rest adequately', 'Avoid solid foods initially', 'Wash hands frequently', 'Avoid contaminated food/water'],
                'Medications': ['Antidiarrheal medicine (e.g., Loperamide)', 'Antinausea drugs (e.g., Ondansetron)', 'Electrolyte solutions'],
                'Workouts': ['Avoid exercise until recovery', 'Light walking when feeling better', 'Eat bland foods like rice and bananas']
            }
        },
        # Urinary Tract Infection (burning_micturition, spotting_urination, fever)
        frozenset(['burning_micturition', 'spotting_urination', 'fever']): {
            'disease': 'Urinary Tract Infection',
            'description': 'A UTI is an infection in any part of the urinary system, causing pain, frequent urination, and fever.',
            'recommendations': {
                'General': ['Drink plenty of water', 'Avoid caffeine and alcohol', 'Urinate frequently', 'Wipe front to back', 'Avoid holding urine'],
                'Medications': ['Antibiotics (e.g., Trimethoprim, Nitrofurantoin)', 'Pain relievers (e.g., Phenazopyridine)'],
                'Workouts': ['Light exercise, avoid strenuous activity', 'Stay hydrated during exercise', 'Maintain hygiene']
            }
        },
        # Chronic Fatigue Syndrome (fatigue, anxiety, sleep_disturbances)
        frozenset(['fatigue', 'anxiety', 'sleep_disturbances']): {
            'disease': 'Chronic Fatigue Syndrome',
            'description': 'Chronic fatigue syndrome is a long-term illness causing extreme tiredness, anxiety, and sleep issues.',
            'recommendations': {
                'General': ['Get regular sleep', 'Manage stress with relaxation techniques', 'Avoid overexertion', 'Maintain a routine', 'Consult a specialist'],
                'Medications': ['Antidepressants', 'Sleep aids (e.g., Melatonin)', 'Pain relievers'],
                'Workouts': ['Gentle exercises like yoga', 'Pacing activities', 'Avoid overtraining', 'Tai Chi']
            }
        },
        # Hypothyroidism (weight_gain, cold_hands_and_feets, fatigue)
        frozenset(['weight_gain', 'cold_hands_and_feets', 'fatigue']): {
            'disease': 'Hypothyroidism',
            'description': 'Hypothyroidism is an underactive thyroid gland, causing weight gain, cold intolerance, and fatigue.',
            'recommendations': {
                'General': ['Eat a balanced diet', 'Avoid goitrogens (e.g., soy, cruciferous veggies)', 'Regular medical checkups', 'Stay warm', 'Monitor thyroid levels'],
                'Medications': ['Levothyroxine', 'Thyroid hormone replacement'],
                'Workouts': ['Moderate exercise like walking', 'Strength training', 'Avoid extreme cold', 'Yoga for energy']
            }
        },
        # Depression (mood_swings, anxiety, sleep_disturbances)
        frozenset(['mood_swings', 'anxiety', 'sleep_disturbances']): {
            'disease': 'Depression',
            'description': 'Depression is a mood disorder causing persistent sadness, anxiety, and sleep disturbances.',
            'recommendations': {
                'General': ['Seek therapy or counseling', 'Maintain a support system', 'Practice mindfulness', 'Get sunlight exposure', 'Establish a routine'],
                'Medications': ['Antidepressants (e.g., SSRIs)', 'Anxiolytics'],
                'Workouts': ['Regular exercise (e.g., jogging)', 'Yoga or meditation', 'Group activities', 'Outdoor walks']
            }
        },
        # Anorexia (weight_loss, fatigue, dizziness)
        frozenset(['weight_loss', 'fatigue', 'dizziness']): {
            'disease': 'Anorexia',
            'description': 'Anorexia is an eating disorder causing significant weight loss, fatigue, and dizziness due to malnutrition.',
            'recommendations': {
                'General': ['Seek professional help (e.g., therapist, nutritionist)', 'Nutritional counseling', 'Monitor weight regularly', 'Avoid triggers', 'Build a support network'],
                'Medications': ['Antidepressants', 'Nutritional supplements (e.g., vitamins, minerals)'],
                'Workouts': ['Light exercise under supervision', 'Avoid overexercise', 'Focus on recovery', 'Gentle stretching']
            }
        },
        # Restless Legs Syndrome (restlessness, anxiety, sleep_disturbances)
        frozenset(['restlessness', 'anxiety', 'sleep_disturbances']): {
            'disease': 'Restless Legs Syndrome',
            'description': 'Restless legs syndrome causes an urge to move the legs, often with anxiety and sleep disturbances.',
            'recommendations': {
                'General': ['Establish a regular sleep schedule', 'Avoid caffeine and alcohol', 'Massage legs', 'Stretch before bed', 'Keep legs warm'],
                'Medications': ['Dopamine agonists (e.g., Pramipexole)', 'Iron supplements (if deficient)', 'Anticonvulsants (e.g., Gabapentin)'],
                'Workouts': ['Light stretching exercises', 'Yoga', 'Avoid intense workouts before bed', 'Leg exercises during the day']
            }
        },
        # Migraine (headache, nausea, dizziness)
        frozenset(['headache', 'nausea', 'dizziness']): {
            'disease': 'Migraine',
            'description': 'Migraine is a neurological condition causing severe headaches, nausea, and dizziness.',
            'recommendations': {
                'General': ['Rest in a quiet, dark room', 'Stay hydrated', 'Avoid triggers (e.g., stress, bright lights)', 'Keep a migraine diary'],
                'Medications': ['Triptans', 'Pain relievers (e.g., Ibuprofen)', 'Anti-nausea drugs'],
                'Workouts': ['Light exercise (e.g., walking)', 'Yoga or meditation for stress relief', 'Avoid intense activity during attacks']
            }
        },
        # Influenza (fever, body_aches, cough, sore_throat)
        frozenset(['fever', 'body_aches', 'cough', 'sore_throat']): {
            'disease': 'Influenza',
            'description': 'Influenza is a viral infection causing fever, body aches, cough, and sore throat.',
            'recommendations': {
                'General': ['Rest adequately', 'Stay hydrated', 'Use a humidifier', 'Get vaccinated annually', 'Avoid close contact'],
                'Medications': ['Antiviral drugs (e.g., Oseltamivir)', 'Fever reducers (e.g., Acetaminophen)', 'Cough suppressants'],
                'Workouts': ['Avoid exercise until recovery', 'Light walking when feeling better', 'Eat nutrient-rich foods']
            }
        },
        # Pneumonia (chest_pain, shortness_of_breath, fever, cough)
        frozenset(['chest_pain', 'shortness_of_breath', 'fever', 'cough']): {
            'disease': 'Pneumonia',
            'description': 'Pneumonia is an infection causing inflammation in the lungs, leading to chest pain, shortness of breath, and fever.',
            'recommendations': {
                'General': ['Seek immediate medical attention', 'Rest adequately', 'Stay hydrated', 'Avoid smoking', 'Elevate head while resting'],
                'Medications': ['Antibiotics (e.g., Amoxicillin)', 'Antiviral drugs if viral', 'Fever reducers'],
                'Workouts': ['Avoid exercise until fully recovered', 'Light breathing exercises under supervision', 'Gradual activity resumption']
            }
        },
        # Anemia (fatigue, dizziness, shortness_of_breath)
        frozenset(['fatigue', 'dizziness', 'shortness_of_breath']): {
            'disease': 'Anemia',
            'description': 'Anemia is a condition with low red blood cell count, causing fatigue, dizziness, and shortness of breath.',
            'recommendations': {
                'General': ['Eat iron-rich foods (e.g., spinach, red meat)', 'Take vitamin supplements', 'Regular blood tests', 'Avoid caffeine with iron intake'],
                'Medications': ['Iron supplements', 'Vitamin B12 or folate if deficient', 'Erythropoietin (in severe cases)'],
                'Workouts': ['Light exercise (e.g., walking)', 'Avoid overexertion', 'Gradual increase in activity']
            }
        },
        # Diabetes (weight_loss, fatigue, spotting_urination, frequent_thirst)
        frozenset(['weight_loss', 'fatigue', 'spotting_urination']): {  # Using 'spotting_urination' as proxy for frequent urination
            'disease': 'Diabetes',
            'description': 'Diabetes is a chronic condition affecting blood sugar levels, causing weight loss, fatigue, and frequent urination.',
            'recommendations': {
                'General': ['Monitor blood sugar regularly', 'Follow a balanced diet', 'Exercise regularly', 'Regular checkups with a doctor'],
                'Medications': ['Insulin', 'Metformin', 'Other oral diabetes medications'],
                'Workouts': ['Moderate exercise (e.g., walking, swimming)', 'Strength training', 'Avoid extreme activities']
            }
        },
        # Default case if no specific match
        frozenset(): {
            'disease': None,
            'description': 'No specific disease identified. Please try again or consult a doctor.',
            'recommendations': {
                'General': ['Please consult a healthcare professional for accurate diagnosis', 'Monitor symptoms closely'],
                'Medications': [],
                'Workouts': []
            }
        }
    }

    # Check for matching symptom combinations
    for symptom_combo, data in disease_mappings.items():
        if symptom_set.issubset(symptom_combo):
            return {
                'disease': data['disease'],
                'description': data['description'],
                'recommendations': data['recommendations']
            }

    # If no exact match, try partial matches or return a generic response
    for symptom_combo, data in disease_mappings.items():
        if symptom_set & symptom_combo:  # Check for any overlapping symptoms
            return {
                'disease': data['disease'],
                'description': data['description'],
                'recommendations': data['recommendations']
            }

    # If no partial match, return default response
    return {
        'disease': None,
        'description': 'No specific disease identified based on the selected symptoms. Please consult a healthcare professional for an accurate diagnosis.',
        'recommendations': {
            'General': ['Please consult a healthcare professional for accurate diagnosis', 'Monitor symptoms closely'],
            'Medications': [],
            'Workouts': []
        }
    }