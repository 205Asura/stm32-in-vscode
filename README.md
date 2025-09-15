# STM32 in Visual Studio Code

### Introduction:

This repo show you a good way to use VSCode in Windows for coding with STM32.

- You have a good "Code Completion" (better than STM32CubeIDE), and be able to create `.hex` and `.bin` file by VSCode
- You can make the pin configuration in STM32CubeMX and it will directly generate code in your VSCode workplace (better than PlatformIO)

### Software Requirements:

- STM32 Apps: _STM32CubeMX_, _STM32CubeProgrammer_
- VSCode (of course), with extensions: _STM32Cube for Visual Studio Code (pre-released version)_ and _CMake Tool_

- _ARM GCC TOOLCHAIN_ from https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads. I am using the `arm-gnu-toolchain-14.3.rel1-mingw-w64-x86_64-arm-none-eabi.zip`

### Getting Started

#### 1. Create a project in STM32CubeMX:

- Open `STM32CubeMX`
- Choose `Start My project from MCU` and choose your MCU
- In `Project Manager` tab, enter the project's name and location
- At `Toolchain/IDE` choose `CMake`
- Then config the pin as you want
- Press `Generate Code`

#### 2. Setup VSCode:

- Open `Edit enviroment variables for your account` and add the Path of the ARM GCC TOOLCHAIN. For example: `D:\Downloads\arm-gnu-toolchain-14.3.rel1-mingw-w64-x86_64-arm-none-eabi\bin`
- In `VSCode`, open the project folder created by STM32CubeMX. Some pop-ups will show immediately
- Choose `Debug`, `Yes` and ignore the `Bad CMake executable`

<img width="700" alt="image" src="https://github.com/user-attachments/assets/14521847-f4c8-4f51-b245-b81e0a661e70" />

<img width="600" alt="image" src="https://github.com/user-attachments/assets/5b919b3e-e069-4223-b15d-a1bd9f9370b4" />

- Open the `Prefrences: Open User Settings (JSON)` and set `"C_Cpp.intelliSenseEngine": "disabled"`, this will fix the confliction warning. **Note:** set back to "default" if you doing with other non-STM32 projects
- Then click `Build` at the left corner of the screen for the first time
- Add the file `config.py` in the project folder and run

```bash
python config.py
```

- `Build` again than you can see the `.hex` and `.bin` file created in the `build` folder
- Now you can start coding in VSCode and add more pin configuration in STM32CubeMX

**_Some bugs can happen in VSCode:_**
1. If you change the directory of the project folder, a bug like "different from the original directory" will occur. To fix it, delete the "build" folder and click "Build".

#### 3. Programming your STM32 Board

- Open `STM32CubeProgrammer`, connect the board via `ST-LINK` then press `Connect`
- Use the `.hex` file for programming

#### Good Luck !
