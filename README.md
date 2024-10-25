# **Project Documentation**

## **How to Run the Project**

### **Step 1: Set Up Virtual Environment**

1. **Download the Project Files**: After downloading the project files, open a terminal window in the project directory.

2. **Create a Virtual Environment**: Use the following command to create a virtual environment:
   ```bash
   python -m venv my_env
   ```

3. **Activate the Virtual Environment**: Once created, activate the virtual environment with the following command:
   ```bash
   my_env\Scripts\activate
   ```

4. **Install Required Packages**: Install all dependencies listed in `requirements.txt` by running:
   ```bash
    pip install -r requirements.txt
   ```
### **Step 2: Run The Project**

1. **Navigate to the Django Project Directory**: Ensure you're in the directory containing `manage.py`.

2. **Start the Django Server**:  Run the following command to start the server:
   ```bash
    python manage.py runserver
   ```
3. **Access the API Endpoint**:  Once the server is running, you can interact with the API using a tool like Postman. The API endpoint for predictions is:
    ```ruby
    http://127.0.0.1:8000/api/predict/
    ```
4. **Send a POST Request in Postman**: 
* Method: `POST`
* URL: `http://127.0.0.1:8000/api/predict/`
* Body: Select `raw` and choose `JSON` as the data format. Use the following JSON structure as a sample request:

  ```json
    {
        "Num_Children": [1],
        "Gender": ["Male"],
        "Income": [75236],
        "Own_Car": ["Yes"],
        "Own_Housing": ["No"]
    }
  ```

5. **Expected API Response: After sending the request, you should receive a response similar to this**
    ```json
    {
        "Prediction": [0]
    }
    ```

6. **Sample Actual Value for Comparison: Here’s an example of an actual test value:**
    ```json
    {
        "Num_Children": [1],
        "Gender": ["Male"],
        "Income": [75236],
        "Own_Car": ["Yes"],
        "Own_Housing": ["No"],
        "Credit_Card_Issuing": ["Denied"] ("Denied" means 0)
    }
    ```
    
7. **Deactivate Virtual Environment**: deactivate the virtual environment when you are done, like this in the terminal:
    ```bash
    deactivate
    ```

**Ensure you keep the virtual environment activated while running the project and installing any additional dependencies in the future.**

**Enjoy using the project!**
