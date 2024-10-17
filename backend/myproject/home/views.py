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
from PIL import Image as PILImage
from tests.autocorrelation_test import AutocorrelationTest
from tests.adaptive_statistical_test import AdaptiveStatisticalTest


from tests.Birthday_spacings_test import BirthdaySpacingsTest
from tests.parking_lot_test import ParkingLotTest
from tests.overlapping_5_permutation_test import Overlapping5PermutationTest
from tests.minimum_distance_test import MinimumDistanceTest
from tests.rank_31matrix_test import Ranks31x31MatricesTest
from tests.spheres_test import Spheres3DTest
from tests.rank_32matrix_test import Ranks32x32MatricesTest
from tests.craps_test import CrapsTest
from tests.bitstream_test import BitstreamTest
from tests.gcd_test import MarsagliaTsangGCDTest
from tests.opso_test import OPSOTest
from tests.oqso_test import OQSOTest
from tests.dna_test import DNATest
from tests.count_one_stream_test import CountThe1sStreamTest
from tests.count_one_byte_test import CountThe1sByteTest
from tests.simple_gcd_test import MarsagliaTsangSimpleGCDTest
from tests.generalized_minimum_test import GeneralizedMinimumDistanceTest
from tests.u01_linear_complexity_test import TestU01LinearComplexityTest
from tests.u01_longest_substring_test import TestU01LongestRepeatedSubstringTest
from tests.u01_matrix_rank_test import TestU01MatrixRankTest

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
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the monobit_test method from the FrequencyTest class
    p_value, result = FrequencyTest.monobit_test(binary_data)

    print("FrequencyTest p_value:", p_value)
    print("FrequencyTest Result:", result)
    
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
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)


    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)
    
    # Call the block_frequency method
    p_value, result = FrequencyTest.block_frequency(binary_data)

    print("run_frequency_block_test p_value:", p_value)
    print("run_frequency_block_test Result:", result)
    
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
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = RunTest.run_test(binary_data)

    print("run_runs_test p_value:", p_value)
    print("run_runs_test Result:", result)
    
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

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result, error_message = RunTest.longest_one_block_test(binary_data)

    
    print("run_longest_one_block_test p_value:", p_value)
    print("run_longest_one_block_test Result:", result)
    
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

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = ApproximateEntropy.approximate_entropy_test(binary_data)

    print("run_approximate_entropy_test p_value:", p_value)
    print("run_approximate_entropy_test Result:", result)
    
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
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = ComplexityTest.linear_complexity_test(binary_data)

    print("run_linear_complexity_test p_value:", p_value)
    print("run_linear_complexity_test Result:", result)
    
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

    # # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = TemplateMatching.non_overlapping_test(binary_data)

    print("run_non_overlapping_test p_value:", p_value)
    print("run_non_overlapping_test Result:", result)
    
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
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = TemplateMatching.overlapping_patterns(binary_data)

    print("run_overlapping_test p_value:", p_value)
    print("run_overlapping_test Result:", result)
    
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
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Universal.statistical_test(binary_data)

    print("run_statistical_test p_value:", p_value)
    print("run_statistical_test Result:", result)
    
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

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Serial.serial_test(binary_data)

    print("run_serial_test p_value:", p_value)
    print("run_serial_test Result:", result)
    
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

    # # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = CumulativeSums.cumulative_sums_test(binary_data)

    print("run_cumulative_sums_test p_value:", p_value)
    print("run_cumulative_sums_test Result:", result)
    
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

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)


    max_lag = 10 

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = AutocorrelationTest.autocorrelation_test(binary_data, max_lag, verbose=True)

    print("run_autocorrelation_test p_value:", p_value)
    print("run_autocorrelation_test Result:", result)
    
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

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = AdaptiveStatisticalTest.adaptive_statistical_test(binary_data)

    print("run_adaptive_statistical_test p_value:", p_value)
    print("run_adaptive_statistical_test Result:", result)
    
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
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    chi_sq, p_value, result = RandomExcursions.random_excursions_test(binary_data)

    print("run_random_excursions_test chi^2:", chi_sq)
    print("run_random_excursions_test p_value:", p_value)
    print("run_random_excursions_test Result:", result)
    
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
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    chi_sq, p_value, result = RandomExcursions.variant_test(binary_data)

    print("random_excursions_variant_test chi^2:", chi_sq)
    print("random_excursions_variant_test p_value:", p_value)
    print("random_excursions_variant_test Result:", result)
    
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

    # # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Matrix.binary_matrix_rank_text(binary_data)

    print("run_binary_matrix_rank_text p_value:", p_value)
    print("run_binary_matrix_rank_text Result:", result)
    
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

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)
    
    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = SpectralTest.spectral_test(binary_data)

    print("run_spectral_test p_value:", p_value)
    print("run_spectral_test Result:", result)
    
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


def run_birthday_spacings_test(request):
    # Example binary data received from the request query parameters
    binary_data_str = request.GET.get('binary_data', '')

    # Print the request URL and parameters for debugging
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Convert binary string to a list of integers
    if binary_data_str:
        # Ensure only '0' and '1' are considered
        binary_data = [int(bit) for bit in binary_data_str if bit in '01']
    else:
        return JsonResponse({'error': 'Invalid or missing binary data.'}, status=400)

    # Check if the converted data has at least two points
    if len(binary_data) < 2:
        return JsonResponse({'error': 'Insufficient data. At least two data points are required.'}, status=400)

    # Call the Birthday Spacings Test method
    p_value, result = BirthdaySpacingsTest.BirthdaySpacingsTest(binary_data)

    print("run_birthday_spacings_test p_value:", p_value)
    print("run_birthday_spacings_test Result:", result)

    # Prepare the response data
    result_text = "random number" if result else "non-random number"
        
    response_data = {
        'p_value': p_value,
        'result': result_text
    }

    return JsonResponse(response_data)


def run_bitstream_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)
    
    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = BirthdaySpacingsTest.BirthdaySpacingsTest(binary_data)

    print("run_bitstream_test p_value:", p_value)
    print("run_bitstream_test Result:", result)
    
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


def run_parking_lot_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = ParkingLotTest.ParkingLotTest(binary_data)

    print("run_parking_lot_test p_value:", p_value)
    print("run_parking_lot_test Result:", result)
    
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




def run_overlapping_5_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)
    
    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Overlapping5PermutationTest.Overlapping5PermutationTest(binary_data)

    print("run_overlapping_5_test p_value:", p_value)
    print("run_overlapping_5_test Result:", result)
    
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



def run_minimum_distance_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)
    
    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = MinimumDistanceTest.MinimumDistanceTest(binary_data)

    print("run_minimum_distance_test p_value:", p_value)
    print("run_minimum_distance_test Result:", result)
    
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


def run_31matrix_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Ranks31x31MatricesTest.Ranks31x31MatricesTest(binary_data)

    print("run_31matrix_test p_value:", p_value)
    print("run_31matrix_test Result:", result)
    
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




def run_spheres_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    if not binary_data:
        # If there's no binary data, return an empty JsonResponse with status code 204 (No Content)
        return JsonResponse({}, status=204)
    
    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Spheres3DTest.Spheres3DTest(binary_data)

    print("run_spheres_test p_value:", p_value)
    print("run_spheres_test Result:", result)
    
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




def run_32matrix_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = Ranks32x32MatricesTest.Ranks32x32MatricesTest(binary_data)

    print("run_32matrix_test p_value:", p_value)
    print("run_32matrix_test Result:", result)
    
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



def run_craps_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = CrapsTest.CrapsTest(binary_data)

    print("run_craps_test p_value:", p_value)
    print("run_craps_test Result:", result)
    
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



def run_bitstream_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = BitstreamTest.BitstreamTest(binary_data)

    print("run_bitstream_test p_value:", p_value)
    print("run_bitstream_test Result:", result)
    
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





def run_gcd_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = MarsagliaTsangGCDTest.MarsagliaTsangGCDTest(binary_data)

    print("run_gcd_test p_value:", p_value)
    print("run_gcd_test Result:", result)
    
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

def run_opso_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = OPSOTest.OPSOTest(binary_data)

    print("run_opso_test p_value:", p_value)
    print("run_opso_test Result:", result)
    
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



def run_oqso_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = OQSOTest.OQSOTest(binary_data)

    print("run_oqso_test p_value:", p_value)
    print("run_oqso_test Result:", result)
    
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



def run_dna_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = DNATest.DNATest(binary_data)

    print("run_dna_test p_value:", p_value)
    print("run_dna_test Result:", result)
    
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




def run_count_one_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = CountThe1sStreamTest.CountThe1sStreamTest(binary_data)

    print("run_count_one_test p_value:", p_value)
    print("run_count_one_test Result:", result)
    
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




def run_count_one_byte_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = CountThe1sByteTest.CountThe1sByteTest(binary_data)

    print("run_count_one_byte_test p_value:", p_value)
    print("run_count_one_byte_test Result:", result)
    
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


def run_simple_gcd_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = MarsagliaTsangSimpleGCDTest.MarsagliaTsangSimpleGCDTest(binary_data)

    print("run_simple_gcd_test p_value:", p_value)
    print("run_simple_gcd_test Result:", result)
    
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



def run_general_minimum_distance_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = GeneralizedMinimumDistanceTest.GeneralizedMinimumDistanceTest(binary_data)

    print("run_general_minimum_distance_test p_value:", p_value)
    print("run_general_minimum_distance_test Result:", result)
    
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



def run_u01_linear_complexity_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = TestU01LinearComplexityTest.TestU01LinearComplexityTest(binary_data)

    print("run_u01_linear_complexity_test p_value:", p_value)
    print("run_u01_linear_complexity_test Result:", result)
    
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




def run_u01_longest_repeated_substring_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest(binary_data)

    print("run_u01_longest_repeated_substring_test p_value:", p_value)
    print("run_u01_longest_repeated_substring_test Result:", result)
    
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



def run_matrix_rank_test(request):
    # Example binary data received from the request query parameters
    binary_data = request.GET.get('binary_data', '')

    # Print the request URL and parameters
    # print("Request URL:", request.get_full_path())
    # print("Request Parameters:", request.GET)

    # Call the block_frequency method
    p_value, result = TestU01MatrixRankTest.TestU01MatrixRankTest(binary_data)

    print("run_matrix_rank_test p_value:", p_value)
    print("run_matrix_rank_test Result:", result)
    
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
   

    binary_data = request.GET.get('binary_data', '')

   
    if not binary_data:
        return HttpResponse("Binary data is required.", status=400)

    # Dictionary to store p-values with error handling
    test_p_values = {}

    # Wrap test calls in try-except blocks and ensure p-values are numeric
    def safe_test_call(test_func, test_name, binary_data):
        result = test_func(binary_data)

        p_value = result[0]
        # print(test_name, p_value)

        # If p_value is not defined (None) or equals -1, return 0
        if p_value is None or p_value == -1  or str(p_value).strip() == '':
            return 0
        if p_value > 1:
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
    test_p_values['Autocorrelation Test'] = safe_test_call(AutocorrelationTest.autocorrelation_test, 'Autocorrelation Test', binary_data)
    test_p_values['Adaptive Statistical Test'] = safe_test_call(AdaptiveStatisticalTest.adaptive_statistical_test, 'Adaptive Statistical Test', binary_data)

    
   
    valid_tests = {k: (0 if v is None or v > 1 else v) for k, v in test_p_values.items()}

    if not valid_tests:
        return HttpResponse("No valid test results to plot.", status=400)

    # Extract test names and p-values for plotting
    x = list(valid_tests.keys())
    y = list(valid_tests.values())

    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 9))

    # Assign color based on the p-value threshold (0.05)
    colors = ['green' if p > 0.01 else 'blue' for p in y]

    # Plot the histogram with colors based on the condition
    ax.bar(x, y, color=colors)

    # Draw a horizontal dotted red line at p_value = 0.05
    ax.axhline(y=0.01, color='red', linestyle='--', linewidth=2, label='p-value = 0.01')

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
    legend_elements = [Patch(facecolor='green', edgecolor='green', label='Random (p > 0.01)'),
                       Patch(facecolor='blue', edgecolor='blue', label='Non-random (p ≤ 0.01)')]

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

def create_graph_dieharder(request):
   

    binary_data = request.GET.get('binary_data', '')

    binary_data = binary_data.replace('%0A', '').replace('%20', '').replace(' ', '').replace('\n', '').replace('\r', '')
    
    if not binary_data:
        return HttpResponse("Binary data is required.", status=400)

    # Dictionary to store p-values with error handling
    test_p_values = {}

    # Wrap test calls in try-except blocks and ensure p-values are numeric
    def safe_test_call(test_func, test_name, binary_data):
        result = test_func(binary_data)

        p_value = result[0]
        print(test_name, p_value)

        # If p_value is not defined (None) or equals -1, return 0
        if p_value is None or p_value == -1  or str(p_value).strip() == '':
            return 0
        if p_value > 1:
            return 0
        try:
            return float(p_value)
        except ZeroDivisionError:
            # Handle float division by zero
            return 0

    
    test_p_values['Birthday Spacing Test'] = safe_test_call(BirthdaySpacingsTest.BirthdaySpacingsTest, 'Birthday Spacing Test', binary_data)
    test_p_values['Parking Lot Test'] = safe_test_call(ParkingLotTest.ParkingLotTest, 'Parking Lot Test', binary_data)
    test_p_values['Overlapping Permutation 5 Test'] = safe_test_call(Overlapping5PermutationTest.Overlapping5PermutationTest, 'Overlapping Permutation 5 Test', binary_data)
    test_p_values['Minimum Distance Test'] = safe_test_call(MinimumDistanceTest.MinimumDistanceTest, 'Minimum Distance Test', binary_data)
    test_p_values['Ranks of 31x31 Test'] = safe_test_call(Ranks31x31MatricesTest.Ranks31x31MatricesTest, 'Ranks of 31x31 Test', binary_data)
    test_p_values['3d Spheres Test'] = safe_test_call(Spheres3DTest.Spheres3DTest, '3d Spheres Test', binary_data)
    test_p_values['Ranks of 32x32 Test'] = safe_test_call(Ranks32x32MatricesTest.Ranks32x32MatricesTest, 'Ranks of 32x32 Test', binary_data)
    test_p_values['Craps Test'] = safe_test_call(CrapsTest.CrapsTest, 'Craps Test', binary_data)
    test_p_values['Bitstream Test'] = safe_test_call(BitstreamTest.BitstreamTest, 'Bitstream Test', binary_data)
    test_p_values['Marsaglia-Tsang GCD Test'] = safe_test_call(MarsagliaTsangGCDTest.MarsagliaTsangGCDTest, 'Marsaglia-Tsang GCD Test', binary_data)
    test_p_values['OPSO Test'] = safe_test_call(OPSOTest.OPSOTest, 'OPSO Test', binary_data)
    test_p_values['OQSO Test'] = safe_test_call(OQSOTest.OQSOTest, 'OQSO Test', binary_data)
    test_p_values['DNA Test'] = safe_test_call(DNATest.DNATest, 'DNA Test', binary_data)
    test_p_values['Count the one(stream) Test'] = safe_test_call(CountThe1sStreamTest.CountThe1sStreamTest, 'Count the one(stream) Test', binary_data)
    test_p_values['Count the one(byte) Test'] = safe_test_call(CountThe1sByteTest.CountThe1sByteTest, 'Count the one(byte) Test', binary_data)
    test_p_values['Marsaglia Tsang Simple GCD Test'] = safe_test_call(MarsagliaTsangSimpleGCDTest.MarsagliaTsangSimpleGCDTest, 'Marsaglia Tsang Simple GCD Test', binary_data)
    test_p_values['Generalized Minimum Distance Test'] = safe_test_call(GeneralizedMinimumDistanceTest.GeneralizedMinimumDistanceTest, 'Generalized Minimum Distance Test', binary_data)
    test_p_values['TestU01 Linear Complexity Test'] = safe_test_call(TestU01LinearComplexityTest.TestU01LinearComplexityTest, 'TestU01 Linear Complexity Test', binary_data)
    test_p_values['TestU01 Longest Repeated Substring Test'] = safe_test_call(TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest, 'TestU01 Longest Repeated Substring Test', binary_data)
    test_p_values['TestU01 Matrix Rank Test'] = safe_test_call(TestU01MatrixRankTest.TestU01MatrixRankTest, 'TestU01 Matrix Rank Test', binary_data)


    
    
    valid_tests = {k: (0 if v is None or v > 1 else v) for k, v in test_p_values.items()}

    if not valid_tests:
        return HttpResponse("No valid test results to plot.", status=400)

    # Extract test names and p-values for plotting
    x = list(valid_tests.keys())
    y = list(valid_tests.values())

    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 9))

    # Assign color based on the p-value threshold (0.05)
    colors = ['green' if p > 0.01 else 'blue' for p in y]

    # Plot the histogram with colors based on the condition
    ax.bar(x, y, color=colors)

    # Draw a horizontal dotted red line at p_value = 0.05
    ax.axhline(y=0.01, color='red', linestyle='--', linewidth=2, label='p-value = 0.01')

    # Label the axes
    ax.set_xlabel('NIST Statistical Tests', fontsize=14)
    ax.set_ylabel('P-values', fontsize=14)
    ax.set_title('P-values of Dieharder Tests', fontsize=16)

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
    legend_elements = [Patch(facecolor='green', edgecolor='green', label='Random (p > 0.01)'),
                       Patch(facecolor='blue', edgecolor='blue', label='Non-random (p ≤ 0.01)')]

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

    binary_data = request.GET.get('binary_data', '')

    
    # Create an HttpResponse object with PDF headers
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

    nist_subtitle = Paragraph("NIST Tests:", subtitle_style)
    graph_subtitle = Paragraph("Graphical Analysis:", subtitle_style)

    subtitle_space = Spacer(1, 0.0 * inch)  # Spacer below the subtitles

    # Initialize x to 0
    x = 0

    # Perform the tests and check results
    frequency_test_result = FrequencyTest.monobit_test(binary_data)[1]
    if frequency_test_result:
        x += 1

    frequency_test_block_result = FrequencyTest.block_frequency(binary_data)[1]
    if frequency_test_block_result:
        x += 1

    runs_test_result = RunTest.run_test(binary_data)[1]
    if runs_test_result:
        x += 1

    approximate_entropy_test_result = ApproximateEntropy.approximate_entropy_test(binary_data)[1]
    if approximate_entropy_test_result:
        x += 1

    longest_run_of_one_test_result = RunTest.longest_one_block_test(binary_data)[1]
    if longest_run_of_one_test_result:
        x += 1

    binary_matrix_rank_test_result = Matrix.binary_matrix_rank_text(binary_data)[1]
    if binary_matrix_rank_test_result:
        x += 1

    dft_test_result = SpectralTest.spectral_test(binary_data)[1]
    if dft_test_result:
        x += 1

    non_overlapping_test_result = TemplateMatching.non_overlapping_test(binary_data)[1]
    if non_overlapping_test_result:
        x += 1

    overlapping_test_result = TemplateMatching.overlapping_patterns(binary_data)[1]
    if overlapping_test_result:
        x += 1

    maurers_universal_test_result = Universal.statistical_test(binary_data)[1]
    if maurers_universal_test_result:
        x += 1

    linear_complexity_test_result = ComplexityTest.linear_complexity_test(binary_data)[1]
    if linear_complexity_test_result:
        x += 1

    serial_test_result = Serial.serial_test(binary_data)[1]
    if serial_test_result:
        x += 1

    cumulative_sums_test_result = CumulativeSums.cumulative_sums_test(binary_data)[1]
    if cumulative_sums_test_result:
        x += 1

    random_excursions_test_result = RandomExcursions.random_excursions_test(binary_data)[1]
    if random_excursions_test_result:
        x += 1

    random_excursion_variant_test_result = RandomExcursions.variant_test(binary_data)[1]
    if random_excursion_variant_test_result:
        x += 1

    autocorrelation_test_result = AutocorrelationTest.autocorrelation_test(binary_data)[1]
    if autocorrelation_test_result:
        x += 1

    adaptive_statistical_test_result = AdaptiveStatisticalTest.adaptive_statistical_test(binary_data)[1]
    if adaptive_statistical_test_result:
        x += 1

    # Now x contains the count of tests that returned True
    # print("Number of tests that returned True:", x)
    final_text='random number' if x > 10 else 'non-random number'


    # Dynamically set the result text based on the test outcome
    frequency_test_text = 'random number' if frequency_test_result else 'non-random number'
    frequency_test_block_text = 'random number' if frequency_test_block_result else 'non-random number'
    runs_text = 'random number' if runs_test_result else 'non-random number'
    approximate_entropy_text = 'random number' if approximate_entropy_test_result else 'non-random number'
    longest_run_of_ones_text = 'random number' if longest_run_of_one_test_result else 'non-random number'
    binary_matrix_rank_text = 'random number' if binary_matrix_rank_test_result else 'non-random number'
    dft_text = 'random number' if dft_test_result else 'non-random number'
    non_overlapping_text = 'random number' if non_overlapping_test_result else 'non-random number'
    overlapping_text = 'random number' if overlapping_test_result else 'non-random number'
    maurers_universal_text = 'random number' if maurers_universal_test_result else 'non-random number'
    linear_complexity_text = 'random number' if linear_complexity_test_result else 'non-random number'
    serial_text = 'random number' if serial_test_result else 'non-random number'
    cumulative_sums_text = 'random number' if cumulative_sums_test_result else 'non-random number'
    random_excursion_variant_text = 'random number' if random_excursion_variant_test_result else 'non-random number'
    random_excursion_text = 'random number' if random_excursions_test_result else 'non-random number'
    autocorrelation_text = 'random number' if autocorrelation_test_result else 'non-random number'
    adaptive_statistical_text = 'random number' if adaptive_statistical_test_result else 'non-random number'

    # Sample Table Data for the first table with "Final Result" in the last row
    data1 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Frequency Test', styles['Normal']), frequency_test_text,
         Paragraph('2. Frequency Test within a Block', styles['Normal']), frequency_test_block_text],
        [Paragraph('3. Runs Test', styles['Normal']), runs_text,
         Paragraph('4. Test for the longest Run of Ones', styles['Normal']), longest_run_of_ones_text],
        [Paragraph('5. Binary Matrix Rank Test', styles['Normal']), binary_matrix_rank_text,
         Paragraph('6. Discrete Fourier Transform Test', styles['Normal']), dft_text],
        [Paragraph('7. Non-overlapping Template Match', styles['Normal']), non_overlapping_text,
         Paragraph('8. Overlapping Template Matching Test', styles['Normal']), overlapping_text],
        [Paragraph('9. Maurers Universal test', styles['Normal']), maurers_universal_text,
         Paragraph('10. Linear complexity Test', styles['Normal']), linear_complexity_text],
        [Paragraph('11. Serial Test', styles['Normal']), serial_text,
         Paragraph('12. Approximate Entropy Test', styles['Normal']), approximate_entropy_text],
        [Paragraph('13. Cumulative Sum Test', styles['Normal']), cumulative_sums_text,
         Paragraph('14. Random Excursions Test', styles['Normal']), random_excursion_text],
        [Paragraph('15. Random Excursions Variant Test', styles['Normal']), random_excursion_variant_text,
         Paragraph('16. Autocorrelation Test', styles['Normal']), autocorrelation_text],
        [Paragraph('17. Adaptive Statistical Test', styles['Normal']), adaptive_statistical_text],
        [Paragraph(' Final Result', styles['Normal']), final_text],
       
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
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Center vertically
    ]))

    # Create the second table with graphical analysis
    data2 = [
        [Image(graph_image_io, width=400, height=300)]
    ]
    table2 = Table(data2, colWidths=[4 * inch])
    table2.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')]))

    # Build the PDF document
    elements = [title, title_space, nist_subtitle, subtitle_space, table1, subtitle_space, graph_subtitle, table2]
    doc.build(elements)

    # Get the PDF data and write it to the response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

def generate_pdf_report_dieharder(request):
    global global_graph_image

    binary_data = request.GET.get('binary_data', '')

    binary_data = binary_data.replace('%0A', '').replace('%20', '').replace(' ', '').replace('\n', '').replace('\r', '')


    # Create a HttpResponse object with PDF headers
    graph_response = create_graph_dieharder(request)
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

    nist_subtitle = Paragraph("Dieharder Tests:", subtitle_style)
    # other_tests_subtitle = Paragraph("Other Tests:", subtitle_style)
    graph_subtitle = Paragraph("Graphical Analysis:", subtitle_style)

    subtitle_space = Spacer(1, 0.0 * inch)  # Spacer below the subtitles


    x = 0

    # Perform tests and increment x for each test that returns True
    birthday_test_result = BirthdaySpacingsTest.BirthdaySpacingsTest(binary_data)[1]
    x += 1 if birthday_test_result else 0

    parking_test_block_result = ParkingLotTest.ParkingLotTest(binary_data)[1]
    x += 1 if parking_test_block_result else 0

    overlapping_5_test_result = Overlapping5PermutationTest.Overlapping5PermutationTest(binary_data)[1]
    x += 1 if overlapping_5_test_result else 0

    minimum_distance_test_result = MinimumDistanceTest.MinimumDistanceTest(binary_data)[1]
    x += 1 if minimum_distance_test_result else 0

    rank_31_test_result = Ranks31x31MatricesTest.Ranks31x31MatricesTest(binary_data)[1]
    x += 1 if rank_31_test_result else 0

    spheres_test_result = Spheres3DTest.Spheres3DTest(binary_data)[1]
    x += 1 if spheres_test_result else 0

    rank_32_result = Ranks32x32MatricesTest.Ranks32x32MatricesTest(binary_data)[1]
    x += 1 if rank_32_result else 0

    craps_test_result = CrapsTest.CrapsTest(binary_data)[1]
    x += 1 if craps_test_result else 0

    bitstream_test_result = BitstreamTest.BitstreamTest(binary_data)[1]
    x += 1 if bitstream_test_result else 0

    gcd_test_result = MarsagliaTsangGCDTest.MarsagliaTsangGCDTest(binary_data)[1]
    x += 1 if gcd_test_result else 0

    opso_test_result = OPSOTest.OPSOTest(binary_data)[1]
    x += 1 if opso_test_result else 0

    oqsq_test_result = OQSOTest.OQSOTest(binary_data)[1]
    x += 1 if oqsq_test_result else 0

    dna_test_result = DNATest.DNATest(binary_data)[1]
    x += 1 if dna_test_result else 0

    count_one_stream_test_result = CountThe1sStreamTest.CountThe1sStreamTest(binary_data)[1]
    x += 1 if count_one_stream_test_result else 0

    count_one_byte_test_result = CountThe1sByteTest.CountThe1sByteTest(binary_data)[1]
    x += 1 if count_one_byte_test_result else 0

    simple_gcd_test_result = MarsagliaTsangSimpleGCDTest.MarsagliaTsangSimpleGCDTest(binary_data)[1]
    x += 1 if simple_gcd_test_result else 0

    generalized_minimum_test_result = GeneralizedMinimumDistanceTest.GeneralizedMinimumDistanceTest(binary_data)[1]
    x += 1 if generalized_minimum_test_result else 0

    u01_linear_complexity_test_result = TestU01LinearComplexityTest.TestU01LinearComplexityTest(binary_data)[1]
    x += 1 if u01_linear_complexity_test_result else 0

    u01_longest_repeated_test_result = TestU01LongestRepeatedSubstringTest.TestU01LongestRepeatedSubstringTest(binary_data)[1]
    x += 1 if u01_longest_repeated_test_result else 0

    u01_matrix_rank_test_result = TestU01MatrixRankTest.TestU01MatrixRankTest(binary_data)[1]
    x += 1 if u01_matrix_rank_test_result else 0


    final_text='random number' if x > 10 else 'non-random number'

    print('hi sir random',x)

    # Dynamically set the result text based on the test outcome
    birthday_text = 'random number' if birthday_test_result else 'non-random number'
    parking_text= 'random number' if parking_test_block_result else 'non-random number'
    oevrlapping_5_text= 'random number' if overlapping_5_test_result else 'non-random number'
    minimum_distance_text= 'random number' if minimum_distance_test_result else 'non-random number'
    rank31x31_text= 'random number' if rank_31_test_result else 'non-random number'
    spheres_text= 'random number' if spheres_test_result else 'non-random number'
    rank32x32_text= 'random number' if rank_32_result else 'non-random number'
    craps_text= 'random number' if craps_test_result else 'non-random number'
    bitstream_text= 'random number' if bitstream_test_result else 'non-random number'
    gcd_text= 'random number' if gcd_test_result else 'non-random number'
    opso_text= 'random number' if opso_test_result else 'non-random number'
    oqsq_text= 'random number' if oqsq_test_result else 'non-random number'
    dna_text= 'random number' if dna_test_result else 'non-random number'
    one_stream_text= 'random number' if count_one_stream_test_result else 'non-random number'
    one_byte_text= 'random number' if count_one_byte_test_result else 'non-random number'
    simple_gcd_text= 'random number' if simple_gcd_test_result else 'non-random number'
    generalised_minimum_text= 'random number' if generalized_minimum_test_result else 'non-random number'
    u01_linear_text= 'random number' if u01_linear_complexity_test_result else 'non-random number'
    u01longest_text= 'random number' if u01_longest_repeated_test_result else 'non-random number'
    u01_matrix_text= 'random number' if u01_matrix_rank_test_result else 'non-random number'




    # Sample Table Data for the first table with "Final Result" in the last row
    data1 = [
        [Paragraph('Test type', styles['Normal']), 'Result', 'Test type', 'Result'],
        [Paragraph('1. Birthday Spacing', styles['Normal']), birthday_text, Paragraph('2. Parking Lot Test', styles['Normal']), parking_text],
        [Paragraph('3. Overlapping 5 Permutation', styles['Normal']), oevrlapping_5_text, Paragraph('4. Minimum Distance Test', styles['Normal']), minimum_distance_text],
        [Paragraph('5. Ranks of 31x31 Test', styles['Normal']), rank31x31_text, Paragraph('6. 3d Spheres Test', styles['Normal']), spheres_text],
        [Paragraph('7. Ranks of 32x32 Test', styles['Normal']), rank32x32_text, Paragraph('8. Craps Test', styles['Normal']), craps_text],
        [Paragraph('9. Bitstream test', styles['Normal']), bitstream_text, Paragraph('10. Marsaglia-Tsang GCD Test', styles['Normal']), gcd_text],
        [Paragraph('11. OPSO Test', styles['Normal']), opso_text, Paragraph('12. OQSO Test', styles['Normal']),oqsq_text],
        [Paragraph('13. DNA Test', styles['Normal']), dna_text, Paragraph('14. Count the Ones(Stream) Test', styles['Normal']), one_stream_text],
        [Paragraph('15. Count the Ones(Bytes) Test', styles['Normal']),one_byte_text,Paragraph('16. Marsalia-Tsang Simple GCD Test', styles['Normal']), simple_gcd_text],
        [Paragraph('17. Generalized Minimum DIstance Test', styles['Normal']),generalised_minimum_text,Paragraph('18. TestU01 Linear Complexity Test', styles['Normal']), u01_linear_text],
        [Paragraph('18. TestU01 Longest Repeated Substring Test', styles['Normal']), u01longest_text,Paragraph('20. TestU01 Matrix Rank Test', styles['Normal']),u01_matrix_text],
        [Paragraph(' Final Result', styles['Normal']), final_text],
       
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
    # elements.append(other_tests_subtitle)
    elements.append(subtitle_space)  # Spacer below the second subtitle
    # elements.append(table2)
    elements.append(graph_subtitle)
    elements.append(subtitle_space)  # Spacer below the graph subtitle
    elements.append(graph_image)
    
    doc.build(elements)

    # Write the PDF to the HttpResponse
    response.write(buffer.getvalue())
    buffer.close()

    return response

