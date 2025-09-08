# STM32 in Visual Studio Code

### Introduction: 

This repo show you a good way to use VSCode in Windows for coding with STM32.
- You have a good "Code Completion" (better than STM32CubeIDE), and be able to create `.hex` and `.bin` file by VSCode
- You can make the pin configuration in STM32CubeMX and it will directly generate code in your VSCode workplace (better than PlatformIO)
### Software Requirements: 

- STM32CubeMX, STM32CubeProgrammer
- VSCode (of course), with extensions: 

```
STM32Cube for Visual Studio Code (pre-released version)
CMake and CMake Tool
```

- `ARM GCC TOOLCHAIN` from https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads. I am using the `arm-gnu-toolchain-14.3.rel1-mingw-w64-x86_64-arm-none-eabi.zip`

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

 - Open the `Prefrences: Open User Settings (JSON)` and set `"C_Cpp.intelliSenseEngine": "disabled"`, this will fix the confliction warning. **Note:** set to "default" if you doing with other non-STM32 projects
 - Then click `Build` at the left corner of the screen for the first time
 - Open the file `CMakelists.txt` (the one right next to `CMakePresets.json`) and do the followings:
   - Add the code in `hex_bin.txt` at the end
   - Replace the these 2 blocks by `linker.txt`
    ```cmake
    # Add sources to executable
    target_sources(${CMAKE_PROJECT_NAME} PRIVATE
     # Add user sources here
    )

    # Add include paths
    target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE
     # Add user defined include paths
    )
    ```
 

- `Build` again than you can see the `.hex` and `.bin` file created in the `build` folder
- Now you can start coding in VSCode and add more pin configuration in STM32CubeMX

#### 3. Programming your STM32 Board

- Open `STM32CubeProgrammer`, connect the board via `ST-LINK` then press `Connect`
- Use the `.hex` file for programming

#### Good Luck !
