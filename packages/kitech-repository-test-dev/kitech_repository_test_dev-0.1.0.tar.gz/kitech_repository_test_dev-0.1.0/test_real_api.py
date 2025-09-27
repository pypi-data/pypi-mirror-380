#!/usr/bin/env python3
"""
실제 API를 사용한 라이브러리 테스트
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_connection():
    """연결 테스트"""
    print("=" * 50)
    print("🔗 API 연결 테스트")
    print("=" * 50)

    try:
        from kitech_repository import KitechClient

        with KitechClient() as client:
            result = client.test_connection()
            print(f"✅ 연결 성공: {result}")
            return True
    except Exception as e:
        print(f"❌ 연결 실패: {e}")
        return False

def test_list_repositories():
    """리포지토리 목록 테스트"""
    print("\n" + "=" * 50)
    print("📂 리포지토리 목록 조회 테스트")
    print("=" * 50)

    try:
        from kitech_repository import list_repositories

        repos = list_repositories()
        print(f"✅ 리포지토리 {len(repos)} 개 조회 성공")

        for i, repo in enumerate(repos[:3]):  # 처음 3개만 출력
            print(f"   {i+1}. ID: {repo.id}, Name: {repo.name}")

        if len(repos) > 3:
            print(f"   ... 및 {len(repos)-3}개 더")

        return repos
    except Exception as e:
        print(f"❌ 리포지토리 목록 조회 실패: {e}")
        return None

def test_list_files(repository_id):
    """파일 목록 테스트"""
    print("\n" + "=" * 50)
    print(f"📄 파일 목록 조회 테스트 (Repository ID: {repository_id})")
    print("=" * 50)

    try:
        from kitech_repository import list_files

        result = list_files(repository_id)
        files = result['files']
        print(f"✅ 파일 {len(files)} 개 조회 성공")

        for i, file in enumerate(files[:5]):  # 처음 5개만 출력
            icon = "📁" if file.is_directory else "📄"
            print(f"   {i+1}. {icon} {file.name}")

        if len(files) > 5:
            print(f"   ... 및 {len(files)-5}개 더")

        return files
    except Exception as e:
        print(f"❌ 파일 목록 조회 실패: {e}")
        return None

def test_client_class():
    """클라이언트 클래스 테스트"""
    print("\n" + "=" * 50)
    print("🔧 KitechClient 클래스 테스트")
    print("=" * 50)

    try:
        from kitech_repository import KitechClient

        with KitechClient() as client:
            # 연결 테스트
            result = client.test_connection()
            print(f"✅ 클라이언트 연결: {result}")

            # 리포지토리 목록
            repos = client.list_repositories()
            print(f"✅ 리포지토리 조회: {len(repos['repositories'])} 개")

            if repos['repositories']:
                repo_id = repos['repositories'][0].id
                # 파일 목록
                files = client.list_files(repo_id)
                print(f"✅ 파일 조회: {len(files['files'])} 개")

        return True
    except Exception as e:
        print(f"❌ 클라이언트 테스트 실패: {e}")
        return False

def test_download_simple(repository_id, file_path=None):
    """간단한 다운로드 테스트"""
    print("\n" + "=" * 50)
    print("⬇️  다운로드 테스트")
    print("=" * 50)

    if not file_path:
        print("⏭️  파일 경로가 없어서 다운로드 테스트 건너뜀")
        return False

    try:
        from kitech_repository import download
        from pathlib import Path

        # 테스트용 다운로드 폴더 생성
        test_dir = Path("./test_downloads")
        test_dir.mkdir(exist_ok=True)

        print(f"파일 다운로드 시도: {file_path}")
        result_path = download(
            repository_id=repository_id,
            path=file_path,
            output_dir=str(test_dir)
        )

        print(f"✅ 다운로드 성공: {result_path}")
        return True
    except Exception as e:
        print(f"❌ 다운로드 실패: {e}")
        return False

def main():
    """메인 테스트 실행"""
    print("🧪 KITECH Repository Library 실제 API 테스트\n")

    # 테스트 실행
    tests_passed = 0
    total_tests = 0

    # 1. 연결 테스트
    total_tests += 1
    if test_connection():
        tests_passed += 1

    # 2. 리포지토리 목록 테스트
    total_tests += 1
    repos = test_list_repositories()
    if repos:
        tests_passed += 1

    # 3. 파일 목록 테스트 (첫 번째 리포지토리 사용)
    if repos and len(repos) > 0:
        total_tests += 1
        first_repo_id = repos[0].id
        files = test_list_files(first_repo_id)
        if files:
            tests_passed += 1

        # 4. 간단한 다운로드 테스트 (첫 번째 파일 사용)
        if files:
            # 디렉토리가 아닌 첫 번째 파일 찾기
            test_file = None
            for file in files:
                if not file.is_directory and file.name not in ["..", "Load more..."]:
                    test_file = file
                    break

            if test_file:
                total_tests += 1
                if test_download_simple(first_repo_id, test_file.actual_path):
                    tests_passed += 1

    # 5. 클라이언트 클래스 테스트
    total_tests += 1
    if test_client_class():
        tests_passed += 1

    # 결과 요약
    print("\n" + "=" * 50)
    print("📊 테스트 결과")
    print("=" * 50)
    print(f"✅ 통과: {tests_passed}/{total_tests}")
    print(f"❌ 실패: {total_tests - tests_passed}/{total_tests}")

    if tests_passed == total_tests:
        print("\n🎉 모든 테스트 통과! 라이브러리가 정상 작동합니다!")
    elif tests_passed > 0:
        print("\n⚠️  일부 테스트 통과. 기본 기능은 작동합니다.")
    else:
        print("\n💥 모든 테스트 실패. 문제를 확인해주세요.")

if __name__ == "__main__":
    main()