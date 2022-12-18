<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine">
    <img src="Assets/icon.ico" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Tom's Enigma Machine</h3>

  <p align="center">
    A precisely-made replica of the german Enigma Machine used after WWI until the end of WWII.
    <br />
    <br />
    <br />
    <a href="https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine/issues">Report Bug</a>
    ·
    <a href="https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Made by myself with patience. Designed to be a complete replica of an Enigma Machine, but with some little added features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Tkinter

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Download the latest release for the best experience.
If you want to run it from source code, use the enigma.py file.

### Prerequisites

No additional software is required, but the "Assets" folder and its contents are necessary.
The following article assumes that you have knowledge about the functioning of the Enigma machine. If not, check out the video below, that might help a bit.

## Usage

Please watch this youtube video if you want visual intstructions : https://youtu.be/m9gquuUSRuI

### General description and definitions

"Rotor" means the individual spinning 26-position rotor that is used in the machine.<br />
"Stepping" means the value at which the next rotor will increase. Defaults to 26.<br />
"Plugboard" means the plugboard which was used with a set of cables.<br />
"Lampboard" means the decorative panel with 26 labled light bulbs on it.<br />
"Encode, Submit and Encrypt" are used to refer to the process of text elaboration.<br />

Looking at the main interface, you can see a "higher" and a "lower" section. The higher section houses the Rotors Assembly and the lampboard. The rotor assembly is composed of three individual rotors. Their default position in 1. Rotor can be set in positions from 1 to 26 using the buttons with a triangle on them corresponding to the chosen rotor. The button below the rotor will increase its value by one, the button above it will decrease it by one. Under each rotor you'll se a button with the number 1 and two gears on it. This button controls the rotor type, and can be set from 1 to 5. The lampboard has 26 unlit labled lightbulbs. Everytime that a character will result as an output the corresponding lightbulb will be turned on for a short period of time.<br />

In the lower section, you can see the input and output textboxes. The "Working speed" slider can be set from 1 to 10 and adjusts the speed that the machine operates at. Its value is measured in "ch/s" which stands for characters per second. It is quite precise. The big "Submit Text" button will start the encryption process if the machine was set correctly (Look down at limitations section). There also is a "Stop Encryption" button if you wish to abort the operation. A sound feature is available, and controllable through the "Sound" chechbox. The "Real Time Encryption" checkbox controls an added feature, which will be covered later in this document.

At the very bottom, a label reads "A software recreation of the famous german machine!" and it's used to display error messages.<br />

At the very top of the window two menus can be seen. The "Info" menu will open a small info window, allowing you to check the version that you are running on.<br />
The "Plugboard" menu opens the plugboard window.<br />

### Machine's Limitations

Tom's Enigma Machine is a replica of the real thing. For this reason, only standard characters from a to z will be encrypted. To allow for an easier use, the space " " character can be used, but will not be encrpyted.<br />

You cannot use the same rotor type while encrypting. This is because the original machine came with 5 rotors, and you had to choose 3. You cannot choose the same rotor twice, obviously.<br />

### Rotor Configuration

To prepare for operation, you have to set the rotors. Three things have to be set up, and will be now explained: rotor position, type, and stepping.<br />

To set the rotor position, use the buttons with the arrow keys. The value that is being used is the one in the center. Note these values as they will change during operation. If they are not reset to the inital values, the text will be not retrievable. This also applies to everything about to be covered.<br />

The rotor stepping can be controlled by the slider at the right of each rotor. The slider for the first rotor (the most left one) does not matter, but it's displayed to look better :) As always, remember the stepping values you use.<br />

Finally, rotor types can be adjusted using the buttons with the gear on them. Changing this value won't reset the rotor.<br />

### Plugboard Configuration

Open the plugboard window from its top menu. Here, you can see every letter in the german QWERTZ layout. To connect two letters, click on them, one at a time. You will se that they will link with the same color. If you want to reset a link, click on either of the letters to destroy its link. When you're done, click the save button. Neglecting to do this will result in the plugboard to be reset to its previous value.<br />

### Encryption and Decryption

They work exactly in the same way. Just input the text (or the encrypted one for decryption) and hit submit! Just remember, during the encryption rotor positions change. You need to remember these. The text can only be decrypted if a machine is using the same exact configuration.<br />

### Real Time Encryption

It's an added "Tom" touch. If you check on it BEFORE typing, and you start to type, it will encrypt as you type!

This comes however with a few limitations. If you make a mistake and hit the backspace key, you'll have to start over and you cannot paste chunks of text to do it instantly, because it will jam!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Main Features

- [ ] Original functioning
- [ ] Complete user-friendly interface
- [ ] Free
    - [ ] And fun!

See the [open issues](https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tommaso "Tom" Brignoli - [Youtube](https://www.youtube.com/channel/UCsS7xRYQ9wPDH_3YmabLVKw) - tommaso07brignoli@gmail.com

Project Link: [https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine](https://github.com/github_username/repo_name)

Built by me, myself and I. Released 18 / 12 / 2022

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/TomProgrammingStudios/Tom-s-Enigma-Machine.svg?style=for-the-badge
[contributors-url]: https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TomProgrammingStudios/Tom-s-Enigma-Machine.svg?style=for-the-badge
[forks-url]: https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine/network/members
[stars-shield]: https://img.shields.io/github/stars/TomProgrammingStudios/Tom-s-Enigma-Machine.svg?style=for-the-badge
[stars-url]: https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine/stargazers
[issues-shield]: https://img.shields.io/github/issues/TomProgrammingStudios/Tom-s-Enigma-Machine.svg?style=for-the-badge
[issues-url]: https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine/issues
[license-shield]: https://img.shields.io/github/license/TomProgrammingStudios/Tom-s-Enigma-Machine.svg?style=for-the-badge
[license-url]: https://github.com/TomProgrammingStudios/Tom-s-Enigma-Machine/blob/master/LICENSE.txt
