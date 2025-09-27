#!/usr/bin/env python3
"""
KITECH Repository Library 테스트 예시 코드
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_import():
    """라이브러리 import 테스트"""
    print("=" * 50)
    print("1. 라이브러리 import 테스트")
    print("=" * 50)

    try:
        # 메인 라이브러리 import
        import kitech_repository
        print(f"✅ kitech_repository 버전: {kitech_repository.__version__}")
        print(f"✅ 작성자: {kitech_repository.__author__}")

        # 사용 가능한 함수들 확인
        print("\n📋 사용 가능한 함수들:")
        for func in kitech_repository.__all__:
            print(f"   - {func}")

        # 개별 import 테스트
        from kitech_repository import (
            download, upload, list_repositories, list_files,
            KitechClient, AuthManager, Config
        )
        print("✅ 모든 함수와 클래스 import 성공!")

        return True
    except ImportError as e:
        print(f"❌ Import 실패: {e}")
        return False
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")
        return False

def test_client_creation():
    """클라이언트 생성 테스트"""
    print("\n" + "=" * 50)
    print("2. 클라이언트 생성 테스트")
    print("=" * 50)

    try:
        from kitech_repository import KitechClient, Config

        # 설정 확인
        config = Config.load()
        print(f"✅ 설정 로드 성공")
        print(f"   - API Base URL: {config.api_base_url}")
        print(f"   - Download Dir: {config.download_dir}")

        # 클라이언트 생성 (토큰 없이)
        client = KitechClient()
        print("✅ 클라이언트 생성 성공 (토큰 없음)")

        # Context manager 테스트
        with KitechClient() as client:
            print("✅ Context manager 사용 성공")

        return True
    except Exception as e:
        print(f"❌ 클라이언트 생성 실패: {e}")
        return False

def test_convenience_functions():
    """편의 함수 테스트 (실제 API 호출 없이)"""
    print("\n" + "=" * 50)
    print("3. 편의 함수 정의 확인")
    print("=" * 50)

    try:
        from kitech_repository import download, upload, list_repositories, list_files

        # 함수 시그니처 확인
        import inspect

        # download 함수
        sig = inspect.signature(download)
        print(f"✅ download 함수: {sig}")

        # upload 함수
        sig = inspect.signature(upload)
        print(f"✅ upload 함수: {sig}")

        # list_repositories 함수
        sig = inspect.signature(list_repositories)
        print(f"✅ list_repositories 함수: {sig}")

        # list_files 함수
        sig = inspect.signature(list_files)
        print(f"✅ list_files 함수: {sig}")

        return True
    except Exception as e:
        print(f"❌ 편의 함수 확인 실패: {e}")
        return False

def show_usage_examples():
    """사용 예시 코드 출력"""
    print("\n" + "=" * 50)
    print("4. 사용 예시 코드")
    print("=" * 50)

    examples = """
# 예시 1: 간단한 다운로드
from kitech_repository import download
result = download(
    repository_id=123,
    path="/data/dataset.csv",
    output_dir="./downloads",
    token="kt_your_token_here"
)

# 예시 2: 파일 업로드
from kitech_repository import upload
result = upload(
    repository_id=123,
    file_path="./my_file.csv",
    remote_path="uploads/data/",
    token="kt_your_token_here"
)

# 예시 3: 리포지토리 목록
from kitech_repository import list_repositories
repos = list_repositories(token="kt_your_token_here")
for repo in repos:
    print(f"{repo.id}: {repo.name}")

# 예시 4: 고급 클라이언트 사용
from kitech_repository import KitechClient

with KitechClient(token="kt_your_token_here") as client:
    # 파일 목록
    files = client.list_files(123, prefix="data/")

    # 파일 다운로드
    path = client.download_file(123, path="/data/file.csv")
    print(f"Downloaded to: {path}")

    # 파일 업로드
    result = client.upload_file(123, file_path="./file.csv")
    print("Upload successful!")
"""

    print(examples)

    print("💡 실제 사용하려면:")
    print("   1. 먼저 CLI로 로그인: kitech auth login")
    print("   2. 또는 토큰을 직접 제공")
    print("   3. repository_id는 실제 리포지토리 ID로 변경")

def main():
    """메인 테스트 함수"""
    print("🚀 KITECH Repository Library 테스트 시작")

    # 테스트 실행
    tests = [
        test_import,
        test_client_creation,
        test_convenience_functions
    ]

    passed = 0
    for test in tests:
        if test():
            passed += 1

    # 결과 요약
    print("\n" + "=" * 50)
    print("📊 테스트 결과 요약")
    print("=" * 50)
    print(f"✅ 통과: {passed}/{len(tests)}")
    print(f"❌ 실패: {len(tests) - passed}/{len(tests)}")

    if passed == len(tests):
        print("🎉 모든 테스트 통과! 라이브러리 사용 준비 완료!")
    else:
        print("⚠️  일부 테스트 실패. 환경 설정을 확인하세요.")

    # 사용 예시 출력
    show_usage_examples()

if __name__ == "__main__":
    main()