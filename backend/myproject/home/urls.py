# myproject/home/urls.py

from django.urls import path
from . import views
from .views import sse_binary_view,sse_binary_example_view


urlpatterns = [
    
    
    path('run_frequency_test/', views.run_frequency_test, name='run_frequency_test'),
    path('run_frequency_block_test/', views.run_frequency_block_test, name='run_frequency_block_test'),
    path('run_runs_test/', views.run_runs_test, name='run_runs_test'),
    path('run_longest_one_block_test/', views.run_longest_one_block_test, name='run_longest_one_block_test'),
    path('run_approximate_entropy_test/',views.run_approximate_entropy_test, name='run_approximate_entropy_test'),
    path('run_linear_complexity_test/',views.run_linear_complexity_test, name='run_linear_test'),
    path('run_non_overlapping_test/',views.run_non_overlapping_test, name='run_non_overlapping_test'),
    path('run_overlapping_test/',views.run_overlapping_test, name='run_overlapping_test'),
    path('run_statistical_test/',views.run_statistical_test, name='run_statistical_test'),
    path('run_serial_test/',views.run_serial_test, name='run_serial_test'),
    path('run_cumulative_sums_test/',views.run_cumulative_sums_test, name='run_cumulative_sums_test'),
    path('random_excursions_test/',views.run_random_excursions_test, name='run_random_excursions_test'),
    path('random_excursions_variant_test/',views.random_excursions_variant_test, name='random_excursions_variant_test'),
    path('run_binary_matrix_rank_text/',views.run_binary_matrix_rank_text, name='run_binary_matrix_rank_test'),
    path('run_spectral_test/',views.run_spectral_test, name='run_spectral_test'),

    path('run_autocorrelation_test/',views.run_autocorrelation_test, name='run_autocorrelation_test'),
    path('run_adaptive_statistical_test/',views.run_adaptive_statistical_test, name='adaptive_statistical_test'),

    path('binary-data/', views.send_binary_data, name='send_binary_data'),

    #live streaming
    path('stream-binary/', sse_binary_view, name='sse_binary_view'),
    path('sse_binary_example/', sse_binary_example_view, name='sse_binary_example_view'),
    
    #report generation
    path('pdf-report/', views.generate_pdf_report, name='generate_pdf_report'),
    #graph generation
    path('graph-generation/', views.create_graph, name='create_graph'),
]

# http://127.0.0.1:8000/sse_binary_example/