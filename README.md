# 🏦 Loan Eligibility Prediction System

> An intelligent Machine Learning application that automates loan approval decisions using historical data and Random Forest algorithm.

## 📖 What's This All About?

Ever wondered how banks decide whether to approve your loan? It's usually a pretty tedious process involving tons of paperwork and manual checks. This project takes that whole process and puts some smart AI behind it!

I built this Machine Learning application to help automate loan approval decisions. Think of it as a helpful assistant that looks at things like your income, credit history, and education, then predicts whether your loan would likely be approved or rejected. No more waiting around wondering!

The brain behind this system is a **Random Forest Classifier** - a fancy way of saying it's pretty accurate at making these predictions. And the best part? You can test it out yourself using a simple command-line interface. No complicated setup needed!

## ✨ Features

* **Lightning-Fast Predictions:** Get instant loan eligibility results instead of waiting days
* **Confidence Scores:** Not just a yes/no - you'll see how confident the model is about its decision
* **Smart Data Handling:** Missing information? No problem! The system fills in gaps intelligently using statistical methods
* **Easy to Use:** Just answer a few simple questions, and boom - you've got your prediction
* **Battle-Tested Algorithm:** Random Forest is known for handling real-world messy data really well

## 🛠️ Tech Stack

* **Language:** Python 3.13
* **Key Libraries:**
    * **Pandas** - For wrestling with all that data
    * **Scikit-learn** - The ML powerhouse making predictions happen
    * **Joblib** - Saves our trained model so we don't start from scratch every time
    * **Numpy** - Does all the math magic behind the scenes

## 📁 Project Structure

```text
Loan_Approval_System/
├── data
│   └── loan_data.csv        # Historical loan data we learn from
├── models                  # Where the trained AI model lives
├── src
│   ├── config.py           # Settings and file paths
│   ├── data_loader.py      # Grabs the data from CSV
│   ├── preprocessing.py    # Cleans up and prepares the data
│   ├── train.py            # Teaches the model to make predictions
│   └── inference.py        # Makes actual predictions on new data
├── app.py                  # Your main entry point - run this!
├── requirements.txt        # All the dependencies you need
└── README.md              # You're reading it! 👋
```

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Loan_Approval_System.git
cd Loan_Approval_System
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model 🧠

**Important!** Before you can make predictions, the model needs to learn from the data:

```bash
python src/train.py
```

You should see output like:
```
Loading data...
Preprocessing data...
Training model...
Model Accuracy: 0.XX
Model saved to models/loan_model.pkl
```

### 5. Run the Application 🎉

```bash
python app.py
```

Follow the prompts and enter the required information to get your loan eligibility prediction!

## 🧪 Testing the System

Here are some test scenarios to try:

### ✅ Scenario 1: The Dream Applicant (Likely Approval)
```
Income: 5000
Education: Graduate
Credit History: 1.0
Loan Amount: 150
Dependents: 0
```

### ❌ Scenario 2: Risky Applicant (Likely Rejection)
```
Income: 2000
Credit History: 0.0
Loan Amount: 500
Education: Not Graduate
```

### 💡 Pro Tips:
- **Don't know a value?** Just press Enter to use smart defaults
- **Watch the confidence score** - higher percentage means the model is more certain
- **Experiment!** Try different combinations to see what factors matter most

## 📊 Model Performance

The Random Forest Classifier achieves:
- High accuracy on test data
- Robust handling of missing values
- Good generalization to unseen data

## 🔧 Troubleshooting

**"Model not found" error?**  
→ Make sure you ran `python src/train.py` first!

**Import errors?**  
→ Check that all dependencies are installed: `pip install -r requirements.txt`

**Weird predictions?**  
→ Ensure `loan_data.csv` is in the `data` folder

## 📝 Usage Example

```bash
$ python app.py

=== Loan Eligibility Prediction System ===

Enter Applicant Income: 5000
Enter Coapplicant Income (or press Enter for 0): 1500
Enter Loan Amount: 150
Married? (Yes/No): Yes
Number of Dependents: 1
Education (Graduate/Not Graduate): Graduate
Self Employed? (Yes/No): No
Credit History (1.0 for good, 0.0 for bad): 1.0
Property Area (Urban/Semiurban/Rural): Urban

Prediction: ✅ Loan Approved!
Confidence: 85%
```

## ⚠️ Disclaimer

This is a learning project and demonstration tool. Real-world loan decisions involve many more factors, regulatory considerations, and human oversight. Always consult with actual financial professionals for real loan applications!

## 🤝 Contributing

Feel free to fork this project and submit pull requests! Whether it's:
- Bug fixes
- Feature additions
- Documentation improvements
- Test cases

All contributions are welcome! 🎉

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by Samarth Shah

---

**Happy predicting! 🎯** If you run into any issues or have questions, feel free to open an issue!

---

## AND HERE'S YOUR `requirements.txt`:

```txt
# Core Data Science Libraries
pandas>=2.0.0
numpy>=1.24.0

# Machine Learning
scikit-learn>=1.3.0

# Model Persistence
joblib>=1.3.0
```

---

## 📦 Quick Start Checklist

- [ ] Clone the repository
- [ ] Create virtual environment
- [ ] Install requirements: `pip install -r requirements.txt`
- [ ] Train the model: `python src/train.py`
- [ ] Run the app: `python app.py`
- [ ] Test with sample scenarios
- [ ] Star the repo if you found it useful! ⭐
