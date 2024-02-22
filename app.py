# # app.py

# from flask import Flask, render_template, request
# import pickle
# import pandas as pd

# app = Flask(__name__)

# # Load the trained model
# with open('knn_model.pkl', 'rb') as file:
#     model = pickle.load(file)


# # Define the route for the home page
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Define the route to handle the form submission and make predictions
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the input values from the form
#     height_cm = float(request.form['height_cm'])
#     weight_kg = float(request.form['weight_kg'])
#     work_rate_numeric = float(request.form['work_rate_numeric'])
#     pace = float(request.form['pace'])
#     physic = float(request.form['physic'])
#     position_numeric = float(request.form['position_numeric'])
#     age = float(request.form['age'])
#     cumulative_minutes_played = float(request.form['cumulative_minutes_played'])
#     minutes_per_game_prev_seasons = float(request.form['minutes_per_game_prev_seasons'])
#     avg_days_injured_prev_seasons = float(request.form['avg_days_injured_prev_seasons'])
#     significant_injury_prev_season = float(request.form['significant_injury_prev_season'])
#     cumulative_days_injured = float(request.form['cumulative_days_injured'])
    
#     # Create a DataFrame with the input data
#     input_data = pd.DataFrame({
#         'height_cm': [height_cm],
#         'weight_kg': [weight_kg],
#         'work_rate_numeric': [work_rate_numeric],
#         'pace': [pace],
#         'physic': [physic],
#         'position_numeric': [position_numeric],
#         'age': [age],
#         'cumulative_minutes_played': [cumulative_minutes_played],
#         'minutes_per_game_prev_seasons': [minutes_per_game_prev_seasons],
#         'avg_days_injured_prev_seasons': [avg_days_injured_prev_seasons],
#         'significant_injury_prev_season': [significant_injury_prev_season],
#         'cumulative_days_injured': [cumulative_days_injured]
#     })
    
#     # Make predictions using the loaded model
#     prediction = model.predict(input_data)
    
#     # Return the prediction
#     return render_template('result.html', prediction=prediction[0])

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# # Define the route for the home page
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get input parameters from request
#     input_data = request.json
    
#     # Extract input features
#     significant_injury_prev_season = input_data.get('significant_injury_prev_season')
#     age = input_data.get('age')
#     cumulative_minutes_played = input_data.get('cumulative_minutes_played')
#     minutes_per_game_prev_seasons = input_data.get('minutes_per_game_prev_seasons')
#     avg_days_injured_prev_seasons = input_data.get('avg_days_injured_prev_seasons')
#     start_year = input_data.get('start_year')
#     height_cm = input_data.get('height_cm')
#     weight_kg = input_data.get('weight_kg')
#     work_rate_numeric = input_data.get('work_rate_numeric')
#     pace = input_data.get('pace')
#     physic = input_data.get('physic')
#     position_numeric = input_data.get('position_numeric')
#     cumulative_days_injured = input_data.get('cumulative_days_injured')
    

#     # Analyze input parameters to determine likelihood of injury
#     injury_likelihood = "Low"

#     # Change output based on input parameters
#     output = ""
    
#     if significant_injury_prev_season == "Yes":
#         output += "Player has a history of significant injury. "
#     else:
#         output += "Player does not have a history of significant injury. "
    
#     if int(age) >= 30:
#         output += "Player is older than 30 years old. "
#     else:
#         output += "Player is younger than 30 years old. "
    
#     if int(cumulative_minutes_played) >= 10000:
#         output += "Player has played more than 10000 minutes. "
#     else:
#         output += "Player has not played more than 10000 minutes. "
    
#     if int(minutes_per_game_prev_seasons) >= 90:
#         output += "Player's average minutes per game is more than 90. "
#     else:
#         output += "Player's average minutes per game is less than 90. "
    
#     if float(avg_days_injured_prev_seasons) > 5:
#         output += "Player has been injured for more than 5 days on average per season. "
#     else:
#         output += "Player has been injured for less than or equal to 5 days on average per season. "
    
#     if int(start_year) <= 2000:
#         output += "Player started their professional career before 2000. "
#     else:
#         output += "Player started their professional career after 2000. "
    
#     if int(height_cm) >= 180:
#         output += "Player's height is above 180 cm. "
#     else:
#         output += "Player's height is below 180 cm. "
    
#     if int(weight_kg) >= 70:
#         output += "Player's weight is above 70 kg. "
#     else:
#         output += "Player's weight is below 70 kg. "
    
#     if int(work_rate_numeric) >= 3:
#         output += "Player's work rate is high. "
#     else:
#         output += "Player's work rate is low. "
    
#     if int(pace) >= 70:
#         output += "Player's pace attribute is high. "
#     else:
#         output += "Player's pace attribute is low. "
    
#     if int(physic) >= 70:
#         output += "Player's physic attribute is high. "
#     else:
#         output += "Player's physic attribute is low. "
    
#     if int(position_numeric) == 1:
#         output += "Player plays as a forward. "
#     elif int(position_numeric) == 2:
#         output += "Player plays as a midfielder. "
#     else:
#         output += "Player plays as a defender. "
    
#     if int(cumulative_days_injured) >= 30:
#         output += "Player has been injured for more than 30 days in total. "
#     else:
#         output += "Player has been injured for less than or equal to 30 days in total. "
    
#     # Analyze injury likelihood based on the gathered information
#     if "history of significant injury" in output or "older than 30" in output or "more than 10000 minutes" in output or "more than 5 days on average per season" in output or "started their professional career before 2000" in output:
#         injury_likelihood = "High"
    
#     # Return output as JSON response
#     return jsonify({"output": output, "injury_likelihood": injury_likelihood})

# if __name__ == '__main__':
#     app.run(debug=True)




# import streamlit as st

# def analyze_injury_likelihood(input_data):
#     # Extract input features
#     significant_injury_prev_season = input_data.get('significant_injury_prev_season')
#     age = input_data.get('age')
#     cumulative_minutes_played = input_data.get('cumulative_minutes_played')
#     minutes_per_game_prev_seasons = input_data.get('minutes_per_game_prev_seasons')
#     avg_days_injured_prev_seasons = input_data.get('avg_days_injured_prev_seasons')
#     start_year = input_data.get('start_year')
#     height_cm = input_data.get('height_cm')
#     weight_kg = input_data.get('weight_kg')
#     work_rate_numeric = input_data.get('work_rate_numeric')
#     pace = input_data.get('pace')
#     physic = input_data.get('physic')
#     position_numeric = input_data.get('position_numeric')
#     cumulative_days_injured = input_data.get('cumulative_days_injured')

#     # Analyze input parameters to determine likelihood of injury
#     injury_likelihood = "Low"

#     # Change output based on input parameters
#     output = ""

#     if significant_injury_prev_season == "Yes":
#         output += "Player has a history of significant injury. "
#     else:
#         output += "Player does not have a history of significant injury. "

#     if int(age) >= 30:
#         output += "Player is older than 30 years old. "
#     else:
#         output += "Player is younger than 30 years old. "

#     if int(cumulative_minutes_played) >= 10000:
#         output += "Player has played more than 10000 minutes. "
#     else:
#         output += "Player has not played more than 10000 minutes. "

#     if int(minutes_per_game_prev_seasons) >= 90:
#         output += "Player's average minutes per game is more than 90. "
#     else:
#         output += "Player's average minutes per game is less than 90. "

#     if float(avg_days_injured_prev_seasons) > 5:
#         output += "Player has been injured for more than 5 days on average per season. "
#     else:
#         output += "Player has been injured for less than or equal to 5 days on average per season. "

#     if int(start_year) <= 2000:
#         output += "Player started their professional career before 2000. "
#     else:
#         output += "Player started their professional career after 2000. "

#     if int(height_cm) >= 180:
#         output += "Player's height is above 180 cm. "
#     else:
#         output += "Player's height is below 180 cm. "

#     if int(weight_kg) >= 70:
#         output += "Player's weight is above 70 kg. "
#     else:
#         output += "Player's weight is below 70 kg. "

#     if int(work_rate_numeric) >= 3:
#         output += "Player's work rate is high. "
#     else:
#         output += "Player's work rate is low. "

#     if int(pace) >= 70:
#         output += "Player's pace attribute is high. "
#     else:
#         output += "Player's pace attribute is low. "

#     if int(physic) >= 70:
#         output += "Player's physic attribute is high. "
#     else:
#         output += "Player's physic attribute is low. "

#     if int(position_numeric) == 1:
#         output += "Player plays as a forward. "
#     elif int(position_numeric) == 2:
#         output += "Player plays as a midfielder. "
#     else:
#         output += "Player plays as a defender. "

#     if int(cumulative_days_injured) >= 30:
#         output += "Player has been injured for more than 30 days in total. "
#     else:
#         output += "Player has been injured for less than or equal to 30 days in total. "

#     # Analyze injury likelihood based on the gathered information
#     if "history of significant injury" in output or "older than 30" in output or "more than 10000 minutes" in output or "more than 5 days on average per season" in output or "started their professional career before 2000" in output:
#         injury_likelihood = "High"

#     return output, injury_likelihood

# def main():
#     st.title("Injury Prediction")

#     st.write("Please provide the following information about the player:")

#     # Input fields
#     significant_injury_prev_season = st.selectbox("Significant Injury Previous Season:", ["Yes", "No"])
#     age = st.number_input("Age:")
#     cumulative_minutes_played = st.number_input("Cumulative Minutes Played:")
#     minutes_per_game_prev_seasons = st.number_input("Minutes Per Game Previous Seasons:")
#     avg_days_injured_prev_seasons = st.number_input("Average Days Injured Previous Seasons:")
#     start_year = st.number_input("Start Year:")
#     height_cm = st.number_input("Height (cm):")
#     weight_kg = st.number_input("Weight (kg):")
#     work_rate_numeric = st.number_input("Work Rate (Numeric):")
#     pace = st.number_input("Pace:")
#     physic = st.number_input("Physic:")
#     position_numeric = st.number_input("Position (Numeric):")
#     cumulative_days_injured = st.number_input("Cumulative Days Injured:")

#     # Predict button
#     if st.button("Predict"):
#         input_data = {
#             "significant_injury_prev_season": significant_injury_prev_season,
#             "age": age,
#             "cumulative_minutes_played": cumulative_minutes_played,
#             "minutes_per_game_prev_seasons": minutes_per_game_prev_seasons,
#             "avg_days_injured_prev_seasons": avg_days_injured_prev_seasons,
#             "start_year": start_year,
#             "height_cm": height_cm,
#             "weight_kg": weight_kg,
#             "work_rate_numeric": work_rate_numeric,
#             "pace": pace,
#             "physic": physic,
#             "position_numeric": position_numeric,
#             "cumulative_days_injured": cumulative_days_injured
#         }

#         output, injury_likelihood = analyze_injury_likelihood(input_data)

#         # Display output
#         st.write("Prediction Output:")
#         st.write(output)
#         st.write("Injury Likelihood:", injury_likelihood)


# if __name__ == "__main__":
#     main()



# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# def analyze_injury_likelihood(input_data):
#     # Extract input features
#     significant_injury_prev_season = input_data.get('significant_injury_prev_season')
#     age = input_data.get('age')
#     cumulative_minutes_played = input_data.get('cumulative_minutes_played')
#     minutes_per_game_prev_seasons = input_data.get('minutes_per_game_prev_seasons')
#     avg_days_injured_prev_seasons = input_data.get('avg_days_injured_prev_seasons')
#     start_year = input_data.get('start_year')
#     height_cm = input_data.get('height_cm')
#     weight_kg = input_data.get('weight_kg')
#     work_rate_numeric = input_data.get('work_rate_numeric')
#     pace = input_data.get('pace')
#     physic = input_data.get('physic')
#     position_numeric = input_data.get('position_numeric')
#     cumulative_days_injured = input_data.get('cumulative_days_injured')

#     # Analyze input parameters to determine likelihood of injury
#     injury_likelihood = "Low"

#     # Change output based on input parameters
#     output = ""

#     if significant_injury_prev_season == "Yes":
#         output += "Player has a history of significant injury. "
#     else:
#         output += "Player does not have a history of significant injury. "

#     if int(age) >= 30:
#         output += "Player is older than 30 years old. "
#     else:
#         output += "Player is younger than 30 years old. "

#     if int(cumulative_minutes_played) >= 10000:
#         output += "Player has played more than 10000 minutes. "
#     else:
#         output += "Player has not played more than 10000 minutes. "

#     if int(minutes_per_game_prev_seasons) >= 90:
#         output += "Player's average minutes per game is more than 90. "
#     else:
#         output += "Player's average minutes per game is less than 90. "

#     if float(avg_days_injured_prev_seasons) > 5:
#         output += "Player has been injured for more than 5 days on average per season. "
#     else:
#         output += "Player has been injured for less than or equal to 5 days on average per season. "

#     if int(start_year) <= 2000:
#         output += "Player started their professional career before 2000. "
#     else:
#         output += "Player started their professional career after 2000. "

#     if int(height_cm) >= 180:
#         output += "Player's height is above 180 cm. "
#     else:
#         output += "Player's height is below 180 cm. "

#     if int(weight_kg) >= 70:
#         output += "Player's weight is above 70 kg. "
#     else:
#         output += "Player's weight is below 70 kg. "

#     if int(work_rate_numeric) >= 3:
#         output += "Player's work rate is high. "
#     else:
#         output += "Player's work rate is low. "

#     if int(pace) >= 70:
#         output += "Player's pace attribute is high. "
#     else:
#         output += "Player's pace attribute is low. "

#     if int(physic) >= 70:
#         output += "Player's physic attribute is high. "
#     else:
#         output += "Player's physic attribute is low. "

#     if int(position_numeric) == 1:
#         output += "Player plays as a forward. "
#     elif int(position_numeric) == 2:
#         output += "Player plays as a midfielder. "
#     else:
#         output += "Player plays as a defender. "

#     if int(cumulative_days_injured) >= 30:
#         output += "Player has been injured for more than 30 days in total. "
#     else:
#         output += "Player has been injured for less than or equal to 30 days in total. "

#     # Analyze injury likelihood based on the gathered information
#     if "history of significant injury" in output or "older than 30" in output or "more than 10000 minutes" in output or "more than 5 days on average per season" in output or "started their professional career before 2000" in output:
#         injury_likelihood = "High"

#     return output, injury_likelihood

# def main():
#     st.title("Injury Prediction")

#     st.write("Please provide the following information about the player:")

#     # Input fields
#     significant_injury_prev_season = st.selectbox("Significant Injury Previous Season:", ["Yes", "No"])
#     age = st.number_input("Age:", min_value=16, max_value=50, value=25)
#     cumulative_minutes_played = st.number_input("Cumulative Minutes Played:", min_value=0, max_value=20000, value=5000)
#     minutes_per_game_prev_seasons = st.number_input("Minutes Per Game Previous Seasons:", min_value=0, max_value=120, value=60)
#     avg_days_injured_prev_seasons = st.number_input("Average Days Injured Previous Seasons:", min_value=0.0, max_value=20.0, value=2.0, step=0.1)
#     start_year = st.number_input("Start Year:", min_value=1950, max_value=2025, value=2010)
#     height_cm = st.number_input("Height (cm):", min_value=100, max_value=300, value=175)
#     weight_kg = st.number_input("Weight (kg):", min_value=30, max_value=200, value=70)
#     work_rate_numeric = st.number_input("Work Rate (Numeric):", min_value=1, max_value=5, value=3)
#     pace = st.number_input("Pace:", min_value=0, max_value=100, value=50)
#     physic = st.number_input("Physic:", min_value=0, max_value=100, value=50)
#     position_numeric = st.selectbox("Position (Numeric):", ["1 (Forward)", "2 (Midfielder)", "3 (Defender)"])
#     cumulative_days_injured = st.number_input("Cumulative Days Injured:", min_value=0, max_value=365, value=10)

#     position_mapping = {"1 (Forward)": 1, "2 (Midfielder)": 2, "3 (Defender)": 3}
#     position_numeric = position_mapping[position_numeric]

#     # Predict button
#     if st.button("Predict"):
#         input_data = {
#             "significant_injury_prev_season": significant_injury_prev_season,
#             "age": age,
#             "cumulative_minutes_played": cumulative_minutes_played,
#             "minutes_per_game_prev_seasons": minutes_per_game_prev_seasons,
#             "avg_days_injured_prev_seasons": avg_days_injured_prev_seasons,
#             "start_year": start_year,
#             "height_cm": height_cm,
#             "weight_kg": weight_kg,
#             "work_rate_numeric": work_rate_numeric,
#             "pace": pace,
#             "physic": physic,
#             "position_numeric": position_numeric,
#             "cumulative_days_injured": cumulative_days_injured
#         }

#         output, injury_likelihood = analyze_injury_likelihood(input_data)

#         # Display output
#         st.write("Prediction Output:")
#         st.write(output)
#         st.write("Injury Likelihood:", injury_likelihood)

#         # Plot some data
#         plot_data = {
#             "Age Distribution": np.random.randint(age - 5, age + 5, 100),
#             "Height Distribution": np.random.randint(height_cm - 10, height_cm + 10, 100)
#         }
#         st.write("### Data Visualization")
#         plot_choice = st.selectbox("Select Plot:", list(plot_data.keys()))
#         fig, ax = plt.subplots()
#         ax.hist(plot_data[plot_choice], bins=20)
#         st.pyplot(fig)


# if __name__ == "__main__":
#     main()



import streamlit as st

def analyze_injury_likelihood(input_data):
    # Extract input features
    significant_injury_prev_season = input_data.get('significant_injury_prev_season')
    age = input_data.get('age')
    cumulative_minutes_played = input_data.get('cumulative_minutes_played')
    minutes_per_game_prev_seasons = input_data.get('minutes_per_game_prev_seasons')
    avg_days_injured_prev_seasons = input_data.get('avg_days_injured_prev_seasons')
    start_year = input_data.get('start_year')
    height_cm = input_data.get('height_cm')
    weight_kg = input_data.get('weight_kg')
    work_rate_numeric = input_data.get('work_rate_numeric')
    pace = input_data.get('pace')
    physic = input_data.get('physic')
    position_numeric = input_data.get('position_numeric')
    cumulative_days_injured = input_data.get('cumulative_days_injured')

    # Analyze input parameters to determine likelihood of injury
    injury_likelihood = "Low"

    # Change output based on input parameters
    output = ""

    if significant_injury_prev_season == "Yes":
        output += "Player has a history of significant injury. "
    else:
        output += "Player does not have a history of significant injury. "

    if int(age) >= 30:
        output += "Player is older than 30 years old. "
    elif int(age) >= 25:
        output = "Player is in the middle age group (25-29 years old). "
    elif int(age) >= 18:
        output = "Player is in the young age group (18-24 years old). "
    else:
        output += "Player is younger than 18 years old. "

    if int(cumulative_minutes_played) >= 10000:
        output += "Player has played more than 10000 minutes. "
    else:
        output += "Player has not played more than 10000 minutes. "

    if int(minutes_per_game_prev_seasons) >= 90:
        output += "Player's average minutes per game is more than 90. "
    else:
        output += "Player's average minutes per game is less than 90. "

    if float(avg_days_injured_prev_seasons) > 5:
        output += "Player has been injured for more than 5 days on average per season. "
    else:
        output += "Player has been injured for less than or equal to 5 days on average per season. "

    if int(start_year) <= 2000:
        output += "Player started their professional career before 2000. "
    else:
        output += "Player started their professional career after 2000. "

    if int(height_cm) >= 180:
        output += "Player's height is above 180 cm. "
    else:
        output += "Player's height is below 180 cm. "

    if int(weight_kg) >= 70:
        output += "Player's weight is above 70 kg. "
    else:
        output += "Player's weight is below 70 kg. "

    if int(work_rate_numeric) >= 3:
        output += "Player's work rate is high. "
    else:
        output += "Player's work rate is low. "

    if int(pace) >= 70:
        output += "Player's pace attribute is high. "
    else:
        output += "Player's pace attribute is low. "

    if int(physic) >= 70:
        output += "Player's physic attribute is high. "
    else:
        output += "Player's physic attribute is low. "

    if int(position_numeric) == 1:
        output += "Player plays as a forward. "
    elif int(position_numeric) == 2:
        output += "Player plays as a midfielder. "
    else:
        output += "Player plays as a defender. "

    if int(cumulative_days_injured) >= 30:
        output += "Player has been injured for more than 30 days in total. "
    else:
        output += "Player has been injured for less than or equal to 30 days in total. "

    # Analyze injury likelihood based on the gathered information
    # if "history of significant injury" in output and "older than 30" in output and "more than 10000 minutes" in output and "more than 5 days on average per season" in output and "started their professional career before 2000" in output:
    #     injury_likelihood = "High"

    # if "history of significant injury" in output and "older than 30" in output and "more than 10000 minutes" in output:
    #     injury_likelihood = "High"

    # elif "history of significant injury" in output and "Player is in the middle age group (25-29 years old)." in output and "more than 10000 minutes" in output and "more than 5 days on average per season" in output and "started their professional career before 2000" in output:
    #     injury_likelihood = "High"

    # elif "Player does not have  history of significant injury" in output and "Player is in the young age group (18-24 years old)." in output and "more than 10000 minutes" in output and "more than 10 days on average per season" in output and "started their professional career before 2000" in output:
    #     injury_likelihood = "High"

    # elif "Player does not have history of significant injury" in output and "Player is younger than 18 years old." in output and "more than 10000 minutes" in output and "more than 10 days on average per season" in output and "started their professional career before 2000" in output:
        
    #     injury_likelihood = "High"
    
    # else:
    #     injury_likelihood = "Low"
        
            # Conditions for different player positions
    if position_numeric == "Defender":
        if "history of significant injury" in output and "older than 30" in output and "more than 10000 minutes" in output:
            injury_likelihood = "High"
        elif "history of significant injury" in output and "Player is in the middle age group (25-29 years old)." in output and "more than 10000 minutes" in output and "more than 5 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
        elif "Player does not have history of significant injury" in output and "Player is in the young age group (18-24 years old)." in output and "more than 10000 minutes" in output and "more than 10 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
        elif "Player does not have history of significant injury" in output and "Player is younger than 18 years old." in output and "more than 10000 minutes" in output and "more than 10 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
    elif position_numeric == 1:
        if "history of significant injury" in output and "older than 30" in output and "more than 10000 minutes" in output:
            injury_likelihood = "High"
        elif "history of significant injury" in output and "Player is in the middle age group (25-29 years old)." in output and "more than 10000 minutes" in output and "more than 5 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
        elif "Player does not have history of significant injury" in output and "Player is in the young age group (18-24 years old)." in output and "more than 10000 minutes" in output and "more than 10 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
        elif "Player does not have history of significant injury" in output and "Player is younger than 18 years old." in output and "more than 10000 minutes" in output and "more than 10 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
    elif position_numeric == 2:
        if "history of significant injury" in output and "older than 30" in output and "more than 10000 minutes" in output:
            injury_likelihood = "High"
        elif "history of significant injury" in output and "Player is in the middle age group (25-29 years old)." in output and "more than 10000 minutes" in output and "more than 5 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
        elif "Player does not have history of significant injury" in output and "Player is in the young age group (18-24 years old)." in output and "more than 10000 minutes" in output and "more than 10 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
        elif "Player does not have history of significant injury" in output and "Player is younger than 18 years old." in output and "more than 10000 minutes" in output and "more than 10 days on average per season" in output and "started their professional career before 2000" in output:
            injury_likelihood = "High"
    else:
        # Default conditions if position is not specified
        injury_likelihood = "Low"

    return output, injury_likelihood

def main():
    st.title("Injury Prediction")

    st.write("Please provide the following information about the player:")

    # Input fields
    significant_injury_prev_season = st.selectbox("Significant Injury Previous Season:", ["Yes", "No"])
    age = st.number_input("Age:", min_value=16, max_value=50, value=25)
    cumulative_minutes_played = st.number_input("Cumulative Minutes Played:", min_value=0, max_value=20000, value=5000)
    minutes_per_game_prev_seasons = st.number_input("Minutes Per Game Previous Seasons:", min_value=0, max_value=120, value=60)
    avg_days_injured_prev_seasons = st.number_input("Average Days Injured Previous Seasons:", min_value=0.0, max_value=20.0, value=2.0, step=0.1)
    start_year = st.number_input("Start Year:", min_value=1950, max_value=2025, value=2010)
    height_cm = st.number_input("Height (cm):", min_value=100, max_value=300, value=175)
    weight_kg = st.number_input("Weight (kg):", min_value=30, max_value=200, value=70)
    work_rate_numeric = st.number_input("Work Rate (Numeric):", min_value=1, max_value=5, value=3)
    pace = st.number_input("Pace:", min_value=0, max_value=100, value=50)
    physic = st.number_input("Physic:", min_value=0, max_value=100, value=50)
    position_numeric = st.selectbox("Position (Numeric):", ["1 (Forward)", "2 (Midfielder)", "3 (Defender)"])
    cumulative_days_injured = st.number_input("Cumulative Days Injured:", min_value=0, max_value=365, value=10)

    position_mapping = {"1 (Forward)": 1, "2 (Midfielder)": 2, "3 (Defender)": 3}
    position_numeric = position_mapping[position_numeric]

    # Predict button
    if st.button("Predict"):
        input_data = {
            "significant_injury_prev_season": significant_injury_prev_season,
            "age": age,
            "cumulative_minutes_played": cumulative_minutes_played,
            "minutes_per_game_prev_seasons": minutes_per_game_prev_seasons,
            "avg_days_injured_prev_seasons": avg_days_injured_prev_seasons,
            "start_year": start_year,
            "height_cm": height_cm,
            "weight_kg": weight_kg,
            "work_rate_numeric": work_rate_numeric,
            "pace": pace,
            "physic": physic,
            "position_numeric": position_numeric,
            "cumulative_days_injured": cumulative_days_injured
        }

        output, injury_likelihood = analyze_injury_likelihood(input_data)

        # # Display output
        # st.write("Prediction Output:")
        # st.write(output)
        # st.write("Injury Likelihood:", injury_likelihood)

                # Display output with CSS styling
        st.write("### Prediction Output")
        st.markdown(
            f"""
            <div style="padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
                <p style="font-weight: bold; color: #333;">Output:</p>
                <p style="color: #555;">{output}</p>
                <p style="font-weight: bold; color: #333;">Injury Likelihood:</p>
                <p style="color: #555;">{injury_likelihood}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        

if __name__ == "__main__":
    main()
