import tkinter
import json
from urllib.request import urlopen
root = tkinter.Tk()
root.title("住所検索")
root.minsize(320, 240)

input_label = tkinter.Label(root, text="検索したい地域の郵便番号(ハイフンなし)を入力してくださ\nい", font=("メイリオ", 10))
input_label.pack()

postal_entry = tkinter.Entry(root)
postal_entry.pack()

search_button = tkinter.Button(root, text="Search")
search_button.pack()

address_label = tkinter.Label(root, text="", font=("メイリオ", 12, "bold"))
address_label.pack()

def search():
    p_code = postal_entry.get()
    # 出典：(位置参照情報) (国土交通省)
    url = f"http://heartrails.com/api/json?code={p_code}"
    
    with urlopen(url) as response:
        locations = json.load(response)["response"].get("location")
    
    display_data = ""
    if locations is None:
        pass
    else:
        for location in locations:
            display_data = display_data + location["city"] + location["town"] + "\n"
            
    if display_data == "":
        display_data = "(住所が見つかりません)"
        
    address_label["text"] = display_data

search_button["command"] = search
root.mainloop()