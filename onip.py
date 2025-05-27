import tkinter as tk
from tkinter import ttk

class ScoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OINP Scoring Calculator")

        # Define categories and corresponding points
        self.categories = {
            "Job Offer NOC TEER": ["NOC TEER 0 or 1", "NOC TEER 2 or 3", "NOC TEER 4 or 5"],
            "Occupational Category": ["Category 0, 2, 3", "Category 7", "Category 1, 9", "Category 4, 8", "Category 5, 6"],
            "Job Offer Wage": ["$40/hr+", "$35-39.99/hr", "$30-34.99/hr", "$25-29.99/hr", "$20-24.99/hr", "<$20/hr"],
            "Work/Study Permit": ["Valid work/study permit", "No valid permit"],
            "Job Tenure": ["6+ months in position", "<6 months or not working"],
            "Earnings History": ["$40k+ in a year", "<$40k in a year"],
            "Highest Education": ["PhD", "Masters", "Bachelors", "Grad Diploma", "Undergrad Diploma", "Trades Certificate", "Less than college"],
            "Field of Study": ["STEM/Health/Trades", "Business/Admin/Social", "Arts/Humanities"],
            "Canadian Education Experience": ["More than one credential", "One credential"],
            "Language Ability": ["CLB 9+", "CLB 8", "CLB 7", "CLB 6 or lower"],
            "Official Languages": ["2 Official Languages", "1 Official Language"],
            "Job Location": ["Northern Ontario", "Outside GTA (except Northern)", "Inside GTA (except Toronto)", "Toronto"],
            "Study Location": ["Northern Ontario", "Outside GTA (except Northern)", "Inside GTA (except Toronto)", "Toronto"]
        }

        self.points_mapping = {
            "Job Offer Wage": [10, 8, 7, 6, 5, 0],
            "Job Offer NOC TEER": [10, 8, 0],
            "Occupational Category": [10, 7, 5, 4, 3],
            "Work/Study Permit": [10, 0],
            "Job Tenure": [3, 0],
            "Earnings History": [3, 0],
            "Highest Education": [10, 8, 6, 6, 5, 5, 0],
            "Field of Study": [12, 6, 0],
            "Canadian Education Experience": [10, 5],
            "Language Ability": [10, 6, 4, 0],
            "Official Languages": [10, 5],
            "Job Location": [10, 8, 3, 0],
            "Study Location": [10, 8, 3, 0]
        }

        self.selected_values = {}

        # Create dropdowns for each category
        for i, (category, options) in enumerate(self.categories.items()):
            label = tk.Label(root, text=category)
            label.grid(row=i, column=0, sticky="w")

            dropdown = ttk.Combobox(root, values=options)
            dropdown.grid(row=i, column=1)
            dropdown.current(0)

            self.selected_values[category] = dropdown

        # Button to calculate points
        self.calculate_button = tk.Button(root, text="Calculate Points", command=self.calculate_points)
        self.calculate_button.grid(row=len(self.categories), column=0, columnspan=2)

        # Label to display total score
        self.result_label = tk.Label(root, text="Total Points: 0", font=("Arial", 12))
        self.result_label.grid(row=len(self.categories) + 1, column=0, columnspan=2)

    def calculate_points(self):
        total_points = 0
        for category, dropdown in self.selected_values.items():
            selected_option = dropdown.get()
            index = self.categories[category].index(selected_option)
            total_points += self.points_mapping[category][index]

        self.result_label.config(text=f"Total Points: {total_points}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScoringApp(root)
    root.mainloop()