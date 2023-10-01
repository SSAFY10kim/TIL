import socket
import math

# User and Game Server Information
NICKNAME = "서울6반_김현정_자바"
HOST = "127.0.0.1"
PORT = 1447

# Predefined variables (Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [[0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130]]

def main():
    balls = [[0, 0] for _ in range(NUMBER_OF_BALLS)]
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"Trying Connect: {HOST}:{PORT}")
            s.connect((HOST, PORT))
            print(f"Connected: {HOST}:{PORT}")

            with s.makefile('rb') as isock, s.makefile('wb') as osock:
                send_data = f"9901/{NICKNAME}\n"
                osock.write(send_data.encode('utf-8'))
                osock.flush()
                print("Ready to play.")

                while True:
                    recv_data = isock.readline().decode('utf-8').strip()
                    print(f"Data Received: {recv_data}")

                    split_data = recv_data.split("/")
                    idx = 0
                    try:
                        for i in range(NUMBER_OF_BALLS):
                            for j in range(2):
                                balls[i][j] = int(split_data[idx])
                                idx += 1
                    except Exception as e:
                        balls = [[0, 0] for _ in range(NUMBER_OF_BALLS)]
                        send_data = "9902/9902\n"
                        osock.write(send_data.encode('utf-8'))
                        osock.flush()
                        print("Received Data has been currupted, Resend Requested.")
                        continue
                    
                    angle = 0
                    power = 0
                    dx = 0
                    dy = 0

                    if balls[1][0] != 0 and balls[1][1] != 0:
                        power = 130
                        dx = balls[1][0] - balls[0][0]
                        dy = balls[1][1] - balls[0][1]
                        각도 = math.atan2(dy, dx)
                        각도 = 각도 * 180 / math.pi
                        angle = 90 - 각도
                    elif balls[2][0] != 0 and balls[2][1] != 0:
                        power = 115
                        dx = balls[2][0] - balls[0][0]
                        dy = balls[2][1] - balls[0][1]
                        각도 = math.atan2(dy, dx)
                        각도 = 각도 * 180 / math.pi
                        angle = 90 - 각도
                    elif balls[3][0] != 0 and balls[3][1] != 0:
                        power = 105
                        dx = balls[3][0] - balls[0][0]
                        dy = balls[3][1] - balls[0][1]
                        각도 = math.atan2(dy, dx)
                        각도 = 각도 * 180 / math.pi
                        angle = 90 - 각도
                    elif balls[4][0] != 0 and balls[4][1] != 0:
                        power = 115
                        dx = balls[4][0] - balls[0][0]
                        dy = balls[4][1] - balls[0][1]
                        각도 = math.atan2(dy, dx)
                        각도 = 각도 * 180 / math.pi
                        angle = 90 - 각도

                    length = math.sqrt(dx**2 + dy**2)

                    merged_data = f"{angle}/{power}\n"
                    osock.write(merged_data.encode('utf-8'))
                    osock.flush()
                    print(f"Data Sent: {merged_data}")
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()