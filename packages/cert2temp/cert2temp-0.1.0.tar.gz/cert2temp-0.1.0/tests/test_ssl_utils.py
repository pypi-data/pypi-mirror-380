#!/usr/bin/env python3
"""
SSL 인증서 ASCII 임시 폴더 생성 테스트
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cert2temp import get_safe_cert_path, get_platform_safe_temp_dir


def test_ascii_temp_folder():
    """ASCII 안전한 임시 폴더 생성 테스트"""
    print("🗂️  SSL 인증서 ASCII 임시 폴더 테스트")
    print("=" * 50)

    # 플랫폼 정보 출력
    import platform
    system = platform.system()
    print(f"📍 플랫폼: {system}")
    print(f"🔧 Python 버전: {platform.python_version()}")

    # 플랫폼별 안전 임시 디렉터리 확인
    try:
        safe_temp_dir = get_platform_safe_temp_dir()
        print(f"🏠 플랫폼 안전 임시 디렉터리: {safe_temp_dir}")
        print(f"📁 디렉터리 존재: {safe_temp_dir.exists()}")
    except Exception as e:
        print(f"❌ 플랫폼 안전 임시 디렉터리 확인 실패: {e}")

    print()

    try:
        print("인증서 경로 생성 중...")
        cert_path = get_safe_cert_path()
        print(f"✅ 인증서 경로: {cert_path}")

        if cert_path:
            # 경로가 ASCII인지 확인
            is_ascii = all(ord(c) < 128 for c in cert_path)
            print(f"✅ ASCII 안전 경로: {is_ascii}")

            if is_ascii:
                print("🎉 영문 임시 폴더 복사 로직 작동 성공!")
            else:
                print("❌ 경로에 비ASCII 문자가 포함되어 있음")
                # 비ASCII 문자 출력
                non_ascii_chars = [c for c in cert_path if ord(c) >= 128]
                print(f"   비ASCII 문자: {non_ascii_chars}")

            # 파일 존재 확인
            if os.path.exists(cert_path):
                file_size = os.path.getsize(cert_path)
                print(f"✅ 인증서 파일 존재: {file_size} bytes")
            else:
                print("❌ 인증서 파일이 존재하지 않음")
        else:
            print("❌ 인증서 경로 생성 실패")

    except Exception as e:
        print(f"❌ 테스트 실패: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_ascii_temp_folder()
