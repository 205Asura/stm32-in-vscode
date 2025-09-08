from pathlib import Path
import re

cmake_file = Path("CMakeLists.txt")

text = cmake_file.read_text(encoding="utf-8")

src_dir = Path("Core/Src")
system_file = None
for f in src_dir.glob("system_stm32*.c"):
    system_file = f
    break

if system_file:
    system_file_path = f"${{CMAKE_SOURCE_DIR}}/{system_file.as_posix()}"
else:
    system_file_path = "# (no system_stm32*.c found)"

pattern = re.compile(
    r"# Add sources to executable.*?# Add include paths.*?\)", re.DOTALL
)

replacement = f"""# Add sources to executable
file(GLOB USER_SOURCES
    "${{CMAKE_SOURCE_DIR}}/Core/Src/*.c"
)

# Exclude system_stm32xx.c
list(REMOVE_ITEM USER_SOURCES "{system_file_path}")

target_sources(${{CMAKE_PROJECT_NAME}} PRIVATE
    ${{USER_SOURCES}}
)

# Add include paths
target_include_directories(${{CMAKE_PROJECT_NAME}} PRIVATE
    # Add user defined include paths
    ${{CMAKE_SOURCE_DIR}}/Core/Inc
)"""

new_text = pattern.sub(replacement, text)

hex_bin_block = """\n
# Create .hex
add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -O ihex $<TARGET_FILE:${CMAKE_PROJECT_NAME}> ${CMAKE_PROJECT_NAME}.hex
    COMMENT "Creating HEX file: ${CMAKE_PROJECT_NAME}.hex"
)

# Create .bin
add_custom_command(TARGET ${CMAKE_PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -O binary $<TARGET_FILE:${CMAKE_PROJECT_NAME}> ${CMAKE_PROJECT_NAME}.bin
    COMMENT "Creating BIN file: ${CMAKE_PROJECT_NAME}.bin"
)
"""

if "Creating HEX file" not in new_text:
    new_text = new_text.rstrip() + hex_bin_block

cmake_file.write_text(new_text, encoding="utf-8")

print("✅ CMakeLists.txt updated")
