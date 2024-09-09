import os
from cairosvg import svg2png

"""png파일이 저장될 경로와, svg파일이 저장된 경로를 설정합니다."""
PNG_DIR_PATH = "./assets/png"
SVG_DIR_PATH = "./assets/svg"


def main():
    if not os.path.exists(SVG_DIR_PATH):
        print("FAIL: 경로가 존재하지 않습니다.")
        return

    if not os.path.isdir(SVG_DIR_PATH):
        print("FAIL: 경로가 디렉토리가 아닙니다.")
        return

    print("START: SVG 파일을 PNG 파일로 변환합니다.")
    file_or_dir_list = os.listdir(SVG_DIR_PATH)
    for item in file_or_dir_list:
        if not item.endswith(".svg"):
            print(f"SKIP: {item}은 SVG 파일이 아닙니다.")
            continue

        convert_svg2png(
            svg_file_name=item,
        )

    print("FINISH: 모든 변환을 완료하였습니다.")
    return


def convert_svg2png(svg_file_name: str):
    """SVG 파일을 PNG 파일로 변환하는 함수"""

    print("----------------------------------")
    svg_file_path = os.path.join(SVG_DIR_PATH, svg_file_name)
    png_file_name = svg_file_name.replace(".svg", ".png")
    png_file_path = os.path.join(PNG_DIR_PATH, png_file_name)

    if os.path.exists(png_file_path):
        """이전에 변환한 파일이 존재할 경우, 삭제"""
        print(f"INFO: {png_file_name} 파일이 이미 존재합니다.")
        print(f"REMOVE: {png_file_name} 파일을 삭제합니다.")
        os.remove(png_file_path)

    svg2png(url=svg_file_path, write_to=png_file_path)

    print(f"SUCCESS: {svg_file_name} 파일을 PNG 파일로 변환합니다.")


if __name__ == "__main__":
    main()
