import os
import json
import time
class GetAttractions(itinerary):
    # Minimum time spent at an attraction in seconds
    MIN_TIME_FOR_ATTRACTION=300
    # Minimum distance covered at an attraction in metres
    MAX_DISTANCE_COVERED_AT_ATTRACTION=50
    # Maximum time spent at an attraction in seconds
    MAX_TIME_SPEND_AT_ATTRACTION=180000
    # Size of each chunk of location updates read from memory 
    LOCATION_UPDATE_CHUNK_SIZE=100
    
    @classmethod
    def get_significant_locations(self):
        # Read chunk sized updates in loop and get locations
        return significant_locations
    
    @classmethod
    def process_location_update_chunk(self, location_update_chunk):
        # Process each update based on the metrics for determining an attraction 
        return candidate_locations
    
    @classmethod
    def prune_redundant_locations(self, candidate_locations):
        # Remove locations returning same attraction
        return significant_locations
