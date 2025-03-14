
![Untitled video - Made with Clipchamp (3) (5)](https://github.com/user-attachments/assets/00ba1b4c-065c-4282-bc32-5382f673eeb9)

# Lung-Disease-Identification

This repository contains a deep learning model designed to classify lung conditions into three categories: **Normal**, **COVID-19**, and **Viral Pneumonia**. The model leverages convolutional neural networks (CNNs) and is trained on chest X-ray images to provide accurate and efficient diagnoses. When tested on **unseen data** the model provided an astonishing **93.94%** accuracy, precision and recall. and when it comes to false positives the model **doesn't** predict any disease case as normal. You can try it yourself by using the test folder provided.

---

### Features:
- **Multi-class Classification**: Distinguishes between normal lungs, COVID-19, and viral pneumonia.
- **Pretrained Model Integration**: Utilizes transfer learning for improved accuracy and reduced training time.
- **User-Friendly Interface**: Streamlit-based application for easy uploading of X-ray images and viewing predictions.
- **Open Source**: Fully documented and customizable for further research and development.

---

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/Leosce/Lung-Disease-Identification/tree/main
   cd LungDiseaseIdentification
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/MacOS
   env\Scripts\activate     # For Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Usage:
1. Start the Streamlit application:
   ```bash
   streamlit run Lung_Disease_App.py
   ```
2. Upload your chest X-ray image through the application interface.
3. View the prediction result in real-time, indicating whether the lung condition is **Normal**, **COVID-19**, or **Viral Pneumonia**.

![uploads_image_5G7gtQBlL1VcRrAvXCN3OWq9doEpsx_Untitled-video---Made-with-Clipchamp-(4)](https://github.com/user-attachments/assets/d4a41a26-1ed8-43cc-a87f-65a93c02238e)

---

### Requirements:
- **Python** 3.8+
- **Streamlit** for creating the user interface
- Dependencies listed in `requirements.txt` (e.g., TensorFlow, NumPy, Pandas, etc.)

Ensure TensorFlow is configured properly for GPU (if available) to enhance performance.

---

### License:
This project is licensed under the [MIT License](LICENSE). By using this repository, you agree to abide by the terms of the license. Ensure compliance with the licensing terms of any datasets or external libraries used.

---

### Acknowledgments
- The dataset used in this project is provided by **Adel Mukashova** on Kaggle. You can find it here: [Covid-19 Image Dataset](https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset/data). This dataset is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

