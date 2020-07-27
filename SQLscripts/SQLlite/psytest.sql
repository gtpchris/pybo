-- 개발용.sqlite3

select * from psytest_psytest pp 

;
--심리검사목록 인서트 
INSERT into psytest_psytest (psytest_nm, description, is_verify, start_age, end_age, create_dt , modify_dt,
								 q1,
								 q2,
								 q3,
                                 q1_1,
                                 q1_2,
                                 q1_3,
                                 q1_4,
                                 q1_5,
                                 q1_6,
                                 q1_7,
                                 q2_1,
                                 q2_2,
                                 q2_3,
                                 q2_4,
                                 q2_5,
                                 q2_6,
                                 q2_7,
                                 q3_1,
                                 q3_2,
                                 q3_3,
                                 q3_4,
                                 q3_5,
                                 q3_6,
                                 q3_7
) 
     values ('BDI', '벡 우울검사',False, 0,0, date('now'), date('now'),
    		" ",
    		" ",
    		" ", 
			"나는 슬프지 않다.",
			"나는 슬프다.",
			"나는 항상 슬퍼서 그 것을 떨쳐버릴 수 없다.",
			"나는 너무나 슬프고 불행해서 도저히 견딜 수 없다.",
			"", 
			"", 
			"", 
			"나는 앞날에 대해서 별로 낙심하지 않는다.",
			"나는 앞날에 대해 비관적인 느낌이 든다. ",
			"나는 앞날에 대해 기대할 것이 아무것도 없다고 느낀다.",
			"나의 앞날은 아주 절망적이고 나아질 가능성이 없다고 느낀다.",
			"",
			"", 
			"", 
			"나는 실패자라고 느끼지 않는다.",
			"나는 보통 사람들보다 더 많이 실패한 것 같다.",
			"내가 살아온 과거를 뒤돌아 보면, 생각나는 것은 실패뿐이다.",
			"나는 인간으로서 완전한 실패자인 것 같다.",
			"",
			"", 
			"" 
     );

--심리검사목록 인서트 
INSERT into psytest_psytest (psytest_nm, description, is_verify, start_age, end_age, create_dt , modify_dt ) 
     values ('BAI', '벡 불안검사',False, 0,0, date('now'), date('now'));

--심리검사목록 인서트 
INSERT into psytest_psytest (psytest_nm, description, is_verify, start_age, end_age, create_dt , modify_dt ) 
     values ('SEI', '자아존중감검사',True, 7,15, date('now'), date('now'));

    --심리검사목록 인서트 
INSERT into psytest_psytest (psytest_nm, description, is_verify, start_age, end_age, create_dt , modify_dt ) 
     values ('TSCC', '외상증상검사',True, 7,15, date('now'), date('now'));

select * from psytest_psytest pp 


delete from psytest_psytest 
where id=1;

select * from psytest_psytest pp 
where id=5;

update psytest_psytest set id=1 
where id=5;

select * from p