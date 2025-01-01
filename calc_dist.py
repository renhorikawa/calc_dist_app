import cv2
import math

while True:
    try:
        image_path = input("画像のパスを入力してください: ")
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError("画像が見つかりません。パスを確認してください。")
        break
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print("不明なエラーが発生しました:", e)

while True:
    try:
        actual_distance = float(input("基準となる距離 (mm) を入力してください: "))
        if actual_distance <= 0:
            raise ValueError("距離は正の値で入力してください。")
        break
    except ValueError as e:
        print(e)
    except Exception as e:
        print("不明なエラーが発生しました:", e)

points = []

def click_event(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"座標 {len(points)}: X={x}, Y={y}")
        cv2.circle(image, (x, y), 3, (255, 0, 0), -1)
        cv2.imshow("Image", image)

        if len(points) == 2:
            x1, y1 = points[0]
            x2, y2 = points[1]
            try:
                pixel_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                pixel_to_mm = actual_distance / pixel_distance
                print("ピクセル距離 (pixel_distance):", pixel_distance)
                print("1ピクセルあたりの距離:", pixel_to_mm, "mm")
            except ZeroDivisionError:
                print("距離の計算に失敗しました (分母がゼロです)。点を再選択してください。")
            except Exception as e:
                print("距離の計算中にエラーが発生しました:", e)

            cv2.destroyAllWindows()

cv2.imshow("Image", image)
cv2.setMouseCallback("Image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
