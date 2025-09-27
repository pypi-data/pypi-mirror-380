# PyPI 발행 가이드 (테스트 배포)

## 🚨 중요: 테스트 배포입니다
- 패키지 이름: `kitech-repository-test-dev`
- 나중에 회사 계정으로 정식 배포 시 `kitech-repository`로 변경 예정

## 📋 사전 준비

### 1. PyPI 계정 생성
- https://pypi.org/account/register/
- 이메일 인증 완료

### 2. API 토큰 생성
- https://pypi.org/manage/account/token/
- 토큰 복사 (한 번만 보여짐!)

### 3. 필요한 패키지 설치
```bash
pip install --upgrade pip
pip install build twine
```

## 🚀 발행 단계

### Step 1: 빌드
```bash
cd "/Users/wim/Developer/한국생산기술연구원 제조 데이터 리포지토리/kitech-repository-CLI"

# 이전 빌드 정리
rm -rf dist/

# 패키지 빌드
python -m build
```

성공하면 `dist/` 폴더에:
- `kitech_repository_test_dev-0.1.0-py3-none-any.whl`
- `kitech_repository_test_dev-0.1.0.tar.gz`

### Step 2: TestPyPI로 먼저 테스트 (선택사항)
```bash
# TestPyPI에 업로드
python -m twine upload --repository testpypi dist/*

# Username: __token__
# Password: <TestPyPI 토큰>

# 테스트 설치
pip install --index-url https://test.pypi.org/simple/ kitech-repository-test-dev
```

### Step 3: 실제 PyPI에 업로드
```bash
# PyPI에 업로드
python -m twine upload dist/*

# Username: __token__
# Password: <PyPI API 토큰>
```

### Step 4: 확인
```bash
# 설치 테스트
pip install kitech-repository-test-dev

# 확인
python -c "import kitech_repository; print(kitech_repository.__version__)"
```

## 📦 업로드 후 사용법

```bash
# 설치
pip install kitech-repository-test-dev

# CLI 사용
kitech --help
kitech auth login
kitech list repos

# Python 라이브러리 사용
from kitech_repository import KitechClient, download, upload

# 리포지토리 목록
client = KitechClient(token="kt_xxxxx")
repos = client.list_repositories()

# 파일 다운로드
download(123, "/data/file.csv", "./downloads")
```

## ⚠️ 주의사항

1. **테스트 배포임을 명시**: README나 설명에 테스트 버전임을 표시
2. **토큰 보안**: API 토큰을 절대 커밋하지 마세요
3. **버전 관리**: 재업로드 시 버전 번호 증가 필요 (0.1.1, 0.1.2 등)
4. **삭제 정책**: PyPI는 패키지 삭제 후 동일 이름 재사용 제한이 있음

## 🔄 업데이트 방법

1. `pyproject.toml`에서 버전 업데이트
2. 빌드 및 업로드 재실행
3. 사용자는 `pip install --upgrade kitech-repository-test-dev`

## 🏢 정식 배포 시 체크리스트

회사 계정으로 정식 배포할 때:

1. [ ] `pyproject.toml`의 name을 `kitech-repository`로 변경
2. [ ] version을 `1.0.0`으로 설정
3. [ ] author email을 회사 이메일로 변경
4. [ ] URLs를 회사 GitHub 저장소로 변경
5. [ ] README 업데이트
6. [ ] 회사 PyPI 계정으로 업로드
7. [ ] 문서화 사이트 준비 (선택)

## 💡 자동화 (선택사항)

`.pypirc` 파일 생성으로 인증 자동화:

```ini
[pypi]
username = __token__
password = pypi-xxxxxxxxxxxxxxxxxxxxx

[testpypi]
username = __token__
password = pypi-xxxxxxxxxxxxxxxxxxxxx
```

위치: `~/.pypirc` (홈 디렉토리)
권한: `chmod 600 ~/.pypirc`

---

**현재 상태**: 테스트 배포 준비 완료! 🎉