# Image Classification Website using Deep Learning 🐼🐶🐱

**Developed by Muhammad Umaid Ehsan**

This project is a web-based Image Classification application built using **Python, Flask, and Deep Learning**. It uses a **ResNet model** to analyze uploaded images and predict their contents.

Users can upload an image through the website and view the model's classification result in their browser.

## 🚀 Features

- Upload images for classification.
- Predict image contents using a pre-trained ResNet deep-learning model.
- Simple and user-friendly web interface.
- Built with Flask, HTML, CSS, and Python.
- Displays classification results on the website.

## 🛠️ Technologies Used

- Python
- Flask
- TensorFlow / Keras
- NumPy
- ResNet deep-learning model
- HTML and CSS

## 📋 Requirements

- Python installed on your system.
- Required Python libraries.
- The trained model file: `model_resnet.h5`.

Install the required libraries in your virtual environment:

```bash
pip install flask numpy tensorflow keras
```

*Note: Depending on the original model and your Python version, compatible TensorFlow and Keras versions may be required.*

## ⚙️ How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/umaidehsan/Image-Classification-Flask.git
```

**2. Open the project directory**

```bash
cd Image-Classification-Flask
```

**3. Activate your virtual environment (if you have one)**

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**4. Run the Flask application**

```bash
python app.py
```

**5. Open the website**

Visit the following URL in your browser:

http://127.0.0.1:5000/

## 📂 Project Structure

```text
Image-Classification-Flask/
├── app.py
├── model_resnet.h5
├── templates/
│   ├── base.html
│   └── index.html
├── static/
├── uploads/
├── .gitignore
└── README.md
```

## 👨‍💻 Developer

**Muhammad Umaid Ehsan**

GitHub: [@umaidehsan](https://github.com/umaidehsan)

## 📌 Project Purpose

This project demonstrates how deep-learning image classification can be integrated into a web application using Flask, allowing users to upload images and receive predictions through a browser-based interface.

---

⭐ If you find this project useful, feel free to star the repository!
