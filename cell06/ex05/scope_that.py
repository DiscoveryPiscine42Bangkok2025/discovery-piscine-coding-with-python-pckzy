def add_one(n: int):
    return n+1

def main():
    num = 42
    print("Before:", num)
    add_one(num)
    print("After:", num)
    # ค่าของ num ไม่เปลี่ยนแปลง เพราะฟังก์ชัน add_one คืนค่าใหม่ แต่ไม่ได้เอาค่าที่คืนมาเก็บในตัวแปรเดิม (num ยังเท่าเดิม)

main()