import tkinter as tk
from tkinter import ttk, messagebox

# Optional: If using pandas for data handling
# import pandas as pd

class MealPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meal Planner App")
        
        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack(padx=10, pady=10)
        self.welcome_frame.config(bg='#2c3e50')
        # Dietary preferences
        tk.Label(self.welcome_frame, text="Dietary Preferences:",bg='#2c3e50',fg='white',font=('times',15,)).grid(row=0, column=0, sticky='w')
        self.dietary_pref = tk.Entry(self.welcome_frame, width=50)
        self.dietary_pref.grid(row=0, column=1, padx=10, pady=15)

        # Allergies/Restrictions
        tk.Label(self.welcome_frame, text="Allergies/Restrictions:",bg='#2c3e50',fg='white',font=('times',15,)).grid(row=1, column=0, sticky='w')
        self.allergies = tk.Entry(self.welcome_frame, width=50)
        self.allergies.grid(row=1, column=1, padx=10, pady=15)

        # Available ingredients
        tk.Label(self.welcome_frame, text="Available Ingredients:",bg='#2c3e50',fg='white',font=('times',15,)).grid(row=2, column=0, sticky='w')
        self.ingredients = tk.Entry(self.welcome_frame, width=50)
        self.ingredients.grid(row=2, column=1, padx=10, pady=15)

        # Next button
        self.next_button = ttk.Button(self.welcome_frame, text="Next", command=self.show_meal_plan)
        self.next_button.grid(row=3, columnspan=2, pady=10)

    def show_meal_plan(self):
        # Collect user inputs
        self.dietary_pref_value = self.dietary_pref.get()
        self.allergies_value = self.allergies.get()
        self.ingredients_value = self.ingredients.get()

        # Implement backend logic to generate meal plan
        self.meal_plan = self.generate_meal_plan()

        # Destroy welcome frame and show meal plan
        self.welcome_frame.destroy()
        self.create_meal_plan_screen()

    def generate_meal_plan(self):
        # Placeholder logic for generating meal plan
        return [
            {"meal": "Salad", "ingredients": "Lettuce, Tomato, Cucumber"},
            {"meal": "Dosa", "ingredients": "Dosa Batter, oil, Chutney"},
            {"meal": "Sambar", "ingredients": "Tomato, dhal, Sambar Powder"},
            {"meal": "Pasta", "ingredients": "Pasta, Tomato Sauce, Cheese"},
            {"meal": "Veg-Briyani", "ingredients": "Rice, vegetables, chilli powder, oil, pudina"},
            {"meal": "Sandwidch", "ingredients": "Bread, Tomato Sauce, Cheese"},
            {"meal": "French Fries", "ingredients": "Potatoes, Sauce, Oil"},
            # Add more meals for the rest of the week
        ]

    def create_meal_plan_screen(self):
        self.meal_plan_frame = tk.Frame(self.root)
        self.meal_plan_frame.pack(padx=10, pady=10)

        tk.Label(self.meal_plan_frame, text="Weekly Meal Plan").pack()

        for day, meal in enumerate(self.meal_plan):
            tk.Label(self.meal_plan_frame, text=f"Day {day + 1}: {meal['meal']} - {meal['ingredients']}").pack()



        # image = PhotoImage(file="")











        self.back_button = ttk.Button(self.meal_plan_frame, text="Back", command=self.back_to_welcome)
        self.back_button.pack(pady=10)

    def back_to_welcome(self):
        self.meal_plan_frame.destroy()
        self.create_welcome_screen()


if __name__ == "__main__":
    root = tk.Tk()
    app = MealPlannerApp(root)
    root.geometry('500x500+450+50')
    root.config(bg='#2c3e50')
    root.mainloop()
