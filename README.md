# ☕ CafePulse — Cafe Revenue Prediction App

CafePulse is a simple Machine Learning web application that predicts **daily cafe revenue** based on key business inputs.  
The project focuses on understanding how real-world operational factors translate into revenue predictions using ML.

## Project Overview

CafePulse takes inputs such as:
- Expected customer footfall  
- Average order value  
- Staff count  
- Opening hours  
- Weekend vs weekday  
- Offers running  
- Weather conditions  

and predicts the **estimated daily revenue** using a **Decision Tree Regressor**.

The app is built with **Streamlit** for interactive inference and visualization.

##  Model Details
- **Algorithm:** Decision Tree Regressor  
- **Why Decision Tree?**
  - Handles non-linear relationships  
  - Easy to interpret  
  - Suitable for business-driven decision logic  

##  The Process
- Designed business-driven input features  
- Performed preprocessing and feature encoding  
- Trained and tuned the Decision Tree model  
- Debugged issues where predictions stayed constant due to feature mismatch  
- Fixed alignment between training and inference pipelines  
- Built a clean two-screen Streamlit app:
  - Input screen
  - Result & visualization screen  

##  Key Learning
A model producing outputs doesn’t always mean it’s working correctly.  
Most real issues appear **after deployment**, especially when preprocessing and feature alignment are incorrect.

This project helped me understand how ML behaves in **real-world applications**, not just notebooks.

##  Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Matplotlib  

---

##  Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/tanishaasaklani/CafePulse.git
   cd CafePulse
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the app:
   ```bash
   streamlit run app.py
