import cv2        #カメラを使うためのモジュール
import pyautogui  #キー入力を行うためのモジュール

cap = cv2.VideoCapture(0)
qr = cv2.QRCodeDetector()

while True:
    
    #フレーム変数に画像を格納
    ret,frame = cap.read()

    #画像サイズが大きいと処理が重いのでリサイズ
    w,h = frame.shape[:2]
    small_size = (int(h/2),int(w/2))

    frame = cv2.resize(frame,small_size)

    #取得した画像をQRコード認識をかけてdata変数に認識した文字列を格納
    data, points, straight_qrcode = qr.detectAndDecode(frame) 
    cv2.imshow("show image!",frame)
    if len(data) != 0:
        print("DATA:",data)
        pyautogui.typewrite(data)
        pyautogui.press('enter')
    
    #プログラムの終了処理 ウィンドウを指定した状態でキーボードのqで終了
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
