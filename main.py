import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6IQVNRI_LlnHNFhr1HcOCo4okVXv73I6xH-ZDqe8cH07A")

def analyze_budget(income, expenses, goals):
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"""
    You are PocketSmart AI, a smart budget and financial recommendation assistant.
    Analyze the following financial details:
    - Monthly Income: ₹{income}
    - Total Monthly Expenses: ₹{expenses}
    - Financial Goal / Notes: {goals}

    Provide a clear and structured response containing:
    1. Income vs Expense Breakdown & Savings Potential
    2. 3-4 Practical Smart Money-Saving Recommendations
    3. Expense Optimization Advice based on their goal
    """
    
    print("Analyzing budget and generating recommendations...\n")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("=== PocketSmart AI: Smart Budget Assistant ===")
    income = input("Enter Monthly Income (in Rs): ")
    expenses = input("Enter Monthly Expenses (in Rs): ")
    goals = input("Enter your financial goal: ")
    
    result = analyze_budget(income, expenses, goals)
    print("\n=== SMART BUDGET ANALYSIS ===\n")
    print(result)
