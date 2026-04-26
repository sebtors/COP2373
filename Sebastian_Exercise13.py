import sqlite3
import random
import matplotlib.pyplot as plt

# -----------------------------
# Function 1: Create Database + Insert 2025 Data
# -----------------------------
def create_database():
    conn = sqlite3.connect("population_ST.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # 10 Florida cities with estimated 2025 populations
    cities = {
        "Miami": 460000,
        "Orlando": 320000,
        "Tampa": 400000,
        "Jacksonville": 1000000,
        "Tallahassee": 200000,
        "St. Petersburg": 270000,
        "Hialeah": 220000,
        "Fort Lauderdale": 185000,
        "Cape Coral": 230000,
        "Gainesville": 150000
    }

    # Insert 2025 data
    for city, pop in cities.items():
        cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2025, pop))

    conn.commit()
    conn.close()

    print("Database and initial data created.")


# -----------------------------
# Function 2: Simulate Growth/Decline
# -----------------------------
def simulate_growth():
    conn = sqlite3.connect("population_ST.db")
    cursor = conn.cursor()

    # Get cities and their 2025 population
    cursor.execute("SELECT city, population FROM population WHERE year = 2025")
    data = cursor.fetchall()

    for city, population in data:
        current_pop = population

        for year in range(2026, 2046):  # Next 20 years
            # Random growth/decline rate between -2% and +3%
            rate = random.uniform(-0.02, 0.03)
            current_pop = int(current_pop * (1 + rate))

            cursor.execute("INSERT INTO population VALUES (?, ?, ?)",
                           (city, year, current_pop))

    conn.commit()
    conn.close()

    print("Population simulation complete.")


# -----------------------------
# Function 3: Plot Population
# -----------------------------
def plot_city_population():
    conn = sqlite3.connect("population_ST.db")
    cursor = conn.cursor()

    # Get list of cities
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    # Show options
    print("\nAvailable Cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    # User choice
    choice = int(input("\nSelect a city (1-10): "))
    selected_city = cities[choice - 1]

    # Get population data
    cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (selected_city,))
    results = cursor.fetchall()

    years = [row[0] for row in results]
    populations = [row[1] for row in results]

    conn.close()

    # Plot
    plt.figure()
    plt.plot(years, populations, marker='o')
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid()

    plt.show()


# -----------------------------
# Main Program
# -----------------------------
def main():
    create_database()
    simulate_growth()
    plot_city_population()


if __name__ == "__main__":
    main()