#!/usr/bin/env python3
"""
라이브러리 업로드 기능 테스트
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def create_test_files():
    """테스트용 파일들 생성"""
    print("=" * 50)
    print("📁 테스트 파일 생성")
    print("=" * 50)

    try:
        from pathlib import Path

        # 테스트 폴더 생성
        test_dir = Path("./test_files")
        test_dir.mkdir(exist_ok=True)

        # 1. 텍스트 파일 생성
        text_file = test_dir / "library_test.txt"
        text_file.write_text("""
KITECH Repository Library 테스트 파일
=====================================

생성 시간: """ + str(__import__('datetime').datetime.now()) + """
파일 유형: 텍스트 파일
목적: 라이브러리 업로드 기능 테스트

이 파일은 라이브러리 업로드 테스트를 위해 자동 생성되었습니다.
""")
        print(f"✅ 텍스트 파일 생성: {text_file}")

        # 2. CSV 파일 생성
        csv_file = test_dir / "library_test_data.csv"
        csv_file.write_text("""name,value,date
라이브러리 테스트,100,2024-01-01
업로드 테스트,200,2024-01-02
KITECH Repository,300,2024-01-03
""")
        print(f"✅ CSV 파일 생성: {csv_file}")

        # 3. JSON 파일 생성
        import json
        json_file = test_dir / "library_test_config.json"
        config_data = {
            "test_name": "KITECH Repository Library Upload Test",
            "timestamp": str(__import__('datetime').datetime.now()),
            "settings": {
                "enable_logging": True,
                "max_retries": 3,
                "timeout": 30
            }
        }
        json_file.write_text(json.dumps(config_data, indent=2, ensure_ascii=False))
        print(f"✅ JSON 파일 생성: {json_file}")

        return [text_file, csv_file, json_file]

    except Exception as e:
        print(f"❌ 테스트 파일 생성 실패: {e}")
        return []

def test_upload_simple_function(repository_id, test_files):
    """간단한 upload 함수 테스트"""
    print("\n" + "=" * 50)
    print("⬆️  간단한 upload 함수 테스트")
    print("=" * 50)

    success_count = 0

    try:
        from kitech_repository import upload

        for i, file_path in enumerate(test_files):
            print(f"\n{i+1}. 업로드 중: {file_path.name}")

            try:
                result = upload(
                    repository_id=repository_id,
                    file_path=str(file_path),
                    remote_path="library_test/"  # 테스트 폴더에 업로드
                )
                print(f"   ✅ 업로드 성공: {result}")
                success_count += 1
            except Exception as e:
                print(f"   ❌ 업로드 실패: {e}")

        print(f"\n📊 업로드 결과: {success_count}/{len(test_files)} 성공")
        return success_count > 0

    except Exception as e:
        print(f"❌ upload 함수 테스트 실패: {e}")
        return False

def test_upload_client_class(repository_id, test_files):
    """클라이언트 클래스 업로드 테스트"""
    print("\n" + "=" * 50)
    print("🔧 KitechClient 업로드 테스트")
    print("=" * 50)

    try:
        from kitech_repository import KitechClient
        from pathlib import Path

        with KitechClient() as client:
            success_count = 0

            for i, file_path in enumerate(test_files):
                print(f"\n{i+1}. 클라이언트로 업로드 중: {file_path.name}")

                try:
                    result = client.upload_file(
                        repository_id=repository_id,
                        file_path=Path(file_path),
                        remote_path="client_test/"  # 클라이언트 테스트 폴더
                    )
                    print(f"   ✅ 업로드 성공: {result}")
                    success_count += 1
                except Exception as e:
                    print(f"   ❌ 업로드 실패: {e}")

            print(f"\n📊 클라이언트 업로드 결과: {success_count}/{len(test_files)} 성공")
            return success_count > 0

    except Exception as e:
        print(f"❌ 클라이언트 업로드 테스트 실패: {e}")
        return False

def verify_upload(repository_id):
    """업로드된 파일 확인"""
    print("\n" + "=" * 50)
    print("🔍 업로드 파일 확인")
    print("=" * 50)

    try:
        from kitech_repository import list_files

        # library_test/ 폴더 확인
        result = list_files(repository_id, path="library_test")
        if result['files']:
            print(f"✅ library_test/ 폴더에 {len(result['files'])} 개 파일 발견:")
            for file in result['files']:
                if not file.is_directory:
                    print(f"   📄 {file.name}")

        # client_test/ 폴더 확인
        result = list_files(repository_id, path="client_test")
        if result['files']:
            print(f"✅ client_test/ 폴더에 {len(result['files'])} 개 파일 발견:")
            for file in result['files']:
                if not file.is_directory:
                    print(f"   📄 {file.name}")

        return True

    except Exception as e:
        print(f"❌ 업로드 확인 실패: {e}")
        return False

def cleanup_test_files():
    """테스트 파일 정리"""
    print("\n" + "=" * 50)
    print("🧹 테스트 파일 정리")
    print("=" * 50)

    try:
        from pathlib import Path
        import shutil

        test_dir = Path("./test_files")
        if test_dir.exists():
            shutil.rmtree(test_dir)
            print("✅ 테스트 파일 폴더 삭제 완료")

        return True

    except Exception as e:
        print(f"❌ 테스트 파일 정리 실패: {e}")
        return False

def main():
    """메인 테스트 실행"""
    print("🧪 KITECH Repository Library 업로드 테스트\n")

    # 먼저 리포지토리 목록 가져오기
    try:
        from kitech_repository import list_repositories
        repos = list_repositories()

        if not repos:
            print("❌ 리포지토리가 없어서 업로드 테스트 불가")
            return

        # 첫 번째 리포지토리 사용
        repository_id = repos[0].id
        print(f"📂 테스트 대상 리포지토리: {repos[0].name} (ID: {repository_id})")

    except Exception as e:
        print(f"❌ 리포지토리 조회 실패: {e}")
        return

    # 테스트 실행
    tests_passed = 0
    total_tests = 0

    # 1. 테스트 파일 생성
    total_tests += 1
    test_files = create_test_files()
    if test_files:
        tests_passed += 1

        # 2. 간단한 upload 함수 테스트
        total_tests += 1
        if test_upload_simple_function(repository_id, test_files):
            tests_passed += 1

        # 3. 클라이언트 클래스 업로드 테스트
        total_tests += 1
        if test_upload_client_class(repository_id, test_files):
            tests_passed += 1

        # 4. 업로드 확인
        total_tests += 1
        if verify_upload(repository_id):
            tests_passed += 1

        # 5. 정리
        total_tests += 1
        if cleanup_test_files():
            tests_passed += 1

    # 결과 요약
    print("\n" + "=" * 50)
    print("📊 업로드 테스트 결과")
    print("=" * 50)
    print(f"✅ 통과: {tests_passed}/{total_tests}")
    print(f"❌ 실패: {total_tests - tests_passed}/{total_tests}")

    if tests_passed == total_tests:
        print("\n🎉 모든 업로드 테스트 통과! 라이브러리 업로드 기능이 정상 작동합니다!")
    elif tests_passed > 0:
        print("\n⚠️  일부 업로드 테스트 통과. 기본 업로드 기능은 작동합니다.")
    else:
        print("\n💥 모든 업로드 테스트 실패. 문제를 확인해주세요.")

if __name__ == "__main__":
    main()