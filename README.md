
# Videogame Bot

**Videogame Bot** is a Python-based automation tool that records user keyboard and mouse inputs, saves them to a JSON file, and replays the inputs. The replay can also be captured as a video file, making it useful for automation, testing, and demonstrations.

## Features

- **Input Recording:** Captures keyboard and mouse actions performed by the user.
- **JSON Storage:** Saves recorded inputs in a JSON format for easy modification and reuse.
- **Input Playback:** Replays recorded inputs seamlessly.
- **Video Recording:** Records the playback into a video file for documentation or testing purposes.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** 
  - `pyautogui`: For automating mouse and keyboard actions.
  - `json`: For handling input storage.
  - Additional libraries as required for video recording (e.g., OpenCV).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JesusFernandez86/Videogame_bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Videogame_bot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Record Inputs:**
   Run the script to start recording keyboard and mouse inputs. The inputs will be saved to a JSON file.
   ```bash
   python record.py
   ```

2. **Replay Inputs:**
   Replay the recorded inputs from the JSON file.
   ```bash
   python replay.py
   ```

3. **Record Replay as Video:**
   Save the replay as a video file for further analysis or presentation.
   ```bash
   python record_video.py
   ```

## Contributions

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a pull request explaining your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions or suggestions, feel free to contact the repository owner.
