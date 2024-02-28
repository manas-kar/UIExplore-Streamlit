import streamlit as st

class HealthTracker:
    @staticmethod
    def display():
        st.title('🩺 Track Your Health')
        st.markdown("""
        Keep track of your health metrics to stay on top of your wellness journey. 
        Log your daily vitals, track improvements, and identify areas that need attention.
        """)
        
        # Example form for health metrics
        with st.form("health_form"):
            st.date_input("Date")
            weight = st.number_input("Weight (kg)", value=60.0, step=0.1)
            blood_pressure = st.text_input("Blood Pressure (e.g., 120/80)")
            hours_slept = st.slider("Hours Slept", min_value=0, max_value=24, value=8)
            mood = st.select_slider("Mood", options=["😭", "😕", "😐", "🙂", "😁"])
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.success("Health data submitted!")

class FoodIntakeTracker:
    @staticmethod
    def display():
        st.title('🍎 Track Food Intake')
        st.markdown("""
        Monitor your daily food intake to ensure a balanced diet. Log meals, 
        calculate caloric intake, and maintain nutritional balance.
        """)
        
        # Example form for logging food intake
        with st.form("food_form"):
            st.date_input("Date")
            meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack"])
            food_item = st.text_input("Food Item")
            calories = st.number_input("Calories", min_value=0)
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.success(f"{meal_type} logged!")

class WorkScheduleManager:
    @staticmethod
    def display():
        st.title('📅 Work Schedule Management')
        st.markdown("""
        Organize your work schedule effectively. Plan your tasks, set deadlines, 
        and manage your time efficiently to boost productivity.
        """)
        
        # Example task planner
        with st.form("schedule_form"):
            st.date_input("Date")
            task = st.text_input("Task")
            deadline = st.time_input("Deadline")
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.success(f"Task '{task}' scheduled!")

def main():
    st.sidebar.title('Navigation')
    app_mode = st.sidebar.radio('Go to', 
                                ['Track your Health', 
                                 'Track Food Intake', 
                                 'Work Schedule Management'])

    if app_mode == 'Track your Health':
        HealthTracker.display()
    elif app_mode == 'Track Food Intake':
        FoodIntakeTracker.display()
    elif app_mode == 'Work Schedule Management':
        WorkScheduleManager.display()

if __name__ == '__main__':
    main()
