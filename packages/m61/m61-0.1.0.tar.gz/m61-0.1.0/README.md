# 프로젝트 개요: M61
## 목적
네트워크 아웃바운드 미터링 테스트용 트래픽 전송 도구입니다.
> [M61](https://namu.wiki/w/M61%20%EB%B0%9C%EC%B9%B8)

* 클라이언트: 특정 서버로 대용량 데이터를 안정적으로 전송할 수 있습니다.
* 서버: 클라이언트로부터 데이터를 안전하게 수신 및 수신된 내용을 기록합니다.

## 조건
* 클라이언트는 실제 전송한 데이터 크기 출력
* 서버는 수신한 데이터 크기 출력

## 특징
* 용량 단위 모드 (--size-gib)
* 시간 단위 모드 (--duration-sec)
* 멀티프로세스 기반 병렬 전송/수신
* 메모리 부족 감지 및 예외 처리

# 프로젝트 구조

``` bash
m61/
├── pyproject.toml         # Poetry 설정
├── README.md
├── m61/
│   ├── __init__.py
│   ├── common.py          # 공통 유틸 (로깅, 메모리 확인 등)
│   ├── exceptions.py      # 사용자 정의 예외
│   ├── client.py          # 클라이언트 코드
│   └── server.py          # 서버 코드
```

# 🚀 실행 방법

1. 코드를 내려 받으세요.
2. 최신 버전의 `poetry`를 설치해주세요.
3. 내려받은 코드가 있는 경로로 이동합니다.
4. `project.toml` 파일이 있는 위치에서 빌드를 수행합니다. 

``` bash
# 빌드
$ poetry build

5. 패키지 빌드가 완료되면, 패키지를 설치합니다.

# 설치
$ pip install dist/m61-0.1.0-py3-none-any.whl
```


## 서버 실행
``` bash
$ m61-server --host 0.0.0.0 --port 5000 --output /data/output.bin --max-workers 4
```

## 클라이언트 (500GiB 전송, 프로세스 8개)
``` bash
$ m61-client --server-ip 192.168.0.10 --server-port 5000 --size-gib 500 --workers 8
```

## 클라이언트 (1시간 동안 전송, 프로세스 2개)
``` bash
$ m61-client --server-ip 192.168.0.10 --server-port 5000 --duration-sec 3600 --workers 2
```

# 제약 사항
* Ubuntu Linux 외 다른 OS 환경에서는 테스트되지 않았음