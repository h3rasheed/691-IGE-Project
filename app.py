import streamlit as st
import joblib
import numpy as np
from PIL import Image
import os

# Load the model and scaler
model = joblib.load('best_IGE_model.pkl')
scaler = joblib.load('scaler.pkl')

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Resume", "Projects", "Intergenerational Income Mobility Predictor"])

# Home page
if page == "Home":
    st.title('Welcome to Haneefuddin Rasheed\'s Homepage')
    st.write('Hello! I am Haneefuddin Rasheed, a data scientist with a passion for understanding and predicting socio-economic trends. This web application showcases my work and projects.')
    
    # Display local image
    image = Image.open('Haneef Picture.png')  # Ensure 'Haneef Picture.png' is in your project directory
    st.image(image, caption='Haneefuddin Rasheed', use_column_width=True)
    
    st.write('### Contact Information')
    st.write('Email: h3rasheed.com')
    st.write('Phone: (226) 791-1310')
    st.write('Location: London, Ontario')

# Resume page
elif page == "Resume":
    st.title('Resume')
    
    # Display local resume file
    resume = 'HR_Resume.pdf'  # Ensure 'HR_Resume.pdf' is in your project directory
    if os.path.exists(resume):
        with open(resume, 'rb') as file:
            btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name=resume,
                mime='application/pdf'
            )
    else:
        st.error('Resume file not found. Please ensure HR_Resume.pdf is in the project directory.')

    st.write('## HANEEF RASHEED')
    st.write('### DATA SPECIALIST')
    
    st.write('### Professional Experience')
    st.write('**Business Intelligence Analyst**')
    st.write('London, ON | 2023 – 2024')
    st.write('''
    - Led a Span of Control Optimization project aimed at reducing high turnover rates among clinical leaders by providing HR executives with actionable insights through prescriptive analytics.
    - Spearheaded the development and maintenance of interactive Power BI dashboards visualizing critical HR metrics like employee turnover, retention, performance, engagement, and satisfaction enhancing decision-making processes.
    - Integrated diverse data sources (Excel, SQL, SharePoint) using Power BI Desktop and Service; transformed and analyzed data employing DAX and M queries ensuring accurate and actionable insights.
    - Utilized Python for comprehensive data collection, cleaning, and preparation from various HR data sources addressing challenges of disparate and unstructured data for analytical exploration.
    - Employed advanced machine learning techniques including regression analysis and Random Forest algorithms to assess impacts on leadership stability and identify key factors influencing leader tenure.
    - Conducted insightful feature importance analysis to pinpoint critical factors for leader tenure informing targeted interventions to enhance leadership stability and reduce turnover.
    - Identified optimal leadership factors such as the ideal number of direct reports through machine learning, providing tailored data-driven recommendations for organizational leadership structure.
    - Led regular project meetings to communicate updates, address concerns, and facilitate decision-making among stakeholders.
    - Performed in-depth survival analysis focusing on leadership behavior over time and the impact of span of control on leader retention and effectiveness offering strategies to improve leader satisfaction and performance.
    - Achieved significant reduction in clinical leader turnover, demonstrating the value of integrating advanced analytics and machine learning into HR decision-making processes for enhancing organizational health and leadership stability.
    - Conducted in-depth presentations of analytics solutions and reports to executive leadership equipping them with the knowledge to utilize dashboards effectively for strategic organizational decision-making.
    ''')

    st.write('**Marketing and Sales Manager**')
    st.write('TaskTak, Redmond, WA | 2022 – 2023')
    st.write(''''
    - Led the successful expansion into the Canadian market for a SaaS product achieving a remarkable 20% increase in sales in the first year demonstrating effective market penetration and growth strategy execution.
    - Crafted and executed a comprehensive marketing strategy significantly enhancing brand awareness and customer acquisition across Canada tailored to the unique demands and opportunities of the SaaS industry.
    - Forged and nurtured strategic partnerships with key distributors and partners in Canada broadening distribution channels and unlocking new growth avenues essential for scaling a SaaS business.
    - Conducted in-depth market research to pinpoint emerging segments and product opportunities culminating in the introduction of two new highly successful SaaS product lines tailored to Canadian market needs.
    - Employed rigorous data analysis techniques to track market trends and refine sales and marketing strategies maximizing SaaS product performance and market share in the competitive Canadian landscape.
    - Facilitated cross-functional collaboration among product development, logistics, and customer service teams to deliver an outstanding customer experience critical for SaaS product success and customer retention in Canada.
    ''')

    st.write('**Writer**')
    st.write('Mississauga, ON | 2017 – 2022')
    st.write(''''
    - Wrote and published “Instructions to Finding Peace in Pain: An Empirical Narrative” with TellWell Publishing.
    - Conducted extensive research on topics such as pain management, mindfulness meditation, spirituality, and psychology.
    - Interviewed patients with life-changing physical and neurological health issues to record their experiences and perception of pain and documented their strategies of finding peace in the face of physical and psychological pain.
    - Collected and synthesized patient accounts and journal entries culminating in the publication of a comprehensive medical self-help book.
    - Developed a unique and engaging writing style that combines storytelling, humor, and practical advice.
    - Promoted the book through social media, podcasts, blogs, and interviews.
    - Received positive feedback and reviews from readers with an average rating of 5 out of 5 stars on Amazon.
    ''')

    st.write('**Data Analysis & Research Assistant**')
    st.write('University of Waterloo, Waterloo, ON | 2016 – 2017')
    st.write(''''
    - Research topic: The role of heuristics and personality in strategic business decision-making.
    - Developed a Web crawler in Python to download all 10-K and 10-Q Securities and Exchange Commission filings for S&P 1500 from 1994 to 2017.
    - Parsed the html files of the 10-K filings and extracted relevant textual data.
    - Performed sentiment analysis on extracted data to compare negative and positive words and to assess changes in reporting trends.
    - Analyzed changes in reporting trend to verify impact on stock price.
    ''')

    st.write('**Data Scientist & Product Manager**')
    st.write('Curiato, Waterloo, ON | 2016 – 2017')
    st.write(''''
    - Led research team for data collection and to extract and identify main physiological predictors for pressure ulcers to incorporate into predictive model.
    - Presented Pressure ulcer prevention technology at competitions, showcases, exhibitions and won over $100000 in grants.
    - Mined Twitter data to find trends and performed sentiment analysis of current competing pressure ulcer prevention devices.
    ''')

    st.write('### Education')
    st.write('**M.S. D.S. in Data Science**')
    st.write('Eastern University, Saint Davids, Pennsylvania | 2023 – 12/24')

    st.write('**Post-Graduate Diploma in Artificial Intelligence for Business**')
    st.write('The University of Texas, Austin, Texas | 2021')

    st.write('**B.A. in Economics**')
    st.write('University of Waterloo, Waterloo, ON | 201
