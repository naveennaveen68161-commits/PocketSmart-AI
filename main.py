import google.generativeai as genai
API_KEY = "AQ.Ab8RN6J6mpOzh5g_P_-WOfhb3uUzblVRM3YXbHRWuBGsgXOSMg"

genai.configure(api_key=API_KEY)

def analyze_budget(income, expenses, goals):
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"""
    You are PocketSmart AI, a smart budget and financial recommendation assistant.
    Analyze the following financial details:
    - Monthly Income: Rs.{income}
    - Total Monthly Expenses: Rs.{expenses}
    - Financial Goal / Notes: {goals}

    Provide a clear and structured response containing:
    1. Income vs Expense Breakdown & Savings Potential
    2. 3-4 Practical Smart Money-Saving Recommendations
    3. Expense Optimization Advice based on their goal
    """
    
    print("\nAnalyzing budget and generating recommendations...\n")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("==================================================")
    print("   PocketSmart AI: Smart Budget Assistant   ")
    print("==================================================\n")
    
    income = input("Enter Monthly Income (in Rs): ")
    expenses = input("Enter Monthly Expenses (in Rs): ")
    goals = input("Enter your financial goal: ")
    
    try:
        result = analyze_budget(income, expenses, goals)
        print("==================================================")
        print("           SMART BUDGET ANALYSIS                  ")
        print("==================================================\n")
        print(result)
        print("\n==================================================")
    except Exception as e:
        print("\nError occurred:", e)
        print("Check your API Key! It must start with 'AIzaSy...'")
