import streamlit as st 

# App Title
st.title('Unit Converter')

# Unit conversion options
conversion_types = ['Length', 'Temperature', 'Weight']

conversion_choice = st.selectbox("Choose conversion type", conversion_types)    

# Length Conversion
if conversion_choice == 'Length':
    length_units = ['meters', 'kilometers', 'feet', 'miles', 'yards']
    input_value = st.number_input('Enter Length value:', min_value=0.0, format="%.2f")  
    from_unit = st.selectbox("From unit", length_units)
    to_unit = st.selectbox("To unit", length_units)
    
    # Conversion Dictionary
    Length_conversion = {
        "meters": 1,
        "kilometers": 1000,
        "feet": 0.3048,
        "miles": 1609.34,
        "yards": 0.9144
    }

    # Conversion Logic
    if st.button('Convert'):
        result = input_value * (Length_conversion[from_unit] / Length_conversion[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

# Weight Conversion
elif conversion_choice == 'Weight':
    weight_units = ['grams', 'kilograms', 'pounds', 'ounces']
    input_value = st.number_input('Enter Weight value:', min_value=0.0, format="%.2f")  
    from_unit = st.selectbox("From unit", weight_units)
    to_unit = st.selectbox("To unit", weight_units)
    
    # Conversion Dictionary
    Weight_conversion = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }

    # Conversion Logic
    if st.button('Convert'):
        result = input_value * (Weight_conversion[from_unit] / Weight_conversion[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

# Temperature Conversion
elif conversion_choice == 'Temperature':
    temp_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    input_value = st.number_input('Enter Temperature value:', format="%.2f")  
    from_unit = st.selectbox("From unit", temp_units)
    to_unit = st.selectbox("To unit", temp_units)

    # Function for Temperature Conversion
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                return (value * 9/5) + 32
            elif to_unit == 'Kelvin':
                return value + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                return (value - 32) * 5/9
            elif to_unit == 'Kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                return value - 273.15
            elif to_unit == 'Fahrenheit':
                return (value - 273.15) * 9/5 + 32

    # Conversion Logic
    if st.button('Convert'):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f'{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}')
