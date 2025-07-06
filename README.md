- [Skin Disease Classification](https://aiformgenerator.onrender.com/)  | Note: not optimized for mobile

# Skin Disease Classification System

A web-based and API-powered system that predicts skin diseases from uploaded images using a CNN model, and provides advice, remedies, and medication suggestions using Gemini AI.

---

## Features

- 📸 Upload infected skin images via web form or REST API  
- 🧬 Predict skin disease using a trained CNN model (`.h5`)  
- 🤖 Generate AI-based advice using Google Gemini API  
- 🧩 RESTful API for integration with mobile/web apps  
- 🔁 HTMX for dynamic frontend updates (no full page reload)  
- 📑 DRF browsable API with file upload support  

---

# Skin Disease Classification REST API

This project provides a RESTful API built using **Django REST Framework (DRF)** to classify skin diseases based on user input and image data. The model predicts the disease and provides personalized advice using **Google Gemini**.

---

## 🔗 API Endpoint

The API can be accessed at:

```

http://127.0.0.1:8000/api/v1/predict/

```

This endpoint accepts a `POST` request with the following inputs:

- **Age**
- **Gender**
- **Image** of the affected skin area

Upon submission, it returns the predicted disease and AI-generated structured advice including:
- General skin care recommendations
- Home remedies
- Potential medications (non-prescriptive)

---

## 🛠 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PiyushJain045/AiForm-Generator.git
   cd AiForm-Generator

2. **Setup a Virtual Environment**:

  ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
 ````

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your Gemini API Key in `.env` file**:

   ```
   GEMINI_API_KEY="your_gemini_1.5_flash_api_key"
   ```

5. **Run Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server**:

   ```bash
   python manage.py runserver
   ```

---

✅ And voilà! Your setup is complete.

Thanks for checking out this repo! 🙌

