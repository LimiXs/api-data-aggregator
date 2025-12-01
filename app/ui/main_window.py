import json
import PySimpleGUI as sg

from app.api.clockify import fetch_clockify_data


def main():
    sg.theme("SystemDefault")

    layout = [
        [sg.Text("API Data Aggregator")],
        [sg.Button("Get Clockify Data", key="-GET_CLOCKIFY-")],
        [sg.Multiline(size=(60, 15), key="-OUTPUT-", disabled=True)],
        [sg.Button("Exit")]
    ]

    window = sg.Window("API Data Aggregator", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "-GET_CLOCKIFY-":
            data = fetch_clockify_data()
            pretty = json.dumps(data, indent=2, ensure_ascii=False)
            window["-OUTPUT-"].update(pretty)
    window.close()


if __name__ == "__main__":
    main()
