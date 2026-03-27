# Simple Inventory Manager

A lightweight, console-based inventory management system built with **Python**. This project demonstrates modular programming by separating the user interface logic from the core business logic.

## 🚀 Features

* **Product Management:** Easily add products with specific names, prices, and quantities.
* **Data Validation:** Includes basic error handling to ensure price and quantity inputs are numeric.
* **Inventory Overview:** Display a complete list of all registered items.
* **Real-time Statistics:** * Calculates the **total monetary value** of the entire stock.
    * Summarizes the **total count of units** available.

## 📂 Project Structure

The project is divided into two main files:

* `main.py`: The entry point of the application. It handles the execution loop and the interactive menu.
* `core.py`: The logic engine. It manages the data structures (lists and dictionaries) and performs all calculations.

## 🛠️ Requirements

* **Python 3.x** or higher.

## 💻 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/inventory-manager-python.git](https://github.com/your-username/inventory-manager-python.git)
    cd inventory-manager-python
    ```

2.  **Run the application:**
    ```bash
    python main.py
    ```

## 📖 Usage Example

Once the script is running, follow the on-screen prompts:

```text
--------Menu--------
1. Add product
2. Show products
3. Calculate statistics
4. Exit
--------------------
Option ->
