import qrcode
from qrcode.constants import ERROR_CORRECT_H

# 创建二维码对象，并指定编码格式为 UTF-8
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
    encode_mode='utf-8'  # 指定编码格式为 UTF-8
)

# 设置二维码的数据
data = ""
qr.add_data(data)

# 填充数据并生成二维码图像
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图像
qr_img.save("qrcode.png")
