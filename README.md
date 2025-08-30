![GitHub contributors](https://img.shields.io/github/contributors/Sekuora/Trezenv?color=blue)

<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="./resources/images/logo.png" alt="Logo" width="240" height="240">
  </a>

<h2 align="center">Trezenv </h2>

<p align="center">
    A CLI tool to produce a project local vcpkg installation. Create IDE agnostic and replicable C/C++ environments with ease and manage dependencies using the vcpkg toolchain. 
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<p>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#readme-top">About</a>
      <ul>
        <li><a href="#contributors">Contributors</a></li>
      </ul>
    </li>
    <li>
      Getting Started
      <ul>
        <li><a href="#compiling-from-source">Compiling From Source</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#Contributing-and-guidelines">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#donations">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</p>

## Contributors

<a href="https://github.com/Sekuora/Trezenv/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Sekuora/Trezenv" />
</a>

We are grateful for all these contributors!


## Installation

Requirements for the software and other tools to build, test and push 
- [Python >= 3.12](https://www.python.org/downloads/)
- requirements.txt


### Compiling from source

Clone this repository:

  ```sh
  https://github.com/Sekuora/Trezenv.git
  ```

Open the project with your IDE of preference and run:

  ```sh
  pip install -r requirements.txt
  ```

Build executable -> in project root run this.
  ```sh
  nuitka --standalone --onefile trezenv.py
  ```

Now, you should have a binary file ready to use, or download the precompiled version from releases.


## Usage

### Step 1
Build or download precompiled binaries of trezenv.   <a href="" Latest release here </a> (note: at the moment the cli has only been tested on windows)
Place the program in your project location, 


### Step 2
Create a plain "trezenv" file without extensions in a C/C++ project where you need vcpkg to be inmediatly recognized and its dependencies installed.

### Step 3
As of the first version 1.1.0 Trezenv' CLI consists of 3 commands
#### set - Sets parameters related to the trezenv environment. See options.
  - Options
    1. --envpath, -ep set the path where trezenv will install dependencies. Default is "externals/vcpkg"
#### check - Checks parameters related to the trezenv environment. See options.
 - Options
     1. --envpath, -ep, check the path where trezenv will install dependencies. Useful in case of changes
#### init - Will perform initialization of the trezenv environment
1. This command will read the "trezenv" file located in your root folder, and pass its dependencies to vcpkg.
2. Once installed add the toolchain directory to your CMake File

### Example CMake File Extract
```CMake
### Example CMake File Tested with trezenv

### vcpkg toolchain file ### 
set(VCPKG_DIR "${CMAKE_SOURCE_DIR}/externals/vcpkg")
set(CMAKE_TOOLCHAIN_FILE "${VCPKG_DIR}/scripts/buildsystems/vcpkg.cmake" CACHE STRING "Vcpkg toolchain file")
###
# Package Dependencies
find_package(SDL3 CONFIG REQUIRED)
find_package(SDL3_ttf CONFIG REQUIRED)
find_package(SDL3_image CONFIG REQUIRED)
find_package(Lua REQUIRED)
find_package(glm CONFIG REQUIRED)
find_package(imgui CONFIG REQUIRED)

target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE SDL3::SDL3 SDL3_ttf::SDL3_ttf-shared imgui::imgui ${LUA_LIBRARIES} glm::glm-header-only)
target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE $<IF:$<TARGET_EXISTS:SDL3_image::SDL3_image-shared>,SDL3_image::SDL3_image-shared,SDL3_image::SDL3_image-static>)

```

3. In this case I've tested trezenv to manage dependencies for a large game engine project. I've linked according to the expected find_package and target_link_libraries commands.
4. You can review said commands by visiting the specific vcpkg library you want to find in vcpkg's webiste and the linkage commands can be found when you install the libraries.

<!-- ROADMAP -->

## Roadmap

- [X] Install dependencies from trezenv file
- [X] Get project dependencies ready with a sinigle trezenv init command
- [X] Work with vcpkg manifest mode
- [ ] Make it work globally from system environment variables
- [ ] Improve trezenv file parsing add support for triplets
- [ ] Create fully featured docs and video demo
- [ ] Add more easy to use commands for miscellaneous features
- [ ] Add and test support with various build tools
- [ ] Automatically Add vcpkg deps in CMakeLists.txt

See the [open issues](https://github.com/Sekuora/Trezenv/issues) for a full list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing and guidelines

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make the project better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- License -->

## License

 Licensed under <a href="https://github.com/Sekuora/Trezenv/blob/main/LICENSE" >  Apache-2.0 License
    
  </a>

## Donations

In hopes you have found the project useful and want to support development I share the platforms where you can show your support! 💓 Any donations are greatly appreciated.

## Acknolwdgements
Thanks to https://github.com/othneildrew/Best-README-Template for the readme template

