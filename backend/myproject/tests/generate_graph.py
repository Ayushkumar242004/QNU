import io
import matplotlib.pyplot as plt
from django.http import HttpResponse
import approximate_entropy_test
import cumulative_sums_test
import frequency_test
import runs_test
import linear_complexity_test
import Matrix
import random_excursions_test
import serial_test
import spectral
import template_matching_test
import universal_test

def collect_p_values():
    test_p_values = {
        'Frequency Monobit': frequency_test.monobit_test(),
        'Frequency Block Test': frequency_test.block_frequency(),
        'Approximate Entropy Test': approximate_entropy_test.approximate_entropy_test(),
        'Runs Test': runs_test.run_test(),
        'Longest Run of Ones Test': runs_test.longest_one_block_test(),
        'Binary Matrix Rank Test': Matrix.binary_matrix_rank_test(),
        'Discrete Fourier Transform Test': spectral.spectral_test(),
        'Non-overlapping Template Match Test': template_matching_test.non_overlapping_test(),
        'Overlapping Template Match Test': template_matching_test.overlapping_patterns(),
        'Maurer’s Universal Statistical Test': universal_test.statistical_test(),
        'Linear Complexity Test': linear_complexity_test.linear_complexity_test(),
        'Serial Test': serial_test.serial_test(),
        'Cumulative Sums Test': cumulative_sums_test.cumulative_sums_test(),
        'Random Excursions Test': random_excursions_test.random_excursions_test(),
        'Random Excursions Variant Test': random_excursions_test.variant_test(),
    }
    return test_p_values

def create_graph(request):
    # Collect p-values from each test
    test_p_values = collect_p_values()

    # Extract test names and p-values for plotting
    x = list(test_p_values.keys())
    y = list(test_p_values.values())

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data with different colors based on the condition
    for i in range(len(x)):
        if y[i] >= 0.05:
            ax.plot(x[i], y[i], marker='o', linestyle='-', color='b')  # Blue for p-values >= 0.05
        else:
            ax.plot(x[i], y[i], marker='o', linestyle='-', color='r')  # Red for p-values < 0.05

    # Plot the line at y = 0.05
    ax.axhline(y=0.05, color='green', linestyle='--', label='y = 0.05')

    # Label the axes
    ax.set_xlabel('NIST Statistical Tests')
    ax.set_ylabel('P-values')
    ax.set_title('P-values of NIST Statistical Tests')

    # Set y-axis ticks at intervals of 0.1
    ax.set_yticks([i / 10.0 for i in range(0, 11)])  # 0.0, 0.1, 0.2, ..., 1.0

    # Set y-axis limits between 0 and 1
    ax.set_ylim(0, 1)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # Ensure tight layout to avoid overlap
    plt.tight_layout()

    # Create a BytesIO object to hold the image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Return the image as a response
    return HttpResponse(buf, content_type='image/png')