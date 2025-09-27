# Ride-The-Duck

Ride The Duck is a gambling, CLI, binary executable game based on the drinking game "Ride The Bus." Ride The Duck incorporates the first stage of Ride The Bus, where you need to guess if the next card fits into either category, with each category giving you a better multiplier to your initial bet, earning you more.

## Features

Ride The Duck contains many different features:

- Save file: When exiting the terminal or the game, your data (money, name, stats) will be saved.
- CLI: The game appears and runs on the Command Line Interface for a techy and hacky vibe.
- ASCII: Part of the game's interface is made using ASCII, which gives a cool visual effect.
- ANSI escape codes: The game's text is configured with color to pop out.
- PyPI: You can play the game using PyPI packages / pip.
- Duck: Ducks are added to replace Jacks.
- Gambling: You are given money to gamble with, for fun.
- macOS Compatibility: Runs on macOS and maybe Linux... not really a feature but I can't make it compatible with Windows (If this game gets enough support I'll try to do it).

## Gameplay
<img width="346" height="260" alt="Picture1" src="https://github.com/user-attachments/assets/4e00b8ba-ba70-4586-9764-f3bb4eec8a01" />
<img width="346" height="274" alt="Picture2" src="https://github.com/user-attachments/assets/70d69142-9120-4d82-be30-5c22d310490d" />
<img width="346" height="219" alt="Picture3" src="https://github.com/user-attachments/assets/a206726d-7650-4d9a-8d3c-36f733194eb1" />
<img width="346" height="257" alt="Picture4" src="https://github.com/user-attachments/assets/2384f1ae-ab28-496f-b001-32e18591ce00" />

## How Do You Play Ride The Duck?

When you play the main game, you first need to enter how much you want to bet. After you complete the bet stage, there are 4 rounds, each round giving you a better multiplier for your money.

1. Red or Black x2

2. Over or Under x3

3. Inside or Outside x4

4. Suit x20

After completing each stage, you're able to cash out and collect your bet with the multiplier of the round or continue and try to collect a higher multiplier.

The first round is guessing if the next/first card is going to be Red or Black. Completing this will give you a **2x** multiplier on your initial bet.

The second round is guessing if the next card is going to be over or under the first card. Completing this will give you a **3x** multiplier on your initial bet.

The third round is guessing if the next card is going to be between the first 2 cards or outside them. Completing this will give you a **4x** multiplier on your initial bet.

Lastly, the fourth round is guessing the suit of the next/last card. Completing this will give you a **20x** multiplier on your initial bet.

On the last stage, you can only cash out, earning the holy 20x multiplier.

## How to play (macOS ONLY, Potentially Linux)

### Binary Executable (macOS arm64 ONLY)

To download the binary executable (TERMINAL CRAFT), you can follow these steps:

1. Go to the releases page of Ride The Duck.

2. Go to the most recent version and download the file: "RTD-G '*VERSION*' macOS arm64 tar.gz". This is the file that has the game on it.

3. Go to the file location (most likely 'Downloads') and open the downloaded file.

4. Bypass the Apple security by:
    - Double click the "RTD-Game" executable file and press "Done" (NOT "Move to Bin"). Go to Settings > Privacy & Security and under Security, select Open Anyway on the game file name "RTD-Game".

    **or**

        Example:

        ```sh
        cd /Users/"UserName"/Downloads 
        ```

        Then use this command to bypass the security:

        ```sh
        xattr -d com.apple.quarantine RTD-Game
        ```

5. Double click or open the game executable file and have fun c:

If you're not comfortable with letting your guard down and bypassing the security, you can message me on Slack (soon to be changed) [@DuckyBoi_XD](https://hackclub.slack.com/team/U08TJ79P0G4) or [Email](braedenjairsytan@icloud.com) and I'll try to respond ASAP to send you the file that shouldn't require any security bypass.

### PyPI (macOS Only, Maybe Linux)

For this you need to have Python installed (most systems should already have it installed).

1. Check for pip or Python in your terminal:

    ```sh
    python --version
    ```

    or

    ```sh
    python3 --version
    ```

    and then

    ```sh
    pip --version
    ```

    or

    ```sh
    pip3 --version
    ```

    If you get a response with a version number then you should be all set. If your Python is 3.8 or above then it should be good. If your pip is 21.3 or above then it should be good.

2. Install Ride The Duck

    In your terminal, install Ride The Duck by using one of these commands:

    ```sh
    pip3 install ride-the-duck
    ```

    or

    ```sh
    pip install ride-the-duck
    ```

    or

    ```sh
    python -m pip install ride-the-duck
    ```

    If you get a confirmation about ride-the-duck being installed then you should be good to go.

3. Run game

    To run the game, all you need to do is use the command 'RTD' or 'ride-the-duck'.

4. Have fun C:

### PyPI Pipx (macOS ONLY, Maybe Linux)

In Terminal:

1. Install: `pipx install ride-the-duck`
2. Play: `RTD`

*Make sure pipx is installed (`pip install pipx`).*
*If RTD command is not found, run `pipx ensurepath` first to set up your PATH.*
