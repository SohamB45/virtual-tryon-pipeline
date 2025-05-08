# import streamlit as st
# import os
# import subprocess
# import sys

# st.write(f"Python Executable: {sys.executable}")  # Debugging
# st.write(f"Virtual Environment: {os.getenv('VIRTUAL_ENV')}")  # Debugging

# # Paths
# PROJECT_DIR = "E:/ML/VITON-HD"
# IMAGE_DIR = os.path.join(PROJECT_DIR, "datasets/test/image")
# CLOTH_DIR = os.path.join(PROJECT_DIR, "datasets/test/cloth")
# PAIRS_FILE = os.path.join(PROJECT_DIR, "datasets/test_pairs.txt")
# RESULT_DIR = os.path.join(PROJECT_DIR, "results/VITONHD/test/try-on")

# st.title("Virtual Try-On with VITON-HD")

# # Select Person Image
# person_images = sorted(os.listdir(IMAGE_DIR))
# selected_person = st.selectbox("Choose a person image:", person_images)

# # Select Clothing Image
# cloth_images = sorted(os.listdir(CLOTH_DIR))
# selected_cloth = st.selectbox("Choose a clothing image:", cloth_images)

# # Display selected images
# col1, col2 = st.columns(2)
# with col1:
#     st.image(os.path.join(IMAGE_DIR, selected_person), caption="Selected Person", use_container_width=True)
# with col2:
#     st.image(os.path.join(CLOTH_DIR, selected_cloth), caption="Selected Clothing", use_container_width=True)

# if st.button("Generate Try-On Result"):
#     with st.spinner("Generating... Please wait!"):
#         # **Update the first line of test_pairs.txt**
#         if os.path.exists(PAIRS_FILE):
#             with open(PAIRS_FILE, "r") as f:
#                 pairs = f.readlines()
#         else:
#             pairs = []

#         # Replace the first line with the new selection
#         if pairs:
#             pairs[0] = f"{selected_person} {selected_cloth}\n"
#         else:
#             pairs.append(f"{selected_person} {selected_cloth}\n")

#         # Write back to the file
#         with open(PAIRS_FILE, "w") as f:
#             f.writelines(pairs)

#         st.write(f"Updated test_pairs.txt:\n{pairs}")  # Debugging output

#         # **Run the VITON-HD test script**
#         PYTHON_EXEC = sys.executable  # Ensure correct Python is used
#         command = [PYTHON_EXEC, "test.py", "--name", "VITONHD", "--dataset_mode", "test"]
#         st.write(f"Running command: {command}")  # Debug info

#         try:
#             result = subprocess.run(
#                 command,
#                 cwd=PROJECT_DIR,  # Set working directory correctly
#                 capture_output=True,
#                 text=True,
#                 env=os.environ.copy(),  # Preserve environment variables
#             )
#             st.write("Command Output:", result.stdout)  # Show output logs
#             if result.stderr:
#                 st.error(f"Error:\n{result.stderr}")
#         except subprocess.CalledProcessError as e:
#             st.error(f"Error occurred: {e}")

#         # **Check if result exists**
#         result_image_path = os.path.join(RESULT_DIR, selected_person.replace('.jpg', '_output.jpg'))
#         if os.path.exists(result_image_path):
#             st.image(result_image_path, caption="Try-On Result", use_container_width=True)
#         else:
#             st.error("Something went wrong! Check logs.")

import streamlit as st
import os
import subprocess
import sys
import time

# Paths
PROJECT_DIR = "F:/Vton-conda"  # Update if needed
IMAGE_DIR = os.path.join(PROJECT_DIR, "datasets/test/image")
CLOTH_DIR = os.path.join(PROJECT_DIR, "datasets/test/cloth")
PAIRS_FILE = os.path.join(PROJECT_DIR, "datasets/test_pairs.txt")
RESULT_DIR = os.path.join(PROJECT_DIR, "results/VITONHD/")  # Corrected result directory

st.title("Virtual Try-On with VITON-HD")

# Debugging Paths
# st.write("Checking directories...")
# for path, name in [
#     (IMAGE_DIR, "Image Directory"),
#     (CLOTH_DIR, "Cloth Directory"),
#     (RESULT_DIR, "Result Directory")
# ]:
#     exists = os.path.exists(path)
#     st.write(f"{name}: {path} - {'Exists' if exists else 'Missing'}")
#     if not exists:
#         st.error(f"Directory does not exist: {path}")

if not all(os.path.exists(path) for path in [IMAGE_DIR, CLOTH_DIR, RESULT_DIR]):
    st.error("One or more required directories are missing! Check paths above.")
    st.stop()

# Select Person Image
person_images = sorted(os.listdir(IMAGE_DIR))
selected_person = st.selectbox("Choose a person image:", person_images)

# Select Clothing Image
cloth_images = sorted(os.listdir(CLOTH_DIR))
selected_cloth = st.selectbox("Choose a clothing image:", cloth_images)

# Display selected images
col1, col2 = st.columns(2)
with col1:
    st.image(os.path.join(IMAGE_DIR, selected_person), caption="Selected Person", use_container_width=True)
with col2:
    st.image(os.path.join(CLOTH_DIR, selected_cloth), caption="Selected Clothing", use_container_width=True)

# if st.button("Generate Try-On Result"):
#     with st.spinner("Generating... Please wait!"):
#         # **Format the result filename correctly: "00006_00008_00.jpg"**
#         person_id = selected_person.split(".")[0]  # Extract only '00006_00'
#         cloth_id = selected_cloth.split(".")[0]  # Extract only '00005_00'

#         person_num = person_id.split("_")[0]  # "00006"
#         cloth_num = cloth_id.split("_")[0] 
#         # Construct filename in desired format
#         result_filename = f"{person_num}_{cloth_num}_00.jpg"

#         # **Write the selected pair to test_pairs.txt**
#         with open(PAIRS_FILE, "w") as f:
#             f.write(f"{person_id} {cloth_id}\n")
#             f.flush()  # Ensure file is written before proceeding
#             os.fsync(f.fileno())  # Force write to disk (Windows/Linux)

#         # **Check if test_pairs.txt is written correctly**
#         st.write("Contents of test_pairs.txt:")
#         with open(PAIRS_FILE, "r") as f:
#             pairs_content = f.read()
#         st.code(pairs_content)  # Show contents in Streamlit

#         # **Run the VITON-HD test script**
#         PYTHON_EXEC = sys.executable  # Ensure using the correct Python
#         command = [PYTHON_EXEC, "test.py", "--name", "VITONHD", "--dataset_mode", "test"]
#         st.write(f"Running command: {command}")  # Debug info

#         try:
#             result = subprocess.run(
#                 command,
#                 cwd=PROJECT_DIR,
#                 capture_output=True,
#                 text=True,
#                 env=os.environ.copy(),
#             )
#             st.write("Command Output:", result.stdout)
#             if result.stderr:
#                 st.error(f"Error:\n{result.stderr}")
#         except Exception as e:
#             st.error(f"Unexpected error occurred: {e}")

#         # **Check if result exists in the correct format**
#         result_image_path = os.path.join(RESULT_DIR, result_filename)
#         st.write(f"Looking for result image: {result_image_path}")  # Debug output

#         # **Wait briefly to ensure result file is written**
#         time.sleep(3)  # Some processes take time to write output

#         if os.path.exists(result_image_path):
#             st.image(result_image_path, caption="Try-On Result", use_container_width=True)
#         else:
#             st.error("Result image not found! Check logs.")

if st.button("Generate Try-On Result"):
    with st.spinner("Generating... Please wait!"):
        # Extract IDs (preserve original format for test_pairs.txt)
        person_id = selected_person    #.split(".")[0]  # "00006_00"
        cloth_id = selected_cloth    #.split(".")[0]    # "00005_00"
        
        # Generate expected output filename format
        person_num = person_id.split("_")[0]  # "00006"
        cloth_num = cloth_id.split("_")[0]    # "00005"
        result_filename = f"{person_num}_{cloth_num}_00.jpg"
        
        # Write to test_pairs.txt (VITON-HD expects original format)
        with open(PAIRS_FILE, "w") as f:
            f.write(f"{person_id} {cloth_id}\n")
            f.flush()
            os.fsync(f.fileno())

        # Prepare test.py command with REQUIRED arguments
        PYTHON_EXEC = sys.executable
        # st.write(f"Using Python: {sys.executable}")

        command = [
            
    "conda", "run", "--no-capture-output", "-n", "vton-fixed", "python",
    os.path.join(PROJECT_DIR, "test.py"), "--name", "VITONHD", "--dataset_mode", "test"
        ]
        
        
        # st.write("Running command:", " ".join(command))
        
        try:
            # Run with timeout (60 seconds)
            result = subprocess.run(
                command,
                cwd=PROJECT_DIR,
                capture_output=True,
                text=True,
                timeout=60,
                env=os.environ.copy()
            )
            
            # Show full execution logs
            # st.code(f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
            
            if result.returncode != 0:
                st.error(f"test.py failed with exit code {result.returncode}")
                st.stop()
                
        except subprocess.TimeoutExpired:
            st.error("test.py timed out after 60 seconds")
            st.stop()
        except Exception as e:
            st.error(f"Failed to execute test.py: {str(e)}")
            st.stop()

        # Check for results in the CORRECT location
        RESULT_DIR = os.path.join(PROJECT_DIR, "results/VITONHD/")
        result_path = os.path.join(RESULT_DIR, result_filename)
        
        # Fallback: Search for any matching file pattern
        if not os.path.exists(result_path):
            possible_files = [f for f in os.listdir(RESULT_DIR) 
                           if f.startswith(f"{person_num}_{cloth_num}")]
            if possible_files:
                result_path = os.path.join(RESULT_DIR, possible_files[0])

        if os.path.exists(result_path):
            st.image(result_path, caption="Try-On Result", use_container_width=True)
        else:
            st.error(f"Result not found at: {result_path}")
            st.write("Directory contents:", os.listdir(RESULT_DIR))
