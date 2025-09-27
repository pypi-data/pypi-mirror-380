#!/usr/bin/env python3
"""
KITECH Repository Library 실제 사용 예시
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def example_simple_functions():
    """간단한 함수 사용 예시"""
    print("=" * 60)
    print("📚 간단한 함수 사용 예시")
    print("=" * 60)

    # 토큰이 있다고 가정 (실제로는 사용자가 제공해야 함)
    token = "kt_your_actual_token_here"  # 실제 토큰으로 교체 필요

    try:
        from kitech_repository import list_repositories, download, upload

        print("1. 리포지토리 목록 조회:")
        print("   from kitech_repository import list_repositories")
        print(f"   repos = list_repositories(token='{token[:10]}...')")
        print("   # X-App-Key 헤더가 자동으로 추가됩니다")

        print("\n2. 파일 다운로드:")
        print("   from kitech_repository import download")
        print("   download(")
        print("       repository_id=123,")
        print("       path='/data/file.csv',")
        print("       output_dir='./downloads',")
        print(f"       token='{token[:10]}...'")
        print("   )")

        print("\n3. 파일 업로드:")
        print("   from kitech_repository import upload")
        print("   upload(")
        print("       repository_id=123,")
        print("       file_path='./local_file.csv',")
        print("       remote_path='uploads/',")
        print(f"       token='{token[:10]}...'")
        print("   )")

        return True
    except Exception as e:
        print(f"❌ 예시 생성 실패: {e}")
        return False

def example_client_class():
    """클라이언트 클래스 사용 예시"""
    print("\n" + "=" * 60)
    print("🔧 클라이언트 클래스 사용 예시")
    print("=" * 60)

    try:
        from kitech_repository import KitechClient

        print("1. 토큰과 함께 클라이언트 생성:")
        print("   from kitech_repository import KitechClient")
        print("   client = KitechClient(token='kt_your_token')")
        print("   # X-App-Key 헤더가 자동으로 설정됩니다")

        print("\n2. Context Manager 사용 (권장):")
        print("   with KitechClient(token='kt_your_token') as client:")
        print("       # 리포지토리 목록")
        print("       repos = client.list_repositories()")
        print("       print(f'Found {len(repos[\"repositories\"])} repositories')")
        print("")
        print("       # 파일 목록")
        print("       files = client.list_files(123, prefix='data/')")
        print("       for file in files['files']:")
        print("           print(f'📄 {file.name}')")
        print("")
        print("       # 파일 다운로드")
        print("       path = client.download_file(123, path='/data/file.csv')")
        print("       print(f'Downloaded to: {path}')")
        print("")
        print("       # 파일 업로드")
        print("       result = client.upload_file(123, file_path='./file.csv')")
        print("       print('Upload successful!')")

        print("\n3. 수동 클라이언트 관리:")
        print("   client = KitechClient(token='kt_your_token')")
        print("   try:")
        print("       repos = client.list_repositories()")
        print("       # 작업 수행...")
        print("   finally:")
        print("       client.close()  # 수동으로 연결 종료")

        return True
    except Exception as e:
        print(f"❌ 예시 생성 실패: {e}")
        return False

def show_authentication_setup():
    """인증 설정 방법"""
    print("\n" + "=" * 60)
    print("🔐 인증 설정 방법")
    print("=" * 60)

    print("방법 1: CLI로 미리 로그인 (권장)")
    print("   $ kitech auth login")
    print("   Enter your API token: kt_xxxxxxxxxxxxxxxxxx")
    print("   ✅ Login successful")
    print("")
    print("   # 이후 라이브러리에서 토큰 자동 사용")
    print("   from kitech_repository import list_repositories")
    print("   repos = list_repositories()  # 토큰 자동 로드")

    print("\n방법 2: 코드에서 직접 토큰 제공")
    print("   from kitech_repository import KitechClient")
    print("   client = KitechClient(token='kt_your_actual_token')")

    print("\n방법 3: 환경변수 사용")
    print("   export KITECH_TOKEN=kt_your_actual_token")
    print("   # 또는 .env 파일에 저장")

def show_header_details():
    """X-App-Key 헤더 세부 정보"""
    print("\n" + "=" * 60)
    print("📋 X-App-Key 헤더 자동 설정")
    print("=" * 60)

    print("라이브러리가 자동으로 추가하는 헤더:")
    print("   X-App-Key: kt_your_token")
    print("   accept: */*")
    print("")
    print("내부 동작:")
    print("   1. AuthManager가 토큰을 로드")
    print("   2. headers 속성에서 X-App-Key 헤더 생성")
    print("   3. httpx.Client가 모든 요청에 헤더 자동 추가")
    print("")
    print("확인 방법:")
    try:
        from kitech_repository.lib.auth import AuthManager
        auth = AuthManager()
        if auth.is_authenticated():
            print(f"   현재 헤더: {auth.headers}")
        else:
            print("   현재 인증되지 않음 - 먼저 로그인하세요")
    except Exception as e:
        print(f"   헤더 확인 실패: {e}")

def main():
    """메인 함수"""
    print("🚀 KITECH Repository Library 사용 가이드\n")

    # 예시들 실행
    example_simple_functions()
    example_client_class()
    show_authentication_setup()
    show_header_details()

    print("\n" + "=" * 60)
    print("✨ 정리")
    print("=" * 60)
    print("✅ 라이브러리에서 X-App-Key 헤더 자동 설정")
    print("✅ CLI로 로그인하거나 토큰 직접 제공")
    print("✅ 간단한 함수와 고급 클라이언트 모두 지원")
    print("✅ Context manager로 자원 관리 자동화")
    print("")
    print("💡 다음 단계:")
    print("   1. 실제 토큰으로 로그인: kitech auth login")
    print("   2. 리포지토리 ID 확인: kitech list repos")
    print("   3. 라이브러리 코드 작성 및 실행!")

if __name__ == "__main__":
    main()