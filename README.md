# 🍽️ Food Orders Data Analysis (Core Python)

## 📌 About the Project
This project performs **data cleaning and analysis** on food delivery order data using **Core Python only**.  
The main goal is to understand how raw, messy data can be cleaned and analyzed to extract useful business insights.

No external libraries such as **pandas, NumPy, or matplotlib** are used.

---

## 📂 Dataset
The dataset is stored in a JSON file:  


Each order contains:
- `order_id`
- `date`
- `restaurant`
- `item`
- `category`
- `price`
- `quantity`
- `payment_mode`
- `customer_city`
- `delivery_time_min`

The dataset intentionally includes inconsistencies to simulate real-world data.

---

## 🧹 Data Cleaning
The following data cleaning steps were implemented:

- Removed duplicate records using `order_id`
- Standardized payment modes (`UPI`, `CARD`, `CASH`)
- Removed extra spaces from restaurant names
- Converted price values from string to integer
- Removed records with invalid quantity values (≤ 0)

The cleaned dataset is saved as:



---

## 📊 Analysis Performed
After cleaning the data, the following analyses were carried out:

- Total sales calculation
- Sales distribution by city
- Most frequently used payment mode
- Average delivery time
- Top restaurant based on revenue

All analysis was done using **basic Python loops and dictionaries**.

---

## 📈 Key Insights
- UPI is the most commonly used payment method
- Pune generates the highest revenue among all cities
- Fast food orders generally have lower delivery times
- Certain restaurants contribute significantly more to total revenue

---

## 🛠️ Built With
- Python (Core Python)
- JSON

---

## 🚀 How to Run
1. Clone the repository
2. Place `food_orders.json` in the project directory
3. Run the data cleaning script
4. Execute the analysis script
5. View results in the terminal

---

## 🎯 Learning Outcomes
- Practical experience with data cleaning
- Understanding real-world data issues
- Strengthened core Python logic
- Business insight generation from raw data

---

## 🔮 Future Improvements
- Use pandas for optimized data processing
- Add visualizations using matplotlib
- Perform deeper city-wise and restaurant-wise analysis
- Export results to CSV

---

## 👩‍💻 Author
**Bhakti Jagtap**  
Computer Engineering & Data Science Student

---

## ⭐ Acknowledgement
This project was created to strengthen foundational data analysis skills using core Python before transitioning to advanced libraries.
