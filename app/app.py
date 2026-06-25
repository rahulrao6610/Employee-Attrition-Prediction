from prediction import predict_employee
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="🏢",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🏢 Navigation")

menu = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "About Project",
        "Predict Employee"
    ]
)

# -----------------------------
# Home Page
# -----------------------------
if menu == "Home":

    st.title("🏢 Employee Attrition Prediction System")

    st.markdown("---")

    st.write("""
Welcome to the **HR Decision Support System**.

This application predicts whether an employee is likely to leave the company using Machine Learning.
""")

    st.subheader("Project Features")

    st.success("✔ Employee Attrition Prediction")

    st.success("✔ HR Analytics Dashboard")

    st.success("✔ Machine Learning Model")

    st.success("✔ HR Recommendations")

    st.success("✔ Explainable AI")

# -----------------------------
# About Page
# -----------------------------
elif menu == "Predict Employee":

    st.title("🤖 Employee Attrition Prediction")

    age = st.slider("Age", 18, 60, 30)

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=50000,
        value=5000
    )

    distance = st.slider("Distance From Home", 1, 30, 5)

    years_company = st.slider("Years At Company", 0, 40, 5)

    years_promotion = st.slider("Years Since Last Promotion", 0, 15, 1)

    environment = st.selectbox(
        "Environment Satisfaction",
        [1,2,3,4]
    )

    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        [1,2,3,4]
    )

    work_life = st.selectbox(
        "Work Life Balance",
        [1,2,3,4]
    )

    business = st.selectbox(
        "Business Travel",
        [
            "Travel_Rarely",
            "Travel_Frequently",
            "Non-Travel"
        ]
    )

    department = st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    overtime = st.selectbox(
        "OverTime",
        [
            "Yes",
            "No"
        ]
    )

    jobrole = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Research Director",
            "Human Resources",
            "Sales Representative"
        ]
    )

    if st.button("Predict"):

        employee = {
            "Age": age,
            "BusinessTravel": business,
            "Department": department,
            "DistanceFromHome": distance,
            "EnvironmentSatisfaction": environment,
            "JobRole": jobrole,
            "JobSatisfaction": job_satisfaction,
            "MonthlyIncome": monthly_income,
            "OverTime": overtime,
            "WorkLifeBalance": work_life,
            "YearsAtCompany": years_company,
            "YearsSinceLastPromotion": years_promotion
        }

        prediction, probability = predict_employee(employee)

        st.markdown("---")

        st.markdown("---")

        st.subheader("📊 Prediction Result")

        if prediction == 1:
            st.error("🚨 Employee is likely to leave")
        else:
            st.success("✅ Employee is likely to stay")
            st.metric(
                label="Attrition Probability",
                value=f"{probability*100:.2f}%"
            )
            if probability < 0.30:
                st.success("🟢 Risk Level : LOW")
            elif probability < 0.70:
                st.warning("🟡 Risk Level : MEDIUM")
            else:
                st.error("🔴 Risk Level : HIGH")

# -----------------------------
# Prediction Page
# -----------------------------
elif menu == "Predict Employee":

    st.title("🤖 Predict Employee Attrition")

    st.info("Prediction module will be added in the next step.")

    st.text_input("Employee Name")

    st.number_input("Age",18,60)

    st.number_input("Monthly Income",1000,50000)

    st.selectbox(
        "Department",
        [
            "Sales",
            "Research & Development",
            "Human Resources"
        ]
    )

    st.button("Predict")