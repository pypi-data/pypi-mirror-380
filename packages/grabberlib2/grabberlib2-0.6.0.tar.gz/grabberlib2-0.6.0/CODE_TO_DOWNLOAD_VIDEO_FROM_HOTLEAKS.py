import requests
import subprocess
import os
from urllib.parse import urljoin

def download_hls_video(m3u8_url, output_filename="output.mp4"):
    """
    Downloads a video from an HLS (.m3u8) stream
    
    Args:
        m3u8_url (str): URL of the master .m3u8 playlist
        output_filename (str): Name for the output file
    """
    try:
        # Option 1: Use ffmpeg (recommended - handles HLS natively)
        try:
            print(f"Downloading using ffmpeg from: {m3u8_url}")
            subprocess.run([
                'ffmpeg',
                '-i', m3u8_url,
                '-c', 'copy',  # Copy streams without re-encoding
                '-bsf:a', 'aac_adtstoasc',  # Fix audio bitstream
                output_filename
            ], check=True)
            print(f"Successfully downloaded to {output_filename}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg failed: {e}")
        
        # Option 2: Manual download (fallback)
        print("Attempting manual download...")
        
        # Get the master playlist
        response = requests.get(m3u8_url)
        if response.status_code != 200:
            print(f"Failed to fetch playlist: HTTP {response.status_code}")
            return False
            
        playlist = response.text
        base_url = m3u8_url.rsplit('/', 1)[0] + '/'
        
        # Find all segment URLs
        segment_urls = [urljoin(base_url, line.strip()) 
                       for line in playlist.split('\n') 
                       if line and not line.startswith('#')]
        
        if not segment_urls:
            print("No segments found in playlist")
            return False
            
        print(f"Found {len(segment_urls)} segments")
        
        # Download all segments
        ts_files = []
        for i, segment_url in enumerate(segment_urls):
            ts_filename = f"segment_{i}.ts"
            try:
                with requests.get(segment_url, stream=True) as r:
                    r.raise_for_status()
                    with open(ts_filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                ts_files.append(ts_filename)
                print(f"Downloaded segment {i+1}/{len(segment_urls)}")
            except Exception as e:
                print(f"Failed to download segment {i}: {e}")
        
        # Combine segments (requires ffmpeg)
        if ts_files:
            try:
                with open('file_list.txt', 'w') as f:
                    for ts_file in ts_files:
                        f.write(f"file '{ts_file}'\n")
                
                subprocess.run([
                    'ffmpeg',
                    '-f', 'concat',
                    '-safe', '0',
                    '-i', 'file_list.txt',
                    '-c', 'copy',
                    output_filename
                ], check=True)
                print(f"Successfully combined segments to {output_filename}")
                
                # Clean up temporary files
                for ts_file in ts_files:
                    os.remove(ts_file)
                os.remove('file_list.txt')
                
                return True
            except Exception as e:
                print(f"Failed to combine segments: {e}")
        
        return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

import requests
from bs4 import BeautifulSoup
import re
import time

def get_fresh_m3u8_url(page_url):
    """Fetches current m3u8 URL from the page"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # 1. Load the video page
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()
        
        # 2. Find the video element
        soup = BeautifulSoup(response.text, 'html.parser')
        video_div = soup.find('div', {'data-video': True})
        
        if not video_div:
            raise ValueError("No video element found")
            
        # 3. Extract fresh URL (may need to parse JS)
        # Alternative: Use regex to find all potential URLs
        urls = re.findall(
            r'https?://cdn\d+\.hotleaks\.tv/[^/]+/\d+/sdb\d+/\d+/\d+/index\.m3u8',
            response.text
        )
        
        if urls:
            return urls[0]
            
        raise ValueError("No m3u8 URL found in page")
        
    except Exception as e:
        print(f"Error fetching fresh URL: {e}")
        return None

# Usage:
page_url = "https://hotleaks.tv/your-video-page"
m3u8_url = get_fresh_m3u8_url(page_url)

if m3u8_url:
    print(f"Fresh URL: {m3u8_url}")
    # Now use the download function from previous examples
else:
    print("Failed to get current URL")

import requests
import base64
import re
from urllib.parse import urljoin
import m3u8
import subprocess

def download_video_from_data_video(website_url, data_video_content):
    # Extract the src from the data-video JSON
    try:
        # Clean the JSON string (it uses single quotes which isn't valid JSON)
        cleaned_json = data_video_content.replace("'", '"')
        
        # Parse the JSON to get the src
        import json
        video_data = json.loads(cleaned_json)
        encoded_src = video_data['source'][0]['src']
        
        # Try decoding the src (might be Base64)
        try:
            decoded_src = base64.b64decode(encoded_src).decode('utf-8')
        except:
            decoded_src = encoded_src  # if not base64, use as-is
            
        # Construct full URL if needed
        if not decoded_src.startswith(('http://', 'https://')):
            decoded_src = urljoin(website_url, decoded_src)
            
        print(f"Video source: {decoded_src}")
        
        # Download options:
        # Option 1: Use ffmpeg (recommended for HLS)
        try:
            output_file = "output.mp4"
            subprocess.run([
                'ffmpeg', '-i', decoded_src, 
                '-c', 'copy', 
                '-bsf:a', 'aac_adtstoasc', 
                output_file
            ], check=True)
            print(f"Video downloaded successfully as {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg failed: {e}")
            # Option 2: Fallback to requests (may not work for HLS)
            try:
                response = requests.get(decoded_src, stream=True)
                with open('video.ts', 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        f.write(chunk)
                print("Video segments downloaded (may need merging)")
            except Exception as e:
                print(f"Download failed: {e}")
                
    except Exception as e:
        print(f"Error processing video data: {e}")

# Example usage:
website_url = "https://hotleaks.tv"  # replace with actual website URL
data_video_content = """{'source': [{'src':'ubnMTqrVwgpEXRCE4U3Mt5CelRmbp9SO3cjN5QDOx8yN2ADMy8CNzIGZz9SM5gzN2gDM1cTMs0TPnl0byRmQ1hHN0BHaQ52Z3hUcVd2RW9id05ycrFWZsR3bo5CNz4GZj9yL6MHc0RHafzVysvQJoVklfY8F', 'type':'application/x-mpegURL'}], 'attributes': {'preload': true, 'playsinline': false, 'controls': true ,'poster':'https://hotleaks.tv/storage/images/4f41/11a3de9/11a3de9.webp'}}"""

download_video_from_data_video(website_url, data_video_content)



