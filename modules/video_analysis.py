import cv2

def analyze_video(video_path):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(video_path)

    total_frames = 0
    face_frames = 0
    eye_contact_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        total_frames += 1
        h, w, _ = frame.shape

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=4,
            minSize=(60, 60)
        )

        if len(faces) > 0:
            face_frames += 1

            # take first detected face
            (x, y, fw, fh) = faces[0]

            face_center_x = x + fw / 2
            frame_center_x = w / 2

            # check if face is near center
            if abs(face_center_x - frame_center_x) < w * 0.15:
                eye_contact_frames += 1

    cap.release()

    if total_frames == 0:
      return 0, 0

    face_percent = (face_frames / total_frames) * 100
    eye_contact_percent = (eye_contact_frames / total_frames) * 100

    return face_percent, eye_contact_percent

