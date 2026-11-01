import os
from pygments import highlight
from pygments.lexers import XmlLexer, KotlinLexer
from pygments.formatters import ImageFormatter
from PIL import Image, ImageDraw, ImageFont

def render_code_image(code, lexer_type, title, output_path):
    # Setup Pygments
    lexer = XmlLexer() if lexer_type == 'xml' else KotlinLexer()
    formatter = ImageFormatter(
        font_name='Consolas',
        font_size=15,
        line_numbers=True,
        style='monokai',
        line_number_bg='#1E1E1E',
        line_number_fg='#6C7086',
        background_color='#1E1E1E',
        line_pad=4
    )
    img_bytes = highlight(code, lexer, formatter)
    
    # Write temp file and open
    temp_path = output_path + ".temp.png"
    with open(temp_path, "wb") as f:
        f.write(img_bytes)
        
    code_img = Image.open(temp_path)
    
    # Create window frame
    header_height = 36
    padding = 10
    total_width = code_img.width + (padding * 2)
    total_height = code_img.height + header_height + padding
    
    final_img = Image.new("RGBA", (total_width, total_height), "#181825")
    draw = ImageDraw.Draw(final_img)
    
    # Title bar
    draw.rectangle([0, 0, total_width, header_height], fill="#11111B")
    
    # Window control circles (macOS style / IDE style)
    draw.ellipse([14, 12, 24, 22], fill="#FF5F56")
    draw.ellipse([30, 12, 40, 22], fill="#FFBD2E")
    draw.ellipse([46, 12, 56, 22], fill="#27C93F")
    
    # Title text
    try:
        font = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 13)
    except:
        font = ImageFont.load_default()
    draw.text((68, 11), title, fill="#CDD6F4", font=font)
    
    # Paste code image
    final_img.paste(code_img, (padding, header_height))
    final_img.save(output_path, "PNG")
    if os.path.exists(temp_path):
        os.remove(temp_path)
    print(f"Generated {output_path} ({total_width}x{total_height})")

if __name__ == "__main__":
    sample_xml = """<com.google.android.material.chip.ChipGroup
    android:id="@+id/chipGroupFilter"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:singleSelection="true">
    <com.google.android.material.chip.Chip
        android:id="@+id/chip1"
        android:text="Semua" />
</com.google.android.material.chip.ChipGroup>"""
    render_code_image(sample_xml, 'xml', 'activity_ninth.xml (ChipGroup)', 'test_code.png')

