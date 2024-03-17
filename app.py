# -*- coding: utf-8 -*-

from PIL import Image
import pickle
import os
import streamlit as st
from streamlit_option_menu import option_menu 

st.set_page_config(layout="wide")

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Home', 'About',
                            'Diabetes Prediction','Heart Disease Prediction',
                            'Parkinsons Prediction',
                            ],
                           icons=['', 'info-circle', 'activity','heart','person'],
                           default_index=0)





# Home Page


if selected == 'Home':
    
    st.markdown(
        """
        <h1 style='text-align: center; color:#6a1b9a; font-size: 52px; font-weight: bold;'>Multiple Disease Detection</h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style='text-align: justify; color: black; font-size: 22px;font-family: Arial, sans-serif;'>
            <span style='padding- justify: 80px;'>Welcome</span> to Multiple Disease Detection, a web application designed to predict and detect various diseases using machine learning algorithms.
            This application allows users to input relevant medical data and receive predictions for different diseases including heart disease, diabetes and  Parkinson's disease
            With the power of machine learning, we aim to assist medical professionals and individuals in early detection and proactive management of these diseases.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image('static/img/big_diab.jpg', use_column_width=True)
    with col2:
        st.write("")
        st.write("")
        st.markdown(
            """
            <h2 style='text-align: center; color: #0d47a1; font-size: 40px; font-weight: bold;'>Key Features</h2>
            <div style='text-align:  justify; color: black; font-size: 20px;'>
                <ul style='list-style-type: none;'>
                    <li style='text-align:  justify; color: black; font-size: 20px;'><b>Heart Disease Prediction:</b> Predict the likelihood of heart disease based on patient data.</li>
                    <li style='text-align:  justify; color: black; font-size: 20px;'><b>Diabetes Prediction:</b> Determine the probability of diabetes based on patient characteristics.</li>
                    <li style='text-align:  justify; color: black; font-size: 20px;'><b>Parkinson's Disease Prediction:</b> Assess the risk of Parkinson's disease using machine learning models.</li>
             </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("")
        st.markdown(
        """
        <h2 style='text-align: center; color: #0d47a1; font-size: 36px; font-weight: bold;'>About</h2>
        <div style='text-align:  justify; color: black; font-size: 20px;'>
            <span style='padding- justify: 80px;'>This project </span>is developed as part of a machine learning application to aid in disease detection and risk assessment.
            It leverages the power of Streamlit for the user interface and machine learning models trained on medical datasets.
            The goal is to provide a user-friendly platform for healthcare professionals and individuals to assess disease risks effectively.
        </div>
        """,
        unsafe_allow_html=True
    )
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.image('static/img/machine.jpg', use_column_width=True)
        
    st.write("")
    st.markdown(
        """
        <h2 style='text-align: center; color: #0d47a1; font-size: 36px; font-weight: bold;'>How to Use</h2>
        <div style='text-align:  justify; color: black; font-size: 20px;'>
           <span style='padding- justify: 80px;'> To use</span> this application, simply select the desired prediction category from the sidebar menu. 
            Then, input the relevant information when prompted, and click the corresponding button to view the prediction results.
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns([1, 1])

    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image('static/img/heart disease 2.jpg', use_column_width=True)

    with col2:
         st.write("")
         st.markdown(
        """
        <h2 style='text-align: center; color: #0d47a1; font-size: 36px; font-weight: bold;'>Overview of Diseases</h2>
        <div style='text-align:  justify; color: black; font-size: 20px;'>
            <span style='padding- justify: 80px;'>Heart disease,</span> diabetes and Parkinson's disease are among the most prevalent health concerns worldwide. Heart disease refers to various conditions that affect the heart's function, including coronary artery disease and arrhythmias. Diabetes is a metabolic disorder characterized by high blood sugar levels, resulting from either insufficient insulin production or the body's inability to effectively use insulin. 
        </div>
        """,
        unsafe_allow_html=True
    )
         
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(
        """

        <div style='text-align:  justify; color: black; font-size: 20px;'>
            <span style='padding- justify: 80px;'>Parkinson's disease</span> is a progressive nervous system disorder that affects movement, causing tremors, stiffness, and difficulty with balance and coordination. Early detection, lifestyle modifications, and appropriate medical management are crucial for preventing and managing these diseases effectively.


        </div>
        """,
        unsafe_allow_html=True
    )
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.image('static/img/main.jpg', use_column_width=True)
        
   
# About Page
if selected == 'About':
    st.markdown("<h1 style='text-align: center; color: #0d47a1; font-size: 48px; font-weight: bold;'>About Us</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: #0d47a1; font-size: 36px; font-weight: bold;'>Our Mission</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:  justify; color: #0d47a1; font-size: 24px;'>Empowering individuals with predictive healthcare solutions</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align:  justify; color: black; font-size: 22px;'>
    <span style='padding- justify: 80px;'>At our core,</span> we believe in leveraging the power of machine learning to revolutionize healthcare.
    Our mission is to provide accessible and accurate predictive models for various diseases,
    empowering individuals to take proactive measures for their health.
    </div>
    """, unsafe_allow_html=True)
    st.write('')


    st.markdown("<h2 style='text-align: center; color: #0d47a1; font-size: 48px; font-weight: bold;'>About Diseases</h2>", unsafe_allow_html=True)

    
    st.markdown("<h3 style='text-align:  justify; color: #0d47a1; font-size: 36px;'>Heart Disease</h3>", unsafe_allow_html=True)
    st.markdown("""<div style='text-align:  justify; color: black; font-size: 22px;'><span style='padding- justify: 80px;'>Heart disease</span> describes a range of conditions that affect your heart. Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease; heart rhythm problems (arrhythmias); and heart defects you're born with (congenital heart defects), among others.
    The term "heart disease" is often used interchangeably with the term "cardiovascular disease." Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that can lead to a heart attack, chest pain (angina) or stroke. Other heart conditions, such as those that affect your heart's muscle, valves or rhythm, also are considered forms of heart disease.
    Many forms of heart disease can be prevented or treated with healthy lifestyle choices.</div>""", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align:  justify; color: black; font-size: 20px;'>
        <strong style='text-align:  justify; color: #0d47a1; font-size: 30px;'>Symptoms:</strong><br>
        <span style='padding- justify: 80px;'>Chest pain,</span> chest tightness, chest pressure and chest discomfort (angina)<br>
        <span style='padding- justify: 80px;'>Shortness</span> of breath<br>
        <span style='padding- justify: 80px;'>Pain,</span> numbness, weakness or coldness in your legs or arms if the blood vessels in those <span style='padding- justify: 50px;'> parts</span> of your body are narrowed<br>
        <span style='padding- justify: 80px;'>Pain in the neck,</span> jaw, throat, upper abdomen or back
        </div>
        """, unsafe_allow_html=True)
    st.write("")
    st.markdown("<h3 style='text-align: justify; color: #0d47a1; font-size: 36px;'>Chest Pain Symptoms</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: justify; color: black; font-size: 22px;'>
        Chest pain, also known as angina, can vary in intensity and presentation. Here are the typical symptoms associated with different types of chest pain:
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: justify; color: black; font-size: 20px;'>
        <strong style='color: #0d47a1; font-size: 30px;'>Typical Angina (0):</strong><br>
        Description: This type of chest pain is considered classic or typical angina, often associated with coronary artery disease.<br>
        Symptoms:
        <ul style='list-style-type: none; padding-left: 0; '>
            <li style='font-size: 19px;'>Substernal chest discomfort or pain that may radiate to the neck, jaw, shoulders, back, or arms (usually left arm).</li>
            <li style='font-size: 19px;>Typically triggered by physical exertion or emotional stress.</li>
            <li style='font-size: 19px;>Relieved by rest or nitroglycerin.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: justify; color: black; font-size: 20px;'>
        <strong style='color: #0d47a1; font-size: 30px;'>Atypical Angina (1):</strong><br>
        Description: Atypical angina shares some characteristics with typical angina but may present differently.<br>
        Symptoms:
        <ul style='list-style-type: none; padding-left: 0;'>
            <li style='font-size: 19px;>Chest discomfort or pain that is less predictable in its occurrence or may not be clearly related to exertion.</li>
            <li style='font-size: 19px;>May have less predictable radiation or quality of pain compared to typical angina.</li>
            <li style='font-size: 19px;>May not be relieved as effectively by rest or nitroglycerin.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: justify; color: black; font-size: 20px;'>
        <strong style='color: #0d47a1; font-size: 30px;'>Non-Anginal Pain (2):</strong><br>
        Description: Non-anginal chest pain is chest discomfort that is not related to coronary artery disease.<br>
        Symptoms:
        <ul style='list-style-type: none; padding-left: 0;'>
            <li style='font-size: 19px;>Chest pain or discomfort that does not have the classic features of angina.</li>
            <li style='font-size: 19px;>May be sharp, stabbing, or burning in nature.</li>
            <li style='font-size: 19px;>Often related to other conditions such as musculoskeletal pain, gastrointestinal issues, or anxiety.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: justify; color: black; font-size: 20px;'>
        <strong style='color: #0d47a1; font-size: 30px;'>Asymptomatic (3):</strong><br>
        Description: Asymptomatic individuals do not experience chest pain or discomfort.<br>
        Symptoms:
        <ul style='list-style-type: none; padding-left: 0;'>
            <li style='font-size: 19px;>Lack of any chest pain or discomfort.</li>
            <li  style='font-size: 19px;>These individuals may still have underlying heart disease but do not experience symptoms.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    st.image(r"static\img\heart.png", caption="Heart Disease",use_column_width=True)
    st.markdown("<p style='text-align: center;'>Image Caption</p>", unsafe_allow_html=True)
    # Add information about diabetes
    st.markdown("<h3 style='text-align:  justify; color: #0d47a1; font-size: 36px;'>Diabetes</h3>", unsafe_allow_html=True)
    st.markdown("""<div style='text-align:  justify; color: black; font-size: 22px;'><span style='padding- justify: 80px;'>Diabetes</span> is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.</div>""", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align:  justify; color: black; font-size: 20px;'>
        <strong style='text-align:  justify; color: #0d47a1; font-size: 30px;'>What health problems can people with diabetes develop?</strong><br>
        Over time, high blood glucose leads to problems such as<br>
        <span style='padding- justify: 80px;'>heart disease<br></span>
        <span style='padding- justify: 80px;'>stroke<br></span>
        <span style='padding- justify: 80px;'>kidney disease<br></span>
        <span style='padding- justify: 80px;'>eye problems<br></span>
        <span style='padding- justify: 80px;'>dental disease<br></span>
        <span style='padding- justify: 80px;'>nerve damage<br></span>
        <span style='padding- justify: 80px;'>foot problems<br></span>
        
        """, unsafe_allow_html=True)
    

    

    st.image(r"static\img\diabetes.png", caption="Diabetes", use_column_width=True)

    # Add information about Parkinson's disease
    st.markdown("<h3 style='text-align:  justify; color: #0d47a1; font-size: 36px;'>Parkinson's Disease</h3>", unsafe_allow_html=True)
    st.markdown("""<div style='text-align:  justify; color: black; font-size: 22px;'><span style='padding- justify: 80px;'>Parkinson's disease</span> is a neurodegenerative disorder that affects movement control. It is characterized by the gradual loss of dopamine-producing cells in the brain, leading to a variety of motor symptoms. These symptoms typically include tremors, stiffness, slowness of movement, and impaired balance and coordination.</div>""", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align:  justify; color: black; font-size: 20px;'>
        <strong style='text-align:  justify; color: #0d47a1; font-size: 30px;'>Symptoms</strong><br>
        Over time, high blood glucose leads to problems such as<br>
        <span style='padding- justify: 80px;'> Tremor: Trembling or shaking, usually starting in a limb, often when the body is at rest.<br></span>      
        <span style='padding- justify: 80px;'> Bradykinesia: Slowed movement, making simple tasks difficult and time-consuming.<br></span>
        <span style='padding- justify: 80px;'>Rigidity: Stiffness or inflexibility of the limbs and trunk, leading to decreased range of motion.<br></span>
        <span style='padding- justify: 80px;'> Postural instability: Impaired balance and coordination, increasing the risk of falls.<br></span>     
        <span style='padding- justify: 80px;'>Changes in speech: Soft, slurred, or monotone speech, often accompanied by a reduction in facial expressions.<br></span>
        <span style='padding- justify: 80px;'> Writing changes: Small, cramped handwriting (micrographia) or other writing difficulties.<br></span>      
        <span style='padding- justify: 80px;'> Reduced arm swing: A decreased or absent swinging of the arms while walking.<br></span>       
        """, unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: justify; color: black; font-size: 20px;'>
    <strong style='text-align: justify; color: #0d47a1; font-size: 20px;'>How this Web application Detection Parkinson's Disease </strong><br>
    This system utilizes a voice dataset to detect the presence of Parkinson's disease in individuals. Various features extracted from the voice signals, such as vocal fundamental frequency, amplitude perturbation, noise to harmonic ratio, and others, are analyzed to identify patterns indicative of Parkinson's disease.<br><br>
    By analyzing these voice features, the system can provide valuable insights into the presence or absence of Parkinson's disease. Early detection of the disease can lead to timely intervention and improved management of the condition.<br><br>
    If you are interested in learning more about the parameters and features used in this detection system, please refer to the descriptions provided below.
    </div>
""", unsafe_allow_html=True)
   
    st.image(r"static\img\brain.png", caption="Parkinson's Disease", use_column_width=True)
    st.markdown("""
    <div style='text-align: justify; color: black; font-size: 20px;'>
    <strong style='text-align: justify; color: #0d47a1; font-size: 30px;'>Voice Analysis Parameters</strong><br>
    <span style='padding-left: 20px;'><strong>MDVP:Fo(Hz):</strong> Average vocal fundamental frequency - Represents the average pitch of the voice, measured in Hertz (Hz).</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:Fhi(Hz):</strong> Maximum vocal fundamental frequency - Represents the highest pitch of the voice, measured in Hertz (Hz).</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:Flo(Hz):</strong> Minimum vocal fundamental frequency - Represents the lowest pitch of the voice, measured in Hertz (Hz).</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:Jitter(%):</strong> Variation in vocal fundamental frequency - Measures the cycle-to-cycle variation in the pitch of the voice, represented as a percentage.</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:Jitter(Abs):</strong> Absolute jitter, another measure of variation in vocal fundamental frequency - Represents the absolute difference between the consecutive pitch periods, typically measured in milliseconds (ms).</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:RAP:</strong> Relative amplitude perturbation, a measure of variation in vocal amplitude - Measures the variation in vocal amplitude between consecutive cycles, expressed as a percentage.</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:PPQ:</strong> Five-point period perturbation quotient, another measure of variation in vocal amplitude - Another measure of vocal amplitude variation, quantified based on five points within each pitch period.</span><br>
    <span style='padding-left: 20px;'><strong>Jitter:DDP:</strong> Average absolute difference of differences between consecutive jitter cycles - Represents the average absolute difference between consecutive cycles of jitter.</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:Shimmer:</strong> Variation in amplitude of vocal frequency - Measures the variation in the amplitude of the voice signal, typically expressed as a percentage.</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:Shimmer(dB):</strong> Shimmer in decibels - Represents shimmer in decibels, another measure of voice amplitude variation.</span><br>
    <span style='padding-left: 20px;'><strong>Shimmer:APQ3:</strong> Amplitude perturbation quotient, another measure of variation in amplitude - A measure of amplitude perturbation over three consecutive periods.</span><br>
    <span style='padding-left: 20px;'><strong>Shimmer:APQ5:</strong> Five-point period perturbation quotient for amplitude - A measure of amplitude perturbation over five consecutive periods.</span><br>
    <span style='padding-left: 20px;'><strong>MDVP:APQ:</strong> Another measure of variation in amplitude - Represents another measure of amplitude perturbation in the voice signal.</span><br>
    <span style='padding-left: 20px;'><strong>Shimmer:DDA:</strong> Average absolute difference between amplitudes of consecutive periods - Represents the average absolute difference between the amplitudes of consecutive periods.</span><br>
    <span style='padding-left: 20px;'><strong>NHR:</strong> Noise to harmonic ratio - Represents the ratio of noise to harmonic components in the voice signal.</span><br>
    <span style='padding-left: 20px;'><strong>HNR:</strong> Harmonic to noise ratio - Represents the ratio of harmonic components to noise in the voice signal.</span><br>
    <span style='padding-left: 20px;'><strong>RPDE, DFA, spread1, spread2, D2, PPE:</strong> Various nonlinear dynamical complexity measures extracted from speech signals - These are various features derived from nonlinear dynamical analysis of the voice signal, which are used to characterize different aspects of the voice and speech patterns.</span><br>
    </div>
""", unsafe_allow_html=True)



# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
   
    # Page title
    st.markdown("<h1 style='text-align: center; color: #0d47a1;'>Diabetes Prediction using ML</h1>", unsafe_allow_html=True)

    # Display an image
    st.image(r"static\img\daibetes.jpg", use_column_width=True)  # Replace "path_to_your_image.png" with the path to your image file
    st.markdown("<p style='text-align: center; color: #0d47a1; font-size:30px;'>Instructions for Filling Out the Form</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;  font-size:20px;'>To ensure accurate input, please follow these instructions:</p>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    .instruction {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    .instruction-item {
        margin-bottom: 10px;
    }
    .instruction-item b {
        color: #0066FF;  /* Blue color for emphasis */
    }
    </style>
    <div class="instruction">
    <div class="instruction-item"><b>Maternity History:</b>: Enter the number of pregnancies.</div>
    <div class="instruction-item"><b>Glucose</b>: Input the plasma glucose concentration measured during a 2-hour oral glucose tolerance test.</div>
    <div class="instruction-item"><b>Blood Pressure</b>: Provide the diastolic blood pressure in mm Hg.</div>
    <div class="instruction-item"><b>Skin Thickness</b>: Enter the skin thickness at the triceps in mm.</div>
    <div class="instruction-item"><b>Insulin</b>: Input the 2-hour serum insulin level in mu U/ml.</div>
    <div class="instruction-item"><b>BMI</b>: Provide the Body Mass Index (BMI), calculated as weight in kilograms divided by the square of height in meters.</div>
    <div class="instruction-item"><b>Diabetes Pedigree Function</b>: Input the Diabetes Pedigree Function value, a measure of diabetes mellitus history in relatives and genetic relationship.</div>
    <div class="instruction-item"><b>Age</b>: Enter the age in years.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #0d47a1; font-size:30px;'>Data Entry Form</p>", unsafe_allow_html=True)
    
    # Getting the input data from the user
    col1, col2 = st.columns([1, 2])

    with col1:
        st.write("")
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>Maternity History:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Glucose Level:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>Blood Pressure value:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")

        
        st.markdown("<p style='font-size:19px;'>Skin Thickness value:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Insulin Level:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        

        st.markdown("<p style='font-size:19px;'>BMI value:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Diabetes Pedigree Function value:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>Age of the Person:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
    with col2:
        st.markdown("""
            <style>
                /* Customize the input box */
                .stTextInput>div>div>input {
                    background-color: #f0f0f0; /* Change to desired color */
                    color: black; /* Change text color if needed */
                    border-color: blue; /* Change border color if needed */
                }
                
                /* Customize the button */
                .stButton>button {
                    width: 200px; /* Adjust the width as needed */
                    height: 50px; /* Adjust the height as needed */
                    font-size: 18px; /* Adjust the font size as needed */
                }
            </style>
        """, unsafe_allow_html=True)
        Pregnancies = st.text_input('', placeholder='Enter number of pregnancies (e.g., 0, 1, 2, ...)', key='Pregnancies')
        Glucose = st.text_input('', placeholder='Enter glucose level (e.g., 100, 120, ...)', key='Glucose')
        BloodPressure = st.text_input('', placeholder='Enter blood pressure value (e.g., 70, 80, ...)', key='BloodPressure')
        SkinThickness = st.text_input('', placeholder='Enter skin thickness value (e.g., 20, 25, ...)', key='SkinThickness')
        Insulin = st.text_input('', placeholder='Enter insulin level (e.g., 50, 100, ...)', key='Insulin')
        BMI = st.text_input('', placeholder='Enter BMI value (e.g., 20, 25, ...)', key='BMI')
        DiabetesPedigreeFunction = st.text_input('', placeholder='Enter diabetes pedigree function value (e.g., 0.5, 0.8, ...)', key='DiabetesPedigreeFunction')
        Age = st.text_input('', placeholder='Enter age (e.g., 30, 40, ...)', key='Age')
    if Pregnancies:
        Pregnancies = int(Pregnancies)
    else:
        st.error('Please enter the number of pregnancies.')
        st.stop()

    if Glucose:
        Glucose = float(Glucose)
    else:
        st.error('Please enter the glucose level.')
        st.stop()

    if BloodPressure:
        BloodPressure = float(BloodPressure)
    else:
        st.error('Please enter the blood pressure.')
        st.stop()

    if SkinThickness:
        SkinThickness = float(SkinThickness)
    else:
        st.error('Please enter the skin thickness.')
        st.stop()

    if Insulin:
        Insulin = float(Insulin)
    else:
        st.error('Please enter the insulin level.')
        st.stop()

    if BMI:
        BMI = float(BMI)
    else:
        st.error('Please enter the BMI (Body Mass Index).')
        st.stop()

    if DiabetesPedigreeFunction:
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
    else:
        st.error('Please enter the diabetes pedigree function.')
        st.stop()

    if Age:
        Age = int(Age)
    else:
        st.error('Please enter the age.')
        st.stop()


    # Code for prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result', key='diabetes_button', help='Click to predict'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)



# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
   
    # Page title
    st.markdown("<h1 style='text-align: center; color: #0d47a1;'>Heart Disease Prediction using ML</h1>", unsafe_allow_html=True)

    # Display an image if needed
    st.image(r"static\img\heart-image-.jpg", use_column_width=True)  # Replace "path_to_your_image.png" with the path to your image file
    st.markdown("<p style='text-align: center; color: #0d47a1; font-size:30px;'>Instructions for Filling Out the Form</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;  font-size:20px;'>To ensure accurate input, please follow these instructions:</p>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    .instruction {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    .instruction-item {
        margin-bottom: 10px;
    }
    .instruction-item b {
        color: #0066FF;  /* Blue color for emphasis */
    }
    </style>
    <div class="instruction">
    <div class="instruction-item"><b>Age:</b>: Enter the age of the individual.</div>
    <div class="instruction-item"><b>Sex:</b>: Specify the gender of the individual (0 = female, 1 = male).</div>
    <div class="instruction-item"><b>Chest Pain Type (cp):</b>: Choose from 0, 1, 2, 3 representing different types of chest pain.</div>
    <div class="instruction-item"><b>Resting Blood Pressure (trestbps):</b>: Provide the resting blood pressure in mm Hg.</div>
    <div class="instruction-item"><b>Serum Cholesterol (chol):</b>: Enter the serum cholesterol level in mg/dl.</div>
    <div class="instruction-item"><b>Fasting Blood Sugar (fbs):</b>: Indicate whether fasting blood sugar is above 120 mg/dl (1 = true, 0 = false).</div>
    <div class="instruction-item"><b>Resting Electrocardiographic Results (restecg):</b>: Enter 0 or 1 for resting electrocardiographic results.</div>
    <div class="instruction-item"><b>Maximum Heart Rate Achieved (thalach):</b>: Enter the maximum heart rate achieved.</div>
    <div class="instruction-item"><b>Exercise Induced Angina (exang):</b>: Specify whether exercise induced angina is present (1 = yes, 0 = no).</div>
    <div class="instruction-item"><b>ST Depression Induced by Exercise (oldpeak):</b>: Enter the ST depression induced by exercise relative to rest.</div>
    <div class="instruction-item"><b>Slope of the Peak Exercise ST Segment (slope):</b>: Choose from 0, 1, 2 for the slope of the peak exercise ST segment.</div>
    <div class="instruction-item"><b>Number of Major Vessels Colored by Fluoroscopy (ca):</b>: Enter the number of major vessels colored by fluoroscopy (0-3).</div>
    <div class="instruction-item"><b>Thalassemia (thal):</b>: Specify the type of thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #0d47a1; font-size:30px;'>Data Entry Form</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.write("")
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>Age:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>Sex:</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Chest Pain Type (cp):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Resting Blood Pressure (trestbps):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>Serum Cholesterol (chol):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Fasting Blood Sugar (fbs):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>Resting Electrocardiographic Results (restecg):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Maximum Heart Rate Achieved (thalach):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Exercise Induced Angina (exang):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>ST Depression Induced by Exercise (oldpeak):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Slope of the Peak Exercise ST Segment (slope):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Number of Major Vessels Colored by Fluoroscopy (ca):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        st.markdown("<p style='font-size:19px;'>Thalassemia (thal):</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")

    with col2:
        st.markdown("""
            <style>
                /* Customize the input box */
                .stTextInput>div>div>input {
                    background-color: #f0f0f0; /* Change to desired color */
                    color: black; /* Change text color if needed */
                    border-color: blue; /* Change border color if needed */
                }

                /* Customize the button */
                .stButton>button {
                    width: 200px; /* Adjust the width as needed */
                    height: 50px; /* Adjust the height as needed */
                    font-size: 18px; /* Adjust the font size as needed */
                }
            </style>
        """, unsafe_allow_html=True)
        age = st.text_input('', placeholder='Enter age (e.g., 40, 50, ...)', key='Age')
        sex = st.text_input('', placeholder='Specify gender (0 = female, 1 = male)', key='Sex')
        cp = st.text_input('', placeholder='Choose chest pain type (0, 1, 2, 3)', key='CP')
        trestbps = st.text_input('', placeholder='Enter resting blood pressure (e.g., 120, 130, ...)', key='Trestbps')
        chol = st.text_input('', placeholder='Enter serum cholesterol (e.g., 200, 220, ...)', key='Chol')
        fbs = st.text_input('', placeholder='Indicate fasting blood sugar (1 = true, 0 = false)', key='Fbs')
        restecg = st.text_input('', placeholder='Enter resting electrocardiographic results (0 or 1)', key='Restecg')
        st.write("")
        st.write("")
        thalach = st.text_input('', placeholder='Enter maximum heart rate achieved (e.g., 150, 160, ...)', key='Thalach')
        exang = st.text_input('', placeholder='Specify exercise induced angina (1 = yes, 0 = no)', key='Exang')
        oldpeak = st.text_input('', placeholder='Enter ST depression induced by exercise (e.g., 0.5, 1.0, ...)', key='Oldpeak')
        slope = st.text_input('', placeholder='Choose slope of peak exercise ST segment (0, 1, 2)', key='Slope')
        st.write("")
        ca = st.text_input('', placeholder='Enter number of major vessels colored by fluoroscopy (0-3)', key='CA')
        st.write("")
        thal = st.text_input('', placeholder='Specify thalassemia type (1 = normal; 2 = fixed defect; 3 = reversible defect)', key='Thal')
            # Convert input values to numeric data types with input validation
    if age:
        age = int(age)
    else:
        st.error('Please enter a valid age.')
        st.stop()

    if sex:
        sex = int(sex)
    else:
        st.error('Please specify the gender.')
        st.stop()

    if cp:
        cp = int(cp)
    else:
        st.error('Please choose the chest pain type.')
        st.stop()

    if trestbps:
        trestbps = float(trestbps)
    else:
        st.error('Please enter the resting blood pressure.')
        st.stop()

    if chol:
        chol = float(chol)
    else:
        st.error('Please enter the serum cholesterol level.')
        st.stop()

    if fbs:
        fbs = int(fbs)
    else:
        st.error('Please indicate the fasting blood sugar status.')
        st.stop()

    if restecg:
        restecg = int(restecg)
    else:
        st.error('Please choose the resting electrocardiographic results.')
        st.stop()

    if thalach:
        thalach = float(thalach)
    else:
        st.error('Please enter the maximum heart rate achieved.')
        st.stop()

    if exang:
        exang = int(exang)
    else:
        st.error('Please specify whether exercise induced angina is present.')
        st.stop()

    if oldpeak:
        oldpeak = float(oldpeak)
    else:
        st.error('Please enter the ST depression induced by exercise relative to rest.')
        st.stop()

    if slope:
        slope = int(slope)
    else:
        st.error('Please choose the slope of the peak exercise ST segment.')
        st.stop()

    if ca:
        ca = float(ca)
    else:
        st.error('Please enter the number of major vessels colored by fluoroscopy.')
        st.stop()

    if thal:
        thal = float(thal)
    else:
        st.error('Please specify the type of thalassemia.')
        st.stop()  

    # Code for prediction
    heart_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Heart Disease Test Result', key='heart_disease_button', help='Click to predict'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)



   



# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
   
    # Page title
    st.markdown("<h1 style='text-align: center; color: #0d47a1;'>Parkinson's Disease Prediction using ML</h1>", unsafe_allow_html=True)

    # Display an image if needed
    st.image(r"static\img\voice.jpg", use_column_width=True)  # Replace "path_to_your_image.png" with the path to your image file

    # Instructions for filling out the form
    st.markdown("<p style='text-align: center; color: #0d47a1; font-size:30px;'>Instructions for Filling Out the Form</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;  font-size:20px;'>To ensure accurate input, please follow these instructions:</p>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    .instruction {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    .instruction-item {
        margin-bottom: 10px;
    }
    .instruction-item b {
        color: #0066FF;  /* Blue color for emphasis */
    }
    </style>
    <div class="instruction">
    <div class="instruction-item"><b>MDVP:Fo(Hz):</b>: Mean frequency of the fundamental frequency in Hz.</div>
    <div class="instruction-item"><b>MDVP:Fhi(Hz):</b>: Maximum fundamental frequency in Hz.</div>
    <div class="instruction-item"><b>MDVP:Flo(Hz):</b>: Minimum fundamental frequency in Hz.</div>
    <div class="instruction-item"><b>MDVP:Jitter(%):</b>: Measure of variation in the fundamental frequency.</div>
    <div class="instruction-item"><b>MDVP:Jitter(Abs):</b>: Absolute jitter, another measure of variation in the fundamental frequency.</div>
    <div class="instruction-item"><b>MDVP:RAP:</b>: Relative amplitude perturbation, a measure of perturbation in the voice signal.</div>
    <div class="instruction-item"><b>MDVP:PPQ:</b>: Five-point period perturbation quotient, another measure of perturbation in the voice signal.</div>
    <div class="instruction-item"><b>Jitter:DDP:</b>: Average absolute difference of differences between consecutive periods.</div>
    <div class="instruction-item"><b>MDVP:Shimmer:</b>: Amplitude variation in the voice signal.</div>
    <div class="instruction-item"><b>MDVP:Shimmer(dB):</b>: Decibel variation in amplitude in the voice signal.</div>
    <div class="instruction-item"><b>Shimmer:APQ3:</b>: Amplitude variation in the voice signal.</div>
    <div class="instruction-item"><b>Shimmer:APQ5:</b>: Amplitude variation in the voice signal.</div>
    <div class="instruction-item"><b>MDVP:APQ:</b>: Amplitude variation in the voice signal.</div>
    <div class="instruction-item"><b>Shimmer:DDA:</b>: Amplitude variation in the voice signal.</div>
    <div class="instruction-item"><b>NHR:</b>: Noise-to-harmonics ratio.</div>
    <div class="instruction-item"><b>HNR:</b>: Harmonics-to-noise ratio.</div>
    <div class="instruction-item"><b>RPDE:</b>: Recurrence period density entropy measure.</div>
    <div class="instruction-item"><b>DFA:</b>: Signal fractal scaling exponent.</div>
    <div class="instruction-item"><b>spread1:</b>: Nonlinear measure of fundamental frequency variation.</div>
    <div class="instruction-item"><b>spread2:</b>: Nonlinear measure of fundamental frequency variation.</div>
    <div class="instruction-item"><b>D2:</b>: Correlation dimension.</div>
    <div class="instruction-item"><b>PPE:</b>: Pitch period entropy.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #0d47a1; font-size:30px;'>Data Entry Form</p>", unsafe_allow_html=True)

    # Getting the input data from the user
    col1, col2 = st.columns([2, 2])  # Combine col1 and col2 into one column

    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:Fo(Hz): Mean frequency of the fundamental frequency in Hz.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:Fhi(Hz): Maximum fundamental frequency in Hz.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:Flo(Hz): Minimum fundamental frequency in Hz.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>MDVP:Jitter(%): Measure of variation in the fundamental frequency.</p>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:Jitter(Abs): Absolute jitter, another measure of variation in the fundamental frequency.</p>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:RAP: Relative amplitude perturbation, a measure of perturbation in the voice signal.</p>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:PPQ: Five-point period perturbation quotient, another measure of perturbation in the voice signal.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:19px;'>Jitter:DDP: Average absolute difference of differences between consecutive periods.</p>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:Shimmer: Amplitude variation in the voice signal.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:Shimmer(dB): Decibel variation in amplitude in the voice signal.</p>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='font-size:19px;'>Shimmer:APQ3: Amplitude variation in the voice signal.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>Shimmer:APQ5: Amplitude variation in the voice signal.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>MDVP:APQ: Amplitude variation in the voice signal.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>Shimmer:DDA: Amplitude variation in the voice signal.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>NHR: Noise-to-harmonics ratio.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>HNR: Harmonics-to-noise ratio.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>RPDE: Recurrence period density entropy measure.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>DFA: Signal fractal scaling exponent.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<p style='font-size:19px;'>spread1: Nonlinear measure of fundamental frequency variation.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
    
        st.markdown("<p style='font-size:19px;'>spread2: Nonlinear measure of fundamental frequency variation.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>D2: Correlation dimension.</p>", unsafe_allow_html=True)
        st.write("")
        st.write("")

        st.markdown("<p style='font-size:19px;'>PPE: Pitch period entropy.</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <style>
                /* Customize the input box */
                .stTextInput>div>div>input {
                    background-color: #f0f0f0; /* Change to desired color */
                    color: black; /* Change text color if needed */
                    border-color: blue; /* Change border color if needed */
                }

                /* Customize the button */
                .stButton>button {
                    width: 200px; /* Adjust the width as needed */
                    height: 50px; /* Adjust the height as needed */
                    font-size: 18px; /* Adjust the font size as needed */
                }
            </style>
        """, unsafe_allow_html=True)
        fo = st.text_input('', placeholder='Enter MDVP:Fo(Hz) (e.g., 100, 150)', key='Fo')
        fhi = st.text_input('', placeholder='Enter MDVP:Fhi(Hz) (e.g., 150, 200)', key='Fhi')
        flo = st.text_input('', placeholder='Enter MDVP:Flo(Hz) (e.g., 50, 100)', key='Flo')
        Jitter_percent = st.text_input('', placeholder='Enter MDVP:Jitter(%) (e.g., 0.1, 0.2)', key='JitterPercent')
        Jitter_Abs = st.text_input('', placeholder='Enter MDVP:Jitter(Abs) (e.g., 0.01, 0.02)', key='JitterAbs')
        RAP = st.text_input('', placeholder='Enter MDVP:RAP (e.g., 0.1, 0.2)', key='RAP')
        PPQ = st.text_input('', placeholder='Enter MDVP:PPQ (e.g., 0.05, 0.1)', key='PPQ')
        DDP = st.text_input('', placeholder='Enter Jitter:DDP (e.g., 0.05, 0.1)', key='DDP')
        Shimmer = st.text_input('', placeholder='Enter MDVP:Shimmer (e.g., 0.05, 0.1)', key='Shimmer')
        Shimmer_dB = st.text_input('', placeholder='Enter MDVP:Shimmer(dB) (e.g., 1.5, 2.0)', key='ShimmerdB')
        APQ3 = st.text_input('', placeholder='Enter Shimmer:APQ3 (e.g., 0.05, 0.1)', key='APQ3')
        APQ5 = st.text_input('', placeholder='Enter Shimmer:APQ5 (e.g., 0.05, 0.1)', key='APQ5')
        APQ = st.text_input('', placeholder='Enter MDVP:APQ (e.g., 0.05, 0.1)', key='APQ')
        DDA = st.text_input('', placeholder='Enter Shimmer:DDA (e.g., 0.05, 0.1)', key='DDA')
        NHR = st.text_input('', placeholder='Enter NHR (e.g., 0.01, 0.02)', key='NHR')
        HNR = st.text_input('', placeholder='Enter HNR (e.g., 20, 25)', key='HNR')
        RPDE = st.text_input('', placeholder='Enter RPDE (e.g., 0.05, 0.1)', key='RPDE')
        DFA = st.text_input('', placeholder='Enter DFA (e.g., 0.5, 0.6)', key='DFA')
        spread1 = st.text_input('', placeholder='Enter spread1 (e.g., -4.33, -7.234)', key='spread1')
        spread2 = st.text_input('', placeholder='Enter spread2 (e.g., 0.02, 0.03)', key='spread2')
        D2 = st.text_input('', placeholder='Enter D2 (e.g., 180, 200)', key='D2')
        PPE = st.text_input('', placeholder='Enter PPE (e.g., 0.5, 0.6)', key='PPE')
    if fo:
        fo = float(fo)
    else:
        st.error('Please enter MDVP:Fo(Hz).')
        st.stop()

    if fhi:
        fhi = float(fhi)
    else:
        st.error('Please enter MDVP:Fhi(Hz).')
        st.stop()

    if flo:
        flo = float(flo)
    else:
        st.error('Please enter MDVP:Flo(Hz).')
        st.stop()

    if Jitter_percent:
        Jitter_percent = float(Jitter_percent)
    else:
        st.error('Please enter MDVP:Jitter(%).')
        st.stop()

    if Jitter_Abs:
        Jitter_Abs = float(Jitter_Abs)
    else:
        st.error('Please enter MDVP:Jitter(Abs).')
        st.stop()

    if RAP:
        RAP = float(RAP)
    else:
        st.error('Please enter MDVP:RAP.')
        st.stop()

    if PPQ:
        PPQ = float(PPQ)
    else:
        st.error('Please enter MDVP:PPQ.')
        st.stop()

    if DDP:
        DDP = float(DDP)
    else:
        st.error('Please enter Jitter:DDP.')
        st.stop()

    if Shimmer:
        Shimmer = float(Shimmer)
    else:
        st.error('Please enter MDVP:Shimmer.')
        st.stop()

    if Shimmer_dB:
        Shimmer_dB = float(Shimmer_dB)
    else:
        st.error('Please enter MDVP:Shimmer(dB).')
        st.stop()

    if APQ3:
        APQ3 = float(APQ3)
    else:
        st.error('Please enter Shimmer:APQ3.')
        st.stop()

    if APQ5:
        APQ5 = float(APQ5)
    else:
        st.error('Please enter Shimmer:APQ5.')
        st.stop()

    if APQ:
        APQ = float(APQ)
    else:
        st.error('Please enter MDVP:APQ.')
        st.stop()

    if DDA:
        DDA = float(DDA)
    else:
        st.error('Please enter Shimmer:DDA.')
        st.stop()

    if NHR:
        NHR = float(NHR)
    else:
        st.error('Please enter NHR.')
        st.stop()

    if HNR:
        HNR = float(HNR)
    else:
        st.error('Please enter HNR.')
        st.stop()

    if RPDE:
        RPDE = float(RPDE)
    else:
        st.error('Please enter RPDE.')
        st.stop()

    if DFA:
        DFA = float(DFA)
    else:
        st.error('Please enter DFA.')
        st.stop()

    if spread1:
        spread1 = float(spread1)
    else:
        st.error('Please enter spread1.')
        st.stop()

    if spread2:
        spread2 = float(spread2)
    else:
        st.error('Please enter spread2.')
        st.stop()

    if D2:
        D2 = float(D2)
    else:
        st.error('Please enter D2.')
        st.stop()

    if PPE:
        PPE = float(PPE)
    else:
        st.error('Please enter PPE.')
        st.stop()

    # Code for prediction
    parkinsons_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button("Parkinson's Test Result", key='parkinsons_prediction_button', help='Click to predict'):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])                          
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)



