import requests
import tkinter
import csv

def save_history(postal_code, address):
    f = open("history.csv", "a", newline="", encoding="utf-8")
    writer = csv.writer(f)
    writer.writerow([postal_code, address])
    f.close()

def load_last_history():
    postal = ""
    address = ""
    try:
        f = open("history.csv", "r", encoding="utf-8")
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)
        f.close()
        if len(rows) > 0:
            last_row = rows[len(rows) - 1]
            postal = last_row[0]
            address = last_row[1]
    except FileNotFoundError:
        postal = ""
        address = ""
    return postal, address

last_postal, last_address = load_last_history()

root = tkinter.Tk()
root.title("住所検索")
root.minsize(320, 240)
input_label = tkinter.Label(root, text="検索したい地域の郵便番号（-なし）を入力してください", font=("メイリオ", 10))
input_label.pack()
postal_entry = tkinter.Entry(root)
postal_entry.insert(0, last_postal)
postal_entry.pack()
search_button = tkinter.Button(root, text="search")
search_button.pack()
address_label = tkinter.Label(root, text=last_address, font=("メイリオ", 12, "bold"))
address_label.pack()

def search():
    postal_code = postal_entry.get()

    url = "http://geoapi.heartrails.com/api/json?method=searchByPostal&postal=" + postal_code

    response = requests.get(url)
    locations = (response.json())["response"].get("location")

    display_data = ""
    if locations != None:
        for location in locations:
            display_data = display_data + (location["city"] + location["town"] + "\n")

        first_address = locations[0]["city"] + locations[0]["town"]
        save_history(postal_code, first_address)

    else:
        display_data = "住所が見つかりません"
    address_label["text"] = display_data

search_button["command"] = search
root.mainloop()