import os
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__, template_folder='templates', static_folder='static')

# Placeholder for energy-saving suggestions
energy_saving_suggestions = [
    "Upgrade to energy-efficient appliances.",
    "Install programmable thermostat for better temperature control during peak hours.",
    "Improve insulation to reduce heating and cooling energy consumption."
]

def generate_energy_plot(total_kWh, peak_hours_start, peak_hours_end):
    hours = range(24)
    energy_values = np.random.randint(10, 50, size=24)

    # Highlight peak hours
    peak_hour_indices = range(peak_hours_start, peak_hours_end + 1)
    energy_values[list(peak_hour_indices)] = np.random.randint(50, 100, size=len(peak_hour_indices))

    plt.plot(hours, energy_values, marker='o')
    plt.xlabel('Hour of Day')
    plt.ylabel('Energy Usage (kWh)')
    plt.title('Energy Usage Pattern')
    plt.grid(True)

    # Save energy plot as PNG
    plt.savefig(os.path.join('static', 'energy_plot.png'))
    plt.close()

def generate_energy_comparison_plot(user_consumption, low_energy_house_consumption, peak_hours_start, peak_hours_end):
    hours = np.arange(24)

    # Generate random energy values for user's consumption
    user_energy_values = np.random.randint(10, 50, size=24)
    user_peak_hour_indices = range(peak_hours_start, peak_hours_end + 1)
    user_energy_values[list(user_peak_hour_indices)] = np.random.randint(50, 100, size=len(user_peak_hour_indices))

    # Placeholder data for low-energy house consumption
    low_energy_values = np.random.randint(5, 30, size=24)

    plt.plot(hours, user_energy_values, marker='o', label='Your Energy Consumption')
    plt.plot(hours, low_energy_values, marker='o', label='Low Energy House')
    plt.xlabel('Hour of Day')
    plt.ylabel('Energy Usage (kWh)')
    plt.title('Comparison of Energy Usage')
    plt.legend()
    plt.grid(True)

    # Save comparison plot as PNG
    plt.savefig(os.path.join('static', 'energy_comparison_plot.png'))
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get energy usage data from the form
        total_kWh = float(request.form['total_kWh'])
        peak_hours_start = int(request.form['peak_hours_start'])
        peak_hours_end = int(request.form['peak_hours_end'])

        # Generate energy plot
        generate_energy_plot(total_kWh, peak_hours_start, peak_hours_end)

        # Placeholder for low energy house consumption (replace with real data)
        low_energy_house_consumption = 100

        # Generate comparison plot
        generate_energy_comparison_plot(total_kWh, low_energy_house_consumption, peak_hours_start, peak_hours_end)

        # Determine energy-saving suggestions based on user's consumption
        suggestions = energy_saving_suggestions if total_kWh > low_energy_house_consumption else []

        # Prepare energy usage data to pass to template
        energy_usage_data = {
            "total_kWh": total_kWh,
            "peak_hours": f"{peak_hours_start} - {peak_hours_end}"
        }

        return render_template('result.html', energy_data=energy_usage_data, suggestions=suggestions)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
