#pip install cx_oracle ← 이걸 cmd든 터미널이든 실행해서 설치해야 아래 코드가 돌아감.

import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("DROP table test")
cursor.execute("create table test(name varchar(20) primary key, price number(10), cnt number(10))")
cursor.execute("insert into test(name,price,cnt) values('사과',3000,5)")
cursor.execute("insert into test(name,price,cnt) values('포도',4000,20)")
cursor.execute("insert into test(name,price,cnt) values('수박',10000,5)")
cursor.close()
conn.commit()
conn.close()
while True:
    choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 입력
        S - 판매
        U - 수정
        D - 삭제
        Q - 종료
        ''').upper()

    if choice=="I":  
        conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
        cursor = conn.cursor()
        menu="SELECT * FROM TEST"
        cursor.execute(menu)
        rs=cursor.fetchall()
        print('\n---------메뉴---------')
        for i in range(len(rs)):
            print(rs[i])
        sql = "insert into test values(:1,:2,:3)"
        name = input('과일이름 >>> ')
        price = input('과일가격 >>> ')
        cnt = input('과일수량 >>> ')
        data = (name,int(price),int(cnt))
        cursor.execute(sql,data)
        menu="SELECT * FROM TEST"
        cursor.execute(menu)
        rs=cursor.fetchall()
        print('\n---------메뉴---------')
        for i in range(len(rs)):
            print(rs[i])
        cursor.close()
        conn.commit()
        conn.close()
    
    elif choice=="S":
        conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
        cursor = conn.cursor()
        menu="SELECT * FROM TEST"
        cursor.execute(menu)
        rs=cursor.fetchall()
        print('\n---------메뉴---------')
        for i in range(len(rs)):
            print(rs[i])
        sellfruit = input("어떤 과일을 판매하시겠습니까?")
        sellcnt = input("몇개를 판매하시겠습니까?")
        sellcnt1=0 #2022-05-25 추가
        for i in range(len(rs)): #2022-05-25 len(rs[i])를 len(rs)로 변경
            if rs[i][0] == sellfruit:
                sellcnt1 = rs[i][2]-int(sellcnt)
                print("판매금액은 {0}원 입니다.".format(int(sellcnt)*rs[i][1]))
        cursor.execute("update test set cnt = '{0}' where NAME = '{1}'".format(sellcnt1,sellfruit))
        menu="SELECT * FROM TEST"
        cursor.execute(menu)
        rs=cursor.fetchall()
        print('\n---------메뉴---------')
        for i in range(len(rs)):
            print(rs[i])
        cursor.close()
        conn.commit()
        conn.close()
    
    elif choice=="U":
        conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
        cursor = conn.cursor()
        menu="SELECT * FROM TEST"
        cursor.execute(menu)
        rs=cursor.fetchall()
        print('\n---------메뉴---------')
        for i in range(len(rs)):
            print(rs[i])
        changename = input('수정하고자 하는 과일이름을 입력하세요.')
        name = input('과일이름 >>> ')
        price = int(input('과일가격 >>> '))
        cnt = int(input('과일수량 >>> '))
        cursor.execute("update test set NAME = '{0}', PRICE = '{1}', CNT = '{2}' where NAME = '{3}'".format(name,price,cnt,changename))
        menu="SELECT * FROM TEST"
        cursor.execute(menu)
        rs=cursor.fetchall()
        print('\n---------메뉴---------')
        for i in range(len(rs)):
            print(rs[i])
        cursor.close()
        conn.commit()
        conn.close()
    
    elif choice=="D":
        conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
        cursor = conn.cursor()
        menu="SELECT * FROM TEST"
        cursor.execute(menu)
        rs=cursor.fetchall()
        print('\n---------메뉴---------')
        for i in range(len(rs)):
            print(rs[i])
        deletename = input('삭제하고자 하는 과일이름을 입력하세요.')
        cursor.execute("delete from test where NAME = '{0}'".format(deletename))
        menu="SELECT * FROM TEST"
        cursor.execute(menu)
        rs=cursor.fetchall()
        print('\n---------메뉴---------')
        for i in range(len(rs)):
            print(rs[i])
        cursor.close()
        conn.commit()
        conn.close()

    elif choice == "Q":
        print('프로그램을 종료합니다.')
        break
