# CodeAlpha_Music_Generation_With_AI
# 🎵 Music Generation AI using LSTM
<img width="800" height="600" alt="generated_music" src="https://github.com/user-attachments/assets/5f162143-ac8c-4f34-8735-dbe59c463b6f" />

## Overview

Music Generation AI is a deep learning project that learns musical patterns from a collection of MIDI files and generates new music. The project uses a **Long Short-Term Memory (LSTM)** network, a type of Recurrent Neural Network (RNN), to predict the next musical note based on a sequence of previous notes.

The project workflow includes:

- Reading MIDI music files.
- Preprocessing notes into numerical sequences.
- Building an LSTM model.
- Training the model.
- Generating new music.
- Saving the generated music as a MIDI file.

---

# Project Structure

```text
Music-Generation-AI/
│
├── preprocess.py
├── model.py
├── train.py
├── generate.py
│
├── data/
│     notes.pkl
│     network_input.pkl
│     network_output.pkl
│     pitchnames.pkl
│
├── models/
│     music_model.keras
│
└── generated_music/
      generated.mid
```

---

# Project Workflow

```text
Classical MIDI Dataset
        │
        ▼
preprocess.py
        │
        ▼
Processed Data (.pkl files)
        │
        ▼
model.py
        │
        ▼
train.py
        │
        ▼
music_model.keras
        │
        ▼
generate.py
        │
        ▼
generated.mid
```

---

# Project Files

## preprocess.py

### Purpose

Reads the MIDI dataset and prepares it for deep learning.

### Input

- MIDI files (`.mid`)

### Processing Steps

- Read every MIDI file.
- Extract notes and chords using **music21**.
- Convert notes into integers.
- Create fixed-length note sequences.
- Normalize input data.
- Save processed data.

### Output

```
data/
├── notes.pkl
├── pitchnames.pkl
├── network_input.pkl
└── network_output.pkl
```

### Generated Files

#### notes.pkl

Stores every extracted musical note.

Example:

```python
['C4', 'E4', 'G4', 'C5', ...]
```

---

#### pitchnames.pkl

Stores every unique note found in the dataset.

Example:

```python
['A3', 'A#3', 'B3', 'C4', ...]
```

---

#### network_input.pkl

Stores normalized input sequences.

Shape

```
(number_of_samples, 100, 1)
```

---

#### network_output.pkl

Stores the expected next note for every input sequence.

---

## model.py

### Purpose

Builds and compiles the LSTM neural network.

### Model Architecture

```
Input Layer
      │
      ▼
LSTM (256)
      │
      ▼
Dropout
      │
      ▼
LSTM (256)
      │
      ▼
Dense (128)
      │
      ▼
Dropout
      │
      ▼
Softmax Output Layer
```

### Responsibilities

- Build the LSTM model.
- Configure optimizer.
- Configure loss function.
- Return the compiled model.

---

## train.py

### Purpose

Trains the neural network using the processed dataset.

### Input

```
network_input.pkl
network_output.pkl
pitchnames.pkl
```

### Processing Steps

- Load processed data.
- Load the LSTM model.
- Train the neural network.
- Learn musical patterns.
- Save the trained model.

### Output

```
models/
└── music_model.keras
```

---

## generate.py

### Purpose

Generates a new music sequence using the trained model.

### Input

```
music_model.keras
notes.pkl
pitchnames.pkl
```

### Processing Steps

- Load the trained model.
- Randomly select 100 notes (seed).
- Predict the next note.
- Remove the oldest note.
- Append the predicted note.
- Repeat until the desired number of notes is generated.
- Convert notes into a MIDI file.
- Save the generated music.

### Output

```
generated_music/
└── generated.mid
```

---

# Dataset

This project uses the **Classical Music MIDI Dataset**.

**Kaggle Dataset**

https://www.kaggle.com/datasets/soumikrakshit/classical-music-midi

---

# Technologies Used

- Python
- TensorFlow / Keras
- LSTM (Long Short-Term Memory)
- Recurrent Neural Networks (RNN)
- Music21
- NumPy
- Pickle
- MIDI

---

# Required Libraries

Install the required packages.

```bash
pip install tensorflow music21 numpy
```

---

# How to Run the Project

## Step 1 – Clone the Repository

Command

```bash
git clone https://github.com/omnia-ghonem/Music-Generation-AI.git
```

Move into the project directory

```bash
cd Music-Generation-AI
```

---

## Step 2 – Preprocess the Dataset

Command

```bash
python preprocess.py
```

Description

- Reads all MIDI files.
- Extracts notes and chords.
- Converts notes into training sequences.
- Saves processed files inside the **data** folder.

Generated files

```
notes.pkl
pitchnames.pkl
network_input.pkl
network_output.pkl
```

---

## Step 3 – Train the Model

Command

```bash
python train.py
```

Description

- Loads processed data.
- Builds the LSTM model.
- Trains the neural network.
- Saves the trained model.

Generated file

```
models/music_model.keras
```

---

## Step 4 – Generate Music

Command

```bash
python generate.py
```

Description

- Loads the trained model.
- Generates new musical notes.
- Converts notes into a MIDI file.
- Saves the generated music.

Generated file

```
generated_music/generated.mid
```

---

# How Music Generation Works

The LSTM model generates music one note at a time.

1. Randomly select **100 consecutive notes** from the dataset as the starting sequence (seed).
2. Feed the sequence to the trained LSTM model.
3. Predict the next note.
4. Remove the oldest note.
5. Append the predicted note.
6. Repeat until the desired number of notes has been generated.
7. Convert the generated notes into a MIDI file.

### Example

```
Seed:

C D E F G

↓

Model predicts:

A

↓

New Sequence:

D E F G A

↓

Model predicts:

C

↓

New Sequence:

E F G A C

...

Repeat until all notes are generated.
```

---

# Expected Output

After running the project successfully, the following files will be generated:

```
Music-Generation-AI/
│
├── data/
│     notes.pkl
│     network_input.pkl
│     network_output.pkl
│     pitchnames.pkl
│
├── models/
│     music_model.keras
│
└── generated_music/
      generated.mid
```

---

# Listening to the Generated Music

The generated output is a **MIDI (.mid)** file.

You can listen to it using:

- MuseScore
- VLC Media Player
- FL Studio
- Ableton Live
- GarageBand
- Windows Media Player (with MIDI support)

You can also convert the MIDI file into **WAV** or **MP3** using MuseScore or FluidSynth.

---

# Real-World Applications

AI-based music generation has many practical applications:

- Assisting composers with melody creation.
- Background music generation for games.
- Film and video soundtrack creation.
- Royalty-free music generation.
- Music education and AI research.
- Interactive entertainment systems.
- Creative AI applications.

---
