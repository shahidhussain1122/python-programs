import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
from bs4 import BeautifulSoup
import threading
import csv

class AIPoweredScraper:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Scraper")
        self.root.geometry("900x700")  # Larger window size for better layout

        # URL Input
        tk.Label(root, text="Website URL:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.url_entry = tk.Entry(root, width=70, font=("Arial", 12))
        self.url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Category Selector
        tk.Label(root, text="Category Selector:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.category_entry = tk.Entry(root, width=70, font=("Arial", 12))
        self.category_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Subcategory Selector
        tk.Label(root, text="Subcategory Selector:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.subcategory_entry = tk.Entry(root, width=70, font=("Arial", 12))
        self.subcategory_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Field Selector Section
        tk.Label(root, text="Field Selectors (CSS):", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=10)

        self.fields = ["Product Name", "Description", "Price", "Image URL", "Variant"]
        self.field_entries = {}

        for idx, field in enumerate(self.fields):
            tk.Label(root, text=f"{field} Selector:", font=("Arial", 12)).grid(row=4+idx, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(root, width=70, font=("Arial", 12))
            entry.grid(row=4+idx, column=1, padx=10, pady=5, sticky="w")
            self.field_entries[field] = entry

        # Start Button
        self.start_button = tk.Button(root, text="Start Scraping", font=("Arial", 12), command=self.start_scraping)
        self.start_button.grid(row=10, column=1, pady=20, sticky="w")

        # Output Area
        tk.Label(root, text="Scraping Output:", font=("Arial", 12)).grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.output_area = tk.Text(root, wrap=tk.WORD, height=15, width=100, font=("Arial", 10))
        self.output_area.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        # Save CSV Button
        self.save_button = tk.Button(root, text="Save as CSV", font=("Arial", 12), command=self.save_csv, state=tk.DISABLED)
        self.save_button.grid(row=13, column=1, pady=10, sticky="w")

        self.scraped_data = []

    def fetch_data(self, url, category_selector, subcategory_selector, field_selectors):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Fetch Categories
            categories = soup.select(category_selector)
            self.output_area.insert(tk.END, "Categories:\n")
            for category in categories:
                self.output_area.insert(tk.END, f"- {category.text.strip()}\n")

            # Fetch Subcategories
            subcategories = soup.select(subcategory_selector)
            self.output_area.insert(tk.END, "\nSubcategories:\n")
            for subcategory in subcategories:
                self.output_area.insert(tk.END, f"- {subcategory.text.strip()}\n")

            # Example: Fetch Product Details
            self.output_area.insert(tk.END, "\nProducts:\n")
            self.scraped_data = []  # Clear previous data

            products = soup.select(category_selector)  # Adjust based on your use case
            for product in products:
                product_data = {}
                for field, selector in field_selectors.items():
                    if selector:
                        element = product.select_one(selector)
                        product_data[field] = element["src"] if field == "Image URL" and element else element.text.strip() if element else "N/A"
                    else:
                        product_data[field] = "N/A"
                self.scraped_data.append(product_data)
                self.output_area.insert(tk.END, f"- {product_data}\n")

            # Enable Save as CSV button if data is scraped
            if self.scraped_data:
                self.save_button.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def save_csv(self):
        if not self.scraped_data:
            messagebox.showwarning("No Data", "No data to save.")
            return

        # Save File Dialog
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                # Write data to CSV
                with open(file_path, "w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=self.fields)
                    writer.writeheader()
                    writer.writerows(self.scraped_data)

                messagebox.showinfo("Success", f"Data successfully saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving: {e}")

    def start_scraping(self):
        url = self.url_entry.get()
        category_selector = self.category_entry.get()
        subcategory_selector = self.subcategory_entry.get()
        field_selectors = {field: entry.get() for field, entry in self.field_entries.items()}

        if not url or not category_selector or not subcategory_selector:
            messagebox.showwarning("Input Required", "Please provide all required inputs.")
            return

        # Clear previous output and data
        self.output_area.delete(1.0, tk.END)
        self.scraped_data = []
        self.save_button.config(state=tk.DISABLED)

        # Run scraping in a separate thread to keep the UI responsive
        threading.Thread(target=self.fetch_data, args=(url, category_selector, subcategory_selector, field_selectors)).start()

# Initialize Tkinter app
root = tk.Tk()
app = AIPoweredScraper(root)
root.mainloop()
