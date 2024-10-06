from django.http import JsonResponse
from tests.frequency_test import FrequencyTest  # Adjust the import path accordingly
from tests.runs_test import RunTest  # Adjust the import path accordingly
from tests.approximate_entropy_test import ApproximateEntropy
from tests.linear_complexity_test import ComplexityTest
from tests.template_matching_test import TemplateMatching
from tests.universal_test import Universal
from tests.serial_test import Serial
from tests.cumulative_sums_test import CumulativeSums
from tests. random_excursions_test import RandomExcursions
from tests.Matrix import Matrix
from tests.spectral import SpectralTest

from tests.autocorrelation_test import AutocorrelationTest
from tests.adaptive_statistical_test import AdaptiveStatisticalTest

from django.http import StreamingHttpResponse
from reportlab.platypus import Image
from reportlab.lib.utils import ImageReader
import mimetypes
import numpy as np

from django.conf import settings
import os
#streaming
import base64
import time
import requests
from django.http import StreamingHttpResponse
from django.shortcuts import render
#report
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend for Matplotlib
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import reportlab
from reportlab.platypus import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfform
# from reportlab.pdfimage import ImageReader
from io import BytesIO


def run_frequency_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the monobit_test method from the FrequencyTest class
    p_value, result = FrequencyTest.monobit_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result == 1:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)
def run_frequency_block_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = FrequencyTest.block_frequency(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_runs_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = RunTest.run_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_longest_one_block_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result, error_message = RunTest.longest_one_block_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)

def run_approximate_entropy_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = ApproximateEntropy.approximate_entropy_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)

def run_linear_complexity_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = ComplexityTest.linear_complexity_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)

def run_non_overlapping_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = TemplateMatching.non_overlapping_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)



def run_overlapping_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = TemplateMatching.overlapping_patterns(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_statistical_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Universal.statistical_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_serial_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Serial.serial_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)



def run_cumulative_sums_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = CumulativeSums.cumulative_sums_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_autocorrelation_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    max_lag = 10 

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = AutocorrelationTest.autocorrelation_test(binary_data, max_lag, verbose=True)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_adaptive_statistical_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = AdaptiveStatisticalTest.adaptive_statistical_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_random_excursions_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')
   
    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    chi_sq, p_value, result = RandomExcursions.random_excursions_test(binary_data)

    print("chi^2:", chi_sq)
    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'chi^2': chi_sq,
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)

def random_excursions_variant_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    chi_sq, p_value, result = RandomExcursions.variant_test(binary_data)

    print("chi^2:", chi_sq)
    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'chi^2': chi_sq,
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_binary_matrix_rank_text(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Matrix.binary_matrix_rank_text(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_spectral_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    print("Request URL:", request.get_full_path())
    print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = SpectralTest.spectral_test(binary_data)

    print("p_value:", p_value)
    print("Result:", result)
    
    # Prepare the response data
    if result:
        result_text = "random number"
    else:
        result_text = "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def send_binary_data(request):
    binary_data = '101010'  # Example binary data as a string
    response_data = {
        'binary_data': binary_data
    }
    return JsonResponse(response_data)

def fetch_binary_data():
    # Replace this URL with the actual URL of the external server
    url = "https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.content

def binary_event_stream():
    while True:
        try:
            binary_data = fetch_binary_data()
            encoded_data = base64.b64encode(binary_data).decode('utf-8')
            yield f'data: {encoded_data}\n\n'
        except requests.RequestException as e:
            yield f'data: Error fetching data: {e}\n\n'
        time.sleep(0.5)  # Adjust the sleep time as needed

def sse_binary_view(request):
    response = StreamingHttpResponse(binary_event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'  # Disable buffering for nginx
    return response

def sse_binary_example_view(request):
    return render(request, 'myapp/sse_binary_example.html')



    # Create a HttpResponse object with PDF headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    # Set up the PDF buffer and document template with margins
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=10, leftMargin=10,
                            topMargin=10, bottomMargin=30)

    # Set up styles
    styles = getSampleStyleSheet()

    # Add a headline (title)
    title = Paragraph("Report-QNu Labs", styles['Title'])
    title_space = Spacer(1, 0.0 * inch)  # Small spacer below the title

    # Add subtitles with underlining
    subtitle_style = styles['Heading2']
    subtitle_style.fontName = 'Helvetica-Bold'
    subtitle_style.fontSize = 12
    subtitle_style.underline = True

    nist_subtitle = Paragraph("NIST Statistical Tests:", subtitle_style)
    other_tests_subtitle = Paragraph("Other Tests:", subtitle_style)
    graph_subtitle = Paragraph("Graphical Analysis:", subtitle_style)

    subtitle_space = Spacer(1, 0.0 * inch)  # Spacer below the subtitles

    # Sample Table Data for the first table with "Final Result" in the last row
    data1 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Frequency Test', styles['Normal']),
         'random number',
         Paragraph('2. Frequency Test within a Block', styles['Normal']),
         'random number'],
        [Paragraph('3. Runs Test', styles['Normal']),
         'non-random number',
         Paragraph('4. Test for the longest Run of Ones', styles['Normal']),
         'random number'],
        [Paragraph('5. Binary Matrix Rank Test', styles['Normal']),
         'non-random number',
         Paragraph('6. Discrete Fourier Transform Test', styles['Normal']),
         'random number'],
        [Paragraph('7. Non-overlapping Template Match', styles['Normal']),
         'random number',
         Paragraph('8. Overlapping Template Matching Test', styles['Normal']),
         'random number'],
        [Paragraph('9. Maurers Universal test', styles['Normal']),
         'non-random number',
         Paragraph('10. Linear complexity Test', styles['Normal']),
         'random number'],
        [Paragraph('11. Serial Test', styles['Normal']),
         'random number',
         Paragraph('12. Approximate Entropy Test', styles['Normal']),
         'non-random number'],
        [Paragraph('13. Cumulative Sum Test', styles['Normal']),
         'random number',
         Paragraph('14. Random Excursions Test', styles['Normal']),
         'non-random number'],
        [Paragraph('15. Random Excursions Variant Test', styles['Normal']),
         'random number', '', ''],
        ['Final Result']
    ]

    # Adjust column widths
    colWidths = [2 * inch, 1.5 * inch, 2 * inch, 1.5 * inch]

    # Create the first table object with adjusted column widths
    table1 = Table(data1, colWidths=colWidths)

    # Apply styles to the first table
    table1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add gridlines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically align text to the middle
        ('WORDWRAP', (0, 0), (-1, -1), True),  # Enable text wrapping
    ]))

    # Sample Table Data for the second table
    data2 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Entropy Test', styles['Normal']),
         'random number',
         Paragraph('2. NIST SP 800-22', styles['Normal']),
         'random number'],
        [Paragraph('3. NIST SP 800-90b', styles['Normal']),
         'non-random number',
         Paragraph('4. Dieharder', styles['Normal']),
         'random number'],
    ]

    # Create the second table object with adjusted column widths
    table2 = Table(data2, colWidths=colWidths)

    # Apply styles to the second table
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add gridlines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically align text to the middle
        ('WORDWRAP', (0, 0), (-1, -1), True),  # Enable text wrapping
    ]))

    # Create the graph and save to a BytesIO object
    graph_io = create_graph()
    graph_image = Image(graph_io, width=6 * inch, height=4 * inch)

    # Build the PDF with the title, subtitles, tables, graph, and spacers
    elements = []
    elements.append(title)
    elements.append(title_space)  # Add space after the title
    elements.append(nist_subtitle)
    elements.append(subtitle_space)  # Spacer below the first subtitle
    elements.append(table1)
    elements.append(Spacer(1, 0.0 * inch))  # Spacer between tables
    elements.append(other_tests_subtitle)
    elements.append(subtitle_space)  # Spacer below the second subtitle
    elements.append(table2)
    elements.append(graph_subtitle)
    elements.append(subtitle_space)  # Spacer below the graph subtitle
    elements.append(graph_image)
    doc.build(elements)

    # Write the PDF to the HttpResponse
    response.write(buffer.getvalue())
    buffer.close()

    return response

global_graph_image=None


def create_graph(request):
   
    binary_data = '1101010101010101'
    # binary_data = request.GET.get('binary_data', '')
    print('my binary data is: ', binary_data)
    if not binary_data:
        return HttpResponse("Binary data is required.", status=400)

    # Dictionary to store p-values with error handling
    test_p_values = {}

    # Wrap test calls in try-except blocks and ensure p-values are numeric
    def safe_test_call(test_func, test_name, binary_data):
        result = test_func(binary_data)

        p_value = result[0]

        # If p_value is not defined (None) or equals -1, return 0
        if p_value is None or p_value == -1 or p_value > 1 or str(p_value).strip() == '':
            return 0

        try:
            return float(p_value)
        except ZeroDivisionError:
            # Handle float division by zero
            return 0

    test_p_values['Frequency Monobit'] = safe_test_call(FrequencyTest.monobit_test, 'Frequency Monobit', binary_data)
    test_p_values['Frequency Block Test'] = safe_test_call(FrequencyTest.block_frequency, 'Frequency Block Test', binary_data)
    test_p_values['Approximate Entropy Test'] = safe_test_call(ApproximateEntropy.approximate_entropy_test, 'Approximate Entropy Test', binary_data)
    test_p_values['Runs Test'] = safe_test_call(RunTest.run_test, 'Runs Test', binary_data)
    test_p_values['Longest Run of Ones Test'] = safe_test_call(RunTest.longest_one_block_test, 'Longest Run of Ones Test', binary_data)
    test_p_values['Binary Matrix Rank Test'] = safe_test_call(Matrix.binary_matrix_rank_text, 'Binary Matrix Rank Test', binary_data)
    test_p_values['Discrete Fourier Transform Test'] = safe_test_call(SpectralTest.spectral_test, 'Discrete Fourier Transform Test', binary_data)
    test_p_values['Non-overlapping Template Match Test'] = safe_test_call(TemplateMatching.non_overlapping_test, 'Non-overlapping Template Match Test', binary_data)
    test_p_values['Overlapping Template Match Test'] = safe_test_call(TemplateMatching.overlapping_patterns, 'Overlapping Template Match Test', binary_data)
    test_p_values['Maurer’s Universal Statistical Test'] = safe_test_call(Universal.statistical_test, 'Maurer’s Universal Statistical Test', binary_data)
    test_p_values['Linear Complexity Test'] = safe_test_call(ComplexityTest.linear_complexity_test, 'Linear Complexity Test', binary_data)
    test_p_values['Serial Test'] = safe_test_call(Serial.serial_test, 'Serial Test', binary_data)
    test_p_values['Cumulative Sums Test'] = safe_test_call(CumulativeSums.cumulative_sums_test, 'Cumulative Sums Test', binary_data)
    test_p_values['Random Excursions Test'] = safe_test_call(RandomExcursions.random_excursions_test, 'Random Excursions Test', binary_data)
    test_p_values['Random Excursions Variant Test'] = safe_test_call(RandomExcursions.variant_test, 'Random Excursions Variant Test', binary_data)

    valid_tests = {k: (0 if v is None or v > 1 else v) for k, v in test_p_values.items()}

    if not valid_tests:
        return HttpResponse("No valid test results to plot.", status=400)

    # Extract test names and p-values for plotting
    x = list(valid_tests.keys())
    y = list(valid_tests.values())

    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 9))

    # Assign color based on the p-value threshold (0.05)
    colors = ['green' if p > 0.05 else 'blue' for p in y]

    # Plot the histogram with colors based on the condition
    ax.bar(x, y, color=colors)

    # Draw a horizontal dotted red line at p_value = 0.05
    ax.axhline(y=0.05, color='red', linestyle='--', linewidth=2, label='p-value = 0.05')

    # Label the axes
    ax.set_xlabel('NIST Statistical Tests', fontsize=14)
    ax.set_ylabel('P-values', fontsize=14)
    ax.set_title('P-values of NIST Statistical Tests', fontsize=16)

    # Set y-axis ticks at intervals of 0.1
    ax.set_yticks([i / 10.0 for i in range(0, 11)])  # 0.0, 0.1, 0.2, ..., 1.0

    # Set y-axis limits between 0 and 1
    ax.set_ylim(0, 1)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # Ensure tight layout to avoid overlap
    plt.tight_layout()

    # Add a custom legend for the color categories
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='green', edgecolor='green', label='Random (p > 0.05)'),
                       Patch(facecolor='blue', edgecolor='blue', label='Non-random (p ≤ 0.05)')]

    # Add the legend for the colors
    ax.legend(handles=legend_elements, loc='upper right')

    # Create a BytesIO object to hold the image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)

    global_graph_image = buf
    print("Hi", global_graph_image)

    # Close the figure to free memory
    plt.close(fig)

    # Return the image as a response
    # return HttpResponse(buf, content_type='image/png')
    return HttpResponse(buf, content_type='image/png')

def generate_pdf_report(request):
    global global_graph_image
    # Create a HttpResponse object with PDF headers
    graph_response = create_graph(request)
    graph_buffer = graph_response.content
    graph_image_io = BytesIO(graph_buffer)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    # Set up the PDF buffer and document template with margins
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=10, leftMargin=10,
                            topMargin=10, bottomMargin=30)

    # Set up styles
    styles = getSampleStyleSheet()

    # Add a headline (title)
    title = Paragraph("Report-QNu Labs", styles['Title'])
    title_space = Spacer(1, 0.0 * inch)  # Small spacer below the title

    # Add subtitles with underlining
    subtitle_style = styles['Heading2']
    subtitle_style.fontName = 'Helvetica-Bold'
    subtitle_style.fontSize = 12
    subtitle_style.underline = True

    nist_subtitle = Paragraph("NIST Statistical Tests:", subtitle_style)
    other_tests_subtitle = Paragraph("Other Tests:", subtitle_style)
    graph_subtitle = Paragraph("Graphical Analysis:", subtitle_style)

    subtitle_space = Spacer(1, 0.0 * inch)  # Spacer below the subtitles

    # Sample Table Data for the first table with "Final Result" in the last row
    data1 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Frequency Test', styles['Normal']), 'random number', Paragraph('2. Frequency Test within a Block', styles['Normal']), 'random number'],
        [Paragraph('3. Runs Test', styles['Normal']), 'non-random number', Paragraph('4. Test for the longest Run of Ones', styles['Normal']), 'random number'],
        [Paragraph('5. Binary Matrix Rank Test', styles['Normal']), 'non-random number', Paragraph('6. Discrete Fourier Transform Test', styles['Normal']), 'random number'],
        [Paragraph('7. Non-overlapping Template Match', styles['Normal']), 'random number', Paragraph('8. Overlapping Template Matching Test', styles['Normal']), 'random number'],
        [Paragraph('9. Maurers Universal test', styles['Normal']), 'non-random number', Paragraph('10. Linear complexity Test', styles['Normal']), 'random number'],
        [Paragraph('11. Serial Test', styles['Normal']), 'random number', Paragraph('12. Approximate Entropy Test', styles['Normal']), 'non-random number'],
        [Paragraph('13. Cumulative Sum Test', styles['Normal']), 'random number', Paragraph('14. Random Excursions Test', styles['Normal']), 'non-random number'],
        [Paragraph('15. Random Excursions Variant Test', styles['Normal']), 'random number', '', ''],
        ['Final Result']
    ]

    # Adjust column widths
    colWidths = [2 * inch, 1.5 * inch, 2 * inch, 1.5 * inch]

    # Create the first table object with adjusted column widths
    table1 = Table(data1, colWidths=colWidths)

    # Apply styles to the first table
    table1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add gridlines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically align text to the middle
        ('WORDWRAP', (0, 0), (-1, -1), True),  # Enable text wrapping
    ]))

    # Sample Table Data for the second table
    data2 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Entropy Test', styles['Normal']), 'random number', Paragraph('2. NIST SP 800-22', styles['Normal']), 'random number'],
        [Paragraph('3. NIST SP 800-90b', styles['Normal']), 'non-random number', Paragraph('4. Dieharder', styles['Normal']), 'random number'],
    ]

    # Create the second table object with adjusted column widths
    table2 = Table(data2, colWidths=colWidths)

    # Apply styles to the second table
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center text alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Set font size
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add gridlines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically align text to the middle
        ('WORDWRAP', (0, 0), (-1, -1), True),  # Enable text wrapping
    ]))

    # Use the BytesIO object to create an Image
    graph_image = Image(graph_image_io)
    
    # Automatically scale the image
    graph_image.drawHeight = 4 * inch  # Set height
    graph_image.drawWidth = 7 * inch  # Set width

    # Ensure the image fits within the page margins
    max_width = A4[0] - 20  # A4 width minus margins
    max_height = A4[1] - 20  # A4 height minus margins

    # Adjust if necessary
    if graph_image.drawWidth > max_width or graph_image.drawHeight > max_height:
        aspect_ratio = graph_image.drawWidth / graph_image.drawHeight
        if graph_image.drawWidth > max_width:
            graph_image.drawWidth = max_width
            graph_image.drawHeight = max_width / aspect_ratio
        if graph_image.drawHeight > max_height:
            graph_image.drawHeight = max_height
            graph_image.drawWidth = max_height * aspect_ratio

    # Build the PDF with the title, subtitles, tables, graph, and spacers
    elements = []
    elements.append(title)
    elements.append(title_space)  # Add space after the title
    elements.append(nist_subtitle)
    elements.append(subtitle_space)  # Spacer below the first subtitle
    elements.append(table1)
    elements.append(Spacer(1, 0.5 * inch))  # Spacer between tables
    elements.append(other_tests_subtitle)
    elements.append(subtitle_space)  # Spacer below the second subtitle
    elements.append(table2)
    elements.append(graph_subtitle)
    elements.append(subtitle_space)  # Spacer below the graph subtitle
    elements.append(graph_image)
    
    doc.build(elements)

    # Write the PDF to the HttpResponse
    response.write(buffer.getvalue())
    buffer.close()

    return response