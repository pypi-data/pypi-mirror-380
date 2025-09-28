# from automation_toolkit import AutomationToolkit
# # 简单使用
# # tool = AutomationToolkit(
# #     device="192.168.1.100:5555",
# #     img_path="./images",
# #     debug_img="./debug"
# # )

from automation_toolkit.core import AutomationToolkit
tool = AutomationToolkit(
    device="R38N100G4EJ",
    img_path="./images",
    debug_img="./debug",
    sleep_time=0
)
print(tool.compare_region_similarity('image.png', (162, 823, 332, 870),debug=True))
# tool.s