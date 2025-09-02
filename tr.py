from graphviz import Digraph

# Create flowchart
dot = Digraph("Neuro_Wheelchair_Flow", format="png")
dot.attr(rankdir="LR", size="8")

# Nodes
dot.node("EEG", "EEG Headset\n(Signal Acquisition)", shape="oval", style="filled", fillcolor="lightblue")
dot.node("Preprocess", "Preprocessing\n(Filters, Artifact Removal)", shape="box", style="rounded,filled", fillcolor="lightyellow")
dot.node("Features", "Feature Extraction\n(PSD, Spectrograms, Band Power)", shape="box", style="rounded,filled", fillcolor="lightyellow")
dot.node("ML", "ML Classifier\n(SVM/CNN/LSTM)", shape="box", style="rounded,filled", fillcolor="lightgreen")
dot.node("Decision", "Decision & Confidence\n(Smoothing, Thresholds)", shape="box", style="rounded,filled", fillcolor="lightpink")
dot.node("Planner", "Motion Planner", shape="box", style="rounded,filled", fillcolor="lightgrey")
dot.node("Motor", "Motor Controller\n(RPi/ESP32 + Driver)", shape="box", style="rounded,filled", fillcolor="lightblue")
dot.node("Wheels", "Wheelchair Movement", shape="oval", style="filled", fillcolor="lightblue")

dot.node("Obstacle", "Obstacle Detection\n(LiDAR / Ultrasonic + IMU)", shape="diamond", style="filled", fillcolor="lightcoral")
dot.node("IoT", "IoT Dashboard\n(Telemetry, Caregiver App)", shape="parallelogram", style="filled", fillcolor="lightgreen")
dot.node("Manual", "Manual Override\n(Joystick / E-Stop)", shape="parallelogram", style="filled", fillcolor="orange")

# Edges
dot.edge("EEG", "Preprocess")
dot.edge("Preprocess", "Features")
dot.edge("Features", "ML")
dot.edge("ML", "Decision")
dot.edge("Decision", "Planner")
dot.edge("Planner", "Motor")
dot.edge("Motor", "Wheels")

dot.edge("Obstacle", "Planner", label="Safety Override")
dot.edge("Motor", "IoT", label="Telemetry")
dot.edge("Planner", "IoT", label="Status Logs")
dot.edge("Manual", "Motor", label="Fail-Safe")

# Render flowchart
file_path = "/mnt/data/Neuro_Wheelchair_Flowchart"
dot.render(file_path, cleanup=True)

file_path + ".png"
