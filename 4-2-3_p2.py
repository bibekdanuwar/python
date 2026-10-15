import requests
import tkinter

root = tkinter.Tk()
root.title("住所検索")
root.minsize(320, 240)
input_label = tkinter.Label(root, text="検索したい地域の郵便番号（-なし）を入力してください", font=("メイリオ", 10))
input_label.pack()
postal_entry = tkinter.Entry(root)
postal_entry.pack()
search_button = tkinter.Button(root, text="search")
search_button.pack()
address_label = tkinter.Label(root, text="", font=("メイリオ", 12, "bold"))
address_label.pack()

def search():
    postal_code = postal_entry.get()
    
    # 出典:「位置参照情報」(国土交通省)の加工情報・「Heartrails Geo API」(Heartrails Inc.)
    url = "http://heartrails.com" + postal_code
    
    response = requests.get(url)
    locations = (response.json())["response"].get("location")
    
    display_data = ""
    if locations != None:
        for location in locations:
            display_data = display_data + (location["city"] + location["town"] + "\n")
            
    else:
        display_data = "住所が見つかりません"
    address_label["text"] = display_data

search_button["command"] = search
root.mainloop()