from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
import time

from modules.audio_analysis import analyze_audio
from modules.video_analysis import analyze_video
from modules.scoring import calculate_score
from modules.questions import get_questions
from modules.speech_to_text import audio_to_text
from modules.answer_scoring import score_answer
from database import init_db
from modules.ai_answer_scoring import semantic_score

# --------------------------------------------------
# App Setup
# --------------------------------------------------

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

init_db()

CURRENT_QUESTIONS = []
CURRENT_DIFFICULTY = "easy"
CURRENT_SUBJECT = "dsa"

# --------------------------------------------------
# Authentication
# --------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        conn = sqlite3.connect("interview.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
        except:
            conn.close()
            return "Username already exists"

        conn.close()
        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("interview.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[1], password):
            session["user_id"] = user[0]
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# --------------------------------------------------
# Main Pages
# --------------------------------------------------

@app.route("/")
def home():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/mode")
def mode():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("mode.html")

@app.route("/set_mode/<mode>")
def set_mode(mode):
    session["mode"] = mode

    # If technical → go to subject selection (existing flow)
    if mode == "technical":
        return redirect("/interview")

    # If HR or Behavioral → skip subject
    return redirect(f"/interview?mode={mode}")


@app.route("/subjects")
def subjects():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("subjects.html")


@app.route("/difficulty")
def difficulty():
    if "user_id" not in session:
        return redirect("/login")
    subject = request.args.get("subject", "dsa")
    return render_template("difficulty.html", subject=subject)


@app.route("/interview")
def interview():
    global CURRENT_QUESTIONS, CURRENT_DIFFICULTY, CURRENT_SUBJECT

    if "user_id" not in session:
        return redirect("/login")

    mode = request.args.get("mode") or session.get("mode", "technical")
    session["mode"] = mode
    subject = request.args.get("subject")
    difficulty = request.args.get("difficulty")

    # Technical flow: need subject first
    if mode == "technical" and not subject:
        return render_template("subjects.html")

    # Technical flow: need difficulty after subject
    if mode == "technical" and subject and not difficulty:
        return render_template("difficulty.html", subject=subject)

    # --- Set globals depending on mode ---
    if mode == "technical":
        CURRENT_SUBJECT = subject
        CURRENT_DIFFICULTY = difficulty
        CURRENT_QUESTIONS = get_questions(subject, difficulty)

    elif mode == "hr":
        CURRENT_SUBJECT = "hr"
        CURRENT_DIFFICULTY = "easy"
        CURRENT_QUESTIONS = get_questions("hr", "easy")

    elif mode == "behavioral":
        CURRENT_SUBJECT = "behavioral"
        CURRENT_DIFFICULTY = "easy"
        CURRENT_QUESTIONS = get_questions("behavioral", "easy")

    else:
        CURRENT_SUBJECT = subject or "dsa"
        CURRENT_DIFFICULTY = difficulty or "easy"
        CURRENT_QUESTIONS = get_questions(CURRENT_SUBJECT, CURRENT_DIFFICULTY)

    return render_template("index.html", questions=CURRENT_QUESTIONS)

# --------------------------------------------------
# Upload & Analysis
# --------------------------------------------------

@app.route("/upload", methods=["POST"])
def upload_video():
    global CURRENT_QUESTIONS, CURRENT_DIFFICULTY, CURRENT_SUBJECT

    if "user_id" not in session:
        return redirect("/login")

    total_answer_score = 0
    total_duration_sum = 0
    total_silence = 0
    total_face = 0
    total_eye = 0
    total_speech = 0
    count = 0
    index = 0
    feedback = []
    speech_failure_flag = False

    for key in request.files:
        video = request.files[key]

        filename = f"interview_{int(time.time())}_{key}.webm"
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        video.save(save_path)

        face_percent, eye_percent = analyze_video(save_path)
        speech_percent, silence_duration, total_duration = analyze_audio(save_path)

        transcript = audio_to_text(save_path.replace(".webm", ".wav"))

        if not transcript or transcript.strip() == "":
            speech_failure_flag = True

        if index < len(CURRENT_QUESTIONS):
            keywords = CURRENT_QUESTIONS[index]["keywords"]
            reference = CURRENT_QUESTIONS[index]["answer"]

            keyword_score = score_answer(transcript, keywords)
            semantic = semantic_score(transcript, reference)

            ans_score = (keyword_score * 0.3) + (semantic * 0.7)

            total_answer_score += ans_score

        index += 1
        total_face += face_percent
        total_eye += eye_percent
        total_speech += speech_percent
        total_silence += silence_duration
        total_duration_sum += total_duration
        count += 1

    if count == 0:
        return "No video uploaded", 400

    avg_face = total_face / count
    avg_eye = total_eye / count
    avg_speech = total_speech / count
    avg_silence = total_silence / count
    avg_answer_score = total_answer_score / count
    avg_duration = total_duration_sum / count

    confidence_score = calculate_score(
        avg_face,
        avg_eye,
        avg_speech,
        avg_silence,
        avg_duration
    )

    final_score = round(
        confidence_score * 0.6 +
        avg_answer_score * 0.4,
        1
    )

    # ---------------- Feedback Engine ----------------

    if speech_failure_flag:
        feedback.append("One or more answers were unclear. Try speaking clearly.")

    if avg_face < 50:
        feedback.append("Try to keep your face visible to the camera.")
    elif avg_face < 80:
        feedback.append("Good face presence, maintain consistency.")
    else:
        feedback.append("Excellent camera presence.")

    if avg_eye < 40:
        feedback.append("Maintain better eye contact with the camera.")
    elif avg_eye < 70:
        feedback.append("Eye contact is decent but can improve.")
    else:
        feedback.append("Strong and confident eye contact.")

    if avg_speech < 40:
        feedback.append("Reduce long pauses and improve speech continuity.")
    elif avg_speech < 70:
        feedback.append("Speech clarity is good but can be smoother.")
    else:
        feedback.append("Excellent speech delivery.")

    if avg_answer_score < 40:
        feedback.append("Include more technical keywords in your answers.")
    elif avg_answer_score < 70:
        feedback.append("Good explanation but add more technical depth.")
    else:
        feedback.append("Strong technical explanation.")

    # ---------------- Save to Database ----------------
    mode = session.get("mode", "technical")

    if mode == "technical":
        subject = CURRENT_SUBJECT if CURRENT_SUBJECT else "dsa"
    elif mode == "hr":
        subject = "hr"
    elif mode == "behavioral":
        subject = "behavioral"
    else:
        subject = CURRENT_SUBJECT if CURRENT_SUBJECT else "dsa"

    difficulty_to_save = CURRENT_DIFFICULTY if CURRENT_DIFFICULTY else "easy"

    db_conn = sqlite3.connect("interview.db")
    db_cursor = db_conn.cursor()

    db_cursor.execute("""
        INSERT INTO attempts
        (user_id, subject, difficulty, mode, face, eye, speech, answer, final_score)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        session["user_id"],
        subject,
        difficulty_to_save,
        mode,
        round(avg_face, 2),
        round(avg_eye, 2),
        round(avg_speech, 2),
        round(avg_answer_score, 2),
        final_score
    ))

    db_conn.commit()
    db_conn.close()

    return render_template(
        "results.html",
        face=round(avg_face, 1),
        eye=round(avg_eye, 1),
        speech=round(avg_speech, 1),
        score=final_score,
        answer_score=round(avg_answer_score, 1),
        difficulty=CURRENT_DIFFICULTY,
        feedback=feedback
    )


# --------------------------------------------------
# History Page
# --------------------------------------------------

@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect("/login")

    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, subject, difficulty, face, eye, speech,
               answer, final_score, date, mode
        FROM attempts
        WHERE user_id = ?
        ORDER BY date ASC
    """, (session["user_id"],))

    rows = cursor.fetchall()
    conn.close()

    labels = []
    final_scores = []
    technical_scores = []
    hr_scores = []
    behavioral_scores = []

    for i, row in enumerate(rows):
        subject = row[1] if row[1] else ""
        score = row[7] if row[7] is not None else 0.0

        labels.append(f"Attempt {i + 1}")
        final_scores.append(float(score))

        if subject in ["dsa", "os", "dbms", "cn"]:
            technical_scores.append(float(score))
            hr_scores.append(None)
            behavioral_scores.append(None)

        elif subject == "hr":
            technical_scores.append(None)
            hr_scores.append(float(score))
            behavioral_scores.append(None)

        elif subject == "behavioral":
            technical_scores.append(None)
            hr_scores.append(None)
            behavioral_scores.append(float(score))

        else:
            technical_scores.append(None)
            hr_scores.append(None)
            behavioral_scores.append(None)

    return render_template(
        "history.html",
        rows=rows,
        labels=labels,
        final_scores=final_scores,
        technical_scores=technical_scores,
        hr_scores=hr_scores,
        behavioral_scores=behavioral_scores
    )


@app.route("/clear_history", methods=["POST"])
def clear_history():
    if "user_id" not in session:
        return redirect("/login")

    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()

    # Delete only current user's data (SAFE)
    cursor.execute("DELETE FROM attempts WHERE user_id = ?", (session["user_id"],))

    conn.commit()
    conn.close()

    return redirect("/history")

# --------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)