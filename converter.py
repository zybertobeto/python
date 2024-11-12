import PySimpleGUI as sg


layout = [
    [sg.Text('Enter number and select Option to calculate:')],
    [sg.Input(key='-INPUT-'), sg.Spin(['Celsius to Fahrenheit', 'Fahrenheit to Celsius',
                                       'Celsius to Kelvin', 'Kelvin to Fahrenheit', 'Fahrenheit to Kelvin',
                                       'Kelvin to Celsius'], key='-OPTION-')],
    [sg.Button('Calculate', key='-CALCULATE-'), sg.Button('Clear', key='-CLEAR-')],
    [sg.Text('Output', key='-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CALCULATE-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-OPTION-']:
                case 'Celsius to Fahrenheit':
                    output = round(float(input_value) * 9 / 5 + 32, 2)
                    output_string = f'{input_value} degrees Celsius is equivalent to {output} degrees Fahrenheit'

                case 'Fahrenheit to Celsius':
                    output = round((float(input_value) - 32) * 5 / 9, 2)
                    output_string = f'{input_value} degrees Fahrenheit is equivalent to {output} degrees Celsius'

                case 'Celsius to Kelvin':
                    output = round(float(input_value) + 273.15, 2)
                    output_string = f'{input_value} degrees Celsius is equivalent to {output} degrees Kelvin'

                case 'Kelvin to Fahrenheit':
                    output = round((float(input_value) - 273.15) * 9 / 5 + 32, 2)
                    output_string = f'{input_value} degrees Kelvin is equivalent to {output} degrees Fahrenheit'

                case 'Fahrenheit to Kelvin':
                    output = round((float(input_value) - 32) * 5 / 9 + 273.15, 2)
                    output_string = f'{input_value} degrees Fahrenheit is equivalent to {output} degrees Kelvin'

                case 'Kelvin to Celsius':
                    output = round(float(input_value) - 273.15, 2)
                    output_string = f'{input_value} degrees Kelvin is equivalent to {output} degrees Celsius'

            window['-OUTPUT-'].update(output_string)

        else:
            window['-OUTPUT'].update('Please enter a valid number')

    if event == '-CLEAR-':
        print('You have cleared the entry')

window.close()
