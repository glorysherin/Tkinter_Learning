import tkinter as tk
from tkinter import ttk


class MealPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('trymeal/icon.ico')
        self.root.title("Weekly Meal Planner App")
        
        tk.Label(root, text='Welcome to Weekly Meal Planner App!!', bg='#2c3e50', fg='white', font=('courier', 30, 'italic', 'bold')).pack()

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack(padx=10, pady=10)
        self.welcome_frame.config(bg='#2c3e50')

        tk.Label(self.welcome_frame, text="Dietary Preferences:", bg='#2c3e50', fg='white', font=('times', 15)).grid(row=0, column=0, sticky='w')
        self.dietary_pref = tk.Entry(self.welcome_frame, width=50)
        
        self.dietary_pref.grid(row=0, column=1, padx=10, pady=15)

        tk.Label(self.welcome_frame, text="Allergies/Restrictions:", bg='#2c3e50', fg='white', font=('times', 15)).grid(row=1, column=0, sticky='w')
        self.allergies = tk.Entry(self.welcome_frame, width=50)
        self.allergies.grid(row=1, column=1, padx=10, pady=15)

        tk.Label(self.welcome_frame, text="Available Ingredients:", bg='#2c3e50', fg='white', font=('times', 15)).grid(row=2, column=0, sticky='w')
        self.ingredients = tk.Entry(self.welcome_frame, width=50)
        self.ingredients.grid(row=2, column=1, padx=10, pady=15)

        self.next_button = tk.Button(self.welcome_frame, text="Find Recipes", bg='#82ccdd', fg='#0a3d62', padx=15, pady=2, font=('times', 12, 'bold'), activebackground='black', activeforeground='white', command=self.show_meal_plan)
        self.next_button.grid(row=3, columnspan=2, pady=10)

    def show_meal_plan(self):
        self.dietary_pref_value = self.dietary_pref.get()
        self.allergies_value = self.allergies.get()
        self.ingredients_value = self.ingredients.get()

        self.meal_plan = self.generate_meal_plan()

        self.welcome_frame.destroy()
        self.create_meal_plan_screen()

    def generate_meal_plan(self):
        return [
            {"meal": "Salad", "ingredients": "Lettuce, Tomato, Cucumber", "recipe": "Chop lettuce, tomato, cucumber. Mix and serve."},
            {"meal": "Dosa", "ingredients": "Dosa Batter, oil, Chutney", "recipe": "Spread batter on hot pan. Cook until golden. Serve with chutney."},
            {"meal": "Sambar", "ingredients": "Tomato, dhal, Sambar Powder", "recipe": "Cook dhal with tomato and sambar powder. Serve hot."},
            {"meal": "Pasta", "ingredients": "Pasta, Tomato Sauce, Cheese", "recipe": "Boil pasta. Mix with sauce and cheese. Serve hot."},
            {"meal": "Veg-Biryani", "ingredients": "Rice, vegetables, chilli powder, oil, pudina", "recipe": "Cook rice with vegetables and spices. Serve hot."},
            {"meal": "Sandwich", "ingredients": "Bread, Tomato Sauce, Cheese", "recipe": "Layer bread with sauce and cheese. Serve cold."},
            {"meal": "French Fries", "ingredients": "Potatoes, Sauce, Oil", "recipe": "Fry potatoes until golden. Serve with sauce."},
        ]

    def create_meal_plan_screen(self):
        self.meal_plan_frame = tk.Frame(self.root)
        self.meal_plan_frame.pack(padx=10, pady=10)
        self.meal_plan_frame.config(background="#2c3e50")

        tk.Label(self.meal_plan_frame, text="Weekly Meal Plan", bg='#2c3e50', fg='white',pady=30, font=('times', 20, 'bold')).pack()

        for day, meal in enumerate(self.meal_plan):
            meal_label = tk.Label(self.meal_plan_frame, text=f"Day {day + 1}: {meal['meal']} - {meal['ingredients']}", bg='#2c3e50', fg='white', font=('times', 15))
            meal_label.pack(pady=5)
            meal_label.bind("<Button-1>", lambda e, meal=meal: self.show_recipe(meal))

        self.back_button = tk.Button(self.meal_plan_frame, text="Back",bg='#82ccdd', fg='#0a3d62', padx=15, pady=2,font=('times', 12, 'bold'), activebackground='black', activeforeground='white', command=self.back_to_welcome)
        self.back_button.pack(pady=10)

    def show_recipe(self, meal):
        self.meal_plan_frame.destroy()

        self.recipe_frame = tk.Frame(self.root)
        self.recipe_frame.pack(padx=10, pady=10)
        self.recipe_frame.config(background="#2c3e50")

        tk.Label(self.recipe_frame, text=meal['meal'], bg='#2c3e50', fg='white', font=('times', 20, 'bold')).pack(pady=10)
        tk.Label(self.recipe_frame, text="Ingredients: " + meal['ingredients'], bg='#2c3e50', fg='white', font=('times', 15)).pack(pady=5)
        tk.Label(self.recipe_frame, text="Recipe: " + meal['recipe'], bg='#2c3e50', fg='white', font=('times', 15)).pack(pady=5)

        self.back_button = tk.Button(self.recipe_frame, text="Back to Meal Plan", bg='#82ccdd', fg='#0a3d62', padx=15, pady=2,font=('times', 12, 'bold'), activebackground='black', activeforeground='white',command=self.back_to_meal_plan)
        self.back_button.pack(pady=10)

    def back_to_meal_plan(self):
        self.recipe_frame.destroy()
        self.create_meal_plan_screen()

    def back_to_welcome(self):
        self.meal_plan_frame.destroy()
        self.create_welcome_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = MealPlannerApp(root)
    root.geometry('900x500+180+85')
    root.config(bg='#2c3e50')
    root.mainloop()
