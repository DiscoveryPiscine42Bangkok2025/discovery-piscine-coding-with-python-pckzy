import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print("โปรดใส่ชื่อไฟล์มาด้วย")
        return
    
    for filename in sys.argv[1:]:
        try:
            with open(filename, "r") as f:
                board = f.read().strip()
        except FileNotFoundError:
            print(f"ผิดพลาด!! ไม่เจอไฟล์: {filename}")
            return
        checkmate(board)

if __name__ == "__main__":
    main()
