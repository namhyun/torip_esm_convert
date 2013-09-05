torip_esm_convert
=================

토르 IP를 ESM 블랙리스트 기능을 통해 자동화 하기 위한 스크립트


<a href="https://raw.github.com/namhyun/torip_esm_convert/master/tor_esm_conv.py"> 다운로드</a> (다른이름으로 저장)



*사용 방법

1. 파이썬 2.7.x를 설치한다.
2. [tor_esm_conv.py] 를 다운 받아 실행한다.

* ESM 등록 방법 

1. ESM 콘솔에 접속해서 상단메뉴에서 [설정-> 블랙리스트->관리] 를 선택한다.
2. 블랙리스트 관리 메뉴에서 [토르IP대역] 그룹명을 추가한 한다. (최초에만 추가하면 된다.)
3. [블랙리스트 관리-> 블랙리스트 설정]에서 추가한 그룹명 [토르IP대역]을 선택한다.
4. 좌측 아래 리스트뷰에서 [오른쪽 버튼->목록 불러오기->Text]를 선택하여, 오늘날짜로 생성된 txt파일을 불러온다.


* TOR관련 IP정보를 제공하는 사이트
- http://torstatus.blutmagie.de/
- http://69.195.137.28/open/suricata/rules/tor.rules
- https://www.dan.me.uk/tornodes
- http://proxy.org/tor.shtml
- http://ipduh.com/ip/tor-exit/

