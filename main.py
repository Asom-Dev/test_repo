from datetime import datetime

def main():
    print("Hello World!")
    formatted_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(formatted_time)


if __name__ == "__main__":
    main()
