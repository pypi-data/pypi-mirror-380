import sys
import os
from datetime import datetime
from colorama import init
import vendy_bc
from vendy_bc import cli

# 초기 설정
프로그램실행 = cli.main
Bth = vendy_bc.__version__

init()

# 바로 모듈 실행
print("프로그램을 실행합니다.")
프로그램실행.Main().main()

# 버전 확인
Btq = sys.argv[1:]
for BtK in Btq:
    if BtK.lower() in ["--version", "-v"]:
        print(Bth)
        sys.exit()
