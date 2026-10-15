# デバッグ練習用のコード
# このファイルにはたくさんのバグが仕込まれています。
# 実行してエラーを直したり、正しい出力になるように修正してください。

# ------------------------------
# 1. リストの合計を計算する関数
# ------------------------------
def calculate_total(numbers):
    total = 0
    for i in range(1, len(numbers)):  # バグ: 0番目の要素が抜ける
        total = total + numbers[i]
    return total


# ------------------------------
# 2. リストの平均を計算する関数
# ------------------------------
def calculate_average(numbers):
    total = calculate_total(numbers)
    average = total / len(numbers) + 1  # バグ: 計算順序が間違っている
    return average


# ------------------------------
# 3. 最大値を探す関数
# ------------------------------
def find_max(numbers):
    max_value = 0  # バグ: 全部負の数だと正しく動かない
    for i in range(len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
    return max_value


# ------------------------------
# 4. 文字列が回文かどうかチェックする関数
# ------------------------------
def is_palindrome(word):
    length = len(word)
    for i in range(length):  # バグ: 半分まで見れば十分なのに全部見ている（動作はするが非効率）
        if word[i] != word[length - i]:  # バグ: インデックスがずれてIndexErrorになる
            return False
    return True


# ------------------------------
# 5. 素数判定をする関数
# ------------------------------
def is_prime(n):
    if n <= 1:
        return True  # バグ: 1以下は素数ではない
    for i in range(2, n):
        if n % i == 0:
            return True  # バグ: 割り切れたら素数ではないのに True を返している
    return False


# ------------------------------
# 6. フィボナッチ数列を再帰で求める関数
# ------------------------------
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) + 1  # バグ: 余計な +1 がある


# ------------------------------
# 7. リストから重複を取り除く関数
# ------------------------------
def remove_duplicates(items):
    result = []
    for i in range(len(items)):
        if items[i] not in result:
            pass  # バグ: result に追加する処理が抜けている
    return result


# ------------------------------
# 8. 2つの数を入れ替える関数
# ------------------------------
def swap_values(a, b):
    a = b
    b = a  # バグ: aが既にbになっているのでswapできていない
    return a, b


# ------------------------------
# 9. カウント辞書を作る関数（各文字の出現回数）
# ------------------------------
def count_characters(text):
    counts = {}
    for i in range(len(text)):
        char = text[i]
        counts[char] = counts[char] + 1  # バグ: 初めて出てきた文字でKeyErrorになる
    return counts


# ------------------------------
# 10. バブルソート
# ------------------------------
def bubble_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(n):  # バグ: 範囲が広すぎてIndexErrorになる可能性
            if items[j] > items[j + 1]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = items[j]  # バグ: tempを使っていないので値が消える
    return items


# ------------------------------
# 11. クラス：銀行口座
# ------------------------------
class BankAccount:
    def __init__(self, owner, balance=[]):  # バグ: ミュータブルなデフォルト引数
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount  # バグ: balanceが数値のはずがリストのまま
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("残高不足です")
        self.balance = self.balance - amount  # バグ: 残高不足でも処理が続いてしまう
        return self.balance


# ------------------------------
# 12. リストを逆順にする関数
# ------------------------------
def reverse_list(items):
    result = []
    for i in range(len(items)):
        result[i] = items[len(items) - i]  # バグ: 空リストへの代入でIndexError、インデックスもずれている
    return result


# ------------------------------
# 13. 2つのリストをマージする関数
# ------------------------------
def merge_lists(list_a, list_b):
    merged = list_a  # バグ: コピーではなく参照を渡しているので元のlist_aが変わってしまう
    for i in range(len(list_b)):
        merged.append(list_b[i])
    return merged


# ------------------------------
# 14. 温度を摂氏から華氏に変換する関数
# ------------------------------
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 5 / 9 + 32  # バグ: 5/9ではなく9/5が正しい
    return fahrenheit


# ------------------------------
# 15. メイン処理
# ------------------------------
def main():
    numbers = [4, 2, 9, 1, 7]

    print("合計:", calculate_total(numbers))
    print("平均:", calculate_average(numbers))
    print("最大値:", find_max(numbers))

    print("回文チェック:", is_palindrome("level"))
    print("素数チェック:", is_prime(7))
    print("フィボナッチ:", fibonacci(6))

    print("重複削除:", remove_duplicates([1, 2, 2, 3, 3, 3]))
    print("スワップ:", swap_values(5, 10))
    print("文字カウント:", count_characters("banana"))

    print("バブルソート:", bubble_sort([5, 3, 8, 1]))

    account = BankAccount("太郎")
    account.deposit(100)
    print("口座残高:", account.balance)

    print("リスト反転:", reverse_list([1, 2, 3]))
    print("マージ:", merge_lists([1, 2], [3, 4]))
    print("華氏変換:", celsius_to_fahrenheit(100))


if __name__ == "__main__":
    main()
