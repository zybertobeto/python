import PySimpleGUI as sg

sg.theme('DarkAmber')
sg.set_options(font='Franklin 15')

layout = [
    [sg.Text('Select option : ', pad=(10, 20)), sg.Combo(['Celsius to Fahrenheit', 'Fahrenheit to Celsius'], default_value='Celsius to Fahrenheit', pad=(15, 10))],
    [sg.Input()],
    [sg.Button('Calculate', key='-CALCULATE-', pad=(25, 25)), sg.Button('Clear', key='-CLEAR-', pad=(25, 25))],
    [sg.Text('Output', key='-OUTPUT-', pad=(5, 15))]
]

window = sg.Window('Temperature Converter', layout, size=(700, 250))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CALCULATE-':
        print('You just calculated')

    if event == '-CLEAR-':
        print('You just cleared the screen')

window.close()
