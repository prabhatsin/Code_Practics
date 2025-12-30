# IMPROVEMENTS LEARNED
'''

1. Follow Python naming conventions

Function names should be snake_case.

❌ Encoding()
✅ encode_department()


2. Handle unseen categories (INTERVIEW GOLD 🥇)
df['Department_encoded'] = df['Department'].map(encoding).fillna(-1)

2. Return encoding dictionary too (interview bonus ⭐

'''

--------------------------------------------------------------------------------------------------
'''
When to use each encoder:


Encoder	           Use case
LabelEncoder	  Target variable (y)
OrdinalEncoder	  Ordered categorical features
OneHotEncoder	  Nominal categorical features
map()	          Full control, small datasets

'''

--------------------------------------------------------------------------------------------
# Encoding – Notes & Mistakes

## ❌ Common Mistakes
- Using LabelEncoder on input features (X)
- Assuming numeric order has meaning for nominal categories

## ✅ Best Practices
- Use map() for small, controlled datasets
- Use OneHotEncoder for nominal features
- Use OrdinalEncoder only when order exists

## Interview Tip
Explain why LabelEncoder is unsafe for X and give an example.
