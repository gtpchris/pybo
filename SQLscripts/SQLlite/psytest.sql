-- 개발용.sqlite3


select * from psytest_psytestsheet pp2 

update psytest_psytestsheet set id=4 
where id=6;

select * from psytest_psytestanswer pp 

update psytest_psytestsheet 
  set q11_1 = '0) 나는 요즈음 전보다 짜증을 더 내는 편은 아니다.'
    , q11_2 = '1) 나는 전보다 더 쉽게 짜증이 나고 귀찮아진다.'
    , q11_3 = '2) 나는 요즈음 항상 짜증스럽다.'
    , q11_4 = '3) 전에는 짜증스럽던 일에 요즈음은너무 지쳐서 짜증조차 나지 않는다.'
    , q12_1 = '0) 나는 다른 사람들에 대한 관심을 잃지 않고 있다.'
    , q12_2 = '1) 나는 전보다 다른 사람들에 대한 관심이 줄었다.'
    , q12_3 = '2) 나는 다른 사람들에 대한 관심이 거의 없어졌다.'
    , q12_4 = '3) 나는 다른 사람들에 대한 관심이 없어졌다.'
    , q13_1 = '0) 나는 평소처럼 결단을 잘 내린다.'
    , q13_2 = '1) 나는 결정을 미루는 때가 전보다 더 많다.'
    , q13_3 = '2) 나는 전에 비해 결정 내리는 데에 큰 어려움을 느낀다.'
    , q13_4 = '3) 나는 더 이상 아무 결정도 내릴 수가 없다.'
    , q14_1 = '0) 나는 전보다 내 모습이 더 나빠졌다고 느끼지 않는다.'
    , q14_2 = '1) 나는 나이들어 보이거나 매력 없어 보일까봐 걱정한다.'
    , q14_3 = '2) 나는 내 모습이 매력 없게 변해 버렸다고 느낀다.'
    , q14_4 = '3) 나는 내가 추하게 보인다고 믿는다.'
    , q15_1 = '0) 나는 전처럼 일을 할 수 있다.'
    , q15_2 = '1) 어떤 일을 시작하려면 특별히 더 많은 노력이 든다.'
    , q15_3 = '2) 무슨 일이든 하려면 나 자신을 매우 심각하게 채찍질 해야만 한다.'
    , q15_4 = '3) 나는 전혀 아무 일도 할 수가 없다.'
    , q16_1 = '0) 나는 평소처럼 잠을 잘 수 있다.'
    , q16_2 = '1) 나는 전처럼 잠을 자지 못한다.'
    , q16_3 = '2) 나는 전보다 한 두 시간씩 일찍 깨고 다시 잠들기 어렵다.'
    , q16_4 = '3) 나는 평소보다 몇 시간이나 일찍 깨고 다시 잠들 수 없다.'
    , q17_1 = '0) 나는 평소보다 더 피곤하지는 않다.'
    , q17_2 = '1) 나는 전보다 더 쉽게 피곤해진다.'
    , q17_3 = '2) 나는 무엇을 해도 언제나 피곤해진다.'
    , q17_4 = '3) 나는 너무나 피곤해서 아무 일도 할 수 없다.'
    , q18_1 = '0) 내 식욕은 평소와 다름 없다.'
    , q18_2 = '1) 나는 요즈음 전보다 식욕이 좋지 않다.'
    , q18_3 = '2) 나는 요즈음 전보다 식욕이 많이 떨어졌다.'
    , q18_4 = '3) 요즈음에는 전혀 식욕이 없다.'
    , q19 = '문항 19. 나는 현재 체중감량 중이다. (0 에 응답)'
    , q19_1 = '0) 요즈음 체중이 별로 줄지 않았다.'
    , q19_2 = '1) 전보다 몸무게가 2kg 가량 줄었다.'
    , q19_3 = '2) 전보다 몸무게가 5kg 가량 줄었다.'
    , q19_4 = '3) 전보다 몸무게가 7kg 가량 줄었다.'
    , q20_1 = '0) 나는 건강에 대해 전보다 더 염려하고 있지는 않다.'
    , q20_2 = '1) 나는 여러 가지 통증, 소화불량, 변비 등과 같은 신체적인 문제로 걱정하고있다.'
    , q20_3 = '2) 나는 건강이 매우 염려되어 다른 일은 생각하기 힘들다.'
    , q20_4 = '3) 나는 건강이 너무 염려되어 다른 일은 아무것도 생각할 수 없다.'
    , q21_1 = '0) 나는 요즈음 성(sex)에 대한 관심에 별다른 변화가 있는 것 같지는 않다.'
    , q21_2 = '1) 나는 전보다 성(sex)에 대한 관심이 줄었다.'
    , q21_3 = '2) 나는 전보다 성(sex)에 대한 관심이 상당히 줄었다.'
    , q21_4 = '3) 나는 성(sex)에 대한 관심을 완전히 잃었다.'
where id=1;





select *
from psytest_psytestanswer pp 



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



SELECT "psytest_psytestsheet"."id",
       "psytest_psytestsheet"."psytest_nm",
       "psytest_psytestsheet"."description",
       "psytest_psytestsheet"."is_effect_verify",
       "psytest_psytestsheet"."start_age",
       "psytest_psytestsheet"."end_age",
       "psytest_psytestsheet"."q1",
       "psytest_psytestsheet"."q1_1",
       "psytest_psytestsheet"."q1_2",
       "psytest_psytestsheet"."q1_3",
       "psytest_psytestsheet"."q1_4",
       "psytest_psytestsheet"."q1_5",
       "psytest_psytestsheet"."q1_6",
       "psytest_psytestsheet"."q1_7",
       "psytest_psytestsheet"."q2",
       "psytest_psytestsheet"."q2_1",
       "psytest_psytestsheet"."q2_2",
       "psytest_psytestsheet"."q2_3",
       "psytest_psytestsheet"."q2_4",
       "psytest_psytestsheet"."q2_5",
       "psytest_psytestsheet"."q2_6",
       "psytest_psytestsheet"."q2_7",
       "psytest_psytestsheet"."q3",
       "psytest_psytestsheet"."q3_1",
       "psytest_psytestsheet"."q3_2",
       "psytest_psytestsheet"."q3_3",
       "psytest_psytestsheet"."q3_4",
       "psytest_psytestsheet"."q3_5",
       "psytest_psytestsheet"."q3_6",
       "psytest_psytestsheet"."q3_7",
       "psytest_psytestsheet"."create_dt",
       "psytest_psytestsheet"."modify_dt"
  FROM "psytest_psytestsheet"
 WHERE "psytest_psytestsheet"."id" = '1'